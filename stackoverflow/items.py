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

class StackQuestion(scrapy.Item):
	"""docstring for StackQuestion"""
	title = scrapy.Field()
	link = scrapy.Field()
	description = scrapy.Field()
	vote = scrapy.Field()
	answer = scrapy.Field()
	view = scrapy.Field()
	tag = scrapy.Field()
	person = scrapy.Field()

class StackPerson(scrapy.Item):
	"""docstring for StackQuestion"""
	name = scrapy.Field()
	avatar = scrapy.Field()
	reputation = scrapy.Field()