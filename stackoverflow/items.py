# -*- coding: utf-8 -*-
import scrapy


class StackoverflowItem(scrapy.Item):
    # define the fields for your item here like:
    language = scrapy.Field()
    description = scrapy.Field()
    link = scrapy.Field()
    asktoday = scrapy.Field()
    askweek = scrapy.Field()
    freq = scrapy.Field()