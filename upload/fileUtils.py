#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

def getSufix(fileName):
    _name = fileName;
    if isinstance(_name ,unicode):
        _name = _name.encode('utf8')
    result = re.findall(r'\.[^.\\/:*?"<>|\r\n]+$', _name)
    try:
        return result[-1][1:]
    except Exception as ex:
        print ex
        raise Exception('未知的文件类型!')



def isSameType(sufix,sufixTuple):
    # print sufixTuple
    if sufix :
        for i in range(len(sufixTuple)) :
            # print sufixTuple[i];
            if re.search(sufixTuple[i], sufix, re.IGNORECASE):
                return True
        return False
    else :
        return False
