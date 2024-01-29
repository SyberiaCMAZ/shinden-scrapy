# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ShindenItem(scrapy.Item):
    pass

class AnimeItem(scrapy.Item):
    name = scrapy.Field()
    description = scrapy.Field()
    tags = scrapy.Field()
    score = scrapy.Field()
    score_votes = scrapy.Field()
    story_score = scrapy.Field()
    animation_score = scrapy.Field()
    music_score = scrapy.Field()
    character_score = scrapy.Field()
    genre = scrapy.Field()
    status = scrapy.Field()
    start_date = scrapy.Field()
    end_date = scrapy.Field()
    episodes = scrapy.Field()
    studio = scrapy.Field()
    lenght = scrapy.Field()
    mpaa = scrapy.Field()
    watching = scrapy.Field()
    watched = scrapy.Field()
    skipped = scrapy.Field()
    dropped = scrapy.Field()
    stopped = scrapy.Field()
    will_watch = scrapy.Field()
    likes = scrapy.Field()
    character = scrapy.Field()
    cast = scrapy.Field()
    comment = scrapy.Field()

class CharacterItem(scrapy.Item):
    name = scrapy.Field()
    actor = scrapy.Field()

class CastsItem(scrapy.Item):
    name = scrapy.Field()
    role = scrapy.Field()
    

class CommentItem(scrapy.Item):
    user = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()