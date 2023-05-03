#已知HASH值穷举确定身份证号
***
##来源于以下两位知乎答主的回答整理：  
- 公布他人身份证号的 SHA256 哈希码违法吗？ - 包子馒头蘸点醋的回答 - 知乎
https://www.zhihu.com/question/598323969/answer/3006329723
- 公布他人身份证号的 SHA256 哈希码违法吗？ - 或与非的回答 - 知乎
https://www.zhihu.com/question/598323969/answer/3006851944  
##相关信息
可以在 https://www.mca.gov.cn/article/sj/xzqh/1980/ 找到最新行政区划代码，最新更新至2022年，需使用县以上行政区划代码
##文件结构
1.包子馒头蘸点醋的回答answer_1
- aeraCode.txt 存放行政区划代码
- exhaustive_1.py

2.或与非的回答answer_2
- exhaustive_1.py
- sd.txt 存放行政区划代码
- prefix.txt 存放生成的身份证前14位