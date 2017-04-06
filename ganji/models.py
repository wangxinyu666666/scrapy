from django.db import models
from mongoengine import*
from mongoengine import  connect
connect('wangxinyu',host='127.0.0.1',port=27017)
# Create your models here.
class ArtiInfo(Document):
    print('hhh')
    title=StringField()
    link=StringField()
    des=StringField()
    meta={'collection':'wangxinyu'}
for i in ArtiInfo.objects[:1]:
    print('999')
    print(i)
