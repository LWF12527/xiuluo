import subprocess
import os
import time
import sys
import tempfile
from PIL import Image, ImageTk
import tkinter as tk
import tkinter.messagebox


class CoordinateFinder:
    def __init__(self, device_id=None):
        self.device_id = device_id
        self.adb_path = self.find_adb_path()
        self.screenshot_path = None
        self.original_width = 0
        self.original_height = 0

    def find_adb_path(self):
        """查找ADB路径"""
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
                        return path
                except:
                    continue
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
            return None

    def take_screenshot(self):
        """获取设备截图"""
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        remote_path = f"/sdcard/screenshot_{timestamp}.png"
        local_path = f"screenshot_{timestamp}.png"

        # 截图
        self.run_adb_command(f"shell screencap -p {remote_path}")

        # 拉取到本地
        self.run_adb_command(f"pull {remote_path} {local_path}")

        # 删除设备上的截图
        self.run_adb_command(f"shell rm {remote_path}")

        if os.path.exists(local_path):
            # 获取原始截图尺寸
            with Image.open(local_path) as img:
                self.original_width, self.original_height = img.size
            return local_path
        return None

    def find_coordinates_interactive(self):
        """交互式坐标查找工具"""
        print("正在获取设备截图...")
        self.screenshot_path = self.take_screenshot()

        if not self.screenshot_path:
            print("截图失败")
            return None

        # 创建GUI界面
        return self.create_coordinate_picker()

    def create_coordinate_picker(self):
        """创建坐标选择界面"""
        root = tk.Tk()
        root.title("安卓坐标选择器 - 点击图片获取坐标")

        # 加载图片
        try:
            image = Image.open(self.screenshot_path)

            # 记录原始尺寸
            orig_width, orig_height = image.size

            # 调整图片大小以适应屏幕
            screen_width = root.winfo_screenwidth() - 100
            screen_height = root.winfo_screenheight() - 150

            if image.width > screen_width or image.height > screen_height:
                ratio = min(screen_width / image.width, screen_height / image.height)
                new_size = (int(image.width * ratio), int(image.height * ratio))
                image = image.resize(new_size, Image.Resampling.LANCZOS)

            photo = ImageTk.PhotoImage(image)

            # 创建画布
            canvas = tk.Canvas(root, width=image.width, height=image.height)
            canvas.pack()

            # 显示图片
            canvas.create_image(0, 0, anchor=tk.NW, image=photo)

            # 坐标显示标签
            coord_label = tk.Label(root, text="点击图片获取坐标", font=("Arial", 12))
            coord_label.pack(pady=10)

            # 点击事件处理
            def on_click(event):
                x, y = event.x, event.y

                # 正确计算原始坐标（考虑缩放比例）
                scale_x = orig_width / image.width
                scale_y = orig_height / image.height
                original_x = int(x * scale_x)
                original_y = int(y * scale_y)

                coord_label.config(text=f"坐标: ({original_x}, {original_y})")
                print(f"获取到坐标: ({original_x}, {original_y})")

                # 询问用户是否使用此坐标
                use_coord = tkinter.messagebox.askyesno("确认坐标",
                                                        f"是否使用坐标 ({original_x}, {original_y})？")
                if use_coord:
                    root.coordinates = (original_x, original_y)
                    root.quit()

            canvas.bind("<Button-1>", on_click)

            # 添加说明
            info_label = tk.Label(root, text="点击图片中的目标位置获取坐标",
                                  font=("Arial", 10), fg="blue")
            info_label.pack(pady=5)

            root.mainloop()

            if hasattr(root, 'coordinates'):
                return root.coordinates
            else:
                return None

        except Exception as e:
            print(f"创建坐标选择器失败: {str(e)}")
            return None


# 使用示例
def main():
    finder = CoordinateFinder()
    coordinates = finder.find_coordinates_interactive()

    if coordinates:
        x, y = coordinates
        print(f"\n最终选择的坐标: ({x}, {y})")
        print("您可以在自动化脚本中使用这些坐标")

        # 测试点击
        test = input("是否测试点击此坐标? (y/n): ")
        if test.lower() == 'y':
            finder.run_adb_command(f"shell input tap {x} {y}")
            print("点击完成")
    else:
        print("未获取到坐标")


if __name__ == "__main__":
    main()