import re

# 单字符匹配
text = 'python'

result = re.match('py', text)
print(result)  # 打印找到的下标范围
print(result.group())  # 打印找到的部分
# match是从起始位置匹配,所以匹配py可以找到,但是yt不能找到

# . 匹配任意一个字符,无法匹配换行符,从起点开始
result = re.match('.y', text)
print(result.group())

# \d 匹配任意一个数字,同样从起点开始
# \D 除数字以外均可以匹配,同样从起点开始
# \s \n \t \r ' ' 匹配空白字符 ~
# \w 匹配大小写字母,数字和下划线
# \W 匹配除\w以外的字符
# \会被转义,需要\\表示

result = re.match('\\w', text)
print(result.group())

# [] 组合匹配,中括号以内的都可以匹配,只匹配一次,只要里面的一个匹配就可以匹配上
result = re.match('[python]', text)
print(result.group())

# 多字符匹配
# * 匹配0-n次,从起始位置开始匹配,直到不符合条件
text = '123-456-789-10'
result = re.match('[\\d-]*', text)
print(result.group())
# + 匹配一个或多个,至少要有一个
result = re.match('[\\d]+',text)
print(result.group())
# ? 匹配0个或1个

# {n} 匹配指定n次

result = re.match('[\\d]{3}',text)
print(result.group())

# {m,n} 匹配m-n次,当前第四个字母是-,最多匹配3次,如果我们不知道text内容,{m,n}会是一个方便的筛选方法
result = re.match('[\\d]{2,4}',text)
print(result.group())