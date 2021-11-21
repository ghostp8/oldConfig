#!/bin/bash

###lock script by petvas
# https://github.com/petvas/i3lock-blur
# requires ffmpeg and xrandr
# this script must be exequtible chmod +x file/path
# bindsym $mod+z exec path/to/me
# insure RES is correct


TMPBG=/tmp/screen.png
LOCK=$HOME/.config/i3/lock.png
RES=1920x1080

ffmpeg -f x11grab -video_size $RES -y -i $DISPLAY -i $LOCK -filter_complex "boxblur=5:1,overlay=(main_w-overlay_w)/2:(main_h-overlay_h)/2" -vframes 1 $TMPBG
i3lock -u -i $TMPBG
