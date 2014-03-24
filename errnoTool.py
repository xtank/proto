#!/usr/bin/env python
#-*-coding:utf-8-*-
# coding=utf-8

import xml.dom.minidom
import sys
import os.path


class MyException(Exception):
    pass

sourceFilePath = './errno.xml'
targetFilePath = '../../XTankNet/locale/zh_CN/error.properties'

print " --------->>> 读取 ", sourceFilePath
#
sourceFileManager = open(sourceFilePath, 'r')
sourceContent = sourceFileManager.read()
sourceFileManager.close()

fileContent = ""

idList = []
contents = []
doc = xml.dom.minidom.parseString(sourceContent)
for node in doc.getElementsByTagName("err"):
    nodeId = str(node.getAttribute("id"))
    nodeDes = node.getAttribute("des")
    nodeDes = nodeDes.encode('utf-8')

    print nodeId, nodeDes

    if nodeId in idList:
        raise NameError('重复的id:[' + nodeId + ']')
    else:
        idList.append(nodeId)
        contents.append(
            "Key_{0} = {1}".format(nodeId, nodeDes))

    # print nodeDes
normalAttrCount = len(contents)
print " --------->>> 共有 ", normalAttrCount, "条数据被处理"


if os.path.exists(targetFilePath):
    fp = open(targetFilePath, 'w')
    fp.truncate()
else:
    # os.mknod(fileSave)
    fp = open(targetFilePath, 'w')

fp.write("\n".join(contents))
fp.close()

print " --------->>> 生成 error.properties 成功！"
