# -*- coding: utf-8 -*-
import scrapy, re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy import Request
from csdn.items import CsdnItem
from scrapy.selector import Selector

class CsdnCourseSpider(CrawlSpider):
    name = 'csdn_course'
    allowed_domains = ['edu.csdn.net']
    start_urls = ['https://edu.csdn.net/courses/p1']

    rules = (
            Rule(LinkExtractor(allow=(r'https://edu.csdn.net/courses/p\d+')), follow=True),
            Rule(LinkExtractor(allow=(r'https://edu.csdn.net/course/detail/\d+')), callback='parse_info', follow=True)
        )


    def parse_info(self, response):
        sel = Selector(response)
        item = CsdnItem()
        title = ''.join(sel.xpath('//div[contains(@class,"info_right")]//h1//text()').extract()) 
        item['title'] = re.sub('\s','',title).strip()
        item['cover'] = ''.join(sel.xpath('//div[contains(@class, "info_left")]/a/img/@src').extract_first())
        item['price'] = ''.join(sel.xpath('//div[@class="price_wrap"]//span[@class="money"]/text()').extract_first()).replace('¥','').replace('.00','')
        item['teacher'] = ''.join(sel.xpath('//div[@class="professor_name"]/a/text()').extract_first())
        info = ''.join(sel.xpath('//div[@class="J_outline_discribe_content"]//text()').extract())
        item['info'] = re.sub('\s','',info).replace('课程简介','')
        section = ''.join(sel.xpath('//div[@class="J_outline_content"]//ul[@class="section_list"]//li//a/@title').extract())
        item['section'] = re.sub('\s','',section)
        item['number'] = ''.join(sel.xpath('//div[@class="course_students"]//span//text()').extract_first()).replace('人已学习','')
        yield item
