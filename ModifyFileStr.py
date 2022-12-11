from genericpath import isfile
import os
import shutil

# 需要修改脚本路径
jsfilePath = r"F:/Hexo/HexoBlog/Hexo/source/live2d-widget/waifu-tips.js"
# 模型路径
live2DPath = r"F:/Hexo/live2dModels/live2d_api/model/"
# 如果更换模型时，输入了“1”，则会同时将当前模型复制到此目录
live2DBackupPath = r"F:/Hexo/live2dModels/fav/"
# 模型的网络路径---或者如果是直接拖到Hexo/Source目录的话，就是相对路径，如“/live2D/”
rootDir = "http://127.0.0.1/Live2d-model/live2d_api/model/"
# 标记符号
defaultName = "/@live2D@/"
nowName = defaultName


def ModifyPath(newPathName):
    global defaultName, nowName
    file_data = ""
    with open(jsfilePath, "r", encoding="utf-8") as f:
        file_data = (f.read().replace(
            nowName, newPathName))
    print("    更换为："+newPathName)
    nowName = newPathName
    with open(jsfilePath, "w", encoding="utf-8") as f:
        f.write(file_data)


def CalcName(dir, shortPath):
    if(dir.startswith(".") or os.path.isfile(dir)):
        return
    for childName in os.listdir(dir):
        if childName.endswith("index.json") or childName.endswith("model.json"):
            folderName = os.path.split(dir)[1]
            newPathName = shortPath+"index.json"
            needModifyName = False
            # 目录下没有index.json
            if not os.path.exists(os.path.join(dir, "index.json")):
                newPathName = shortPath+"model.json"
                needModifyName = True
            ModifyPath(newPathName)
            key = input("按回车更换，输入1会同时备份当前模型：")
            if(key == "1"):
                try:
                    backupPath = live2DBackupPath+folderName
                    if os.path.exists(backupPath):
                        shutil.rmtree(backupPath)
                    shutil.copytree(dir, backupPath)
                    if needModifyName:
                        os.rename(backupPath+"/model.json",
                                  backupPath+"/index.json")
                finally:
                    print(folderName+" 已经被复制到目录"+live2DBackupPath)
            break
        else:
            CalcName(os.path.join(dir, childName), shortPath+childName+"/")


try:
    print("初始标记值为："+defaultName)
    CalcName(live2DPath, rootDir)
except KeyboardInterrupt:
    # 还原标记
    ModifyPath(defaultName)
else:
    # 还原标记
    ModifyPath(defaultName)


# live2dFiles = os.listdir(live2DPath)
# for live2d in live2dFiles:
#     if(live2d.startswith(".") or os.path.isfile(os.path.join(live2DPath, live2d))):
#         continue

# for line in f:
#     if old_str in line:
#     line = line.replace(old_str,new_str)
#     file_data += line
# with open(file,"w",encoding="utf-8") as f:
# f.write(file_data)
