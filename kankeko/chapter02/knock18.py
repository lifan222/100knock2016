#!-*-coding:utf-8-*-


list = []
answer = []
for line in open("hightemp.txt", 'r'):
    line = line.strip()
    list.append(line.split())
list.sort(key=lambda x:x[2])
list.reverse()
for line in list:
    print("\t".join(line))

