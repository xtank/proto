#!/usr/bin/env python
#-*-coding:utf-8-*-
# coding=utf-8

import xml.dom.minidom
import sys
import os.path


class MyException(Exception):
    pass

sourceFilePath = './command.xml'
targetFilePath = '../../../XTankNet/src/x/tank/net/core/CommandSet.as'

print " --------->>> 读取 ", sourceFilePath
#
sourceFileManager = open(sourceFilePath, 'r')
sourceContent = sourceFileManager.read()
sourceFileManager.close()

fileTemplateHead = """
package x.tank.net.core
{
    import onlineproto.* ;
    import x.game.log.core.Logger ;

	/**
	 * command list
	 * @author	fraser
	 */
	public final class CommandSet
	{
        static public function initCMDS():void
        {
            Logger.info("init cmds") ;
        }

"""
fileTemplateTail = """

	}
}
"""

fileContent = ""

#<?xml version="1.0" encoding="UTF-8"?>
#<data>
#
#    <section id="100" des="客户端逻辑模块与逻辑服务器通讯协议">
#        <!--进服务器初始化相关协议 101-110-->
#        <command id="101" name="cs_enter_srv" des="进入在线服务器" cs="cs_enter_server" sc="sc_enter_server"/>
#
#    </section>
#
#</data>
# public static const $101:Command = new
# Command(101,cs_enter_server,sc_enter_server) ;  // 通信样例


# print sys.getdefaultencoding()
idList = []
contents = []
doc = xml.dom.minidom.parseString(sourceContent)
for node in doc.getElementsByTagName("command"):
    nodeName = str(node.getAttribute("name"))
    nodeId = str(node.getAttribute("id"))
    nodeDes = node.getAttribute("des")
    nodeDes = nodeDes.encode('utf-8')
    nodeCS = node.getAttribute("cs")
    nodeSC = node.getAttribute("sc")

    print nodeId, nodeDes, nodeCS, nodeSC

    if nodeId in idList:
        raise NameError('重复的id:[' + nodeId + ']')
    else:
        idList.append(nodeId)
        contents.append(
            "       public static const ${0}: Command = new Command({1}, {2}, {3}); // {4}".format(nodeId, nodeId, nodeCS, nodeSC, nodeDes))

    # print nodeDes
normalAttrCount = len(contents)
print " --------->>> 共有 ", normalAttrCount, "条数据被处理"


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

print " --------->>> 生成 CommandSet.as 成功！"
