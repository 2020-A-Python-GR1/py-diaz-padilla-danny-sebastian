import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import csv



class SpiderCrawlGames(CrawlSpider):
    name = "apps"

    allowed_domains = [ # Heredado
        'play.google.com'
    ]

    start_urls = [
        'https://play.google.com/store/apps/category/GAME',
        'https://play.google.com/store/apps/category/GAME_ACTION',
        'https://play.google.com/store/apps/category/GAME_ADVENTURE',
        'https://play.google.com/store/apps/category/GAME_RACING',
        'https://play.google.com/store/apps/category/GAME_CARD',
        'https://play.google.com/store/apps/category/GAME_CASINO',
        'https://play.google.com/store/apps/category/GAME_EDUCATIONAL',
        'https://play.google.com/store/apps/category/GAME_STRATEGY',
        'https://play.google.com/store/apps/category/GAME_SPORTS',
        'https://play.google.com/store/apps/category/GAME_BOARD',
        'https://play.google.com/store/apps/category/GAME_WORD',
        'https://play.google.com/store/apps/category/GAME_ROLE_PLAYING',
        'https://play.google.com/store/apps/category/GAME_CASUAL',
        'https://play.google.com/store/apps/category/GAME_MUSIC',
        'https://play.google.com/store/apps/category/GAME_TRIVIA',
        'https://play.google.com/store/apps/category/GAME_PUZZLE',
        'https://play.google.com/store/apps/category/GAME_ARCADE',
        'https://play.google.com/store/apps/category/GAME_SIMULATION'
    ]


    """

        'store/apps/category/GAME',
        'store/apps/category/GAME_ACTION',
        'store/apps/category/GAME_ADVENTURE',
        'store/apps/category/GAME_RACING',
        'store/apps/category/GAME_CARD',
        'store/apps/category/GAME_CASINO',
        'store/apps/category/GAME_EDUCATIONAL',
        'store/apps/category/GAME_STRATEGY',
        'store/apps/category/GAME_SPORTS',
        'store/apps/category/GAME_BOARD',
        'store/apps/category/GAME_WORD',
        'store/apps/category/GAME_ROLE_PLAYING',
        'store/apps/category/GAME_CASUAL',
        'store/apps/category/GAME_MUSIC',
        'store/apps/category/GAME_TRIVIA',
        'store/apps/category/GAME_PUZZLE',
        'store/apps/category/GAME_ARCADE',
        'store/apps/category/GAME_SIMULATION',

    """

    
    segmentos_url_permitidos = (
        'store/apps/details',
        'store/apps/category'

    )

    segmentos_restringidos = (

    )

    regla_tres = (
        Rule(
            LinkExtractor(
                allow_domains = allowed_domains,
                allow = segmentos_url_permitidos,
                deny = segmentos_restringidos
            ),
            callback = 'parse_page'
        ),
    )


    rules = regla_tres # heredado

    # df = pd.DataFrame({"titulo": [], "count_reviews": [], "publisher_name": [], "category": [], "count_installs": [], "rating": [],})
    
    # row = [{"titulo": titulo, "count_reviews": count_reviews, "publisher_name": publisher_name, "category": category, "count_installs": count_installs, "rating": rating}]
    #       df = pd.concat([pd.DataFrame(row), df], ignore_index=True)
    iniciado = True

    def parse_page(self, response):
        titulo = response.css('h1.AHFaub > span::text').extract()[0]
        count_reviews = int(response.xpath('(//span[@class="AYi5wd TBRnV"])/span[@class=""]/text()').extract()[0].replace(",", ""))
        publisher_name, category = response.xpath('(//a[@class="hrTbp R8zArc"])/text()').extract()
        count_installs =  response.css('span.htlgb ::text').extract()[2].replace(",","").replace("+", "")
        rating =  float(response.css('div.BHMmbe ::text').extract()[0])

        
        if self.iniciado:
            f = open('apps.csv', 'w', newline='')

            with f:
                row = ["titulo", "count_reviews", "publisher_name", "category", "count_installs", "rating"]
                writer = csv.writer(f)
                writer.writerow(row)
                self.iniciado = False


        if titulo is not None and count_reviews is not None and publisher_name is not None and category is not None and count_reviews is not None and rating is not None:
            
            f = open('apps.csv', 'a', newline='')

            with f:
                row = [titulo, count_reviews, publisher_name, category, count_installs, rating]
                writer = csv.writer(f)
                writer.writerow(row)
                    

    
