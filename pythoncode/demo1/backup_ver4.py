import os
import time
import zipfile

def zip_write(z,  filePath):
    print('压缩目录: ', filePath)
    if os.path.isdir(filePath):
        for d in os.listdir(filePath):
            childFilePath = filePath + os.sep + d
            if os.path.isdir(childFilePath):
                zip_write(z, childFilePath)
            else:
                print('压缩文件: ', childFilePath)
                z.write(childFilePath)

    z.write(filePath)

source = ['E:\\pythoncode']
target_dir = 'E:\\Backup'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
if not os.path.exists(today):
    os.mkdir(today)

annotation = input('Enter the annotation --> ')

target = today + os.sep + time.strftime('%H%M%S') + '_' + \
    annotation.replace(' ', '_') + '.zip'

z = zipfile.ZipFile(target, 'w')
zip_write(z, source[0])

z.close()
