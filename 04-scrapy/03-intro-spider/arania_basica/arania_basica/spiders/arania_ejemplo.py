import scrapy

class IntroSpider(scrapy.Spider):

    name = 'introduccion_spider'

    urls = [
        'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
    ]

    def start_requests(self):

        for url in self.urls:
            yield scrapy.Request(url=url)

    def parse(self, response):

        etiqueta_contenedora = response.css(
            'article.product_pod'
        )
        titulos = etiqueta_contenedora.css(
            'h3 > a::text'
        ).extract()

        image_url = etiqueta_contenedora.css(
            "div.image_container > a > img::attr(src)"
        ).extract()


        product_price = etiqueta_contenedora.css(
            "div.product_price > p.price_color::text"
        ).extract()

        en_stock = etiqueta_contenedora.css(
            "p.availability::text"
        ).extract()  # outofstock instock  -> otras clases


        stars = etiqueta_contenedora.css(
            "p.star-rating::attr(class)"
        ).extract()


        print("TITULOS")
        print(titulos)
        print("URL IMAGEN")
        print(image_url)
        print("PRECIO")
        print(product_price)
        print("TRANSFORMACIÓN")
        print(list(map(lambda s: float(s[1:]) , product_price)))

        print("EN STOCK")
        print(list(
                filter(
                    lambda f: f != "",
                    map(
                        lambda s: s.replace("\n", "").strip() , en_stock
                        )
                    )
                )
            )
        print("Stars")
        print(list(
            map(
                IntroSpider.my_transform_stars,
                map(
                    lambda s: s.strip().split(" "),
                    stars
                )
            
            )
            
        ))

    @staticmethod
    def my_transform_stars(full_split):

        if len(full_split) == 2:
            numero_cadena = full_split[1]
            if numero_cadena == "One":
                return 1
            elif numero_cadena == "Two":
                return 2
            elif numero_cadena == "Three":
                return 3
            elif numero_cadena == "Four":
                return 4
            elif numero_cadena == "Five":
                return 5
            else:
                print(numero_cadena, "NO CONTEMPLADO")
                raise Exception("Imposible")
        else:
            return 0
        


    