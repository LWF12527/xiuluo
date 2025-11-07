import subprocess
import os
import time
import re
import sys
from loguru import logger
import random
import base64


class AndroidElementOperator:
    def __init__(self, device_id=None):
        self.device_id = device_id
        self.adb_path = self.find_adb_path()
        self.screen_size = None
        self.adb_keyboard_installed = False

        if not self.adb_path:
            logger.info("错误: 无法找到ADB路径")
            sys.exit(1)

        if not self.device_id:
            self.device_id = self.get_default_device()

        if not self.device_id:
            logger.info("错误: 没有可用的设备")
            sys.exit(1)

        logger.info(f"已选择设备: {self.device_id}")
        self.get_screen_size()
        self.check_adb_keyboard()

    def find_adb_path(self):
        """尝试在常见位置查找ADB"""
        possible_paths = [
            r"D:\platform-tools\adb.exe"
        ]

        for path in possible_paths:
            if os.path.exists(path) or path == "adb":
                try:
                    result = subprocess.run([path, "--version"],
                                            capture_output=True,
                                            text=True,
                                            check=True)
                    if "Android Debug Bridge" in result.stdout:
                        logger.info(f"找到ADB: {path}")
                        return path
                except:
                    continue
        return None

    def get_default_device(self):
        """获取默认设备ID"""
        result = self.run_adb_command("devices")
        if not result:
            return None

        for line in result.splitlines():
            if "device" in line and not line.startswith("List"):
                return line.split("\t")[0]
        return None

    def run_adb_command(self, command):
        """执行ADB命令"""
        cmd = [self.adb_path]
        if self.device_id:
            cmd.extend(["-s", self.device_id])
        cmd.extend(command.split())

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            logger.info(f"命令执行失败: {' '.join(cmd)}")
            logger.info(f"错误信息: {e.stderr.strip()}")
            return None

    def get_screen_size(self):
        """获取设备屏幕尺寸"""
        if self.screen_size:
            return self.screen_size

        result = self.run_adb_command("shell wm size")
        if not result:
            logger.info("无法获取屏幕尺寸，使用默认值 1080x1920")
            self.screen_size = (1080, 1920)
            return self.screen_size

        match = re.search(r'(\d+)x(\d+)', result)
        if match:
            width = int(match.group(1))
            height = int(match.group(2))
            self.screen_size = (width, height)
            logger.info(f"屏幕尺寸: {width}x{height}")
            return self.screen_size
        else:
            logger.info("无法解析屏幕尺寸，使用默认值 1080x1920")
            self.screen_size = (1080, 1920)
            return self.screen_size

    def tap(self, x, y):
        """点击指定坐标"""
        logger.info(f"点击坐标: ({x}, {y})")
        self.run_adb_command(f"shell input tap {x} {y}")
        return True

    def get_ui_hierarchy_raw(self):
        """获取原始UI层次结构XML内容 - 改进版本"""
        # 尝试不同的方法获取UI层次结构
        methods = [
            self._get_ui_hierarchy_via_file,
            self._get_ui_hierarchy_via_exec_out
        ]

        for method in methods:
            content = method()
            if content:
                return content

        logger.info("所有方法都无法获取UI层次结构")
        return None

    def _get_ui_hierarchy_via_file(self):
        """通过文件方式获取UI层次结构"""
        remote_path = "/sdcard/window_dump.xml"
        self.run_adb_command(f"shell uiautomator dump {remote_path}")
        time.sleep(1)  # 等待文件生成

        temp_file = tempfile.NamedTemporaryFile(suffix=".xml", delete=False)
        local_path = temp_file.name
        temp_file.close()

        # 尝试拉取文件
        pull_result = self.run_adb_command(f"pull {remote_path} {local_path}")
        if not pull_result or "0 skipped" not in pull_result:
            logger.info(f"无法拉取UI层次结构文件: {pull_result}")
            os.unlink(local_path)
            return None

        try:
            with open(local_path, 'r', encoding='utf-8') as f:
                content = f.read()
            os.unlink(local_path)
            return content
        except Exception as e:
            logger.info(f"读取UI层次结构失败: {str(e)}")
            return None
        finally:
            # 尝试删除设备上的文件
            self.run_adb_command(f"shell rm {remote_path}")

    def _get_ui_hierarchy_via_exec_out(self):
        """通过exec-out直接获取UI层次结构"""
        try:
            cmd = [self.adb_path]
            if self.device_id:
                cmd.extend(["-s", self.device_id])
            cmd.extend(["exec-out", "uiautomator", "dump", "/dev/tty"])

            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            return result.stdout.strip()
        except Exception as e:
            logger.info(f"exec-out方法失败: {str(e)}")
            return None

    def extract_element_info(self, content, resource_id):
        """从XML内容中提取元素信息"""
        if not content:
            return None

        pattern = f'resource-id="{re.escape(resource_id)}"[^>]*bounds="\\[(\\d+),(\\d+)\\]\\[(\\d+),(\\d+)\\]"'
        match = re.search(pattern, content)

        if match:
            x1, y1, x2, y2 = map(int, match.groups())
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            text_pattern = f'resource-id="{re.escape(resource_id)}"[^>]*text="([^"]*)"'
            text_match = re.search(text_pattern, content)
            text = text_match.group(1) if text_match else ""

            return {
                'bounds': f"[{x1},{y1}][{x2},{y2}]",
                'center': (center_x, center_y),
                'text': text,
                'found': True
            }
        else:
            return {'found': False}

    def tap_by_id(self, resource_id):
        """通过资源ID点击元素"""
        logger.info(f"尝试通过ID点击: {resource_id}")

        content = self.get_ui_hierarchy_raw()
        if not content:
            logger.info("无法获取UI层次结构")
            return False

        element_info = self.extract_element_info(content, resource_id)

        if element_info['found']:
            x, y = element_info['center']
            logger.info(f"找到元素: {element_info['text']}")
            logger.info(f"元素边界: {element_info['bounds']}")
            logger.info(f"点击中心点: ({x}, {y})")

            result = self.run_adb_command(f"shell input tap {x} {y}")
            if result is not None:
                logger.info("点击成功！")
                return True
            else:
                logger.info("点击失败")
                return False
        else:
            logger.info(f"未找到资源ID: {resource_id}")
            return False

    def check_adb_keyboard(self):
        """检查并安装ADBKeyboard"""
        logger.info("检查ADBKeyboard安装状态...")
        adb_keyboard_check = self.run_adb_command("shell pm list packages com.android.adbkeyboard")
        if "com.android.adbkeyboard" in adb_keyboard_check:
            logger.info("已检测到ADBKeyboard")
            self.adb_keyboard_installed = True
            return True

        logger.info("未检测到ADBKeyboard，尝试安装...")
        # 尝试从当前目录查找APK
        apk_path = os.path.join(os.path.dirname(__file__), "ADBKeyboard.apk")
        if os.path.exists(apk_path):
            logger.info(f"找到APK文件: {apk_path}")
            install_result = self.run_adb_command(f"install {apk_path}")
            if "Success" in install_result:
                logger.info("ADBKeyboard安装成功")
                self.adb_keyboard_installed = True
                return True
            else:
                logger.info(f"ADBKeyboard安装失败: {install_result}")
                return False
        else:
            logger.info("未找到ADBKeyboard.apk，请下载并放在脚本同目录下")
            return False

    def input_text_using_ime(self, text):
        """使用输入法服务直接输入文本"""
        if not self.adb_keyboard_installed:
            logger.info("ADBKeyboard未安装，无法使用IME输入")
            return False

        logger.info(f"使用IME服务输入文本: {text}")

        # 获取当前输入法
        current_ime = self.run_adb_command("shell settings get secure default_input_method")
        logger.info(f"当前输入法: {current_ime}")

        # 切换到ADB输入法
        self.run_adb_command("shell ime set com.android.adbkeyboard/.AdbIME")
        time.sleep(1)

        # 使用ADB输入法广播输入文本
        # 对文本进行Base64编码以处理特殊字符
        encoded_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        result = self.run_adb_command(f"shell am broadcast -a ADB_INPUT_B64 --es msg {encoded_text}")

        if "Broadcast completed" in result:
            logger.info("文本输入成功")
            # 恢复原始输入法
            if current_ime and "null" not in current_ime:
                self.run_adb_command(f"shell ime set {current_ime}")
            return True
        else:
            logger.info(f"文本输入失败: {result}")
            return False

    def input_text_by_coordinates(self, x, y, text):
        """通过坐标点击输入框并输入文本"""
        logger.info(f"通过坐标输入文本: ({x}, {y}) -> {text}")

        # 点击输入框
        self.tap(x, y)
        time.sleep(1)

        # 清空输入框
        self.run_adb_command("shell input keyevent KEYCODE_MOVE_HOME")
        time.sleep(0.2)
        self.run_adb_command("shell input keyevent --longpress KEYCODE_DEL")
        time.sleep(0.5)

        # 使用IME服务输入文本
        return self.input_text_using_ime(text)

    def perform_comment_cycle(self, cycles=1):
        """执行评论循环操作 - 改进版本"""
        for i in range(cycles):
            try:
                logger.info(f"\n===== 开始第 {i + 1} 次循环 =====")

                logger.info("1. 点击同城按钮")
                self.tap(290, 1560)
                time.sleep(2 + random.random())
                try:
                    logger.info("2. 点击评论按钮")
                    self.tap_by_id("cn.soulapp.android:id/tvComment")
                except:
                    time.sleep(2 + random.random())
                    continue

                logger.info("3. 点击AI输入-调用输入框")
                self.tap(65, 1500)
                time.sleep(2 + random.random())

                logger.info("3_2. 点击输入框")
                self.tap(125, 965)
                time.sleep(1 + random.random())

                logger.info("4. 输入文本")
                # 使用坐标方式输入文本，避免依赖UI层次结构
                self.input_text_by_coordinates(125, 965,
                                               "嗨喽小姐姐，02年程序员，坐标龙岗坳背。性格好相处，生活圈简单，想重启一下社交圈。希望能认识附近要求简单、好聊天的朋友。不介意我目前薪资一般的，欢迎联系，见面喝杯咖啡/奶茶聊聊看？")
                time.sleep(1 + random.random())

                logger.info("5. 发送评论")
                self.tap(830, 1230)
                time.sleep(2 + random.random())

                logger.info("6. 返回")
                self.tap(40, 70)
                time.sleep(2 + random.random())

                logger.info(f"===== 第 {i + 1} 次循环完成 =====")
            except Exception as e:
                logger.error(f"错误，{e}")


# 主程序
if __name__ == "__main__":
    device_id = None
    cycles = 3

    if len(sys.argv) > 1:
        device_id = sys.argv[1]

    if len(sys.argv) > 2:
        try:
            cycles = int(sys.argv[2])
        except ValueError:
            logger.info("循环次数参数无效，使用默认值3")

    operator = AndroidElementOperator(device_id)
    operator.perform_comment_cycle(cycles)

    logger.info("\n所有循环操作已完成！")