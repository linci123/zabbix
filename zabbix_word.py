# import preppy
# from z3c.rml import rml2pdf
# import docx
# from docx import Document
# from docx.shared import Inches
# import os
# from PIL import Image
from multiprocessing import AuthenticationError
from sqlite3 import connect
import requests


import os
import datetime
import json

class ZabbixApi:
    def __init__(self):
        # self.session = requests.session()
        self.url = 'http://192.168.2.26/zabbix/api_jsonrpc.php'
        self.username = "Admin"
        self.password = "030699Tbo"
        self.headers = {'Content-Type': 'application/json'} 
        self.current_date = datetime.datetime.now().strftime("%Y%m%d")

    def login(self):
        auth = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.username,
                "password": self.password
            },
            "id": 0,
            "auth": None,
        }
        # requests.encoding = "utf8"
        request = requests.post(self.url, data=json.dumps(auth), headers=self.headers)
        connect = json.loads(request.text)
        return connect['result']

    def host_get(self,token_code):
        auth = {
            # "jsonrpc": "2.0",
            # "method": "host.get",
            # "params": {
            #     "output": [
            #         "hostid",
            #         "host"
            #     ],
            #     "selectInterfaces":[
            #         "interfaceid",
            #         "ip"
            #     ],
            #     "selectGraphs": [
            #         "graphid",
            #         "name"
            #     ]                
            # },
            # "id": 2,
            # "auth": token_code            
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "hostid": 10438,
                "selectGraphs": [
                    "graphid",
                    "name"
                ],
            },
            "id": 1,
            "auth": token_code,
        }
        request = requests.post(self.url,headers=self.headers,data=json.dumps(auth))
        dict = json.loads(request.content)
        #print dict['result']
        return dict['result']


    def fetchDataGraph(self, graph_id):
        # data = requests.get("http://zabbix.tb.com/zabbix/chart2.php?graphid={graph_id}&from=now-1d%2Fd&to=now-1d%2Fd&profileIdx=web.graphs.filter&profileIdx2={graph_id}&width=600&height=150&_=ube2loaa&screenid=".format(graph_id=graph_id), stream=True, headers=self.headers, cookies=self.cookie)
        data = requests.get("http://192.168.2.26/zabbix/chart2.php?graphid=1962&from=2022-09-02%2017%3A25%3A14&to=2022-09-08%2012%3A14%3A14&height=201&width=1535&profileIdx=web.charts.filter&_=vm9qpihe")
        # if not os.path.exists("E:\\images%s" % self.current_date): os.makedirs("E:\\images%s" % self.current_date)
        with open("E:\\images", "wb") as fd:
            fd.write(data.content)
            # for chunk in data.iter_content():       
            #     fd.write(chunk)

    # def testToGeneratePDF(self):
    #     template = preppy.getModule('./template.prep')
	#     current_date = self.current_date
    #     rmlText = template.get(current_date, pic_data)
    #     pdf = rml2pdf.parseString(rmlText)
    #     if not os.path.exists("./output"): os.makedirs("./output")
    #     f = open("./output/服务器监控指标-%s.pdf" % self.current_date, "w+")
    #     f.write(pdf.read())
    #     f.close()


if __name__ ==  "__main__":


   zabbixApi = ZabbixApi()
   token_code =zabbixApi.login()
   zabbix_connect = zabbixApi.host_get(token_code)
   print(zabbix_connect)


    # pic_data = [
    #     {"name": "Nginx状态", "data": (1404, 1405)},
    #     {"name": "Redis状态", "data":  (1404, 1405)},
    #     {"name": "MYSQL指标", "data":  (1404, 1405)},
    #     {"name": "CPU 使用率", "data":  (1404, 1405)},
    #     {"name": "IO Stat", "data":  (1404, 1405)},
    #     {"name": "磁盘使用率", "data":  (1404, 1405)},
    #     {"name": "内存可用率", "data":  (1404, 1405)},
    #     {"name": "网络流量", "data":  (1404, 1405)},
    # ]
    # api = Api()
    # for v in pic_data:
    #     for x in v['data']:
    #     # if os.path.exists("images/%s/%s.png" % (current_date, x)):
    #     #    continue
    #         api.fetchDataGraph(x)
    # api.testToGeneratePDF()