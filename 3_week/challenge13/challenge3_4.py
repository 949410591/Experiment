# -*- coding: utf-8 -*-

import re
from datetime import datetime

def open_parser(filename):
    with open(filename) as logfile:
        pattern =  (r'' 
                r'(\d+.\d+.\d+.\d+)\s-\s-\s'  
                r'\[(.+)\]\s'  
                r'"GET\s(.+)\s\w+/.+"\s' 
                r'(\d+)\s'  
                r'(\d+)\s'  
                r'"(.+)"\s'  
                r'"(.+)"' 
        )
        parsers = re.findall(pattern, logfile.read())
    return parsers

def main():
    logs = open_parser('/home/shiyanlou/Code/nginx.log')
    dict_date = {}
    dict_url = {}
    for log in logs:
        url = log[2]
        ip = log[0]

        if log[1].split(':')[0] == '11/Jan/2017':
            dict_date.setdefault(ip,0)
            dict_date[ip] += 1 

        if log[3] == '404':
            dict_url.setdefault(url,0)
            dict_url[url] += 1

    key_date = max(dict_date,key = dict_date.get)

    key_url = max(dict_url,key = dict_url.get)

    
    return {key_date: dict_date[key_date]}, {key_url: dict_url[key_url]} 


if __name__ == '__main__':
    ip_dict, url_dict = main()
    print(ip_dict, url_dict)
