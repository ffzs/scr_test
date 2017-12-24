# -*- coding: utf-8 -*-
import scrapy
from scr_test.items import ScrTestItem

class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['hr.tencent.com']
    base_url = 'http://hr.tencent.com/position.php?lid=2156&tid=&keywords=python&start='
    offset = 0
    start_urls = [base_url+str(offset)]

    def parse(self, response):
        node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")
        for node in node_list:
            item = ScrTestItem()
            item["position_name"] = node.xpath("./td[1]/a/text()")[0].extract()
            item["position_link"] = node.xpath("./td[1]/a/@href")[0].extract()
            item["position_type"] = node.xpath("./td[2]/text()")[0].extract()
            item["people_num"] = node.xpath("./td[3]/text()")[0].extract()
            item["work_location"] = node.xpath("./td[4]/text()")[0].extract()
            item["publish_time"] = node.xpath("./td[5]/text()")[0].extract()

            yield item
        #
        if self.offset<80:
            self.offset +=10
            url = self.base_url+str(self.offset)+"#a"
            yield scrapy.Request(url,callback=self.parse)


        # pass
