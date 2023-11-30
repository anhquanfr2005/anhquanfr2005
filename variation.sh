#/bin/bash
#cp -ir /root/GNS3/configs /home/stock

mkdir /home/stock 2> t.tmp

z=$(($RANDOM % 1000))
m=$(ls /root/Dictionaries | tail -1)
cp -r /root/Dictionaries/$m /home/stock/$z

if [ $(($RANDOM % 3)) == 1 ];
    then
    echo "b"
    z=$(($RANDOM % 1000))
    cp -r /root/Dictionaries/$m /home/stock/$z
else
    nom=$(ls /home/stock | tail -1)
    rm /home/stock/$nom 2> t.tmp
    nom=$(ls /home/stock | tail -1)
    rm /home/stock/$nom 2> t.tmp
    nom=$(ls /home/stock | tail -1)
    rm /home/stock/$nom 2> t.tmp
    
    z=$(($RANDOM % 1000))
    cp -r /root/Dictionaries/$m /home/stock/$z
fi
exit 0

