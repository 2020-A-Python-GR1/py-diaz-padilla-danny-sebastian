import scrapy
import json

class FybecaSpider(scrapy.Spider):

    name = 'deber_fybeca'

    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=537&s=0&pp=25',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=446&s=0&pp=25',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=627&s=0&pp=25',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=558&s=0&pp=25',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=562&s=0&pp=25',
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=489&s=0&pp=25'
    ]

    def start_requests(self):

        for url in self.urls:
            yield scrapy.Request(url=url)



    def parse(self, response):

        etiqueta_contenedora = response.css(
            'div.product-tile-inner'
        )

        name = etiqueta_contenedora.css(
            'a.name::text'
        ).extract()

        normal_price = etiqueta_contenedora.css(
            'div.detail > div.side > div.price::attr(data-bind)'
        ).extract()

        member_price = etiqueta_contenedora.css(
            'div.detail > div.side > div.price-member > div::attr(data-bind)'
        ).extract()

        url_image = etiqueta_contenedora.css(
            'div.detail > a.image > img::attr(src)'
        ).extract()


        # print("Name")
        # print(name)
        # print("normal_price")
        normal_price = list(
            map(
                FybecaSpider.transform_price,
                normal_price
            )
        )
        # print(normal_price)
        # print("\nmember_price")
        member_price = list(
            map(
                FybecaSpider.transform_price,
                member_price
            )
        )
        # print(member_price)
        # print("\nurl_image")
        # print(url_image)

        normal_price_min = min(normal_price)
        normal_price_max = max(normal_price)

        member_price_min = min(member_price)
        member_price_max = max(member_price)

        sum_normal_price = sum(normal_price)
        sum_member_price = sum(member_price)

        print("\nPROCESAMIENTO para")
        print(name)
        print("Menor de precio normal: {0}, Máximo de precio normal: {1}".format(normal_price_min, normal_price_max))
        print("Menor de precio miembro: {0}, Máximo de precio miembro: {1}".format(member_price_min, member_price_max))
        print("Normal pago: {0}, Si soy miembro pago: {1} y ahorro: {2}\n".format(sum_normal_price, sum_member_price, sum_normal_price-sum_member_price))
        



    """


        index_min, min, index_max, max, sum_presentation, sum_vitalcard = FybecaSpider.get_highest_lowest(FybecaSpider.transform_json(price))

        print("El de menor valor: ", name[index_min], "Con valor: ", min)
        print("El de mayor valor: ", name[index_max], "Con valor: ", max)

        
        print("Si se compra normal: ", sum_presentation)
        print("Si se compra como afiliado: ", sum_vitalcard, " Se ahorra: ", sum_vitalcard-sum_presentation)
    """
    @staticmethod
    def transform_price(string_fybeca_data_bind):
        # text:'$' + (8.08).formatMoney(2, '.', ',')
        return float(string_fybeca_data_bind[12:16])


    


    #1ra cual es el item con mayor y menor precio

    #cuanto ahorramos si compramos todo como afiliado
