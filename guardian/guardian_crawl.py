import scrapy
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class GuardianSpider(CrawlSpider):

    # if (os.path.isfile('GUARDIANlist.txt')):
    #     with open('GUARDIANlist.txt') as file:
    #         thelist = file.read().splitlines()
    #     print(thelist)
    # else:
    #     thelist = []

    name = "guardian"
    allowed_domains = ['https://www.theguardian.com']
    start_urls = [
        'https://www.theguardian.com/world'
    ]

    rules = (
        Rule(LinkExtractor(allow=('https://www.theguardian.com/world/')), callback='parse_item', follow=True),
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
            #     thefile = open('GUARDIANlist.txt', 'a')
            #     thefile.write(response.url+"\n")
            self.log('Saved file %s' % filename)  
