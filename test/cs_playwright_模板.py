import asyncio
from loguru import logger
import os
import random
import sys
import tempfile
import time
from collections import defaultdict

import cv2
import numpy as np
from PIL import Image
from playwright_stealth import Stealth

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from playwright.async_api import async_playwright


MAX_CONCURRENT_TASKS = 5  # 并发任务数量
TEST_REQUESTS = 10  # 总共请求次数
REQUEST_DELAY = 1.0  # 请求间隔时间(秒)
MIN_SUCCESS_LENGTH = 100000  # 成功的最小内容长度修改为100,000字节

# 增强的指纹防护配置
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (iPad; CPU OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Linux; Android 11; SM-G991B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.120 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) FxiOS/36.0 Mobile/15E148 Safari/605.1.15"
]

VIEWPORT_SIZES = [
    {'width': 1920, 'height': 1080},
    {'width': 1366, 'height': 768},
    {'width': 1536, 'height': 864},
    {'width': 1440, 'height': 900},
    {'width': 1280, 'height': 720},
    {'width': 1600, 'height': 900},
    {'width': 1024, 'height': 768},
    {'width': 800, 'height': 600},
    {'width': 414, 'height': 896},  # iPhone XR
    {'width': 375, 'height': 812}  # iPhone X
]

# 固定测试URL
TEST_URL = 'https://www.onbuy.com/gb/p/kitchen-metal-dish-drainer-rack-organizer-sink-with-removable-drip-tray~p124683456/'

async def handle_captcha(page, task_id=None):
    """处理验证码（对整个页面截图后进行模板匹配）"""
    try:
        start_time = time.time()
        refresh_count = 0
        max_refreshes = 3

        while time.time() - start_time < 120:  # 最多尝试2分钟
            content = await page.content()

            # 检测验证码关键词
            has_captcha = any(phrase in content for phrase in [
                '验证您是真人',
                'Verifying you are human',
                'Just a moment',
                'Nous vérifions que vous êtes humain'
            ])

            if has_captcha:
                if refresh_count < max_refreshes:
                    # 尝试刷新页面
                    logger.info(f'ID={task_id} 检测到验证码，正在进行第 {refresh_count + 1}/{max_refreshes} 次刷新...')
                    await page.reload()
                    refresh_count += 1
                    await asyncio.sleep(3)
                    continue
                else:
                    # 刷新失败后的处理
                    logger.warning(f'ID={task_id} {max_refreshes}次刷新未解决验证码，准备点击验证码...')
                    return await _process_captcha_directly(page, task_id)
            else:
                # 验证码已消失时的处理
                if refresh_count > 0:
                    logger.info(f'ID={task_id} 刷新成功！验证码已消失')
                # else:
                #     logger.info(f'ID={task_id} 页面无验证码')
                return True

        logger.error(f"ID={task_id} 验证码处理超时(120秒)")
        return False

    except Exception as e:
        logger.error(f'ID={task_id} 验证码处理失败: {str(e)}')
        return False


