#!/bin/bash
#apt-get install sshpass -y
test=$(sshpass -p "lannion" scp -v /home/etudiant/Bureau/SAE/fich etudiant@127.0.0.1:/home/etudiant/Téléchargements 2> test.tmp)

essai=$(more test.tmp | tail -3 | head -n 1)

more test.tmp | tail -3 | head -n 2 | tail -1 > /root/Bureau/travail_SAE/donnees.txt


var1=$( echo $essai | cut -d ' ' -f 3 | cut -d ',' -f 1 )
var2=$( echo $essai | cut -d ' ' -f 5 | cut -d ',' -f 1 )
var3=$( echo $essai | cut -d ' ' -f 8 | cut -d ',' -f 1 )


echo $var1,$var2,$var3 >> /root/Bureau/travail_SAE/donnees.csv

more donnees.csv


exit 0
