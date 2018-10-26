""" 
@file: log1.py
@Time: 2018/10/13
@Author:heningqiu
"""
import logging
# 设置log名称
LOG1=logging.getLogger('b.c')
LOG2=logging.getLogger('d.e')

# 设置log保存格式
filehandler = logging.FileHandler('reptile.log','a')
formatter = logging.Formatter('%(name)s %(asctime)s %(levelname)s %(message)s')
filehandler.setFormatter(formatter)

filter=logging.Filter('b') # 控制只允许'b'开头的事件名称输出
filehandler.addFilter(filter)
LOG1.addHandler(filehandler)
LOG2.addHandler(filehandler)

# 设置开启等级
LOG1.setLevel(logging.INFO)
LOG2.setLevel(logging.DEBUG)

LOG1.debug('it is a debug info for log1')
LOG1.info('normal infor for log1')
LOG1.warning('warning info for log1:b.c')
LOG1.error('error info for log1:abcd')
LOG1.critical('critical info for log1:not worked')

LOG2.debug('debug info for log2')
LOG2.info('normal info for log2')
LOG2.warning('warning info for log2')
LOG2.error('error:b.c')
LOG2.critical('critical')