import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import logging
from scrapy.utils.log import configure_logging


class MainSpider(CrawlSpider):
    name = 'main'
    allowed_domains = ['x']
    start_urls = ['http://x/']

    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
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
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item
