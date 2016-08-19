# -*- coding: utf-8 -*-
import scrapy

from stackoverflow.items import *

class StackdocSpider(scrapy.Spider):
    name = "stackDoc"
    allowed_domains = ["stackoverflow.com"]
    start_urls = (
        'http://stackoverflow.com/documentation?page=1&tab=popular',
    )

    def parse(self, response):
        print response.url
        print 80 * '-'
        for item in response.xpath('//div[@class="doctag-card"]'):
            doc = StackDocument()
            doc['name'] = item.xpath('div[1]/a/text()').extract()[0]
            doc['link'] = item.xpath('div[1]/a/@href').extract()[0]
            try:
            	doc['numTopic'] = item.xpath('div[1]/span/span/text()').re("\d+")[0]
            except IndexError, e:
            	doc['numTopic'] = item.xpath('div[1]/span/span/text()').extract()
            except Exception, e:
            	doc['numTopic'] = item.xpath('div[1]/span/span/text()').extract()[0]

            try:
            	doc['numRequest'] = item.xpath('div[2]/a[2]/text()').re("\d+")[0]
            except IndexError, e:
            	doc['numRequest'] = item.xpath('div[2]/a[2]/text()').extract()
            except Exception, e:
            	doc['numRequest'] = item.xpath('div[2]/a[2]/text()').extract()[0]
            try:
            	doc['numProposed'] = item.xpath('div[2]/a[3]/text()').re("\d+")[0]
            except IndexError, e:
            	doc['numProposed'] = item.xpath('div[2]/a[3]/text()').extract()
            except Exception, e:
            	doc['numProposed'] = item.xpath('div[2]/a[3]/text()').extract()[0]
            try:
            	doc['numImprovement'] = item.xpath('div[2]/a[4]/text()').re("\d+")[0]
            except IndexError, e:
            	doc['numImprovement'] = item.xpath('div[2]/a[4]/text()').extract()
            except Exception, e:
            	doc['numImprovement'] = item.xpath('div[2]/a[4]/text()').extract()[0]

            yield doc
        print response.url
        page = response.url.split("=")[1].split("&")[0]
        num = int(page) + 1
        print 'Number: ', num
        yield scrapy.Request("http://stackoverflow.com/documentation?page=" + str(num) + "&tab=popular", self.parse)