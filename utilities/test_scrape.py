import json
import asyncio
import random
from playwright.async_api import async_playwright

product_list = [
    {"id": 0, "url": "https://www.woolworths.com.au/shop/productdetails/134034/gourmet-tomato"},
    {"id": 1, "url": "https://www.woolworths.com.au/shop/productdetails/137130/lebanese-cucumbers"},
    # ... add your full list here
]

async def scrape_products():
    results = []
    async with async_playwright() as p:
        # 1. Use a real browser profile and disable automation flags
        browser = await p.chromium.launch(headless=False) # Headless=False helps avoid detection
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            viewport={'width': 1920, 'height': 1080}
        )
        page = await context.new_page()

        for item in product_list:
            try:
                print(f"Opening: {item['url']}")
                # 2. Wait for 'domcontentloaded' instead of 'networkidle'
                await page.goto(item['url'], wait_until="domcontentloaded", timeout=60000)
                
                # 3. Use updated 2026 CSS Selectors (They often change class names)
                # We use a broad 'h1' search if the specific class fails
                await page.wait_for_selector("h1", timeout=15000)
                
                name = await page.inner_text("h1")
                # 3. Extract Price using the shared-price component
                # We look for the dollar and cent parts specifically
                dollars = await page.inner_text(".price-dollars")
                cents = await page.inner_text(".price-cents")
                full_price = f"{dollars}.{cents}"
                
                # 4. Extract Unit Price (e.g., "$12.00 / 1kg")
                unit_price = await page.inner_text(".price-cup")
                
                results.append({
                    "id": item['id'],
                    "name": name.strip(),
                    "price": float(full_price),
                    "unit_price": unit_price.strip(),
                    "url": item['url']
                })
                
                # 4. Human-like delay: Don't blitz the server!
                await asyncio.sleep(random.uniform(3, 7)) 
                
            except Exception as e:
                print(f"Blocked or Timeout on ID {item['id']}: {e}")
                # If blocked, wait longer before next attempt
                await asyncio.sleep(10)

        with open('mongo_collection.json', 'w') as f:
            json.dump(results, f, indent=4)
        
        await browser.close()

if __name__ == "__main__":
    asyncio.run(scrape_products())