# -*- coding: utf-8 -*-
import scrapy

from stackoverflow.items import StackoverflowItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class StackSpider(CrawlSpider):
    name = 'stack'
    allowed_domains = ['stackoverflow.com']
    start_urls = ('http://stackoverflow.com/tags?page=14&tab=popular',)


    def parse(self, response):
        print response.url
        print 80 * '-'
        for td in response.xpath('//td[@class="tag-cell"]'):
            lang = StackoverflowItem()
            lang['language'] = td.xpath('a/text()').extract()[0]
            lang['link'] = td.xpath('a/@href').extract()[0]
            lang['freq'] = td.xpath('span/span[2]/text()').extract()[0]
            lang['description'] = td.xpath('div[1]/text()').extract()[0]
            try:
                lang['askweek'] = td.xpath('div[2]/div[1]/a[2]/text()').re("\d+")[0]
            except IndexError, e:
                lang['askweek'] = td.xpath('div[2]/div[1]/a[2]/text()').extract()                
            except Exception, e:
                lang['askweek'] = td.xpath('div[2]/div[1]/a[2]/text()').extract()[0]
                raise e            

            try:
                lang['asktoday'] = td.xpath('div[2]/div[1]/a[1]/text()').re("\d+")[0]               
            except IndexError, e:
                lang['asktoday'] = td.xpath('div[2]/div[1]/a[1]/text()').extract()
            except Exception, e:
                lang['asktoday'] = td.xpath('div[2]/div[1]/a[1]/text()').extract()[0]                
                raise e
            yield lang
        print response.url
        page = response.url.split("=")[1].split("&")[0]
        num = int(page) + 1
        print 'Number: ', num
        yield scrapy.Request("http://stackoverflow.com/tags?page=" + str(num) + "&tab=popular", self.parse)