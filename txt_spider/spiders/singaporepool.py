import scrapy
from scrapy_selenium import SeleniumRequest


class SingaporepoolSpider(scrapy.Spider):
    name = "singaporepool"
    allowed_domains = ["online.singaporepools.com"]
    # start_urls = ["https://online.singaporepools.com/cn/sports/category/1/football"]

    def start_requests(self):
        url = 'https://online.singaporepools.com/cn/sports/category/1/football'
        yield SeleniumRequest(url=url, callback=self.parse)


    def parse(self, response):
        pass
