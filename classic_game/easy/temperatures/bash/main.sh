#/usr/bin/env bash

read n
read temps

if [ $n -eq 0 ]
then
    echo $n
else
echo $temps | tr " " "\n" | awk \
'function abs(v) {return v<0 ? -v : v}
 BEGIN{res=5526}
 { if (abs(res) > abs($1) || (abs(res) == abs($1) && $1 > res)) {res = $1} }
 END{print res}' 
fi