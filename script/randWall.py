### python script to randomley select wallpaper from folder using nitrogen

### imports
import random
import os

### settingis
homeDir='/home/cathal/'
path=homeDir+'pictures/wallpapers/fav/'
conf=homeDir+'.config/nitrogen/bg-saved.cfg'


## confirm path
if os.path.exists(path) :

    # pick picture
    pics=os.listdir(path)
    picN=random.randint(0,len(pics)-1)
    pic=pics[picN]

    # set using nitrogen
    f=open(conf,'w')
    f.write(' [xin_-1]\nfile='+path+pic+'\nmode=0 \nbgcolor=#000000')
    f.close()

    # restore
    os.system('nitrogen --restore')

else :
    print('ERROR : randWall.py : specified path does not exist, aborting...')