async def _process_captcha_directly(page, task_id=None):
    """直接处理验证码（截图+模板匹配）"""
    try:
        yzm_png = '验证码.png' if '真人' in await page.content() else '验证码es.png'
        # 等待页面稳定
        await asyncio.sleep(5)
        logger.info(f'ID={task_id} 开始验证码识别流程...')

        # 步骤1: 对整个页面进行截图
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as tmp_file:
            screenshot_path = tmp_file.name

        await page.screenshot(path=screenshot_path, full_page=True, timeout=60000)
        logger.debug(f'ID={task_id} 页面截图保存至: {screenshot_path}')

        # 步骤2: 图像识别匹配
        template_path = rf'D:\project\collect_reverse\manomano\{yzm_png}'

        if not os.path.exists(template_path):
            logger.error(f'模板图片不存在: {template_path}')
            return False

        # 读取模板图片
        try:
            template_pil = Image.open(template_path)
            template = np.array(template_pil)
            if template.shape[2] == 4:
                template = cv2.cvtColor(template, cv2.COLOR_RGBA2RGB)
            elif len(template.shape) == 2:
                template = cv2.cvtColor(template, cv2.COLOR_GRAY2BGR)
        except Exception as img_error:
            logger.error(f'读取模板失败: {str(img_error)}')
            return False

        # 读取页面截图
        screenshot = cv2.imread(screenshot_path)
        if screenshot is None:
            logger.error(f'页面截图读取失败: {screenshot_path}')
            return False

        # 转换为灰度图提高处理速度
        gray_screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
        gray_template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

        # 多尺度模板匹配
        scales = [0.8, 0.9, 1.0, 1.1, 1.2]
        max_confidence = 0
        best_location = None
        best_size = None

        for scale in scales:
            resized_template = cv2.resize(gray_template, None, fx=scale, fy=scale)
            rH, rW = resized_template.shape

            if rW > gray_screenshot.shape[1] or rH > gray_screenshot.shape[0]:
                continue

            result = cv2.matchTemplate(gray_screenshot, resized_template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(result)

            if max_val > max_confidence:
                max_confidence = max_val
                best_location = max_loc
                best_size = (rW, rH)

        logger.debug(f'ID={task_id} 最高匹配置信度: {max_confidence:.2f}')

        # 检查匹配度
        if max_confidence < 0.4:
            logger.warning(f'ID={task_id} 识别置信度过低({max_confidence:.2f}<0.4)，放弃点击')
            return False

        # 计算点击位置
        click_x = best_location[0] + best_size[0] // 2
        click_y = best_location[1] + best_size[1] // 2
        logger.info(f'ID={task_id} 准备点击坐标: ({click_x}, {click_y})')

        # 执行点击
        await page.mouse.click(click_x, click_y)
        logger.info(f'ID={task_id} 已成功点击验证码')

        # 等待验证完成
        await asyncio.sleep(10)
        logger.info(f'ID={task_id} 完成验证等待流程')

        return True

    except Exception as e:
        logger.error(f'ID={task_id} 验证码识别流程失败: {str(e)}')
        return False

    finally:
        # 清理临时文件
        if 'screenshot_path' in locals() and os.path.exists(screenshot_path):
            try:
                os.unlink(screenshot_path)
            except Exception as e:
                logger.warning(f'删除临时文件失败: {str(e)}')



async def fetch_page(browser, request_id):
    """获取网页内容并返回长度和状态"""
    page = None
    context = None
    try:
        # 为每个请求使用不同的指纹
        user_agent = random.choice(USER_AGENTS)
        viewport = random.choice(VIEWPORT_SIZES)
        logger.info(f"请求 #{request_id}: 使用 UA: {user_agent[:40]}...")

        context = await browser.new_context(
            user_agent=user_agent,
            viewport=viewport,
            java_script_enabled=True,
            ignore_https_errors=True,
            extra_http_headers={
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
                'DNT': '1',
                'Upgrade-Insecure-Requests': '1',
                'Cache-Control': 'max-age=0'
            }
        )
        page = await context.new_page()

        # 记录开始时间
        start_time = time.time()

        # 导航到页面
        await page.goto(TEST_URL, timeout=60000, wait_until="domcontentloaded")

        # 验证码处理
        await handle_captcha(page)


        # 获取页面内容
        content = await page.content()
        length = len(content)

        # 计算耗时
        elapsed = time.time() - start_time

        # 根据内容长度判断成功或失败
        if length > MIN_SUCCESS_LENGTH:
            status = "success"
            logger.info(f"请求 #{request_id} 成功! 内容长度: {length} 字符, 耗时: {elapsed:.2f}秒")
        else:
            status = "short_content"
            logger.warning(f"请求 #{request_id} 内容过短! 长度: {length} 字符 (<{MIN_SUCCESS_LENGTH}), 耗时: {elapsed:.2f}秒")

        return {"status": status, "length": length, "time": elapsed}

    except asyncio.TimeoutError:
        logger.error(f"请求 #{request_id} 超时")
        return {"status": "timeout", "length": 0, "time": 0}
    except Exception as e:
        logger.error(f"请求 #{request_id} 失败: {str(e)}")
        return {"status": "error", "length": 0, "time": 0}
    finally:
        if page and not page.is_closed():
            await page.close()
        if context:
            await context.close()
        await asyncio.sleep(0.5)


async def worker(browser, semaphore, request_id, results):
    """并发工作函数"""
    async with semaphore:
        # 添加随机延迟避免同时发起请求
        delay = random.uniform(0, REQUEST_DELAY)
        await asyncio.sleep(delay)

        result = await fetch_page(browser, request_id)
        results.append(result)
        return result


async def main():
    """主程序入口 - 并发测试"""
    async with Stealth().use_async(async_playwright()) as p:
        browser = await p.chromium.launch(
            headless=False,
            args=[
                '--disable-blink-features=AutomationControlled',
                '--disable-infobars',
                '--no-first-run',
                '--no-default-browser-check',
                '--disable-popup-blocking',
                '--disable-extensions',
                '--disable-notifications',
                '--disable-gpu',
                '--disable-dev-shm-usage',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-web-security',
                '--disable-features=IsolateOrigins,site-per-process',
                '--disable-blink-features=AutomationControlled'
            ]
        )

        try:
            logger.info(f"开始并发测试，URL: {TEST_URL}")
            logger.info(f"总请求数: {TEST_REQUESTS}, 并发数: {MAX_CONCURRENT_TASKS}")
            logger.info(f"成功标准: 内容长度 > {MIN_SUCCESS_LENGTH} 字符")

            # 创建任务列表
            tasks = []
            results = []
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TASKS)

            # 启动所有任务
            for i in range(TEST_REQUESTS):
                task = asyncio.create_task(worker(browser, semaphore, i + 1, results))
                tasks.append(task)

            # 等待所有任务完成
            await asyncio.gather(*tasks)

            # 分析结果
            status_counts = defaultdict(int)
            total_length = 0
            total_time = 0
            success_count = 0

            for result in results:
                status_counts[result['status']] += 1
                if result['status'] == 'success':
                    total_length += result['length']
                    total_time += result['time']
                    success_count += 1

            # 计算成功率
            success_rate = (success_count / TEST_REQUESTS) * 100 if TEST_REQUESTS > 0 else 0

            # 输出汇总报告
            print("\n" + "=" * 50)
            print("测试结果汇总:")
            print("=" * 50)
            print(f"总请求数: {TEST_REQUESTS}")
            print(f"成功 (长度 > {MIN_SUCCESS_LENGTH}): {status_counts['success']} 次")
            print(f"内容过短: {status_counts['short_content']} 次")
            print(f"超时: {status_counts['timeout']} 次")
            print(f"错误: {status_counts['error']} 次")
            print(f"成功率: {success_rate:.2f}%")  # 添加成功率显示

            if success_count > 0:
                avg_length = total_length / success_count
                avg_time = total_time / success_count
                print(f"\n成功请求平均内容长度: {avg_length:.0f} 字符")
                print(f"成功请求平均耗时: {avg_time:.2f} 秒")

            # 计算总体成功率
            overall_success_rate = (status_counts['success'] / TEST_REQUESTS) * 100
            print(f"\n总体成功率: {overall_success_rate:.1f}%")
            print("=" * 50)

            return results

        finally:
            await browser.close()


if __name__ == "__main__":
    print("开始并发性能测试...")
    test_results = asyncio.run(main())

    # 输出详细结果
    print("\n详细结果:")
    for i, result in enumerate(test_results, 1):
        if result['status'] == 'success':
            status_icon = "✅"
            status_text = f"SUCCESS ({result['length']} chars)"
        elif result['status'] == 'short_content':
            status_icon = "⚠️"
            status_text = f"SHORT CONTENT ({result['length']}/{MIN_SUCCESS_LENGTH} chars)"
        elif result['status'] == 'timeout':
            status_icon = "⏱️"
            status_text = "TIMEOUT"
        else:
            status_icon = "❌"
            status_text = "ERROR"

        print(f"请求 #{i}: {status_icon} {status_text}, 耗时: {result['time']:.2f}s")

    print("\n测试完成!")