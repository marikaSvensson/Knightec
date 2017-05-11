#!/bin/bash

# my first chell script
echo "Hello World!"
echo "knowledge is power"
ls -l
cd ../pythonProgs/readingAndWriting/
python  main.py

clear
echo "Hello $USER." 
echo -e "Today is \c "; date # -e \c : stay on line!
echo -e "Nbr of user login: \c "; who | wc -l
echo "Calendar" ; cal
# loops
for i in {1..4}
do
	echo "welcome $i times"
done

for i in $(seq 1 2 20)
do 
	echo "welcome $i times"
done

for ((c = 1; c<=5; c++))
do 
	echo "$c"
done
exit 0






