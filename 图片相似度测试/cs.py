from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np
import glob

def compute_similarity(img_path1, img_path2):
    # 读取图像（灰度模式）
    img1 = cv2.imread(img_path1, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img_path2, cv2.IMREAD_GRAYSCALE)

    # 调整为相同尺寸
    h = max(img1.shape[0], img2.shape[0])
    w = max(img1.shape[1], img2.shape[1])
    img1_resized = cv2.resize(img1, (w, h))
    img2_resized = cv2.resize(img2, (w, h))

    # 计算 SSIM
    score, diff = ssim(img1_resized, img2_resized, full=True)
    return score

# 示例：比较两张图
img1 = "1.png"
img2 = "2.png"

similarity_score = compute_similarity(img1, img2)
print("图片相似度（SSIM）:", similarity_score)
