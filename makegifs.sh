#! /bin/bash
j=0
i=0
while [ $i -lt $2 ]; do
        upper=$(($i+$3))
        python map.py $1 $i $upper $j gif
        let j=$j+1
        let i=upper
done
