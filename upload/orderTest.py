#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 
__author__ = 'pulin'

import unittest
import logging
import order


class TestOrder(unittest.TestCase):
    def setUp(self):
        logging.info('init by setUp...')

    def tearDown(self):
        logging.info( 'end by tearDown...')

    def test_compareAndWriteAttr(self):
        _order = order.Order()
        _order.setAttr('client_name','Acde')
        self.assertEqual(_order.getAttr('client_name'),'Acde')
        _order.setAttr('client_name','Acde')
        self.assertEqual(_order.getAttr('client_name'),'Acde')
        with self.assertRaises(BaseException):
            _order.setAttr('client_name','Ccde')

    def test_getNull(self):
        _order = order.Order()
        if _order.getAttr('Acde'):
            self.assertTrue(False)
        if _order.getAttr(''):
            self.assertTrue(False)

if __name__ == '__main__':
    unittest.main()

