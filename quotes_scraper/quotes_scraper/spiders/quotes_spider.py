import scrapy
from quotes_scraper.items import QuoteItem, AuthorItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            text = quote.css('span.text::text').get()
            author_name = quote.css('small.author::text').get()
            author_url = quote.css('small.author ~ a::attr(href)').get()

            yield QuoteItem(quote=text, author=author_name)
            yield response.follow(author_url, self.parse_author)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def parse_author(self, response):
        fullname = response.css('h3.author-title::text').get()
        born_info = response.css('span.author-born-date::text').get()
        born_date, born_location = born_info.split(' in ')

        author_item = AuthorItem(
            fullname=fullname,
            born_date=born_date,
            born_location=born_location,
            description=response.css('div.author-description::text').get(),
            url=response.url
        )
        yield author_item

