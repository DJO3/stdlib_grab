from scrapy import Spider
from scrapy.selector import Selector
from stdlib_grab.items import StdlibGrabItem


class StdlibGrabSpider(Spider):
    name = "stdlib_grab"
    allowed_domains = ["pymotw.com"]
    start_urls = [
        "http://pymotw.com/2/py-modindex.html",
    ]

    def parse(self, response):
        modules = Selector(response).xpath('//tr/td/a')
        http = 'http://pymotw.com/2/'
        position = 0

        for module in modules:
            item = StdlibGrabItem()
            module_name = module.xpath('//tt[@class="xref"]/text()').extract()[position]
            if module_name == "xml":  # table unfortunately has an incomplete row, needs to be avoided
                module_name = "xml.etree.ElementTree"
                position += 1
            url = http + module.xpath('@href').extract()[0]
            item['module'] = module_name
            item['url'] = url
            position += 1
            yield item