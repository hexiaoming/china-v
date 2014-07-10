#!/usr/bin/env python
# coding=utf-8

#需要实现添加xlrd模块，pip

import xlrd

if __name__ == '__main__':
	data = xlrd.open_workbook('ChinaVoicepromotion.xls')
	