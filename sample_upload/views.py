#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render

# 表单
def home(request):
    return render(request, 'index.html')