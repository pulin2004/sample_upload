#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from django.shortcuts import render
# 额外需要导入的模块
from django.template import RequestContext

# 表单
def index(request):
    return render(request, 'upload2.html')


def upload_file(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理ok
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            c = RequestContext({"message_info": "upload fail!"})
            return render(request, 'message.html',c)
        destination = open(os.path.join("../upload", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        c = RequestContext({"message_info": "upload over!"})
        return render(request, 'message.html',c)
