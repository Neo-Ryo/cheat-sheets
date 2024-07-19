## DECODING

### decode some base64 encoded string
`echo <STRING> | base64 -d`
### decode hex value to string
`cat file.txt | sed 's/\([0-9A-F]\{2\}\)/\\\\\\x\1/gI' | xargs printf`

## DISPLAY

### Display a specific line in a file
`$ sed -n 5p file` > `5p` for line 5
### display several lines
`sed -n -e 5p -e 8p file` for line 5 AND 8\
`sed -n 5,8p file` for line 5 TO 8

## MANIPULATE

### combine word list
`cat file1.txt file2.txt file3.txt > combined_list.txt`
### sort and unique
`sort combined_list.txt | uniq -u > cleaned_combined_list.txt`

## WEB CRAWLING

### get words from a website
`cewl -w list.txt -d 5 -m 5 <URL>` (`-d 5` is for the depth level of crawling and `-w 5` is for word length)
