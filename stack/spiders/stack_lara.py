# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest, Request
from scrapy.linkextractors import LinkExtractor
from stack.items import LaraItem
from stack.settings import *


class StackLaraSpider(CrawlSpider):
    name = 'lara'
    allowed_domains = ["laracasts.com"]
    start_urls = ["https://laracasts.com/all"]

    rules = (
        Rule(LinkExtractor(allow=("all\?page=3$")), follow=False, process_request='req_with_cookie', callback='parse_item'),
    )

    def __init__(self, *args, **kwargs):
        super(StackLaraSpider, self).__init__(*args, **kwargs) 
        self.headers = HEADER
        self.cookies = COOKIES

    def req_with_cookie(self, request):
        return request.replace(headers=self.headers, cookies=self.cookies)

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield FormRequest(url, meta={'cookiejar':i}, headers=self.headers, cookies=self.cookies)

    def parse_item(self, response):

        for ele in response.xpath('//div[@class="list-group-item__details"]') :

            yield FormRequest(url=ele.xpath('a/@href').extract()[0], meta={'cookiejar':1}, headers=self.headers, cookies=self.cookies, callback=self.parse_eve)

    def parse_eve(self, response):
        selector = Selector(response)
        i = LaraItem()

        i['title'] = selector.xpath('//h1/text()').extract()[0]
        i['url'] = selector.xpath('//h1/a/@href').extract()[0]
        i['download'] = selector.xpath('//source/@src').extract()[0]

        return i;
