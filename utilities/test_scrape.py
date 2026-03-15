import json
import asyncio
from playwright.async_api import async_playwright

# Your list of 251 URLs (truncated for example)
urls = [
    "https://www.woolworths.com.au/shop/productdetails/134034/gourmet-tomato",
    "https://www.woolworths.com.au/shop/productdetails/137130/lebanese-cucumbers",
    # ... add all 251 URLs here
]

async def scrape_woolies():
    results = []
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        for url in urls:
            try:
                print(f"Scraping: {url}")
                await page.goto(url, wait_until="networkidle")
                
                # Extract Data using CSS Selectors (Updated for 2026)
                data = {
                    "name": await page.inner_text("h1.product-title"),
                    "price": await page.inner_text(".price-dollar"), # Simplified
                    "unit_price": await page.inner_text(".price-cup"),
                    "stock": "In Stock" if await page.query_selector(".add-to-cart-button") else "Out of Stock",
                    "url": url
                }
                results.append(data)
                await asyncio.sleep(2) # Prevent being flagged as a bot
            except Exception as e:
                print(f"Error on {url}: {e}")

        # Save to JSON
        with open('woolworths_collection.json', 'w') as f:
            json.dump(results, f, indent=4)
            
        await browser.close()

asyncio.run(scrape_woolies())