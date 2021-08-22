# Scrapy project to webscrape the WhiskyShop website and list out the different names of whiskys with prices and links
# Beginner tutorial from YouTube channel - John Watson Rooney

# scrapy startproject projectname
# scrapy shell
# fetch('URL_LINK HERE')
# response
# response.css('div.product-item-info')
# response.css('div.product-item-info').get()
# products = response.css('div.product-item-info')
# products.css('a.product-item-link').get()
# products.css('a.product-item-link::text').getall()
# products.css('span.price::text').get()
# products.css('span.price::text').get().replace('£', '')
# products.css('a.product-item-link').attrib['href']
# scrapy crawl whisky
# Make sure to save .py file into the /spiders folder
# Make sure to cd into the root of the project folder name for the Scrapy spider to work properly

import scrapy

class WhiskySpider(scrapy.Spider):
    name = 'whisky'
    start_urls = ['https://www.whiskyshop.com/scotch-whisky?item_availability=In+Stock']

    def parse(self, response):
        for products in response.css('div.product-item-info'):
            try:
                yield {
                    'name': products.css('a.product-item-link::text').get(),
                    'price': products.css('span.price::text').get().replace('£', ''),
                    'link': products.css('a.product-item-link').attrib['href'], 
                }
            except:
                yield {
                    'name': products.css('a.product-item-link::text').get(),
                    'price': 'sold out',
                    'link': products.css('a.product-item-link').attrib['href'], 
                }

        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)





