### find file
`find / 2>/dev/null | grep file.txt`

### Enum files SUID
`find / -perm -4000 2>/dev/null`

### check binary groups
`ls -al /usr/bin/<some>`

### check binary env and so
`ltrace <some binaries>`
### check who is currently connected on the machine
`who`
### check who is currently connected on the machine and what they are doing
`w`
