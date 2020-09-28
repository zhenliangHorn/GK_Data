
import scrapy
import json
# from gk_two.getIp import GetIpThread
import time


from gk_two.items import ProvinceIdNameItem
import pymysql


class ProvinceIdName(scrapy.Spider):
    name = 'provinceIdName'
    headers = {
        'Origin': 'https://gkcx.eol.cn',
        # 'Referer':'https://gkcx.eol.cn/school/54'
        'Referer': 'https://gkcx.eol.cn/school/566/provinceline',
        'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
    }
    custom_settings = {
        'ITEM_PIPELINES': {
            'gk_two.pipelines.ProvinceIdNamePipeline': 301,
        }
    }


    year = 0
    def start_requests(self):
        start_urls = []
        for i in range(149):
            url = 'https://api.eol.cn/gkcx/api/?request_type=1&size=20&sort=view_total&uri=apigkcx/api/school/hotlists&page={}'.format(
                i + 1)
            start_urls.append(url)

        for url in start_urls:

            # start_urls = ['https: // data - gkcx.eol.cn / soudaxue / queryschool.html?messtype = json & page = 1 & size = 2843']
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)
            print("=========")
            time.sleep(0.3)
            # yield scrapy.FormRequest(url=url, callback=self.parse, formdata=form_data,headers=self.headers)
    # 解析首页
    def parse(self, response):
        # print("response!!!!!!!!!!")
        # print(response)
        doc = json.loads(response.body_as_unicode(),encoding="utf-8")
        # print(len(doc))
        # if len(doc) != 1:
        datas = doc['data']['item']

        for data in datas:
            # 拿到每个学校的id和名称
            province_id = data['province_id']
            province_name = data['province_name']
            print(province_name)
            provincelIdName_items = ProvinceIdNameItem()
            provincelIdName_items['province_id'] = data['province_id']
            provincelIdName_items['province_name'] = data['province_name']

            provincelIdName_items['author'] = "郝振良"

            yield provincelIdName_items

