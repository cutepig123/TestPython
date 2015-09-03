#coding=utf-8

import re

#将def替换为[def]，并且不分大小写
print re.sub(re.compile('(def)', re.I), '[\\1]', "1234dEfabc")