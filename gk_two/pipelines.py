# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

pymysql.install_as_MySQLdb()
import MySQLdb
import MySQLdb.cursors


class GkTwoPipeline(object):
    def process_item(self, item, spider):
        print('哈哈哈哈', item)
        return item


class ProvinceIdNamePipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='localhost',
            db='gk',
            user='root',  # replace with you user name
            passwd='123456',  # replace with you password
            port=3306,
            charset='utf8',
            use_unicode=True,
        )
        self.cursor = self.connect.cursor()

    def process_item(self, provincelIdName_items, spider):
        try:
            print('beginning')
            sql = "insert into `province_id_name` (`province_id`,`province_name`,`author`) " \
                  "values ('%s','%s','%s')" % \
                  (provincelIdName_items['province_id'],
                   provincelIdName_items['province_name'],
                   provincelIdName_items['author'])
            print('进行中')
            self.cursor.execute(sql)
            print('存库中')
            self.connect.commit()
            print('存库完成')
        except pymysql.Error as error:  # pymysql.Error
            ssql = "insert into `province_id_name` (`province_id`,`province_name`,`author`) " \
                   "values ('%s','%s','%s')" % \
                   (provincelIdName_items['province_id'],
                    provincelIdName_items['province_name'],
                    provincelIdName_items['author'])
            with open('enroll_plan_right_error.txt', 'a', encoding='gbk') as f:
                f.write(sql + '\n')
                f.write(str(error) + '\n')
                f.close()
            # logging.error(error)
        return provincelIdName_items

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


class MajorScorePipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='localhost',
            db='gk',
            user='root',  # replace with you user name
            passwd='123456',  # replace with you password
            port=3306,
            charset='utf8',
            use_unicode=True,
        )
        self.cursor = self.connect.cursor()

    def process_item(self, majorScore_items, spider):
        try:
            print('beginning')
            sql = "insert into `major_score` (`school_id`,`province_id`," \
                  "`recruit_type`,`major_name`, `year`,`low_majscore`,`recruit_batch`,`batch_id`,`avg_majscore`," \
                  "`edu_mode`," \
                  "`category`,`first_level`,`author`) " \
                  "values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                  (majorScore_items['school_id'], majorScore_items['province_id'], majorScore_items['recruit_type'],
                   majorScore_items['major_name'], majorScore_items['year'], majorScore_items['low_majscore'],
                   majorScore_items['recruit_batch'],majorScore_items['batch_id'], majorScore_items['avg_majscore'], majorScore_items['edu_mode'],
                   majorScore_items['category'], majorScore_items['first_level'], majorScore_items['author'])
            print('进行中')
            self.cursor.execute(sql)
            print('存库中')
            self.connect.commit()
            print('存库完成')
        except pymysql.Error as error:  # pymysql.Error
            sql = "insert into `major_score` (`school_id`,`province_id`," \
                  "`recruit_type`,`major_name`, `year`,`low_majscore`,`recruit_batch`,`batch_id`,`avg_majscore`," \
                  "`edu_mode`," \
                  "`category`,`first_level`,`author`) " \
                  "values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                  (majorScore_items['school_id'], majorScore_items['province_id'], majorScore_items['recruit_type'],
                   majorScore_items['major_name'], majorScore_items['year'], majorScore_items['low_majscore'],
                   majorScore_items['recruit_batch'],majorScore_items['batch_id'], majorScore_items['avg_majscore'], majorScore_items['edu_mode'],
                   majorScore_items['category'], majorScore_items['first_level'], majorScore_items['author'])
            with open('Major_score_error.txt', 'a', encoding='gbk') as f:
                f.write(sql + '\n')
                f.write(str(error) + '\n')
                f.close()
            # logging.error(error)
        return majorScore_items

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


class SchoolScorePipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='localhost',
            db='gk',
            user='root',  # replace with you user name
            passwd='123456',  # replace with you password
            port=3306,
            charset='utf8',
            use_unicode=True,
        )
        self.cursor = self.connect.cursor()

    def process_item(self, schoolScore_items, spider):
        try:
            print('beginning')
            sql = "insert into `school_score` (`school_id`,`province_id`," \
                  "`low_schscore`,`recruit_type`, `recruit_batch`, `batch_id`,`year`,`avg_schscore`,`author`) " \
                  "values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                  (schoolScore_items['school_id'], schoolScore_items['province_id'], schoolScore_items['low_schscore'],
                   schoolScore_items['recruit_type'], schoolScore_items['recruit_batch'],schoolScore_items['batch_id'], schoolScore_items['year'],
                   schoolScore_items['avg_schscore'], schoolScore_items['author'])
            print('进行中')
            self.cursor.execute(sql)
            print('存库中')
            self.connect.commit()
            print('存库完成')
        except pymysql.Error as error:  # pymysql.Error
            sql = "insert into `school_score` (`school_id`,`province_id`," \
                  "`low_schscore`,`recruit_type`, `recruit_batch`, `batch_id`,`year`,`avg_schscore`,`author`) " \
                  "values ('%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                  (schoolScore_items['school_id'], schoolScore_items['province_id'], schoolScore_items['low_schscore'],
                   schoolScore_items['recruit_type'], schoolScore_items['recruit_batch'],schoolScore_items['batch_id'], schoolScore_items['year'],
                   schoolScore_items['avg_schscore'], schoolScore_items['author'])
            with open('school_score_error.txt', 'a', encoding='gbk') as f:
                f.write(sql + '\n')
                f.write(str(error) + '\n')
                f.close()
            # logging.error(error)
        return schoolScore_items

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()


class EnrollPlanPipeline(object):
    def __init__(self):
        # 连接数据库
        self.connect = pymysql.connect(
            host='localhost',
            db='gk',
            user='root',  # replace with you user name
            passwd='123456',  # replace with you password
            port=3306,
            charset='utf8',
            use_unicode=True,
        )
        self.cursor = self.connect.cursor()

    def process_item(self, enrollPlan_items, spider):
        try:
            print('beginning')
            sql = "insert into `enroll_plan_right` (`school_id`,`province_id`," \
                  "`year`,`major_name`, `recruit_num`,`category`,`first_level`,`educate_year`,`recruit_type`," \
                  "`recruit_batch`,`batch_id`) " \
                  "values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                  (enrollPlan_items['school_id'],
                   enrollPlan_items['province_id'], enrollPlan_items['year'],
                   enrollPlan_items['major_name'], enrollPlan_items['recruit_num'], enrollPlan_items['category'],
                   enrollPlan_items['first_level'], enrollPlan_items['educate_year'], enrollPlan_items['recruit_type'],
                   enrollPlan_items['recruit_batch'], enrollPlan_items['batch_id'])
            print('进行中')
            self.cursor.execute(sql)
            print('存库中')
            self.connect.commit()
            print('存库完成')
        except pymysql.Error as error:  # pymysql.Error
            sql = "insert into `enroll_plan_right` (`school_id`,`province_id`," \
                  "`year`,`major_name`, `recruit_num`,`category`,`first_level`,`educate_year`,`recruit_type`," \
                  "`recruit_batch`,`batch_id`) " \
                  "values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % \
                  (enrollPlan_items['school_id'],
                   enrollPlan_items['province_id'], enrollPlan_items['year'],
                   enrollPlan_items['major_name'], enrollPlan_items['recruit_num'], enrollPlan_items['category'],
                   enrollPlan_items['first_level'], enrollPlan_items['educate_year'], enrollPlan_items['recruit_type'],
                   enrollPlan_items['recruit_batch'], enrollPlan_items['batch_id'])
            with open('enroll_plan_right_error.txt', 'a', encoding='gbk') as f:
                f.write(sql + '\n')
                f.write(str(error) + '\n')
                f.close()
            # logging.error(error)
        return enrollPlan_items

    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
