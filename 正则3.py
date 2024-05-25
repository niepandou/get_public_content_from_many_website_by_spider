# 特殊匹配进阶
# 关于match函数,都是从头开始匹配的

import re

# search函数,从左到右匹配,只要找到了,就是匹配到,且匹配到之后不会再匹配

text = 'testpytest'
result = re.search('py', text)
print(result.group())  # py

# ^在[]内是表示取反,如果在[]之外,比如^$,他表示的就是他从$开始匹配,和match的从头开始匹配意思差不多

text = 'baaabbb'
result = re.search('^b[a]+', text)
print(result.group())  # baaa

text = 'abcdefg'
result = re.match('^a[a-z]+',text)
print(result.group())  # abcdefg

# $ 必须以某某结尾,以下是以com为结尾
text = 'abcd@163.com'
result = re.match('[\\w]+@[0-9a-z]+[.]com$',text)  # 切记[.]才是真正表示.
print(result.group())

# | 匹配多个表达式或字符串 即或,|在[]会认为是字符或(匹配一个字符),在()会认为是字符串或(匹配一个字符串)
text = 'https://www.baidu.com'
result = re.search('[https|ftp|file|http]',text)
print(result.group()) # h 只匹配了一次,而如果加上一个+,匹配多次后就是正常结果
result = re.search('(https|ftp|file|http)',text)
print(result.group())

# 两种匹配都匹配到了https,只不过前者只能匹配一个字符,后者是一个完整的字符串

# 贪婪模式
# 正则表达式尽可能多地匹配字符
text = 'python'
result = re.match('[a-z]+',text)
print(result.group())
# 非贪婪模式
# 正则表达式尽可能少的匹配字符
result = re.match('p?[a-z]',text)
print(result.group())

# 贪婪模式有时达不到预期效果
# 比如我要得到以下html代码的tr属性那一行
# 结果我们得到的是整个的代码,从<tr 匹配字符一次到多次到最下面的>而非这一行最后的>
text = \
"""
<tr class="hots">
    <td class="1">hot1</td>
    <td class="2">hot2</td>
    <td class="3">hot3</td>
    <td class="5">hot4</td>
    <td class="5">爬虫</td>
</tr>
"""
result = re.match('\n<tr[\\d\\D]+>',text)
print(result.group())
# 采用非贪婪模式
result = re.match('\n<tr[\\d\\D]+?>',text) # 把? 放> 前面 非贪婪,匹配一次>就结束
print(result.group())

# 