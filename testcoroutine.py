# -*- coding: utf8 -*-
def foo():
    for i in range(10):
        yield i
        print u'foo:'

bar = foo()
print '----------1'
print bar.next()
print '----------2'
print u'main:'
print '----------3'
print 'main:hello baby!'
print '----------4'
print bar.next()
print '----------5'
print bar.next()