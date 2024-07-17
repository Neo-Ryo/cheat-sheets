## CLI

### decode some base64 encoded string
`echo <STRING> | base64 -d`

### decode hex value to string
`cat file.txt | sed 's/\([0-9A-F]\{2\}\)/\\\\\\x\1/gI' | xargs printf`

### Display a specific line in a file
`$ sed -n 5p file` > `5p` for line 5
### display several lines
`sed -n -e 5p -e 8p file` for line 5 AND 8\
`sed -n 5,8p file` for line 5 TO 8
