import scrapy
from scrapy_selenium import SeleniumRequest


class CoinmarketcapSpider(scrapy.Spider):
    name = "coinmarketcap"
    allowed_domains = ["api.coinmarketcap.com"]
    # start_urls = ["https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug={symbol}&start=1&limit=20&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc"]

    def start_requests(self):
        # print work directory
        import os
        print(os.getcwd())
        symbol = "bitcoin"
        url = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug={symbol}&start=1&limit=20&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc"
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
        print(response.text)
        pass
