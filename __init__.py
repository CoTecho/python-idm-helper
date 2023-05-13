# -*- coding: UTF-8 -*-
"""IDM控制模块"""
from . import CIdmHelper


def DownloadUrlList(dUrl, sPath, sDequeName="", bStart=True):
    """
    向某队列添加任务列表
    @param dUrl: 下载链接字典{sName:sUrl}
    @param sPath: 目标目录
    @param sDequeName: 队列名，默认为主要下载队列
    @param bStart: 是否立刻开始
    """


def Start(sDequeName=""):
    """
    开始某队列
    """


def Stop(sDequeName=""):
    """
    停止某队列
    """
