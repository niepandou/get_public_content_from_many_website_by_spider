import re
import requests

# 匹配规则的替代方案
text = '123-456'
result = re.match('[-0-9]*', text)  # 匹配-或这0-9的数字多次,等价于[-\d]*
print(result.group())
result = re.match('[^0-9]*', text)  # ^取他的补集,^0-9表示匹配除0-9以外所有的字符
print(result.group())

# 特殊匹配
# . 匹配任意一个字符
result = re.match('.+',text) # [.]表示字符. , 而 单独一个 . 表示任意字符
print(result.group())
