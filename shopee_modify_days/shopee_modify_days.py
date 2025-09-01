import asyncio
import logging
import random
import sys

from playwright.async_api import async_playwright

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())
# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 登录地址
LOGIN_URL = 'https://seller.shopee.cn/account/signin'
WAIT_TIME = random.uniform(1.5, 2)
# 任务账号 (修正为元组列表)
ACCOUNTS = [
    ('BrownShane3035:main', 'Aa123456.'),
    ('GibsonBrenda1091:main', 'Aa123456.'),
    # 添加更多账号...
]


async def login(page, username, password):
    """执行登录操作"""
    logger.info(f"开始登录: {username}")
    try:
        # 导航到登录页
        await page.goto(LOGIN_URL, timeout=60000, wait_until="domcontentloaded")

        # 填写登录表单（根据实际网站元素修改选择器）
        await page.fill('xpath=(//div[@class="eds-input__inner eds-input__inner--large"])[1]', username)
        await page.fill('xpath=(//div[@class="eds-input__inner eds-input__inner--large"])[2]', password)

        # 点击登入
        await page.click('(//button[@type="button"])[1]')

        # 等待登录成功（示例：等待导航完成）
        await page.wait_for_url('**/cnsc_shop_id/**', timeout=30000)
        logger.info(f"登录成功: {username}")
        return True
    except Exception as e:
        logger.error(f"登录失败: {username} - {str(e)}")
        return False


async def process_account(page, account, account_idx):
    """处理单个账号的任务"""
    username, password = account
    try:
        # 登录账号
        login_success = await login(page, username, password)
        if not login_success:
            return False

        # 这里添加登录后的具体业务逻辑
        logger.info(f"开始处理任务 #{account_idx + 1} - {username}")



        await asyncio.sleep(WAIT_TIME)

        logger.info(f"账号处理完成: {username}")
        return True
    except Exception as e:
        logger.error(f"处理账号 {username} 时出错: {str(e)}")
        return False


async def main():
    """主程序入口"""
    # 启动Playwright
    async with async_playwright() as p:
        # 创建持久化浏览器上下文
        context = await p.chromium.launch_persistent_context(
            user_data_dir=r"D:\project\myProject\shopee_modify_days\chrome9601",
            headless=False,
            args=[
                "--disable-gpu",
                "--disable-dev-shm-usage",
                "--no-sandbox",
                "--disable-blink-features=AutomationControlled",
            ]
        )
        logger.info("浏览器上下文创建成功")

        try:
            # 创建主页
            page = await context.new_page()
            page.set_default_timeout(60000)

            # 处理所有账号（顺序执行）
            for idx, account in enumerate(ACCOUNTS):
                logger.info(f"开始处理账号 #{idx + 1}/{len(ACCOUNTS)}")
                result = await process_account(page, account, idx)

                status = "成功" if result else "失败"
                logger.info(f"账号 #{idx + 1} 处理状态: {status}")

                # 任务间等待
                await asyncio.sleep(3)

        except Exception as e:
            logger.error(f"主程序出错: {str(e)}")
        finally:
            # 确保关闭浏览器
            await context.close()
            logger.info("浏览器上下文已关闭")


if __name__ == "__main__":
    asyncio.run(main())
