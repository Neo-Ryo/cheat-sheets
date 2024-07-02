# NMAP
## ENUM Open port and vulnerability script
`nmap -sV -sC -oN <output.txt> -p- MACHINE_IP` (`-oN` is for normal output)
## ENUM shares for smb 
`nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse MACHINE_IP`
## ENUM network file system
`nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount MACHINE_IP`

# SMB
## SMBCLIENT Linux
`smbclient //MACHINE_IP/<path>`
## Download files in a repo
`smbget -R smb://MACHINE_IP/anonymous`

# SSH
## login ssh with a private key
`ssh -i id_rsa <user>@MACHINE_IP`

# HYDRA
## BRUTE FORCE WEB FORM
`hydra -s <port> -L </path/to/namelist> -P </path/to/passwordlist> <TARGET_IP> http-post-form '<route_uri>:<field1>=^USER^&<field2>=^PASS^:<invalid value returned>' -f -o <output_file>`
