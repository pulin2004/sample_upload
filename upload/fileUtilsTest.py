#!/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'pulin'

import unittest
import logging
import fileUtils


class TestFileUtils(unittest.TestCase):
    def setUp(self):
        logging.info('init by setUp...')

    def tearDown(self):
        logging.info( 'end by tearDown...')

    def test_isSameType(self):
        py_suffix = ('csv', 'txt', 'py')
        self.assertTrue(fileUtils.isSameType('Csv', py_suffix),'匹配错误！')
        self.assertFalse(fileUtils.isSameType('jpg',py_suffix),'应该过滤！')
        self.assertFalse(fileUtils.isSameType(None, py_suffix),'空指针问题！')
        self.assertTrue(fileUtils.isSameType(fileUtils.getSufix(u'已发货.csv'),py_suffix))

    def test_getSufix(self):
        self.assertEqual(fileUtils.getSufix('//wee.wee//中国.c.cvs'),'cvs')
        try :
            fileUtils.getSufix('中国')
            self.assertTrue(False)
        except Exception as ex:
            self.assertTrue(True);




if __name__ == '__main__':
    unittest.main()
