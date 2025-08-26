import os
import sys

from you_get import common as you_get

tx_cookie={}
tx_header={}

# 视频网址
url_blbl='https://www.douyin.com/video/7394122966067350822'
url = "https://v.youku.com/v_show/id_XNjQ3MTc1MDYwMA==.html?s=eaea48e7a4c746c7b62b&scm=20140719.manual.48260.show_eaea48e7a4c746c7b62b&spm=a2hkl.14919748_WEBHOME_HOME.drawer1.d_zj1_1"
url_vip = "https://v.youku.com/v_show/id_XNjQ3MjM2NTAyNA==.html?s=eaea48e7a4c746c7b62b&scm=20140719.apircmd.298496.video_XNjQ3MjM2NTAyNA==&spm=a2hkt.13141534.1_6.d_1_8"

# 设置文件存储地址
dir = "D:\Downloads"

# 设置ffmpeg到项目环境  ffmpeg用于下载优酷的m3u8视频
os.environ["path"] = os.environ.get("path") + r";C:\film\ffmpeg-20160626-074fdf4-win32-static\bin"
sys.argv = ["you-get", "--debug", "-o", dir, url_blbl]  # 下载视频
# sys.argv = ["you-get","-i",url]#查看视频信息
# sys.argv = ["you-get","--format=4k","-o",dir,url]#选择清晰度下载视频

# # 使用 Cookie 下载
# sys.argv = [
#     "you-get",
#     "--debug",          # 调试模式
#     "--cookies", tx_cookie,  # 指定 Cookie 文件
#     "-o",
#     dir,          # 下载目录
#     url_vip             # 视频地址
# ]

you_get.main()
