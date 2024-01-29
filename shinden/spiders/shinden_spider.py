from pathlib import Path
from shinden.items import AnimeItem, CharacterItem, CastsItem, CommentItem
import scrapy


class ShindenSpider(scrapy.Spider):
    name = "shinden"
    user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
    start_urls = [
        "https://shinden.pl/series",
    ]

    def parse(self, response):
        for anime in response.xpath('//section[@class="title-table"]/article/ul'):
            relative_url = anime.xpath('.//li/h3/a/@href').get()
            yield response.follow(relative_url, callback=self.parse_anime_page)
        next_page = response.xpath('//a[@rel="next"]/@href').get()

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

    def parse_anime_page(self, response):

        character_details = response.xpath('//div[@class="ch-st-item"]')
        character_items = []

        for character in character_details:
            character_item = CharacterItem(
                name=character.xpath('span[1]/div/h3/a/text()').get(),
                actor=character.xpath('span[2]/div/h3/a/text()').get(),
            )
            character_items.append(dict(character_item))

        casts = response.xpath('//div[@class="person-character-text"]')
        casts_items = []

        for cast in casts:
            casts_item = CastsItem(
                name=cast.xpath('h3/a/text()').get(),
                role=cast.xpath('p/text()').get(),
            )
            casts_items.append(dict(casts_item))

        comments = response.xpath('//ul[@class="posts"]/li')
        comment_items = []
        for comment in comments:
            comment_item = CommentItem(
                user=comment.xpath('summary/strong/text()').get(),
                content=comment.xpath('div/text()').get(),
                date=comment.xpath('details/span/text()').get(),
            )
            comment_items.append(dict(comment_item))

        anime_details = AnimeItem()
        anime_details["name"] = response.xpath("//h1/span[2]/text()").get()
        anime_details["description"] = response.xpath('//div[@id="description"]/p/text()').get()
        anime_details["tags" ] = response.xpath('//ul[@class="tags"]/li/a/text()').getall()
        anime_details["score" ] = response.xpath('//div/h3/span/text()').get()
        anime_details["score_votes" ] = response.xpath('substring-before(//span[@class="h6"], "głosów")').get()
        anime_details["story_score" ] = response.xpath('//ul[@class="info-aside-overall-rating"]/li[1]/text()').get()
        anime_details["animation_score" ] = response.xpath('//ul[@class="info-aside-overall-rating"]/li[2]/text()').get()
        anime_details["music_score" ] = response.xpath('//ul[@class="info-aside-overall-rating"]/li[3]/text()').get()
        anime_details["character_score" ] = response.xpath('//ul[@class="info-aside-overall-rating"]/li[4]/text()').get()
        anime_details["character_score" ] = response.xpath('//ul[@class="info-aside-overall-rating"]/li[4]/text()').get()
        anime_details["genre"] = response.xpath("//dl[@class='info-aside-list']/dd[1]/text()").get()
        anime_details["status"] = response.xpath("//dl[@class='info-aside-list']/dd[2]/text()").get()
        anime_details["start_date"] = response.xpath("//dl[@class='info-aside-list']/dd[3]/text()").get()
        anime_details["end_date"] = response.xpath("//dl[@class='info-aside-list']/dd[4]/text()").get()
        anime_details["episodes"] = response.xpath("//dl[@class='info-aside-list']/dd[5]/text()").get()
        anime_details["studio"] = response.xpath("//dl[@class='info-aside-list']/dd[6]/a/text()").getall()
        anime_details["lenght"] = response.xpath("//dl[@class='info-aside-list']/dd[7]/text()").get()
        anime_details["mpaa"] = response.xpath("//dl[@class='info-aside-list']/dd[8]/text()").get()
        anime_details["watching"] = response.xpath("//section[@class='title-stats']/dl/dd[1]/text()").get()
        anime_details["watched"] = response.xpath("//section[@class='title-stats']/dl/dd[2]/text()").get()
        anime_details["skipped"] = response.xpath("//section[@class='title-stats']/dl/dd[3]/text()").get()
        anime_details["dropped"] = response.xpath("//section[@class='title-stats']/dl/dd[4]/text()").get()
        anime_details["stopped"] = response.xpath("//section[@class='title-stats']/dl/dd[5]/text()").get()
        anime_details["will_watch"] = response.xpath("//section[@class='title-stats']/dl/dd[6]/text()").get()
        anime_details["likes"] = response.xpath("//section[@class='title-stats']/dl/dd[7]/text()").get()
        anime_details['character'] = character_items
        anime_details['cast'] = casts_items
        anime_details['comment'] = comment_items
        



        yield anime_details