#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @version: python 2.7.13
# @author: baorunchen(runchen0518@gmail.com)
# @date: 2018/6/29

import matplotlib.pyplot as plt
import numpy as np
import os.path

# 区域名称的拼音
region = ['ganjingzi', 'shahekou', 'zhongshan', 'xigang', 'gaoxinyuanqu']
# 区域名称的中文
regnam = ['甘井子', '沙河口', '中山', '西岗', '高新园']

# 房屋总价
price = [[], [], [], [], []]
# 房屋均价
uprice = [[], [], [], [], []]
# 房屋信息
house = [[], [], [], [], []]
# GPS经度
gpsx = [[], [], [], [], []]
# GPS纬度
gpsy = [[], [], [], [], []]
# 五个区的均价
average_price = [0, 0, 0, 0, 0]
# 五个区里最高总价
max_price = [0, 0, 0, 0, 0]
# 五个区里最低总价
min_price = [0, 0, 0, 0, 0]


def main():
    for i in range(5):
        regnum = i
        with open(region[regnum] + '.txt') as f:
            # 读取文件内容
            fd = f.readlines()
        # 按行读取
        for i in range(len(fd)):
            # 分解数据
            tmp = fd[i].split(',')
            # 获得房屋总价数据
            price[regnum].insert(i, float(tmp[0]))
            # 获得房屋均价数据
            uprice[regnum].insert(i, float(tmp[1]))
            # 获得房屋信息数据
            house[regnum].insert(i, tmp[2])
            # 获得房屋GPS数据
            gpsx[regnum].insert(i, float(tmp[3]))
            gpsy[regnum].insert(i, float(tmp[4]))

        average_price[regnum] = np.mean(uprice[regnum][:])
        # 计算这个区的最高房价数据
        max_price[regnum] = max(price[regnum][:])
        min_price[regnum] = min(price[regnum][:])
        # 打印显示数据
        print(regnam[regnum] + '区的房价均值是' + str(average_price[regnum]) + '元/平方米')
        print(regnam[regnum] + '区的房价最高的房子是' + str(max_price[regnum]) + '万元, 地点是: ' + house[regnum][
            price[regnum][:].index(max_price[regnum])])
        print(regnam[regnum] + '区的房价最低的房子是' + str(min_price[regnum]) + '万元, 地点是: ' + house[regnum][
            price[regnum][:].index(min_price[regnum])])

    # 均值
    # 图的序号是1
    plt.figure(1)
    # 图的标题
    plt.title('Average price of house in Dalian', fontsize=15, color='r')
    # 画个柱状图
    plt.bar(range(5), average_price, tick_label=region, color='rygbk')

    # 画这个区域最高房价柱状图
    # 图的序号是1
    plt.figure(2)
    # 图的标题
    plt.title('The most expensive house in Dalian', fontsize=15, color='r')
    # 画个柱状图
    plt.bar(range(5), max_price, tick_label=region, color='rygbk')

    # 最低房价
    # 图的序号是1
    plt.figure(3)
    # 图的标题
    plt.title('The cheapest house in Dalian', fontsize=15, color='r')
    # 绘制柱状图
    plt.bar(range(5), min_price, tick_label=region, color='rygbk')

    # 下面四行是大连地铁GPS信息
    # 大连地铁1号线gps信息
    line1x = [121.722382, 121.671789, 121.637726, 121.594607, 121.577934, 121.53999, 121.550051]
    # 大连地铁1号线gps信息
    line1y = [38.917269, 38.934447, 38.922658, 38.919065, 38.919402, 38.933661, 38.962507]
    # 大连地铁2号线gps信息
    line2x = [121.520587, 121.554075, 121.590295, 121.600069, 121.582103, 121.586702, 121.592882, 121.625509]
    # 大连地铁2号线gps信息
    line2y = [38.849525, 38.882001, 38.890876, 38.933773, 38.948254, 38.962956, 39.009062, 39.024536]
    # 绘制这个区域的热力图
    plt.figure(4)
    # 图的标题
    plt.title('House price heatmap of Dalian', fontsize=15, color='r')
    # 绘制热力图
    plt.scatter(gpsx[regnum], gpsy[regnum], c=uprice[regnum], s=price[regnum], vmin=10000, vmax=30000, alpha=0.3,
                cmap=plt.cm.get_cmap('RdYlBu_r'))

    # 绘制大连地铁1号线
    plt.plot(line1x, line1y, 'b')
    # 绘制大连地铁2号线
    plt.plot(line2x, line2y, 'g')
    # 绘制热力棒
    plt.colorbar()
    # 使x轴y轴比例尺一致
    plt.axis('equal')
    # 显示图
    plt.show()


if __name__ == '__main__':
    main()
