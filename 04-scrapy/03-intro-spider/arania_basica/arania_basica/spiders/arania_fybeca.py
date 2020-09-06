import scrapy
import json

class FybecaSpider(scrapy.Spider):

    name = 'spyder_fybeca'

    urls = [
        'https://www.fybeca.com/FybecaWeb/pages/search-results.jsf?cat=639&s=0&pp=25'
    ]

    def start_requests(self):

        for url in self.urls:
            yield scrapy.Request(url=url)



    """
    li class="product-tile " 
    data-id="100199774" 
    data-name="EST 5 PZS GRC CREMA LAVENDER GRC-5729" 
    data-price="{&quot;unit&quot;:0, &quot;presentation&quot;:29.57, &quot;vitalcard&quot; : 29.57}" 
    data-unit="GOTAS" 
    data-box="1" 
    data-type="N" 
    data-isoffer="false">

    """
    def parse(self, response):

        etiqueta_contenedora = response.css(
            'li.product-tile'
        )

        id = etiqueta_contenedora.css(
            '::attr(data-id)'
        ).extract()

        name = etiqueta_contenedora.css(
            '::attr(data-name)'
        ).extract()

        
        price = etiqueta_contenedora.css(
            '::attr(data-price)'
        ).extract()

        unit = etiqueta_contenedora.css(
            '::attr(data-unit)'
        ).extract()

        is_offer = etiqueta_contenedora.css(
            '::attr(data-isoffer)'
        ).extract()

        print("\nID")
        print(id)
        print("\nName")
        print(name)
        print("\nPrice")
        print(
            FybecaSpider.transform_json(price)
        )
        print("\nUnit")
        print(unit)
        print("\nIsOffer")
        print(is_offer)


        index_min, min, index_max, max, sum_presentation, sum_vitalcard = FybecaSpider.get_highest_lowest(FybecaSpider.transform_json(price))

        print("El de menor valor: ", name[index_min], "Con valor: ", min)
        print("El de mayor valor: ", name[index_max], "Con valor: ", max)

        
        print("Si se compra normal: ", sum_presentation)
        print("Si se compra como afiliado: ", sum_vitalcard, " Se ahorra: ", sum_vitalcard-sum_presentation)

        
    

    @staticmethod
    def transform_json(price_json):

        prices = []

        for price in price_json:
            prices.append(json.loads(price))

        return prices


    @staticmethod
    def get_highest_lowest(prices_dict):
        index_min = 0
        min = prices_dict[index_min]['presentation']
        index_max = 0
        max = prices_dict[index_max]['presentation']

        sum_presentation = 0
        sum_vitalcard = 0

        for index, price_dict in enumerate(prices_dict):

            value = price_dict['presentation']

            sum_presentation += price_dict['presentation']
            sum_vitalcard += price_dict['vitalcard']
            
            if value > max:
                max = value
                index_max = index

            if value < min:
                min = value
                index_min = index
        
        return index_min, min, index_max, max, sum_presentation, sum_vitalcard



    #1ra cual es el item con mayor y menor precio

    #cuanto ahorramos si compramos todo como afiliado
