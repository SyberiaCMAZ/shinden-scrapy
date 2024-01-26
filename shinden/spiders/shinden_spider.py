from pathlib import Path

import scrapy


class ShindenSpider(scrapy.Spider):
    name = "shinden"
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    start_urls = [
        "https://shinden.pl/series",
    ]

    def parse(self, response):
        for anime in response.xpath('//section[@class="title-table"]/article/ul'):
            yield {
                "name": anime.xpath('.//li[@class="desc-col"]/h3/a/text()').get(),
                "tags": anime.xpath('.//ul[@class="tags"]/li/a/text()').getall(),
                "type": anime.xpath('.//li[@class="title-kind-col"]/text()').get(),
                "episodes": anime.xpath('.//li[@class="episodes-col"]/text()').get(),
                "ratings": anime.xpath('.//li[@class="ratings-col"]/div/span/text()').getall(),
                "status": anime.xpath('.//li[@class="title-status-col"]/text()').get(),
                "ratetop": anime.xpath('.//li[@class="rate-top"]/text()').get(),
            }
        next_page = response.xpath('//a[@rel="next"]/@href').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)