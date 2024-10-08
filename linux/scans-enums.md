## RUSTSCAN
`rustscan -a <IP>`

## NMAP
### ENUM Open port and vulnerability script
`nmap -sV -sC -oN <output.txt> -p- MACHINE_IP` (`-oN` is for normal output)
### ENUM shares for smb 
`nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse MACHINE_IP`
### ENUM network file system
`nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount MACHINE_IP`

## SMB
### SMBCLIENT enumerate shares
`smbclient -L \\\\MACHINE_IP\\`
### SMBCLIENT Linux connect to smb as anonymous
`smbclient //MACHINE_IP/<path>`
### SMBCLIENT Linux connect to smb as milesdyson
`smbclient -U milesdyson //$ip/milesdyson`
### Download files in a repo
`smbget -R smb://MACHINE_IP/anonymous`
### Download recursivly the current content
```
smb: \> mask ""
smb: \> recurse ON
smb: \> prompt OFF
smb: \> mget *
```
## POP3
### CONNECTION
`telnet $ip <PORT>`

### AUTH

`USER <username>`
`PASS <password>`

### ENUM
#### list emails
`list`
#### check one
`retr <email number>`
