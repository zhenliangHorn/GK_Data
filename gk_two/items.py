# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GkTwoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class EnrollPlanItem(scrapy.Item):


    school_id = scrapy.Field()
    first_level = scrapy.Field()
    major_name = scrapy.Field()
    recruit_num = scrapy.Field()
    recruit_type = scrapy.Field()
    recruit_batch = scrapy.Field()
    category = scrapy.Field()
    educate_year = scrapy.Field()
    year = scrapy.Field()
    batch_id = scrapy.Field()

    school_name = scrapy.Field()
    province_id = scrapy.Field()
    pass


class SchoolIdNameItem(scrapy.Item):


    school_id = scrapy.Field()
    school_name = scrapy.Field()
    author = scrapy.Field()

class MajorScoreItem(scrapy.Item):


    school_id = scrapy.Field()
    province_id = scrapy.Field()
    recruit_type = scrapy.Field()
    major_name = scrapy.Field()
    year = scrapy.Field()
    low_majscore = scrapy.Field()
    recruit_batch = scrapy.Field()
    batch_id = scrapy.Field()
    avg_majscore = scrapy.Field()
    edu_mode = scrapy.Field()
    category = scrapy.Field()
    first_level = scrapy.Field()
    author = scrapy.Field()



class ProvinceIdNameItem(scrapy.Item):


    province_id = scrapy.Field()
    province_name = scrapy.Field()
    author = scrapy.Field()

class SchoolScoreItem(scrapy.Item):


    school_id = scrapy.Field()
    province_id = scrapy.Field()
    low_schscore = scrapy.Field()
    recruit_type = scrapy.Field()
    recruit_batch = scrapy.Field()
    batch_id = scrapy.Field()
    year = scrapy.Field()
    avg_schscore = scrapy.Field()
    author = scrapy.Field()

    pass









