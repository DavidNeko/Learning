# coding=utf-8

import csv

"""
This is a python decoder to convert Unicode to Simplified Chinese
and output converted result into a csv file.

Input/output files were ignored by .gitignore for local testing.

This py script should work with output file from practice_two.py.
Just simply change the loading directory of input file to whatever
directoty you saved your result using practice_two.py.
"""

input_file = open('./scrapped_data/data_from_taobao.txt', 'r')

"""
信息处理逻辑：
    读第一行
    加入字典
    将字典加入list
    进行输出/或者加入csv表格
    处理完毕，清空当前行处理字典，list
    读下一行...
"""
with open('./scrapped_data/data_from_taobao_output.csv', 'w+') as csvfile:
    writer = csv.writer(csvfile)
    # 先写入column names
    writer.writerow(["shop","price","location","deal","title"])

    try:
        for line in input_file:
            # init dic
            dic = {}
            dic = eval(line)

            # init values in dict and encode values with 'utf-8'
            shop_val = dic['shop'].encode('utf-8')
            price_val = dic['price'].replace('\n','').encode('utf-8')
            location_val = dic['location'].encode('utf-8')
            deal_val = dic['deal'].encode('utf-8')
            title_val = dic['title'].replace('\n',' ').encode('utf-8')
            
            # init list for all values in line
            val_list = []
            val_list.append(shop_val)
            val_list.append(price_val)
            val_list.append(location_val)
            val_list.append(deal_val)
            val_list.append(title_val)
            
            # write list as a row into csv file
            writer.writerow(val_list)

            # print dic['shop']
            # print dic['price'].replace('\n','')
            # print dic['location']
            # print dic['deal']
            # print dic['title'].replace('\n',' ')
            # 打印测试

    finally:
        input_file.close()
