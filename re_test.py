#coding=utf-8

import re

#��def�滻Ϊ[def]�����Ҳ��ִ�Сд
print re.sub(re.compile('(def)', re.I), '[\\1]', "1234dEfabc")