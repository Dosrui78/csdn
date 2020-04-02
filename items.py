# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    cover = scrapy.Field()
    price = scrapy.Field()
    teacher = scrapy.Field()
    info = scrapy.Field()
    section = scrapy.Field()
    number = scrapy.Field()
    #cover_path = scrapy.Field()
    

