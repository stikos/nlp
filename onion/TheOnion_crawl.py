import scrapy
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ONIONSpider(CrawlSpider):

    # if (os.path.isfile('Onionlist.txt')):
    #     with open('Onionlist.txt') as file:
    #         thelist = file.read().splitlines()
    #     print(thelist)
    # else:
    #     thelist = []

    name = "theonion"
    allowed_domains = ['www.theonion.com']
    start_urls = [
        'http://www.theonion.com'
    ]

    rules = (
        Rule(LinkExtractor(allow=('http://www.theonion.com/article/')), callback='parse_item', follow=True),
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
            #     thefile = open('Onionlist.txt', 'a')
            #     thefile.write(response.url+"\n")
            self.log('Saved file %s' % filename)  
