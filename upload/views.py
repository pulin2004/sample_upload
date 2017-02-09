#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from django.shortcuts import render
# 额外需要导入的模块
from django.template import RequestContext

# 表单
def index(request):
    print("upload index new1!")
    return render(request, 'upload2.html')


def upload_file(request):
    print("start upload file!")
    if request.method == "POST":  # 请求方法为POST时，进行处理ok
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return render(request, 'message.html',{"message": "上传失败!","message_detail":"错误的文件类型！"})
        destination = open(os.path.join("C:\\Users\\lin.pu\\Documents\\temp\\files", myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        return render(request, 'message.html',{"message": "上传成功!","message_detail":"处理成功！"})

def upload_file2(request):
    print("test url post!")
