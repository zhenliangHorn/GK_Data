# -*- coding: utf-8 -*-
# @Time : 2020/9/14 18:47
# @Author : 郝振良
# @FileName: ChooseClass.py
# @Software: PyCharm

from lxml import etree
import scrapy
import json
# from gk_two.getIp import GetIpThread
from gk_two.items import EnrollPlanItem
import pymysql

import  time


class ChooseClass(scrapy.Spider):
    name = 'chooseClass'
    headers = {
        'Origin': 'http://zt.zjzs.net/',
         # 'Referer':'http://zt.zjzs.net/xk2020/subject_0.html'
        'Referer': 'http://zt.zjzs.net/xk2020/subject_0.html',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'gk_two.pipelines.EnrollPlanPipeline': 301,
        }
    }


    j = 1
    def start_requests(self):

        # for i in range(9999,16450):
        #     self.j = i;
            url = 'http://zt.zjzs.net/xk2020/10001.html'
            time.sleep(0.5)
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    # 解析首页
    def parse(self, response):
        time.sleep(0.5)
        data =  response.text
        html = etree.HTML(data)
        page = html.xpath("//div[@class='subTitle']/div/text()")
        schoolName = str (page[0])
        schoolName = schoolName.strip()
        schoolName = schoolName.split('：')
        print(schoolName[1])

        page1 = html.xpath("//div[@class='search']/table/tr/td/text()")[0:4]
        # print(schoolName.strip().split(";"))
        print(page1)
        # if(len(data)>0):
        #     with open("D:/GKProject/2020年全国各省选考要求/浙江/{}.txt".format(self.j), "w") as f:
        #         f.write(response.body_as_unicode())
        # else:
        #     print("空咔咔咔咔咔咔扩扩扩")

            # datas = doc['data']['item']
        #
        # for data in datas:
        #     # 拿到每个学校的id和名称
        #     school_id = data['school_id']
        #     # for provinceNumber in range(1,36):
        #     for recruit_type in range(1,4):
        #         for batchNumber in range(1,100):
        #             for i in range(1,6):
        #                 url ='https://static-data.eol.cn/www/2.0/schoolplanindex/2020/{}/13/{}/{}/{}.json'.format(school_id,recruit_type,batchNumber,i)
        #
        #                 yield scrapy.Request(url=url, callback=self.parseSpecial, headers=self.headers)
        #                 time.sleep(0.01)


    # def parseSpecial(self, response):
    #     print("=====================================")
    #     # 拿到招生计划表的json
    #     specilaData = json.loads(response.body_as_unicode())
    #     if len(specilaData)!=0:
    #         for special in specilaData['data']['item']:
    #             enrollPlan_items = EnrollPlanItem()
    #             enrollPlan_items['school_id'] = special['school_id']
    #             # enrollPlan_items['school_code'] = schoolCode
    #             enrollPlan_items['province_id'] = special['province']
    #             enrollPlan_items['recruit_num'] = special['num']
    #             enrollPlan_items['recruit_type'] = special['type']
    #             enrollPlan_items['year'] = 2020
    #             # 这里只有批次的代码数字
    #             enrollPlan_items['batch_id'] = special['batch']
    #             enrollPlan_items['educate_year'] = special['length']
    #             enrollPlan_items['category'] = special['level2_name']
    #             enrollPlan_items['first_level'] = special['level3_name']
    #             enrollPlan_items['major_name'] = special['spname']
    #             enrollPlan_items['recruit_batch'] = special['local_batch_name']
    #
    #             time.sleep(0.01)
    #             yield enrollPlan_items
    #     else:
    #         print("json为空")
