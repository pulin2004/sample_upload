#!/usr/bin/env python
# -*- coding:utf-8 -*-



__author__ = 'pulin'

import unittest
import logging
import views


class TestViews(unittest.TestCase):
    def setUp(self):
        logging.info('init by setUp...')

    def tearDown(self):
        logging.info( 'end by tearDown...')

    def test_addMessage(self):
        messageinfo =  views.MessageInfo()
        messageinfo.addMessage(True,1,'处理成功！')
        self.assertTrue(messageinfo.isSuccess(),'第一次加载失败！')
        self.assertDictEqual({1:'处理成功！'},messageinfo.getMessage(),'数据不对！')
        messageinfo.addMessage(False,2,'失败！')
        self.assertFalse(messageinfo.isSuccess(), '第二次加载失败！')
        messageinfo.addMessage(True, 3, '成功！')
        self.assertFalse(messageinfo.isSuccess(), '第三次加载失败！')
        self.assertDictEqual({1: '处理成功！',2:'失败！', 3:'成功！'}, messageinfo.getMessage(), '数据不对！')






if __name__ == '__main__':
    unittest.main()