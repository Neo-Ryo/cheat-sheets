### find file
`find / 2>/dev/null | grep file.txt`

### Enum files SUID
`find / -perm -4000 2>/dev/null`

### check binary groups
`ls -al /usr/bin/<some>`

### check binary env and so
`ltrace <some binaries>`
