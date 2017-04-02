#coding=utf-8
import re
import json
import string
import os
from scrapy.selector import Selector
try:
	from scrapy.spider import Spider
except:
	from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.lxmlhtml import  LxmlLinkExtractor as sle
from sinanet.items import *
from scrapy.http import Request
class SinanetSpider(CrawlSpider) :
	#定义爬虫的名称
	name = "SinanetSpider"
	#定义允许抓取的域名,如果不是在此列表的域名则放弃抓取
	allowed_domains = ["news.sina.com.cn"]
	#定义抓取的入口url
	start_urls = [
		"http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_1.shtml"
	]
	def parse2(self,response):


		hxs =Selector(response)
		item = response.meta['item']
		#items=[]
		List= hxs.xpath('//*[@id="artibody"]/p/text()').extract()
		item['desc']=''.join(List)
		#item.remove('\u3000')
		print(item['desc'])
		#print(item)
		return item
	#定义回调函数
	#提取数据到Items里面，主要用到XPath和CSS选择器提取网页数据
	def parse(self, response):
		#print "-----------------"

		items=[]
		sel = Selector(response)
		base_url = get_base_url(response)
		postTitle = sel.xpath('//ul[@class="list_009"]/li')
		#print(len(postTitle))
		for eachpostTitle in postTitle:
			item = SinanetItem()
			#print(eachpostTitle)

			item['title'] = eachpostTitle.xpath('a/text()').extract()[0]
			#print(item['title'] + "***************\r\n")
			#print ("hahahhahahah" )
			item['link'] = eachpostTitle.xpath('a/@href').extract()[0]

			items.append(item)
		for item in items:
			#print(item)


			yield scrapy.Request(item['link'],callback=self.parse2,meta={'item':item})

			#print('------------------------------------------')







