import scrapy

class zoo(scrapy.Spider):
    name = 'zoozoo'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self,response):
        title = response.css('title::text').extract()
        yield {'titletext': title}
