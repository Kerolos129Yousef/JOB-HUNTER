import asyncio

from playwright.async_api import async_playwright


async def log_request(request):
    url = request.url.lower()

    # نطبع فقط الطلبات الخاصة بـ Ashby أو GraphQL
    if "ashby" not in url and "graphql" not in url:
        return

    print("\n" + "=" * 100)
    print("METHOD :", request.method)
    print("URL    :", request.url)

    headers = await request.all_headers()

    print("\nHEADERS")
    print("-" * 100)
    for key, value in headers.items():
        print(f"{key}: {value}")

    if request.post_data:
        print("\nPOST DATA")
        print("-" * 100)
        print(request.post_data)


async def log_response(response):
    url = response.url.lower()

    if "ashby" not in url and "graphql" not in url:
        return

    print("\nRESPONSE STATUS:", response.status)

    try:
        body = await response.text()
        print("\nRESPONSE BODY")
        print("-" * 100)
        print(body[:3000])
    except Exception as e:
        print(e)


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=False,
            slow_mo=300,
        )

        context = await browser.new_context()

        page = await context.new_page()

        page.on(
            "request",
            lambda request: asyncio.create_task(log_request(request)),
        )

        page.on(
            "response",
            lambda response: asyncio.create_task(log_response(response)),
        )

        await page.goto(
            "https://openai.com/careers/search",
            wait_until="networkidle",
        )

        print("\nصفح صفحة الوظائف أو استخدم الفلاتر.")
        input("\nاضغط Enter بعد ظهور الوظائف...")

        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())