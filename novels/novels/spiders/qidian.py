import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from novels.items import NovelsItem


class QidianSpider(CrawlSpider):
    name = 'qidian'
    allowed_domains = ['www.qidian.com']
    start_urls = ['https://www.qidian.com/all']

    page_link = LinkExtractor(restrict_xpaths='//*[@id="page-container"]/div/ul/li/a')
    rules = (
        Rule(page_link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = NovelsItem()

        novel_name = response.xpath('//div[@class="book-mid-info"]/h4/a/text()').extract()
        novel_author = response.xpath('//p[@class="author"]/a[1]/text()').extract()
        novel_classification = response.xpath('//p[@class="author"]/a[2]/text()').extract()
        novel_status = response.xpath('//p[@class="author"]/span/text()').extract()
        # novel_number_of_words = response.xpth('').extracts()[0]
        novel_brief_introduction = response.xpath('//p[@class="intro"]/text()').extract()

        # print("#" * 100)

        item['novel_name'] = novel_name
        item['novel_author'] = novel_author
        item['novel_classification'] = novel_classification
        item['novel_status'] = novel_status
        item['novel_brief_introduction'] = novel_brief_introduction
        yield item
