# -*- coding: utf-8 -*-

import configparser
import os
import sys
import time
import subprocess
import shutil
import tempfile
import coluaco
import paramiko
from pathlib import Path

# 开启debug模式
debug = False

exportTxtSignal = None
progressSignal = None
copyCount = 0

home_path = Path.home()
settings_path = Path(str(home_path) + os.sep + "fstCol")

def copyFile(filepath,toDir):
    shutil.copyfile(filepath,toDir)       
    global copyCount    
    copyCount = copyCount + 1 

data_dir = "data"

def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)


def getResPathByName(name):
    return resource_path(os.path.join(data_dir, name))


if not Path.exists(settings_path):
    Path.mkdir(settings_path)
    print(getResPathByName("items.conf"))
    print(getResPathByName("generalConfig.conf"))
    copyFile(getResPathByName("items.conf"),str(settings_path) + os.sep + "items.conf")
    copyFile(getResPathByName("generalConfig.conf"),str(settings_path) + os.sep + "generalConfig.conf")

itemConf = configparser.ConfigParser()
itemConfigPath = str(settings_path) + os.sep + "items.conf"
itemConf.read(itemConfigPath,encoding="utf-8")


generalConf = configparser.ConfigParser()
generalConfigPath = str(settings_path) + os.sep + "generalConfig.conf"
print("generalConfig:" + generalConfigPath)
generalConf.read(generalConfigPath,encoding="utf-8")


def reloadConf():
    print("reload")
    global itemConf 
    itemConfigPath = str(settings_path) + os.sep + "items.conf"
    itemConf.read(itemConfigPath,encoding="utf-8")

    global generalConf 
    generalConfigPath = str(settings_path) + os.sep + "generalConfig.conf"
    print("generalConfig:" + generalConfigPath)
    generalConf.read(generalConfigPath,encoding="utf-8")

def exportProgress(text):
    if progressSignal != None:
        print("aa")
        progressSignal.emit(text)

def exportTxt(text):
    global exportTxtSignal
    if exportTxtSignal != None:
        exportTxtSignal.emit(text) 
    else:
        print(text)


def saveOptions():
    with open(itemConfigPath,"w+",encoding="utf-8") as f:
        itemConf.write(f)
    with open(generalConfigPath,"w+",encoding="utf-8") as f:
        generalConf.write(f)


def getLastConf():
    lastVer = generalConf.get("general_settings","last_version")
    if len(lastVer) > 0:
        return lastVer
    else:
        return "jp"

def setLastConf(ver):
    generalConf.set("general_settings","last_version",ver)


def uploadFile(version,allFile = True):
    exportProgress("开始执行上传")
    exportTxt('开始执行上传')
    combined = False 
    onlyVer = None
    try:
        if itemConf.has_option(version,"combined"):
            combined = itemConf.getboolean(version,"combined")
        if itemConf.has_option(version,"onlyVer"):
            onlyVer = itemConf.get(version,"onlyVer")

        if not itemConf.has_option(version,"remote_sftp_port"):
            t = paramiko.Transport((itemConf.get(version,"remote_sftp_ip")))
        else:
            t = paramiko.Transport((itemConf.get(version,"remote_sftp_ip"),itemConf.getint(version,"remote_sftp_port")))
    
        t.connect(username = "honor", password = "zK2p@dM$bh")
        sftp = paramiko.SFTPClient.from_transport(t)

        if allFile:
            files = [
                "next",
                "clientDataConfig",
                "Battle",
                "fixedWins",
                "floatWins",
                "luaConfig",
                "Managers",
                "others",
                "plots",
                "scene",
                "suictrl",
            ]
        else:
            files = [
                "next",
                "clientDataConfig",
            ]

        # return

        if onlyVer != "adr":
            suffix = "remote_suffix_ios_debug"
            for i in files:
                remotepath = itemConf.get(version,"remote_path_ios_debug") + i + itemConf.get(version,suffix)
                localpath = itemConf.get(version,"local_path_ios_release") + "out" + os.sep + i + itemConf.get(version,suffix)
                exportTxt( '上传: ' + localpath + '到:' + remotepath)
                sftp.put(localpath,remotepath)

        if (not combined) or onlyVer == "adr":
            suffix = "remote_suffix_adr_debug"
            for i in files:
                remotepath = itemConf.get(version,"remote_path_adr_debug") + i + itemConf.get(version,suffix)
                localpath = itemConf.get(version,"local_path_adr_release") + "out" + os.sep + i + itemConf.get(version,suffix)
                exportTxt( '上传: ' + localpath + '到:' + remotepath)
                sftp.put(localpath,remotepath)
        elif combined:
            suffix = "remote_suffix_adr_debug"
            for i in files:
                remotepath = itemConf.get(version,"remote_path_adr_debug") + i + itemConf.get(version,suffix)
                localpath = itemConf.get(version,"local_path_ios_release") + "out" + os.sep + i + itemConf.get(version,suffix)
                exportTxt( '上传: ' + localpath + '到:' + remotepath)
                sftp.put(localpath,remotepath)

    except Exception as e:
        print(e)
        exportTxt("上传文件出错，错误详情：")
        exportTxt("    " + str(e))
        return False
    finally:
        t.close()

    return True


