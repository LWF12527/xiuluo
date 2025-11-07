import subprocess
import os
import time
import re
import sys
import xml.etree.ElementTree as ET
import tempfile


class AndroidElementOperator:
    def __init__(self, device_id=None):
        self.device_id = device_id
        self.adb_path = self.find_adb_path()
        self.screen_size = None  # 添加屏幕尺寸属性

        if not self.adb_path:
            print("错误: 无法找到ADB路径")
            sys.exit(1)

        if not self.device_id:
            self.device_id = self.get_default_device()

        if not self.device_id:
            print("错误: 没有可用的设备")
            sys.exit(1)

        print(f"已选择设备: {self.device_id}")
        self.get_screen_size()  # 获取屏幕尺寸

    def find_adb_path(self):
        """尝试在常见位置查找ADB"""
        possible_paths = [
            r"E:\Android-platform-tools\adb.exe",
            r"C:\Program Files (x86)\Android\android-sdk\platform-tools\adb.exe",
            r"C:\android-sdk\platform-tools\adb.exe",
            "adb"
        ]

        for path in possible_paths:
            if os.path.exists(path) or path == "adb":
                try:
                    result = subprocess.run([path, "--version"],
                                            capture_output=True,
                                            text=True,
                                            check=True)
                    if "Android Debug Bridge" in result.stdout:
                        print(f"找到ADB: {path}")
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
            print(f"命令执行失败: {' '.join(cmd)}")
            print(f"错误信息: {e.stderr.strip()}")
            return None

    def get_screen_size(self):
        """获取设备屏幕尺寸"""
        if self.screen_size:
            return self.screen_size

        result = self.run_adb_command("shell wm size")
        if not result:
            print("无法获取屏幕尺寸，使用默认值 1080x1920")
            self.screen_size = (1080, 1920)
            return self.screen_size

        # 解析屏幕尺寸 "Physical size: 1080x1920"
        match = re.search(r'(\d+)x(\d+)', result)
        if match:
            width = int(match.group(1))
            height = int(match.group(2))
            self.screen_size = (width, height)
            print(f"屏幕尺寸: {width}x{height}")
            return self.screen_size
        else:
            print("无法解析屏幕尺寸，使用默认值 1080x1920")
            self.screen_size = (1080, 1920)
            return self.screen_size

    def tap(self, x, y):
        """点击指定坐标 - 从文档1中添加的方法"""
        print(f"点击坐标: ({x}, {y})")
        self.run_adb_command(f"shell input tap {x} {y}")
        return True

    def get_ui_hierarchy_raw(self):
        """获取原始UI层次结构XML内容"""
        # 在设备上生成UI层次结构XML文件
        remote_path = "/sdcard/window_dump.xml"
        self.run_adb_command(f"shell uiautomator dump {remote_path}")

        # 创建临时文件 - 修复参数错误
        temp_file = tempfile.NamedTemporaryFile(suffix=".xml", delete=False)
        local_path = temp_file.name
        temp_file.close()  # 关闭文件以便后续使用

        # 从设备拉取XML文件
        self.run_adb_command(f"pull {remote_path} {local_path}")

        # 删除设备上的文件
        self.run_adb_command(f"shell rm {remote_path}")

        # 读取XML内容
        try:
            with open(local_path, 'r', encoding='utf-8') as f:
                content = f.read()
            os.unlink(local_path)  # 删除临时文件
            return content
        except Exception as e:
            print(f"读取UI层次结构失败: {str(e)}")
            return None

    def extract_element_info(self, content, resource_id):
        """从XML内容中提取元素信息"""
        if not content:
            return None

        # 查找包含指定resource-id的行
        pattern = f'resource-id="{re.escape(resource_id)}"[^>]*bounds="\\[(\\d+),(\\d+)\\]\\[(\\d+),(\\d+)\\]"'
        match = re.search(pattern, content)

        if match:
            x1, y1, x2, y2 = map(int, match.groups())
            center_x = (x1 + x2) // 2
            center_y = (y1 + y2) // 2

            # 查找元素的文本内容
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
        print(f"尝试通过ID点击: {resource_id}")

        # 获取UI层次结构
        content = self.get_ui_hierarchy_raw()
        if not content:
            print("无法获取UI层次结构")
            return False

        # 提取元素信息
        element_info = self.extract_element_info(content, resource_id)

        if element_info['found']:
            x, y = element_info['center']
            print(f"找到元素: {element_info['text']}")
            print(f"元素边界: {element_info['bounds']}")
            print(f"点击中心点: ({x}, {y})")

            # 执行点击
            result = self.run_adb_command(f"shell input tap {x} {y}")
            if result is not None:
                print("点击成功！")
                return True
            else:
                print("点击失败")
                return False
        else:
            print(f"未找到资源ID: {resource_id}")
            print("正在搜索相似的资源ID...")

            # 尝试查找相似的资源ID
            similar_ids = self.find_similar_resource_ids(content, resource_id)
            if similar_ids:
                print("找到相似的资源ID:")
                for i, sid in enumerate(similar_ids, 1):
                    print(f"{i}. {sid}")

                # 询问用户是否尝试点击相似的ID
                choice = input("是否尝试点击相似的资源ID? (输入编号或n取消): ")
                if choice.isdigit() and 1 <= int(choice) <= len(similar_ids):
                    return self.tap_by_id(similar_ids[int(choice) - 1])

            return False

    def find_similar_resource_ids(self, content, resource_id):
        """查找相似的资源ID"""
        # 提取包名和ID部分
        parts = resource_id.split('/')
        if len(parts) == 2:
            package, id_part = parts
            # 查找相同包名的资源ID
            pattern = f'resource-id="{re.escape(package)}/[^"]*"'
            matches = re.findall(pattern, content)
            similar_ids = [match.split('"')[1] for match in matches]
            return list(set(similar_ids))  # 去重
        return []

    def input_text(self, text):
        """直接输入文本"""
        # 转义特殊字符
        # ADB input text命令需要转义空格和特殊字符
        escaped_text = text.replace(" ", "%s")
        escaped_text = escaped_text.replace("\\", "\\\\")
        escaped_text = escaped_text.replace("\"", "\\\"")
        escaped_text = escaped_text.replace("'", "\\'")

        print(f"输入文本: {text}")
        result = self.run_adb_command(f"shell input text \"{escaped_text}\"")
        return result is not None

    def input_text_by_id(self, resource_id, text):
        """通过资源ID找到元素并输入文本"""
        print(f"尝试通过ID输入文本: {resource_id} -> {text}")

        # 获取UI层次结构
        content = self.get_ui_hierarchy_raw()
        if not content:
            print("无法获取UI层次结构")
            return False

        # 提取元素信息
        element_info = self.extract_element_info(content, resource_id)

        if element_info['found']:
            x, y = element_info['center']
            print(f"找到元素: {element_info['text']}")
            print(f"元素边界: {element_info['bounds']}")
            print(f"点击中心点: ({x}, {y})")

            # 先点击元素
            result = self.run_adb_command(f"shell input tap {x} {y}")
            if result is None:
                print("点击元素失败")
                return False

            # 等待一下，确保输入框获得焦点
            time.sleep(0.5)

            # 输入文本
            return self.input_text(text)
        else:
            print(f"未找到资源ID: {resource_id}")
            return False

    def perform_comment_cycle(self, cycles=1):
        """执行评论循环操作"""
        for i in range(cycles):
            print(f"\n===== 开始第 {i + 1} 次循环 =====")

            # 1. 点击同城按钮坐标 (330, 1827)
            print("1. 点击同城按钮")
            self.tap(330, 1827)
            time.sleep(2)

            # 2. 点击评论ID
            print("2. 点击评论按钮")
            self.tap_by_id("cn.soulapp.android:id/tvComment")
            time.sleep(2)

            # 3. 点击输入框按钮坐标 (170, 1700)
            print("3. 点击AI输入-调用输入框")
            self.tap(125, 1700)
            time.sleep(2)

            # 3. 点击输入框按钮坐标 (170, 1700)
            print("3_2. 点击输入框")
            self.tap(190, 660)
            time.sleep(2)

            # 4. 输入文本
            print("4. 输入文本")
            self.input_text("11111111")
            time.sleep(2)

            # 5. 点击发送评论坐标 (950, 790)
            print("5. 发送评论")
            self.tap(954, 786)
            time.sleep(2)

            # 6. 点击返回按钮坐标 (66, 200)
            print("6. 返回")
            self.tap(66, 200)
            time.sleep(2)

            print(f"===== 第 {i + 1} 次循环完成 =====")


# 主程序
if __name__ == "__main__":
    # 尝试获取设备ID作为参数
    device_id = None
    cycles = 3  # 默认循环1次

    if len(sys.argv) > 1:
        device_id = sys.argv[1]

    if len(sys.argv) > 2:
        try:
            cycles = int(sys.argv[2])
        except ValueError:
            print("循环次数参数无效，使用默认值1")

    # 创建元素操作器
    operator = AndroidElementOperator(device_id)

    # 执行评论循环
    operator.perform_comment_cycle(cycles)

    print("\n所有循环操作已完成！")