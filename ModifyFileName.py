import os

dirPath = r"F:/Hexo/live2dModels/Live2d-model/"


def RenameDirFileNames(enterDirPath):
    if(not os.path.isdir(enterDirPath)):
        return
    paths = os.listdir(enterDirPath)
    for item in paths:
        childPath = os.path.join(enterDirPath, item)
        if os.path.isfile(childPath):
            # for file in os.listdir(childPath):
            if childPath.endswith("model.json"):
                print(childPath)
                try:
                    os.rename(childPath, os.path.join(
                        enterDirPath, "index.json"))
                except:
                    print("这个文件重命名失败！")
        else:
            RenameDirFileNames(childPath)


# paths=os.listdir(dirPath)
# for path in paths:
RenameDirFileNames(dirPath)
