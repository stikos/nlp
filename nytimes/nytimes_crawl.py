import scrapy
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class NYTIMESSpider(CrawlSpider):

    # if (os.path.isfile('NYTIMESlist.txt')):
    #     with open('NYTIMESlist.txt') as file:
    #         thelist = file.read().splitlines()
    #     print(thelist)
    # else:
    #     thelist = []

    name = "nytimes"
    allowed_domains = ['http://www.nytimes.com']
    start_urls = [
        'http://www.nytimes.com/2016'
    ]

    rules = (
        Rule(LinkExtractor(allow=('http://www.nytimes.com/2016')), callback='parse_item', follow=True),
        )


    def parse_item(self, response):
        page = response.url.replace("/", "$")
        filename = '%s.html' % page
        if (not os.path.isfile(filename)):
            with open(filename, 'wb') as f:
                f.write(response.body)
            # if not file.closed:
            #     file.write(response.url+"\n")
            # else:
            #     thefile = open('NYTIMESlist.txt', 'a')
            #     thefile.write(response.url+"\n")
            self.log('Saved file %s' % filename)  
