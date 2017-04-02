# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy import signals
import json
import codecs

from sqlalchemy.orm import sessionmaker
from sinanet.model import Article, db_connect, create_articless_table
class DataBasePipeline(object):
    def __init2__(self):
        engine = db_connect()
        create_articless_table(engine)
        self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        session = self.Session()
        print('888888888888888888888888')
        print(item['title'])
        articless = Article(**item)
        session.add(articless)  # 添加数据
        session.commit()  # 保存修改
        return item

