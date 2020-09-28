import scrapy
import json
# from gk_two.getIp import GetIpThread
from gk_two.items import SchoolScoreItem
import pymysql

import  time


class ScoreSchoolMajor(scrapy.Spider):
    name = 'scoreSchool'
    headers = {
        'Origin': 'https://gkcx.eol.cn',
        # 'Referer':'https://gkcx.eol.cn/school/54'
        'Referer': 'https://gkcx.eol.cn/school/566/provinceline',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'gk_two.pipelines.SchoolScorePipeline': 301,
        }
    }


    year = 0
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
                for i in range(1,6):
                    url ='https://static-data.eol.cn/www/2.0/schoolprovinceindex/detial/{}/13/{}/{}.json'.format(school_id,recruit_type,i)
                # 获取专业计划（文理科、批次啥的）
                    yield scrapy.Request(url=url, callback=self.parseSpecial, headers=self.headers)
                    time.sleep(0.1)

    def parseSpecial(self, response):
        print("=====================================")
        # 拿到招生计划表的json
        specilaData = json.loads(response.body_as_unicode())
        if len(specilaData)!=0:
            for special in specilaData['data']['item']:
                schoolScore_items = SchoolScoreItem()

                schoolScore_items['school_id'] = special['school_id']
                schoolScore_items['province_id'] = special['province_id']
                schoolScore_items['low_schscore'] = special['min']
                schoolScore_items['recruit_type'] = special['type']
                schoolScore_items['recruit_batch'] = special['local_batch_name']
                schoolScore_items['batch_id'] = special['batch']
                schoolScore_items['year'] = special['year']
                schoolScore_items['avg_schscore'] = special['average']
                schoolScore_items['author'] = "郝振良"
                # enrollPlan_items['school_code'] = schoolCode


                time.sleep(0.1)
                yield schoolScore_items
        else:
            print("json为空")
