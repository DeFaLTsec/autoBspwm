#!/bin/bash

ip_address=$(cat /home/$USER/.config/bin/target | awk '{print $1}')
machine_name=$(cat /home/$USER/.config/bin/target | awk '{print $2}')

if [ $ip_address ] && [ $machine_name ]; then
    echo "%{F#24c3cc} %{F#ffffff} $ip_address - $machine_name%{u-}"
else
    echo "%{F#24c3cc}ﲅ %{u-}%{F#ffffff} No target"
fi
