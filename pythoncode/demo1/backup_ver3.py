import os 
import time

source = ['E:\\pythoncode']

target_dir = 'E:\\Backup'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')
#添加注释
annotation = input('Enter an annotation --> ')
if len(annotation) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + \
    annotation.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

zip_command = 'zip.exe -r {0} {1}'.format(target, ' '.join(source))

print('zip command is:', zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup failed')