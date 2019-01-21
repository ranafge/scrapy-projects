# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader import ItemLoader
from scrapy.loader.processors import Compose, MapCompose, Join, TakeFirst
clean_text = Compose(MapCompose(lambda v: v.strip()), Join())
to_int = Compose(TakeFirst(), int)

class MyItem(scrapy.Item):
    Ponster_Name = scrapy.Field()
    Phone_Number = scrapy.Field()
    Church_Name = scrapy.Field()
    Address = scrapy.Field()
    No_of_Member = scrapy.Field()
    Website = scrapy.Field()

class MyItemLoader(ItemLoader):
    default_item_class = MyItem
    Ponster_Name = clean_text
    Phone_Number = clean_text
    Church_Name = clean_text
    Address = clean_text
    No_of_Member = clean_text
    Website = clean_text
