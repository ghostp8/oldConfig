# config

my .config files for Archlinux i3

swapconfig is a python script used to copy config files into .config and reload the programs
it is settup for polybar, picom and i3 with two diffrent config files 'focus' and 'gaps'

randWall is a python script that changes the wallpaper to a randome file from a given directory
requires nitrogen, the program used to set the wallpaper.
the directory used can be changed by changing the variable 'path'
the 'homeDir' must also be changed to your home directory (ie '/home/USERNAME/' )

setNit is a python script that changes the background to the given file
requires nitrogen, the program used to set the wallpaper
as python requires the full path to the nitrogen config file, you will have to edit the script and change the variable 'homeDir'
to your home directory (ie '/home/USERNAME/' )
