"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""

import logging

# 日志配置

# 创建logger实例
logger = logging.getLogger('simple_example')
# 设置日志级别
logger.setLevel(logging.DEBUG)

# 流处理器
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 日志打印格式
formatter = logging.Formatter\
('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 添加格式配置
ch.setFormatter(formatter)
# 添加日志配置
logger.addHandler(ch)