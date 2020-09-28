import scrapy
import json
# from gk_two.getIp import GetIpThread
from gk_two.items import EnrollPlanItem
import pymysql

import  time


class ScoreSchoolMajor(scrapy.Spider):
    name = 'ecrollPlan'
    headers = {
        'Origin': 'https://gkcx.eol.cn',
        # 'Referer':'https://gkcx.eol.cn/school/54'
        'Referer': 'https://gkcx.eol.cn/school/566/provinceline',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'gk_two.pipelines.EnrollPlanPipeline': 301,
        }
    }



    def start_requests(self):
        start_urls = []
        for i in range(148):
            url = 'https://api.eol.cn/gkcx/api/?request_type=1&size=20&sort=view_total&uri=apigkcx/api/school/hotlists&page={}'.format(
                i + 1)
            start_urls.append(url)

        for url in start_urls:
            # start_urls = ['https: // data - gkcx.eol.cn / soudaxue / queryschool.html?messtype = json & page = 1 & size = 2843']
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)
            # time.sleep(0.33)
            # yield scrapy.FormRequest(url=url, callback=self.parse, formdata=form_data,headers=self.headers)
    # 解析首页
    def parse(self, response):
        # print("response!!!!!!!!!!")
        # print(response)
        doc = json.loads(response.body_as_unicode())
        # print(len(doc))
        # if len(doc) != 1:
        datas = doc['data']['item']

        for data in datas:
            # 拿到每个学校的id和名称
            school_id = data['school_id']
            # for provinceNumber in range(1,36):
            for recruit_type in range(1,4):
                for batchNumber in range(1,100):
                    for i in range(1,6):
                        url ='https://static-data.eol.cn/www/2.0/schoolplanindex/2020/{}/13/{}/{}/{}.json'.format(school_id,recruit_type,batchNumber,i)

                        yield scrapy.Request(url=url, callback=self.parseSpecial, headers=self.headers)
                        time.sleep(0.01)

    def parseSpecial(self, response):
        print("=====================================")
        # 拿到招生计划表的json
        specilaData = json.loads(response.body_as_unicode())
        if len(specilaData)!=0:
            for special in specilaData['data']['item']:
                enrollPlan_items = EnrollPlanItem()
                enrollPlan_items['school_id'] = special['school_id']
                # enrollPlan_items['school_code'] = schoolCode
                enrollPlan_items['province_id'] = special['province']
                enrollPlan_items['recruit_num'] = special['num']
                enrollPlan_items['recruit_type'] = special['type']
                enrollPlan_items['year'] = 2020
                # 这里只有批次的代码数字
                enrollPlan_items['batch_id'] = special['batch']
                enrollPlan_items['educate_year'] = special['length']
                enrollPlan_items['category'] = special['level2_name']
                enrollPlan_items['first_level'] = special['level3_name']
                enrollPlan_items['major_name'] = special['spname']
                enrollPlan_items['recruit_batch'] = special['local_batch_name']

                time.sleep(0.01)
                yield enrollPlan_items
        else:
            print("json为空")
    #         if special['year'] == 2019:
    #             for item in special['province']:  # 这个学校2019年对各个省份的招生计划
    #                 for category in item['type']:  # 这个学校2019年对文理科的招生计划
    #                     for batch in item['batch']:  # 这个学校2019年对批次的招生计划
    #                         for i in range(5):  # 这个学校2019年对某个省份文/理科某个批次的第几页的招生计划
    #                             specialUrl = 'https://api.eol.cn/gkcx/api/?local_batch_id={}&local_province_id={}&local_type_id={}&page={}&school_id={}&size=10&uri=apidata/api/gk/plan/special&year=2019'.format(
    #                                 batch, item['pid'], category, i + 1, schoolId)
    #                             # yield scrapy.Request(url=specialUrl, callback=self.parseEnroll, headers=self.headers)
    #                             yield scrapy.Request(url=specialUrl, callback=self.parseEnroll, headers=self.headers,
    #                                                  meta={'schoolId': schoolId, 'schoolName': schoolName,
    #                                                        # 'schoolCode': schoolCode,
    #                                                        'provinceId': item['pid'], 'category': category})
    #                             # print(specialUrl)
    #     # print('专业计划', specilaData['data']['data'])
    #
    # def parseEnroll(self, response):
    #     schoolId = response.meta['schoolId']
    #     # schoolName = response.meta['schoolName']
    #     provinceId = str(response.meta['provinceId']) + '0000'
    #     # schoolCode = response.meta['schoolCode']
    #     category = response.meta['category']
    #     # print('类型：', type(category))
    #     if category == 1:
    #         category = '理科'
    #     elif category == 2:
    #         category = '文科'
    #     # print(category)
    #     enrollInfo = json.loads(response.body_as_unicode())
    #     print('招生信息', enrollInfo)
    #     enrollDetail = enrollInfo['data']['item']
    #     if len(enrollDetail) != 0:
    #         for item in enrollDetail:
    #             enrollPlan_items = EnrollPlanItem()
    #             enrollPlan_items['school_id'] = schoolId
    #             # enrollPlan_items['school_code'] = schoolCode
    #             enrollPlan_items['school_name'] = item['name']
    #             enrollPlan_items['province_id'] = provinceId
    #             enrollPlan_items['province_name'] = ''
    #             enrollPlan_items['major_id'] = ''
    #             enrollPlan_items['major_big_name'] = item['level2_name']
    #             enrollPlan_items['major_second_name'] = item['level3_name']
    #             enrollPlan_items['major_name'] = item['spname']
    #             enrollPlan_items['category'] = category
    #             # enrollPlan_items['category'] = item['status']
    #             enrollPlan_items['batch'] = item['local_batch_name']
    #             enrollPlan_items['enroll_num'] = item['num']
    #             yield enrollPlan_items
