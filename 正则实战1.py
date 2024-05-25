import requests
import re

text = \
    """
    <ul class="ullist" padding="1" spacing="1">
        <li>
            <div id="top">
                <span class="position" width="350">职位名称</span>
                <span>职位类别</span>
                <span>人数</span>
                <span>地点</span>
                <span>发布时间</span>
            </div>
            <div id="even">
                <span class="l square">
                  <a target="_blank" href="position_detail.php?id=33824&amp;keywords=python&amp;tid=87&amp;lid=2218">python开发工程师</a>
                </span>
                <span>技术类</span>
                <span>2</span>
                <span>上海</span>
                <span>2018-10-23</span>
            </div>
            <div id="odd">
                <span class="l square">
                  <a target="_blank" href="position_detail.php?id=29938&amp;keywords=python&amp;tid=87&amp;lid=2218">python后端</a>
                </span>
                <span>技术类</span>
                <span>2</span>
                <span>上海</span>
                <span>2018-10-23</span>
            </div>
            <div id="even">
                <span class="l square">
                  <a target="_blank" href="position_detail.php?id=31236&amp;keywords=python&amp;tid=87&amp;lid=2218">高级Python开发工程师</a>
                </span>
                <span>技术类</span>
                <span>2</span>
                <span>上海</span>
                <span>2018-10-23</span>
            </div>
            <div id="odd">
                <span class="l square">
                  <a target="_blank" href="position_detail.php?id=31235&amp;keywords=python&amp;tid=87&amp;lid=2218">python架构师</a>
                </span>
                <span>技术类</span>
                <span>1</span>
                <span>上海</span>
                <span>2018-10-23</span>
            </div>
            <div id="even">
                <span class="l square">
                  <a target="_blank" href="position_detail.php?id=34531&amp;keywords=python&amp;tid=87&amp;lid=2218">Python数据开发工程师</a>
                </span>
                <span>技术类</span>
                <span>1</span>
                <span>上海</span>
                <span>2018-10-23</span>
            </div>
            <div id="odd">
                <span class="l square">
                  <a target="_blank" href="position_detail.php?id=34532&amp;keywords=python&amp;tid=87&amp;lid=2218">高级图像算法研发工程师</a>
                </span>
                <span>技术类</span>
                <span>1</span>
                <span>上海</span>
                <span>2018-10-23</span>
            </div>
            <div id="even">
                <span class="l square">
                  <a target="_blank" href="position_detail.php?id=31648&amp;keywords=python&amp;tid=87&amp;lid=2218">高级AI开发工程师</a>
                </span>
                <span>技术类</span>
                <span>4</span>
                <span>上海</span>
                <span>2018-10-23</span>
            </div>
            <div id="odd">
                <span class="l square">
                  <a target="_blank" href="position_detail.php?id=32218&amp;keywords=python&amp;tid=87&amp;lid=2218">后台开发工程师</a>
                </span>
                <span>技术类</span>
                <span>1</span>
                <span>上海</span>
                <span>2018-10-23</span>
            </div>
            <div id="even">
                <span class="l square">
                  <a target="_blank" href="position_detail.php?id=32217&amp;keywords=python&amp;tid=87&amp;lid=2218">Python开发（自动化运维方向）</a>
                </span>
                <span>技术类</span>
                <span>1</span>
                <span>上海</span>
                <span>2018-10-23</span>
            </div>
            <div id="odd">
                <span class="l square">
                  <a target="_blank" href="position_detail.php?id=34511&amp;keywords=python&amp;tid=87&amp;lid=2218">Python数据挖掘讲师 </a>
                </span>
                <span>技术类</span>
                <span>1</span>
                <span>上海</span>
                <span>2018-10-23</span>
            </div>
        </li>
    </ul>
    """

# 1.获取所有div标签
# findall获取所有匹配数据

# 错误示范
# result = re.findall('<div>.*</div>',text)
# print(result)
# div标签后面还有东西,比如带着一些属性
# 同时, . 无法匹配换行

# 法1 需要用\d\D来匹配所有字符
result = re.findall('<div[\\d\\D]*</div>',text)
# for ans in result:
#     print(ans)
print(len(result))  # 1
# 法2 非贪婪模式
result = re.findall('<div[\\d\\D]*?</div>',text)
print(len(result))  # 11

# 法3 使用编译标志
result = re.findall('<div.*?</div>',text,re.DOTALL)
print(len(result))


# 获取某个属性值的div标签
result = re.findall('<div id=[\\d\\D]*?</div>',text)
print(len(result))


# 获取所有id=even的div标签
result = re.findall('<div id="even"[\\d\\D]*?</div>',text)
print(len(result))


# 获取某个标签的属性值
# ()内是要提取的数据
# 第一个.*?即提取()内所有的值
result = re.findall('<div id="(.*?)[\\d\\D]*?</div>',text)

# 获取a标签中的href属性
result = re.findall('<a .*?href="(.*?)"[\\d\\D]*?</a>',text)

# 获取div标签中的全被职位信息
result = re.findall('<span>(.*?)</span>',text)

# 获取所有的岗位信息
result = re.findall('<a.*?>(.*?)</a>',text)
print(result)