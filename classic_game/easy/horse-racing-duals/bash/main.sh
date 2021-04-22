#!/usr/bin/env bash

read N
while read Pi
do
    echo $Pi
done | sort -n |
awk 'BEGIN {min=10000000; old=0}
{if ($1-old<min) {min=$1-old} old=$1}
END {print min}'
