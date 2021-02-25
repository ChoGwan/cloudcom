import scrapy
from Stock.items import StockItem

class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['finance.naver.com/item/main.nhn?code=017670']
    start_urls = ['https://finance.naver.com/item/main.nhn?code=017670']

    def parse(self, response):
        times = response.xpath('//*[@id="time"]/em/text()').extract()
        volumes = response.xpath('//*[@id="middle"]/dl/dd[11]/text()').extract()
        prices = response.xpath('//*[@id="middle"]/dl/dd[4]/text()').extract()
        h_prices = response.xpath('//*[@id="middle"]/dl/dd[7]/text()').extract()
        l_prices = response.xpath('//*[@id="middle"]/dl/dd[9]/text()').extract()
        codes = response.xpath('//*[@id="middle"]/div[1]/div[1]/div/span[1]/text()').extract()

        items = []
        for idx in range(len(times)):
            item = StockItem()
            item['time'] = times[idx].split(' ')[1]
            item['volume'] = volumes[idx].split(' ')[1]
            item['price'] = prices[idx].split(' ')[1]
            item['h_price'] = h_prices[idx].split(' ')[1]
            item['l_price'] = l_prices[idx].split(' ')[1]
            item['code'] = codes[idx]            
            items.append(item)
        
        
        return items

