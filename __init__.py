# -*- coding: UTF-8 -*-
"""IDM控制模块"""
from . import CIdmHelper as _CIdmHelper


def DownloadUrlList(dUrl, sPath, bStart=True):
    """
    向队列添加任务列表
    @param dUrl: 下载链接字典{sName:sUrl}
    @param sPath: 目标目录
    @param bStart: 是否立刻开始
    """
    mgr = _CIdmHelper.GetMgr()
    for sName, sUrl in dUrl.items():
        mgr.AddList(sUrl, sPath, sName)
    if bStart:
        mgr.Start()
        mgr.Clear()


def Start():
    """
    开始队列
    """
    _CIdmHelper.GetMgr().Start()


def Stop():
    """
    停止队列
    """
