#!-*-coding:utf-8-*-

import json
import re

pattern = "Category:"
f = open("jawiki-country.json", 'r')
for line in f:
   dict = json.loads(line)
   if dict["title"] == u"イギリス":
       dict = dict["text"].split()
       for text in dict:
           match = re.search(pattern , text)
           if match:
                i = match.end()
                list = []
                while text[i] != "]":
                    list.append(text[i])
                    i += 1
                print("".join(list))






