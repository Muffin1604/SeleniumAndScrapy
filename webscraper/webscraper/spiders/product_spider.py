import scrapy
from .. selenium_script.test2 import selenium1

class ProductSpider(scrapy.Spider):
        name = "product_spider"
        start_urls = ['https://docs.scrapy.org/en/latest/topics/commands.html']

        def parse(self, response):
            selenium = selenium1()
            product = response.xpath('//*[@id="command-line-tool"]/p[2]/text()').get()
            #print("Extracted Product:+++++++++*****@@@@@@@@@_______-------------++++++++++++++++++", product)
            data1 = response.xpath('//*[@id="using-the-scrapy-tool"]/h2/text()[1]').get()
            #print("Extracted Product:+++++++++*****@@@@@@@@@_______-------------++++++++++++++++++", data1)
            
