# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:59:17 2023

@author: 86182
"""

"""
Spyder Editor

This is a temporary script file.
"""

scores = [] #定义列表存储分数
for i in range(10):
    score = float(input(f"请输入第{i+1}名评委的打分:"))#输入分数
    while score < 0 or score > 100:
          score = float(input("打分错误，请重新打分："))
    scores.append(score)#将打分存入列表中
max_score = max(scores)#取最大值
min_score = min(scores)#取最小值
print(f"去掉一个最低分: {min_score}")
scores.remove(min_score)#去最小值
print(f"去掉一个最高分: {max_score}")
scores.remove(max_score)#去最大值
print("该歌手的得分为: %.2f" % (sum(scores) / len(scores)))#总分
