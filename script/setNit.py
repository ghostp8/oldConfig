### python script to set wallpaper to specified file using nitrogen

### imports
import sys
import os

### settingis
homeDir='/home/cathal/'
path=sys.argv[1]
conf=homeDir+'.config/nitrogen/bg-saved.cfg'


## confirm path
if os.path.exists(path) :

    # set using nitrogen
    f=open(conf,'w')
    f.write('[xin_-1]\nfile='+path+'\nmode=0 \nbgcolor=#000000')
    f.close()

    # restore
    os.system('nitrogen --restore')

else :
    print('ERROR : setNit.py : specified path does not exist, aborting...')
