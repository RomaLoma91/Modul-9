import scrapy
from scrapy.item import Item, Field

class QuoteItem(Item):
    quote = Field()
    author = Field()

class AuthorItem(scrapy.Item):
    fullname = scrapy.Field()
    born_date = scrapy.Field()
    born_location = scrapy.Field()
    description = scrapy.Field()
    url = scrapy.Field()
