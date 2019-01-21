# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.selector import Selector
from ..items import MyItemLoader


class AdventistdirectorySpider(scrapy.Spider):
    name = 'adventistdirectory'
    allowed_domains = ['adventistdirectory.org']
    start_urls = ['http://adventistdirectory.org/default.aspx?&&&&&&&&&&&page=searchresults&CtryCode=US&EntityType=C&PageIndex=%s'%page for page in range(0,251)]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url)

    def parse(self, response):
        urls =response.xpath('//tr/td/a/@href').extract()

        for url in urls:
            yield response.follow(url, callback=self.parse_item)

        # next_page= response.css('#_ctl0_ctlEntitySearchResults_rptEntitySearchList__ctl0_lnkNextPage ::attr(href)').extract()
        # if next_page is not None:
        #     yield response.follow(next_page)


    def parse_item(self,response):
        l = MyItemLoader(selector=response)
        l.add_xpath('Ponster_Name','//*[@id="_ctl0_pnlMainContent"]/table[4]/tr[3]/td/text()')
        l.add_xpath('Phone_Number','//*[@id="_ctl0_pnlMainContent"]/table[4]/tr[4]/td/text()')
        l.add_xpath('Church_Name','//*[@id="_ctl0_pnlMainContent"]/table[4]/tr[14]/td/text()')
        l.add_xpath('Address','//*[@id="_ctl0_Tr2"]/td[2]/text()')
        l.add_xpath('No_of_Member', '//*[@id="_ctl0_pnlMainContent"]/table[4]/tr[2]/td/text()')
        l.add_xpath('Website','//*[@id="_ctl0_Tr3"]/td[2]/a/@href')
        return l.load_item()

        # yield {
        #     'Ponster_Name':response.xpath('//*[@id="_ctl0_pnlMainContent"]/table[4]/tr[3]/td/text()').extract(),
        #     'Phone_Number':response.xpath('//*[@id="_ctl0_pnlMainContent"]/table[4]/tr[4]/td/text()').extract() ,
        #     'Church_Name':response.xpath('//*[@id="_ctl0_pnlMainContent"]/table[4]/tr[14]/td/text()').extract(),
        #     'Address':response.xpath('//*[@id="_ctl0_Tr2"]/td[2]/text()').extract(),
        #     'No_of_Member':response.xpath('//*[@id="_ctl0_pnlMainContent"]/table[4]/tr[2]/td/text()').extract(),
        #     'Website':response.xpath('//*[@id="_ctl0_Tr3"]/td[2]/a/@href').extract(),
        # }
        #
        #

