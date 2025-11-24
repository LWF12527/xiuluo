import os
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from tkinter import *
from tkinter import filedialog, scrolledtext, messagebox
from openpyxl import Workbook


def imread_utf8(path):
    """解决 cv2.imread 无法读取中文路径"""
    try:
        with open(path, "rb") as f:
            data = f.read()
        img_array = np.frombuffer(data, np.uint8)
        return cv2.imdecode(img_array, cv2.IMREAD_GRAYSCALE)
    except:
        return None


def compute_similarity(img_path1, img_path2):
    """计算两张图片的 SSIM 相似度"""
    img1 = imread_utf8(img_path1)
    img2 = imread_utf8(img_path2)

    if img1 is None or img2 is None:
        return None

    try:
        h = max(img1.shape[0], img2.shape[0])
        w = max(img1.shape[1], img2.shape[1])
        img1 = cv2.resize(img1, (w, h))
        img2 = cv2.resize(img2, (w, h))

        score, _ = ssim(img1, img2, full=True)
        return score
    except:
        return None


def choose_folder(entry_box):
    folder = filedialog.askdirectory()
    if folder:
        entry_box.delete(0, END)
        entry_box.insert(0, folder)


def start_compare():
    global results
    results = []  # 清空之前记录

    folder1 = folder1_entry.get().strip()
    folder2 = folder2_entry.get().strip()
    threshold = float(threshold_entry.get().strip())

    if not os.path.isdir(folder1) or not os.path.isdir(folder2):
        messagebox.showerror("错误", "请选择有效的两个文件夹！")
        return

    log_box.insert(END, f"开始比较:\n文件夹1: {folder1}\n文件夹2: {folder2}\n阈值: {threshold}\n\n")
    log_box.update()

    exts = (".png", ".jpg", ".jpeg", ".bmp")

    try:
        imgs1 = [os.path.join(folder1, f) for f in os.listdir(folder1) if f.lower().endswith(exts)]
        imgs2 = [os.path.join(folder2, f) for f in os.listdir(folder2) if f.lower().endswith(exts)]
    except Exception as e:
        log_box.insert(END, f"读取文件夹失败：{e}\n")
        return

    if not imgs1 or not imgs2:
        log_box.insert(END, "其中一个文件夹没有图片。\n")
        return

    for f1 in imgs1:
        for f2 in imgs2:
            score = compute_similarity(f1, f2)
            if score is None:
                continue

            if score >= threshold:
                msg = f"[相似] {score:.4f}\n  {f1}\n  {f2}\n\n"
                log_box.insert(END, msg)
                log_box.update()

                # 保存到结果列表
                results.append((score, f1, f2))

    log_box.insert(END, "------ 比较完成 ------\n")
    log_box.update()


def export_excel():
    if not results:
        messagebox.showwarning("提示", "暂无可导出的数据，请先进行比较。")
        return

    folder1 = folder1_entry.get().strip()
    folder2 = folder2_entry.get().strip()

    folder1_name = os.path.basename(folder1)
    folder2_name = os.path.basename(folder2)

    import time
    timestamp = time.strftime("%Y%m%d_%H%M%S")
    default_filename = f"{folder1_name}_{folder2_name}_{timestamp}.xlsx"

    save_path = filedialog.asksaveasfilename(
        initialfile=default_filename,
        defaultextension=".xlsx",
        filetypes=[("Excel 文件", "*.xlsx")],
        title="保存为 Excel 文件"
    )

    if not save_path:
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "相似度结果"

    # 写表头
    ws.append(["相似度", "图片1路径", "图片2路径"])

    # 写内容
    for score, f1, f2 in results:
        ws.append([score, f1, f2])

    wb.save(save_path)

    messagebox.showinfo("完成", f"Excel 已成功导出：\n{save_path}")



# ---------------- GUI -----------------

root = Tk()
root.title("图片相似度筛选工具（SSIM）")
root.geometry("900x700")

# 文件夹选择 1
Label(root, text="文件夹 1：", font=("微软雅黑", 10)).pack()
folder1_entry = Entry(root, width=100)
folder1_entry.pack()
Button(root, text="选择文件夹 1", command=lambda: choose_folder(folder1_entry)).pack()

# 文件夹选择 2
Label(root, text="文件夹 2：", font=("微软雅黑", 10)).pack()
folder2_entry = Entry(root, width=100)
folder2_entry.pack()
Button(root, text="选择文件夹 2", command=lambda: choose_folder(folder2_entry)).pack()

# 阈值设置
Label(root, text="相似度阈值（0~1）：", font=("微软雅黑", 10)).pack()
threshold_entry = Entry(root, width=10)
threshold_entry.insert(0, "0.5")
threshold_entry.pack()

# 操作按钮
Button(root, text="开始比较", height=2, width=20, command=start_compare).pack(pady=10)
Button(root, text="导出为 Excel", height=2, width=20, command=export_excel).pack(pady=5)

# 日志输出窗口
Label(root, text="日志输出：", font=("微软雅黑", 10)).pack()
log_box = scrolledtext.ScrolledText(root, width=110, height=25, font=("Consolas", 10))
log_box.pack()

# 结果存储（全局变量）
results = []

root.mainloop()