def processCombine(version,isRelease):
    exportProgress("开始执行合并操作")
    combined = False 
    onlyVer = None
    try:
        if itemConf.has_option(version,"combined"):
            combined = itemConf.getboolean(version,"combined")
        if itemConf.has_option(version,"onlyVer"):
            onlyVer = itemConf.get(version,"onlyVer")

        if onlyVer != "adr":
            if isRelease:
                suffix = "remote_suffix_ios_release"
            else:
                suffix = "remote_suffix_ios_debug"
            coluaco.process(itemConf.get(version,"local_path_ios_release") + "src" + os.sep,
                itemConf.get(version,"local_path_ios_release") + "out" + os.sep,
                None, #build setting
                ".lua",
                "",
                None, #in filter
                itemConf.get(version,suffix),True,True)
        if (not combined) or onlyVer == "adr":
            if isRelease:
                suffix = "remote_suffix_adr_release"
            else:
                suffix = "remote_suffix_adr_debug"
            coluaco.process(itemConf.get(version,"local_path_adr_release") + "src" + os.sep,
                itemConf.get(version,"local_path_adr_release") + "out" + os.sep,
                None, #build setting
                ".lua",
                "",
                None, #in filter
                itemConf.get(version,suffix),True,True)

        return True
    except Exception as e:
        exportTxt("合并压缩操作出错，错误详情：")
        exportTxt("    " + str(e))
        return False

    


def getFromSvn(ver):
    exportProgress("从SVN拉取配置表")
    try:

        dataVroot = generalConf.get("svn_settings","client_data_root") + "/" + itemConf.get(ver,"release_svn_game_data_path")
        dataVroot = dataVroot.encode('utf-8').decode()
        if debug:
            exportTxt(dataVroot)
        exportTxt("开始搜寻最新的发布日志：")
        exportTxt("搜寻目录：" + dataVroot)
        maxResult = getMaxReleaseData(dataVroot)
        print('maxResult')
        exportTxt("找到发布最新发布日志：")
        exportTxt("目录：" + maxResult)
        exportTxt("开始拉取配置表")
        copySvnToCode(maxResult,ver)
        exportTxt("复制完成，一共复制了" + str(copyCount) + "个文件")
        return True
    except Exception as e:
        exportTxt("拉取配置表出错，错误详情：")
        exportTxt("    " + str(e))
        return False

