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


class StackDocument(scrapy.Item):
	"""docstring for StackDocument"""
	name = scrapy.Field()
	numTopic = scrapy.Field()
	numRequest = scrapy.Field()
	numProposed = scrapy.Field()
	numImprovement = scrapy.Field()
	link = scrapy.Field()
		