# python script to copy config files to .config and reset

# imports
import os
import sys


# parameters 
# not used
target=sys.argv[1]

# file paths
confPath='~/.config/'
getPath="~/script/swapconfig/config/"

#copy config
os.system('cp '+getPath+'i3/'+target+' '+confPath+'i3/config')
os.system('cp '+getPath+'picom/'+target+' '+confPath+'picom/picom.conf')

#restart
os.system('pkill picom')
os.system('pkill polybar')

os.system('i3-msg restart')

