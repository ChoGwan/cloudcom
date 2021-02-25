# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class StockPipeline:
    def __init__(self):
        self.setupDBconnect()
        self.createTable()

    def process_item(self, item, spider):
        self.storeInDb(item)
        return item

    def storeInDb(self, item):
        sql = 'INSERT INTO STOCK(create_at, code, price, h_price, l_price, volume) VALUES (%s,%s,%s,%s,%s,%s)'

        self.cur.execute(sql, (item.get('time'), item.get('code'), item.get('price'), item.get('h_price'), item.get('l_price'), item.get('volume')))
        print('Data stored in DB')
        self.conn.commit()


    def setupDBconnect(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='mydb', charset='utf8')
        self.cur = self.conn.cursor()
        print("DB Connected")

    def createTable(self):
        # self.cur.execute("DROP TABLE IF EXISTS STOCK")

        self.cur.execute('''
        CREATE TABLE IF NOT EXISTS STOCK(
            time TIMESTAMP DEFAULT NOW(), 
            create_at VARCHAR(50), 
            code VARCHAR(50), 
            price VARCHAR(50),
            h_price VARCHAR(50), 
            l_price VARCHAR(50),
            volume VARCHAR(50)    
        )''')
