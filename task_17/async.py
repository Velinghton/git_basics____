import asyncio
import aiohttp
import csv
from bs4 import BeautifulSoup
import requests


CATEGORY_URL = "https://www.gorgany.com/odiah/kurtky"



async def main():
    async  with aiohttp.ClientSession() as session:
        async with session.get(CATEGORY_URL) as response:
            r = await  aiohttp.StreamReader.read(response.content)
            soup = BeautifulSoup(r, "html.parser")
            items = soup.select(".item.product.product-item")
            count = 1
            for el in items[0].select("a.page"):
                count += 1

            length = 0
            filename = CATEGORY_URL.split("/")
            filename = filename[-1]
            with open(filename + ".csv", "w", newline="") as csvfile:
                writter = csv.writer(csvfile, delimiter=',')
                writter.writerow(["sku", "name", "price", "link"])
                for i in range(count):
                    response = requests.get(CATEGORY_URL + "?p=" + str(i))
                    page_doc = BeautifulSoup(response.text, features="html.parser")
                    products = page_doc.select(".item.product.product-item")

                    for product in products:
                        product_link = product.select_one(".product-item-link")
                        if product_link:
                            length = length + 1
                            name = product_link.getText()
                            price = product.select_one(".price").getText()
                            link = product_link.get("href")
                            sku = product.select_one("form").get("data-product-sku")
                            writter.writerow([sku, name, price, link])



if __name__ == '__main__':
    asyncio.run(main())