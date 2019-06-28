import scrapy
import os
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class CNNSpider(CrawlSpider):

    # if (os.path.isfile('CNNlist.txt')):
    #     with open('CNNlist.txt') as file:
    #         thelist = file.read().splitlines()
    #     print(thelist)
    # else:
    #     thelist = []

    name = "cnn"
    allowed_domains = ['us.cnn.com']
    start_urls = [
        'http://us.cnn.com/?hpt=header_edition-picker'
    ]

    rules = (
        Rule(LinkExtractor(allow=('http://us.cnn.com/')), callback='parse_item', follow=True)

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
            #     thefile = open('CNNlist.txt', 'a')
            #     thefile.write(response.url+"\n")
            self.log('Saved file %s' % filename)  
