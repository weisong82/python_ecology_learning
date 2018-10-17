# -*- coding:utf-8 -*-
import re

def tld(x):
    # 如果 x 非None，则替代www.为空
    if x is not None and x.find('.') != -1:
        if(x. startswith("www.")):
            x = x.replace("www.", "")
        # 返回剩余.以后的字段
        tld = x[x.find('.'):]
        # logger.info("[tld-function]-input:{}-output:{}".format(x, tld))
        return tld
    else:
        return None


def prefix(x):
    # 如果 x 非None，则替代www.为空
    if x is not None and x.find('.') != -1:
        x = x.replace("www.", "")
        # 返回剩余.以后的字段
        prefix = x[0:x.find('.')]
        # logger.info("[tld-function]-input:{}-output:{}".format(x, tld))
        return prefix
    else:
        return None


def contain_zh(word):
    zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')

    '''
    判断传入字符串是否包含中文
    :param word: 待判断字符串
    :return: True:包含中文  False:不包含中文
    '''
    #     word = word.decode('utf-8') python3 字符串已经是unicode
    match = zh_pattern.search(word)
    if match:
        return True
    else:
        return False

        #     return match


if __name__ == '__main__':
    domains = ['jyzs.中国', '煎少.cn', 'abc.com', 'cherrytech.com.cn']
    for d in domains:
        print("domain here : {}".format(d))
        prefix(d)
        tld(d)
        contain_zh(prefix(d))
