# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StockItem(scrapy.Item):
    time = scrapy.Field()
    volume = scrapy.Field()
    price = scrapy.Field()
    h_price = scrapy.Field()
    l_price = scrapy.Field()
    code = scrapy.Field()


# 시간 = time
# 거래량 = volume 
# 가격 = price
# 최고가 = h_price
# 최저가 = l_price
# 종목코드 = code