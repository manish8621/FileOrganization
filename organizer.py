# To organize files 
# catogorizing all files

import os
import sys
import shutil

# Local Variables
curr_dir = ''
Folders = ['Music','Videos','Photos','Documents','Compressed','Programs','Others']
Files = []
Extensions = {
    'Music':('mp3','m4a','flac','aac','wma','wav','ac3','dts')
    ,'Videos':('mp4','mkv','avi','webm','mov','wmv','flv','mpeg')
    ,'Photos':('jpg','jpeg','png','gif','webp','bmp','ico')
    ,'Documents':('txt','pdf','doc','docx','xls','xlsx')
    ,'Compressed':('zip','7z','gz','tar')
    ,'Programs':('apk','exe','deb')
    ,'Others':('')
    }

# The working directory
if len(sys.argv) == 2 and os.path.exists(sys.argv[1]):
    if sys.argv[1][len(sys.argv[1])-1] != '/':
        curr_dir = sys.argv[1]+'/'
else:
    curr_dir = os.getcwd()+'/'
#print(curr_dir)
#exit()
# check if folders exist if not create folders 
for folder in Folders:
    if not os.path.exists(curr_dir+folder):
        os.mkdir(curr_dir+folder)
        print(folder+' created')

# Get the list of files in the curr_dir filter out the folders out
for f in os.listdir(curr_dir):
    if os.path.isfile(curr_dir+f):
        Files.append(f)

# organize
for files in Files:
    ext = files.split(".").pop()
    act_folder = 'Others'
    for folder in Folders:
        if ext in Extensions.get(folder):
            act_folder = folder
            break
    shutil.move(curr_dir+files, curr_dir+act_folder+'/'+files)
    print(files+"-> moved to ->"+act_folder)
