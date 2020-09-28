import scrapy
import json
# from gk_two.getIp import GetIpThread
from gk_two.items import MajorScoreItem
import pymysql

import  time


class MajorScore(scrapy.Spider):
    name = 'majorScore'
    headers = {
        'Origin': 'https://gkcx.eol.cn',
        # 'Referer':'https://gkcx.eol.cn/school/54'
        'Referer': 'https://gkcx.eol.cn/school/566/provinceline',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'gk_two.pipelines.MajorScorePipeline': 301,
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
        # for yeraNumber in range(2019,2016,-1):

        for data in datas:
            # 拿到每个学校的id和名称
            school_id = data['school_id']
            # for provinceNumber in range(1,36):
            for recruit_type in range(1,4):
                for i in range(1,10):
                    url ='https://static-data.eol.cn/www/2.0/schoolspecialindex/2018/{}/13/{}/{}.json'.format(school_id,recruit_type,i)
                # 获取专业计划（文理科、批次啥的）
                    yield scrapy.Request(url=url, callback=self.parseSpecial, headers=self.headers)
                    time.sleep(0.05)

    def parseSpecial(self, response):
        print("=====================================")
        # 拿到招生计划表的json
        specilaData = json.loads(response.body_as_unicode())
        if len(specilaData)!=0:
            for special in specilaData['data']['item']:
                majorScore_items = MajorScoreItem()
                majorScore_items['school_id'] = special['school_id']
                # enrollPlan_items['school_code'] = schoolCode
                majorScore_items['province_id'] = special['province']
                majorScore_items['recruit_type'] = special['type']
                majorScore_items['major_name'] = special['spname']
                majorScore_items['year'] = 2018
                # 这里只有批次的代码数字
                majorScore_items['low_majscore'] = special['min']
                majorScore_items['recruit_batch'] = special['local_batch_name']
                majorScore_items['batch_id'] = special['batch']
                majorScore_items['avg_majscore'] = special['average']
                majorScore_items['edu_mode'] = special['zslx_name']
                majorScore_items['category'] = special['level2_name']
                majorScore_items['first_level'] = special['level3_name']
                majorScore_items['author'] = "郝振良"

                time.sleep(0.05)
                yield majorScore_items
        else:
            print("json为空")
