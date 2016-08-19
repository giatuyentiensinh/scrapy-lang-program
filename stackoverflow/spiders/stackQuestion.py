# -*- coding: utf-8 -*-
import scrapy
from stackoverflow.items import *

class StackquestionSpider(scrapy.Spider):
    name = "stackQuestion"
    allowed_domains = ["stackoverflow.com"]
    start_urls = (
        'http://stackoverflow.com/questions?page=371&sort=newest',
    )

    def parse(self, response):
        print response.url
        print 80 * '-'
        for item in response.xpath('//div[@class="question-summary"]'):
            question = StackQuestion()
            question['vote'] = item.xpath('div[@class="statscontainer"]/div[2]/div[1]/div/span/strong/text()').extract()[0]
            question['answer'] = item.xpath('div[@class="statscontainer"]/div[2]/div[2]/strong/text()').extract()[0]
            question['view'] = item.xpath('div[@class="statscontainer"]/div[3]/text()').re("\d+")[0]
            question['title'] = item.xpath('div[@class="summary"]/h3/a/text()').extract()[0]
            question['link'] = item.xpath('div[@class="summary"]/h3/a/@href').extract()[0]
            question['description'] = " ".join(item.xpath('div[@class="summary"]/div[@class="excerpt"]/text()').re('\w+'))
            
            tags = item.xpath('div[@class="summary"]/div[2]/a')
            tagname = []
            for tag in tags:
            	tagname.append(tag.xpath('text()').extract()[0])
            question['tag'] = tagname

            person = StackPerson()
            try:
            	person['name'] = item.xpath('div[@class="summary"]/div[3]/div/div[3]/a/text()').extract()[0]
            except IndexError, e:
            	person['name'] = item.xpath('div[@class="summary"]/div[3]/div/div[3]/text()').extract()
            try:
            	person['avatar'] = item.xpath('div[@class="summary"]/div[3]/div/div[2]/a/div/img/@src').extract()[0]
            except IndexError, e:
            	person['avatar'] = item.xpath('div[@class="summary"]/div[3]/div/div[2]/span/@class').extract()
            try:
            	person['reputation'] = item.xpath('div[@class="summary"]/div[3]/div/div[3]/div/span[1]/text()').extract()[0]
            except IndexError, e:
            	person['reputation'] = item.xpath('div[@class="summary"]/div[3]/div/div[3]/div/span[1]/text()').extract()

            question['person'] = person

            yield question
        page = response.url.split("=")[1].split("&")[0]
        num = int(page) + 1
        print 'Number: ', num
        yield scrapy.Request("http://stackoverflow.com/questions?page=" + str(num) + "&sort=newest", self.parse)