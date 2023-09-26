from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import scrapy
from ..settings import SELENIUM_DRIVER_EXECUTABLE_PATH, SELENIUM_BROWSER_EXECUTABLE_PATH


class SingaporepoolSpider(scrapy.Spider):
    name = "singaporepool"
    allowed_domains = ["online.singaporepools.com"]
    # start_urls = ["https://online.singaporepools.com/cn/sports/category/1/football"]

    def __init__(self, *args, **kwargs):
        super(SingaporepoolSpider, self).__init__(*args, **kwargs)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = SELENIUM_BROWSER_EXECUTABLE_PATH
        service = Service(SELENIUM_DRIVER_EXECUTABLE_PATH)
        self.driver = webdriver.Chrome(service=service, options=chrome_options)  # Replace with your ChromeDriver path

    def start_requests(self):
        url = 'https://online.singaporepools.com/cn/sports/category/1/football'
        yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        self.driver.get(response.url)
        pass
