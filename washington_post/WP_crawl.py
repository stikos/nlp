import scrapy
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class WPSpider(CrawlSpider):

    # if (os.path.isfile('WPlist.txt')):
    #     with open('WPlist.txt') as file:
    #         thelist = file.read().splitlines()
    #     print(thelist)
    # else:
    #     thelist = []

    name = "washingtonpost"
    allowed_domains = ['www.washingtonpost.com']
    start_urls = [
        'https://www.washingtonpost.com/news/'
    ]

    rules = (
        Rule(LinkExtractor(allow=('https://www.washingtonpost.com/news/')), callback='parse_item', follow=True),
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
            #     thefile = open('WPlist.txt', 'a')
            #     thefile.write(response.url+"\n")
            self.log('Saved file %s' % filename)  
