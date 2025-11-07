import concurrent.futures
import yt_dlp
import os
import random

from fake_useragent import UserAgent


class YouTubeDownloader:
    def __init__(self):
        self.output_dir = "YouTube_Downloads"
        os.makedirs(self.output_dir, exist_ok=True)

        # 设置 FFmpeg 路径
        self.ffmpeg_path = r"E:\ffmpeg-8.0-full_build\bin\ffmpeg.exe"  # 直接指定 FFmpeg 路径
        self.ffprobe_path = r"E:\ffmpeg-8.0-full_build\bin\ffprobe.exe"  # 如果需要的话

    def random_header(self, url):
        # 随机生成设备像素比 (常见范围0.5-3.0，保留两位小数)
        dpr = round(random.uniform(0.5, 3.0), 2)
        # 随机生成网络下行速度 (0.5-100 Mbps，保留两位小数)
        downlink = round(random.uniform(0.5, 100.0), 2)
        v4 = random.choice([6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36])
        headers_or = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Connection": "keep-alive",
            "DNT": "1",
            "Origin": "https://www.youtube.com",
            "Referer": "https://www.youtube.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Storage-Access": "none",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
            "X-Browser-Channel": "stable",
            "X-Browser-Copyright": "Copyright 2025 Google LLC. All rights reserved.",
            "X-Browser-Validation": "AGaxImjg97xQkd0h3geRTArJi8Y=",
            "X-Browser-Year": "2025",
            "X-Client-Data": "CKW1yQEIkLbJAQiktskBCKmdygEIo43LAQiWocsBCLCkywEIhaDNAQjc1s4BCOjkzgEI1IjPAQjLi88BCJaMzwEIpIzPAQiOjs8BCOyOzwEIpY/PAQiekc8BGKWHzwEYmIjPARjFi88B",
            "sec-ch-ua": "\"Google Chrome\";v=\"141\", \"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"141\"",
            "sec-ch-ua-arch": "\"x86\"",
            "sec-ch-ua-bitness": "\"64\"",
            "sec-ch-ua-form-factors": "\"Desktop\"",
            "sec-ch-ua-full-version": "\"141.0.7390.76\"",
            "sec-ch-ua-full-version-list": "\"Google Chrome\";v=\"141.0.7390.76\", \"Not?A_Brand\";v=\"8.0.0.0\", \"Chromium\";v=\"141.0.7390.76\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-model": "\"\"",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-ch-ua-platform-version": "\"15.0.0\"",
            "sec-ch-ua-wow64": "?0"
        }
        headers = {
            "apollographql-client-name": "spartacux-b2c",
            "apollographql-client-version": "1.0",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "sec-gpc": "1",
            "upgrade-insecure-requests": "1",
            **headers_or,
            "sec-ch-ua": f"\"Not)A;Brand\";v=\"{v4}\", \"Chromium\";v=\"138\", \"Brave\";v=\"138\"",
            "accept-language": random.choice(['zh-CN,zh;q=0.9', 'en-US,en;q=0.9', 'en-GB,en;q=0.9']),
            "downlink": str(downlink),  # 动态下行速度
            "dpr": str(dpr),  # 动态设备像素比
            "referer": url,
            f"x-rand{random.randint(100, 999)}": str(random.randint(1000000, 9999999)),
            "user-agent": UserAgent().random
        }
        return headers

    def proxy_qgsd(self):
        pass
        return None

    def get_random_user_agent(self):
        return random.choice(self.user_agents)

    def download_video(self, url):
        """下载单个视频"""
        # 添加输出路径配置和FFmpeg路径
        ydl_opts = {
            'outtmpl': os.path.join(self.output_dir, '%(title)s.%(ext)s'),
            'ffmpeg_location': self.ffmpeg_path,  # 指定FFmpeg路径
            'user_agent': self.random_header(url),
            # 'proxy': None,  # 代理配置
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                if info:
                    print(f"下载完成: {info.get('title', '未知标题')}")
                    return True
                else:
                    print(f"下载失败: 无法获取视频信息 - {url}")
                    return False
        except Exception as e:
            print(f"下载失败: {url} - {str(e)}")
            return False

    def batch_download(self, url_list, max_workers=10):
        """批量下载视频"""
        print(f"开始批量下载 {len(url_list)} 个视频...")
        success_count = 0
        fail_count = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_url = {executor.submit(self.download_video, url): url for url in url_list}

            for future in concurrent.futures.as_completed(future_to_url):
                url = future_to_url[future]
                try:
                    success = future.result()
                    if success:
                        success_count += 1
                        print(f"成功下载: {url}")
                    else:
                        fail_count += 1
                        print(f"下载失败: {url}")
                except Exception as e:
                    fail_count += 1
                    print(f"处理异常: {url} - {str(e)}")

        print(f"\n下载完成! 成功: {success_count}, 失败: {fail_count}")
        return success_count, fail_count


# 使用示例
if __name__ == "__main__":
    downloader = YouTubeDownloader()

    # 检查FFmpeg路径是否存在
    if os.path.exists(downloader.ffmpeg_path):
        print(f"FFmpeg路径正确: {downloader.ffmpeg_path}")
    else:
        print(f"警告: FFmpeg路径不存在: {downloader.ffmpeg_path}")
        print("请检查FFmpeg安装路径是否正确")

    with open('urls.txt', 'r') as f:
        url_list = [line.strip() for line in f.readlines() if line.strip()]
        # 开始批量下载（使用3个线程）
        downloader.batch_download(url_list, max_workers=10)