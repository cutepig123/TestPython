# 简介

[最近机工社宣布开放工程科技数字图书馆， 全网免费共克时艰！](https://mp.weixin.qq.com/s/yKDp1xwczPb0LaDlPT-kZQ)          

发现有些书是以web页面的方式给用户看的，一张一张，很难一次性下载

有没有办法一次性下载他们呢？

所以编写了这个程序

# 用法

## 运行pydownload.bat

功能：

下载登记在pydownloadurls.txt里面的图书到当前目录

## tampermonkey.js

一个tampermonkey脚本，当进入网站http://ebooks.cmanuf.com/的图书页面时，F12打开chrome的developer窗口，刷新页面，就会断下来。继续运行, 就会在log窗口显示出解析到的文件链接。你可以把它拷贝到pydownloadurls.txt里面

