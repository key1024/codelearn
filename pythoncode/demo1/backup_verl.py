import os
import time

#1.需要备份的文件与目录将被指定在一个列表中
#  例如在windows下：
#  source = ['"C:\\My Documents"', 'C:\\code']
#  又例如在Mac os x 与 Linux 下：
#  source = ['/Users/swa/notes']
#  在这里需要注意到我们必须在字符串中使用双引号，用以括起其中包含空格的名称
#2.备份文件必须存储在一个主备份目录中
#  例如在Windows下：
#  target_dir = 'E:\\Backup'

source  = ['E:\\pythoncode']
target_dir = 'E:\\Backup'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

#如果目录不存在则创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip.exe -r {} {}'.format(target, ' '.join(source))

print('Zip command is:', zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED!!!')