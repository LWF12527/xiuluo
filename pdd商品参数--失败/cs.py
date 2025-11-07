import asyncio
from loguru import logger
import os
import random
import sys
import time
from collections import defaultdict

from playwright_stealth import Stealth

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from playwright.async_api import async_playwright

PORT = 9401
MAX_CONCURRENT_TASKS = 1  # 并发任务数量
TEST_REQUESTS = 10  # 总共请求次数
REQUEST_DELAY = 1.0  # 请求间隔时间(秒)
MIN_SUCCESS_LENGTH = 100000  # 成功的最小内容长度修改为100,000字节


# 固定测试URL
TEST_URL = 'https://mobile.yangkeduo.com/goods.html?goods_id=646412814724&page_from=23&_oc_trace_mark=199&pxq_secret_key=X67STX55YTEKXLNROANJYN3SITN3PPRSY4DH2RPYVQYIZMPZSPMQ&_oak_share_snapshot_num=9234&_oak_share_detail_id=11049298564&_oak_share_time=1762401651&share_oak_rcto=YWJh5yobti54i9JYDLHRocyaQVTSDk2lTYKYUDjBkmkvOHEFNGqroopvtBeyG2s1sXoIme6M_T7HIw&share_uin=IKHNWPHXIOUGBXPTTRWCGVSB4A_GEXDA&refer_share_id=25f8edbcd1d1472382f3e25258ae2594&refer_share_uin=IKHNWPHXIOUGBXPTTRWCGVSB4A_GEXDA&refer_share_channel=copy_link&refer_share_form=text&_x_share_id=25f8edbcd1d1472382f3e25258ae2594&refer_page_name=login&refer_page_id=10169_1762406858739_ncl98krp4r&refer_page_sn=10169&uin=ICAYJDEEP6XEXOZM6ICCDWIX5I_GEXDA'


async def fetch_page(context, request_id):
    """获取网页内容并返回长度和状态"""
    page = None
    try:
        page = await context.new_page()

        # 记录开始时间
        start_time = time.time()

        # 导航到页面
        await page.goto(TEST_URL, timeout=20000, wait_until="domcontentloaded")

        # 点击按钮-去拼单
        await page.wait_for_selector('xpath=//span[@class and @style and text()="限量价"]', state='visible', timeout=10000)
        button = page.locator('//span[@class and @style and text()="限量价"]')
        await button.click()

        # 等待属性出现
        await page.wait_for_selector('//span[@class="sku-specs-key"]', state='visible', timeout=10000)
        # 点击value1-白色 //span[@class="sku-specs-key"][.="颜色"]/following-sibling::div/div[.="白色"]
        button = page.locator('//span[@class="sku-specs-key"][.="颜色"]/following-sibling::div/div[.="白色"]')
        await button.click()
        # 点击value2-10个320箱（35-27-13）cm //span[@class="sku-specs-key"][.="尺寸"]/following-sibling::div/div[.="10个320箱（35-27-13）cm"]
        button = page.locator('//span[@class="sku-specs-key"][.="尺寸"]/following-sibling::div/div[.="10个320箱（35-27-13）cm"]')
        await button.click()

        # 获取价格 //span[@style="font-size: 0.19rem;"] 整数  //span[@style="font-size: 0.16rem;"]小数
        # 等待元素加载
        try:
            await page.wait_for_selector('//span[@style="font-size: 0.19rem;"]', timeout=5000)
        except Exception as e:
            logger.debug('价格不存在')

        try:
            await page.wait_for_selector('//span[@style="font-size: 0.16rem;"]', timeout=5000)
        except Exception as e :
            logger.debug('检查是否有小数')

        # 获取整数部分
        integer_element =await page.query_selector('//span[@style="font-size: 0.19rem;"]')
        integer_part = integer_element.inner_text() if integer_element else ""

        # 获取小数部分
        decimal_element =await page.query_selector('//span[@style="font-size: 0.16rem;"]')
        decimal_part = decimal_element.inner_text() if decimal_element else ""
        # 组合成完整价格
        if integer_part:
            price = f"{integer_part}.{decimal_part}"
            # 转换为浮点数（如果需要）
            price_value = float(price)
            print(f"获取到的价格: {price_value}")
            return price_value
        else:
            print("未找到价格元素")
            return None
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
        await asyncio.sleep(0.5)


async def worker(context, semaphore, request_id, results):
    """并发工作函数"""
    async with semaphore:
        # 添加随机延迟避免同时发起请求
        delay = random.uniform(0, REQUEST_DELAY)
        await asyncio.sleep(delay)

        result = await fetch_page(context, request_id)
        results.append(result)
        return result


async def main():
    """主程序入口 - 并发测试"""
    async with Stealth().use_async(async_playwright()) as p:
        browser = await p.chromium.connect_over_cdp("http://localhost:" + str(PORT))

        try:
            # 获取浏览器上下文
            contexts = browser.contexts
            if not contexts:
                context = await browser.new_context()
            else:
                context = contexts[0]  # 使用第一个可用上下文

            logger.info(f"开始并发测试，URL: {TEST_URL}")
            logger.info(f"总请求数: {TEST_REQUESTS}, 并发数: {MAX_CONCURRENT_TASKS}")
            logger.info(f"成功标准: 内容长度 > {MIN_SUCCESS_LENGTH} 字符")

            # 创建任务列表
            tasks = []
            results = []
            semaphore = asyncio.Semaphore(MAX_CONCURRENT_TASKS)

            # 启动所有任务
            for i in range(TEST_REQUESTS):
                task = asyncio.create_task(worker(context, semaphore, i + 1, results))
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