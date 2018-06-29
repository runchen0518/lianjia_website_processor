#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: python 2.7.13
# @author: baorunchen(runchen0518@gmail.com)
# @date: 2018/6/28

import requests
from bs4 import BeautifulSoup
import re
import sys
from sys import version_info

# python3是默认'utf-8'编码的；如果是python2版本，不是'utf-8'编码，可设成'utf-8'编码
if version_info.major == 2:
    from imp import reload

    reload(sys)
    sys.setdefaultencoding('utf-8')

# 伪装成浏览器
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}

# 房屋总价
price = []
# 房屋均价
uprice = []
# 房屋信息
house = []
# 位置信息
position = []

region = ['ganjingzi', 'shahekou', 'zhongshan', 'xigang', 'gaoxinyuanqu']
regnam = ['甘井子', '沙河口', '中山', '西岗', '高新园']


def main():
    for i in range(0, 5):
        regnum = i
        for j in range(0, 10):
            page = j + 1
            print('开始抓取' + regnam[regnum] + '区的第' + str(page) + '页房产信息, 每一页大概有30个房子')
            # 请求网页
            r = requests.get('https://dl.lianjia.com/ershoufang/' + region[regnum] + '/pg' + str(page), headers,
                             timeout=30)
            # 转码
            r.encoding = r.apparent_encoding
            # 获取网页源代码
            demo = r.text
            # 解析网页源代码
            soup = BeautifulSoup(demo, 'html.parser')
            # 抓取房屋总价
            totalprice = soup.find_all('div', 'totalPrice')
            # 抓取房屋均价
            uniteprice = soup.find_all('div', 'unitPrice')
            # 抓取房屋信息
            houseinfo = soup.find_all('div', 'houseInfo')

            for k in range(len(totalprice)):
                # 把房屋总价放进price list
                price.insert(k, float(totalprice[k].text[:-1]))
                # 把房屋均价放进uprice list
                uprice.insert(k, float(uniteprice[0].text[2:-4]))
                # 把房屋信息装进house list
                house.insert(k, houseinfo[k].text)

                # 获取房子GPS详情页
                r = requests.get(houseinfo[k].find('a').get('href'), headers, timeout=30)
                # 解析房子GPS详情页
                findpos = BeautifulSoup(r.text, 'html.parser')
                # 获取房子所在地GPS经纬度
                pos = re.findall(r'resblockPosition:\'[\d\.\,]*', str(findpos))
                # 将GPS经纬度存入position变量
                position.insert(k, pos[0][18:-1])
                # 打印爬取结果
                print('抓到了第' + str(k + 1) + '个房子')

            # 写入文件
            with open(region[regnum] + '.txt', 'w') as f:
                for m in range(len(price)):
                    # 将房屋总价写入txt文件
                    f.write(str(price[m]) + ',' + str(uprice[m]) + ',' + str(house[m]) + ',' + str(position[m]) + '\n')
            print('抓完了，保存到 ' + region[regnum] + '.txt 里面了')


if __name__ == '__main__':
    main()
