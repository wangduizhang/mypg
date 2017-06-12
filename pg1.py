#!/usr/bin/python
#_*_coding:utf-8_*_
#观看教学视频，没有中文字幕。所以只做了小脚本，可以翻译字幕文件。
#Google-translate-python：一个Python在线翻译模块
#安装方法：pip install translate


from translate import Translator
import codecs

result = ''
translator= Translator(to_lang="zh")
#读取文件内容
try:
    with open('/Users/wp/Desktop/srt.txt', 'r') as txt:
        lines = txt.readlines()
except IOError,e:
    with open('srt.txt', 'r') as txt:
        lines = txt.readlines()
finally:
    print '读取文件完成'
        
for i, l in enumerate(lines):
    if i % 32 ==0:
        translation = translator.translate(l.strip()) #去除换行符,并将每行单独翻译
        result += translation
        
with codecs.open('/Users/wp/Desktop/字幕.txt','w','utf-8') as files:
    files.write(result)

print '写入完成'    
    