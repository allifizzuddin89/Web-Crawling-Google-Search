import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging
from scrapy.utils.log import configure_logging
# Proxy, if necessary
# from scraper_api import ScraperAPIClient
# client = ScraperAPIClient("<token>")


class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['www.google.com']
    start_urls = ['https://www.google.com/search?q=dimensity+8100+mobile+phone+list&sxsrf=ALiCzsZnVzp8OGPeInvJMcB118Yb9HJJsg%3A1669455894842&ei=FuCBY7aBM9i03LUP_tWh0A0&ved=0ahUKEwi25NHsx8v7AhVYGrcAHf5qCNoQ4dUDCA8&uact=5&oq=dimensity+8100+mobile+phone+list&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQogQyBQgAEKIEOgoIABBHENYEELADOgYIABAWEB46BQgAEIYDOgUIIRCgAToHCCEQoAEQCkoECEEYAEoECEYYAFCGM1jwN2CGOWgBcAF4AIABqQGIAaUFkgEDMC41mAEAoAEByAEIwAEB&sclient=gws-wiz-serp']

    rules = (
        Rule(LinkExtractor(restrict_css='div.TbwUpd.NJjxre>cite'), callback='parse_item', follow=False),
        # Rule(LinkExtractor(allow=('dimensity','8100'))),
    )

    configure_logging(
        install_root_handler=False
    )
    logging.basicConfig(
        filename="Logfile.log",
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode='w',
        level=logging.DEBUG,
    )

    def parse_item(self, response):
        print('\n')
        print(response.url)
        print('\n')
        # item = {}
        # # item['Title'] = response.css('div.yuRUbf>a>h3::text').get()
        # # item['Description'] =  
        # # ite['Tags'] = 


        # # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # # item['name'] = response.xpath('//div[@id="name"]').get()
        # # item['description'] = response.xpath('//div[@id="description"]').get()
        # return item
