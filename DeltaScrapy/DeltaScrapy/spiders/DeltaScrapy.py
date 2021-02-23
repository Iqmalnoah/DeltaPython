import scrapy

class NewSpider(scrapy.Spider):
    name = 'NewSpider'
    start_urls = ['https://www.wikipedia.org']


