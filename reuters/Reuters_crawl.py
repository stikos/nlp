import scrapy
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class REUTERSSpider(CrawlSpider):

    # if (os.path.isfile('Reuterslist.txt')):
    #     with open('Reuterslist.txt') as file:
    #         thelist = file.read().splitlines()
    #     print(thelist)
    # else:
    #     thelist = []

    name = "reuters"
    allowed_domains = ['www.reuters.com']
    start_urls = [
        'http://www.reuters.com/article/'
    ]

    rules = (
        Rule(LinkExtractor(allow=('http://www.reuters.com')), callback='parse_item', follow=True),
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
            #     thefile = open('Reuterslist.txt', 'a')
            #     thefile.write(response.url+"\n")
            self.log('Saved file %s' % filename)  
