#!/usr/bin/env python
#-*-coding:utf-8-*-
# coding=utf-8

import xml.dom.minidom
import sys
import os.path


class MyException(Exception):
    pass

sourceFilePath = '../attribute.xml'
targetFilePath = '../../client/ClientApp/src/com/taomee/blitz/app/model/type/UserAttr.as'
#targetFilePath = 'UserAttr.as'

print " --------->>> 读取 ", sourceFilePath
#
sourceFileManager = open(sourceFilePath, 'r')
sourceContent = sourceFileManager.read()
sourceFileManager.close()

fileTemplateHead = """
package com.taomee.blitz.app.model.type
{
	/**
	 * 用户属性枚举
	 * @author	Rock
	 */
	public final class UserAttr
	{

"""
fileTemplateTail = """

	}
}
"""

fileContent = ""


# print sys.getdefaultencoding()
idList = []
contents = []
doc = xml.dom.minidom.parseString(sourceContent)
for node in doc.getElementsByTagName("attr"):
    nodeName = str(node.getAttribute("name"))
    nodeId = str(node.getAttribute("id"))
    nodeDes = node.getAttribute("des")
    nodeDes = nodeDes.encode('utf-8')
    if nodeId in idList:
        raise NameError('重复的id:[' + nodeId + ']')
    else:
        idList.append(nodeId)
        contents.append(
            "               public static const {0:<50} = {1} ; // {2}".format(nodeName.upper() + ":int", nodeId, nodeDes))

    # print nodeDes
normalAttrCount = len(contents)
print " --------->>> 共有 ", normalAttrCount, "条数据被处理"

for node in doc.getElementsByTagName("attr"):
    nodeName = str(node.getAttribute("name"))
    #nodeId = str(node.getAttribute("id"))
    nodeDes = node.getAttribute("des")
    maxValue = node.getAttribute("max")
    if len(maxValue) == 0:
        maxValue = 0
    nodeDes = nodeDes.encode('utf-8')
    idList.append(nodeId)
    contents.append(
        "               public static const MAX_{0:<50} = {1} ; // {2}".format(nodeName.upper() + ":int", maxValue, nodeDes))

    # print nodeDes
print " --------->>> 共有 ", len(contents) - normalAttrCount, "条最大值数据被处理"


if os.path.exists(targetFilePath):
    fp = open(targetFilePath, 'w')
    fp.truncate()
else:
    # os.mknod(fileSave)
    fp = open(targetFilePath, 'w')

fp.write(fileTemplateHead)
fp.write("\n".join(contents))
fp.write(fileTemplateTail)
fp.close()

print " --------->>> 生成 UserAttr.as 成功！"
