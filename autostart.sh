#!/bin/sh
#setando o teclado abnt2
setxkbmap -model abnt2 -layout br -variant abnt2 &
#wallpaper
feh --bg-scale ~/Pictures/Wallpapers/purple.jpg &
#compton

picom -b &
