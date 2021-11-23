#!/bin/sh

target=$(cat ~/.config/bin/target)

if [ $target ]; then
    echo "%{F#24c3cc}什%{F#ffffff} $target%{u-}"
else
    echo "%{F#24c3cc}ﲅ %{u-}%{F#ffffff} No target"
fi
