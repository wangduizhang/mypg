#!/usr/bin/python
#_*_coding:utf-8_*_
#观看教学视频，没有中文字幕。所以只做了小脚本，可以翻译字幕文件。

result = ''

try:
    with open('/Users/wp/Desktop/srt.txt', 'r') as txt:
        lines = txt.readlines()
except IOError,e:
    with open('srt.txt', 'r') as txt:
        lines = txt.readlines()
finally:
    print '读取文件完成'
        
for i, l in enumerate(lines):
    if i % 4 ==0:
        result += l.strip()#去除换行符

open('字幕.txt','w')