#搜寻最大的发布日志
def getMaxReleaseData(dataVroot,level = 0):
    exportProgress("搜索最新配置表")
    global timeMax
    global copyCount
    copyCount = 0
    localTimeMax = None
    if level == 0:
        timeMax = time.strptime("2000年1月", "%Y年%m月")
    retPath = None
    ##读取SVN文件
    cmdStr = 'svn list --username ' + generalConf.get("svn_settings","user_name") + " --password '" + generalConf.get("svn_settings","password") + "' " + dataVroot

    verifty_luac=subprocess.check_output(cmdStr, shell=True) 

    verifty_luac = verifty_luac.decode('utf-8')

    dirList = verifty_luac.split("\n")
    if debug:
        for i in dirList:
            exportTxt(i)
    for f in dirList:
        cYear = None
        if f == '':
            continue
        filepath = dataVroot+"/"+f
        if debug:
            exportTxt( filepath)
        try:
            dataVroot.index("年") 
            cYear = dataVroot[dataVroot.index("年") - 4:dataVroot.index("年")]
            if debug:
                exportTxt( "今年是：" + str(cYear))
        except:
            pass
        try:
            f.index("年") 
        except:
            try:
                f.index("月")
                if cYear != None:
                    f = str(cYear) + "年" + f
                else:
                    f = "2015年"+f
                if debug:
                    exportTxt( "Maxxxxxx" + f)
            except:
                pass
        if os.name == "nt":
            # f = f.encode('utf-8')
            endIndex = -2
        else:
            endIndex = -1
        if f[endIndex] == "/":
            f = f[0:endIndex]
            if localTimeMax == None and (f == "LUA" or f == "Lua" or f == "lua"):
                return filepath
            else:
                timeCur = None
                if debug:
                    exportTxt( "处理目录：" + f)
                try:
                    if timeCur == None:
                        timeCur = time.strptime(f, "%Y年%m月")
                except:
                    pass
                try:
                    if timeCur == None:
                        timeCur = time.strptime(f, "%m月")
                except:
                    pass
                try:
                    if timeCur == None:
                        timeCur = time.strptime(f, "%Y年%m月%d日")
                except:
                    pass
                try:
                    if timeCur == None:
                        timeCur = time.strptime(f, "%m月%d日")
                except:
                    pass
                if debug:
                    exportTxt( "timeCur:" + repr(timeCur))
                    exportTxt("timeCur:" + repr(timeMax))
                if timeCur != None and timeCur >= timeMax:
                    localTimeMax = timeCur
                    timeMax = timeCur
                    retPath = filepath[0:-1]
                    print("retPath:" + retPath)
                    if debug:
                        exportTxt( "filepathMax:" + filepath)

                        exportTxt( "retPath:" + retPath)

    if retPath!=None:
        if debug:
            exportTxt( 'reellllRet')
            exportTxt( "filepathMax:" + filepath)
            exportTxt( "retPath:" + retPath)
        return getMaxReleaseData(retPath,level + 1)


def copySvnToCode(path,version,para = "both"):
    exportProgress("从SVN拉取配置表")
    temp_dir = tempfile.mktemp()
    os.mkdir(temp_dir)

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

    cmdStr = "svn export --username " + generalConf.get("svn_settings","user_name")  + " --password '" + generalConf.get("svn_settings","password") + "' '" + path + "' '" + temp_dir +"' "

    if debug:
        exportTxt(cmdStr)

    exportTxt( '正在从SVN导出：' + path + ' 到 ' + temp_dir)

    verifty_luac = subprocess.check_output(cmdStr,shell=True)

    copyToCode(temp_dir,version,para)

    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

def copyToCode(path,version,para = "both"):
    exportProgress("复制配置表到开发版与发布版")
    combined = False 
    onlyVer = None
    if itemConf.has_option(version,"combined"):
        combined = itemConf.getboolean(version,"combined")
    if itemConf.has_option(version,"onlyVer"):
        onlyVer = itemConf.get(version,"onlyVer")

    fileList = os.listdir(path)
    for f in fileList:
        filepath = os.path.join(path,f)
        if os.path.isfile(filepath):
            toDir = []
            try:
                f.index("PropertitesClientData")
                if para == "both" or para == "dev":
                    if onlyVer != "adr":
                        toDir.append(itemConf.get(version,"local_path_ios_debug") + "src" + os.sep + "next")
                    if (not combined) or onlyVer == "adr":
                        toDir.append(itemConf.get(version,"local_path_adr_debug") + "src" + os.sep + "next")
                        
                if para == "both" or para == "release":
                    if onlyVer !=  "adr":
                        toDir.append(itemConf.get(version,"local_path_ios_release") + "src" + os.sep + "next")
                    if (not combined) or onlyVer == "adr":
                        toDir.append(itemConf.get(version,"local_path_adr_release") + "src" + os.sep + "next")
                       
            except:
                if para == "both" or para == "dev":
                    if onlyVer !=  "adr":
                        toDir.append(itemConf.get(version,"local_path_ios_debug") + "src" + os.sep + "clientDataConfig")
                    if (not combined) or onlyVer == "adr":
                        toDir.append(itemConf.get(version,"local_path_adr_debug") + "src" + os.sep + "clientDataConfig")
                       
                if para == "both" or para == "release":
                    if onlyVer !=  "adr":
                        toDir.append(itemConf.get(version,"local_path_ios_release") + "src" + os.sep + "clientDataConfig")
                    if (not combined) or onlyVer == "adr":
                        toDir.append(itemConf.get(version,"local_path_adr_release") + "src" + os.sep + "clientDataConfig")
                       
            for i in toDir:
                exportTxt( '复制' + filepath + "到" + i) 
                copyFile(filepath,i + os.sep + f) 





