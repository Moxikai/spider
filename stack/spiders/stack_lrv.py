# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import FormRequest, Request
from scrapy.linkextractors import LinkExtractor
from stack.items import StackItem
from stack.settings import *


class StackLrvSpider(CrawlSpider):
    name = 'lrv'
    allowed_domains = ["0720.app"]
    start_urls = ["http://0720.app/home"]

    rules = (
        Rule(LinkExtractor(allow=("\/\?page=[0-9]+$")), follow=True, process_request='req_with_cookie', callback='parse_item'),
    )

    def __init__(self, *args, **kwargs):
        super(StackLrvSpider, self).__init__(*args, **kwargs)  # 这里是关键
        self.headers = HEADER
        self.cookies = COOKIES

    def req_with_cookie(self, request):
        return request.replace(headers=self.headers, cookies=self.cookies)

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield FormRequest(url, meta={'cookiejar':i}, headers=self.headers, cookies=self.cookies)

    def parse_item(self, response):

        for ele in response.xpath('//div[@class="list-group"]/a') :
            i = StackItem()

            i['name'] = ele.xpath('text()').extract()[0]
            i['url'] = ele.xpath('@href').extract()[0]

            yield i
