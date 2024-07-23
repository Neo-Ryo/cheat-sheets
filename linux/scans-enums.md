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
## WEB ENUM
### GOBUSTER
`gobuster dir -u http://<IP_TARGET> -w </path/to/wordlist> -x php,sh,txt,html`

### FFUF
`ffuf -u http://<IP_TARGET>/FUZZ -w /path/to/wrdlist`

### wpscan
#### enum potential users
`wpscan --url <url> -e u`
#### bruteforce with found user
`wpscan --url <url> -U <user1,user2> -P /opt/wordlists/rockyou.txt --password-attack wp-login -t 64`

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
