## NMAP
### ENUM Open port and vulnerability script
`nmap -sV -sC -oN <output.txt> -p- MACHINE_IP` (`-oN` is for normal output)
### ENUM shares for smb 
`nmap -p 445 --script=smb-enum-shares.nse,smb-enum-users.nse MACHINE_IP`
### ENUM network file system
`nmap -p 111 --script=nfs-ls,nfs-statfs,nfs-showmount MACHINE_IP`

## SMB
### SMBCLIENT Linux
`smbclient //MACHINE_IP/<path>`
### Download files in a repo
`smbget -R smb://MACHINE_IP/anonymous`
### Download recursivly the current content
```
smb: \> mask ""
smb: \> recurse ON
smb: \> prompt OFF
smb: \> mget *
```

## SSH
### login ssh with a private key
`ssh -i id_rsa <user>@MACHINE_IP`
### Tunneling
Reverse SSH port forwarding specifies that the given port on the remote server host is to be forwarded to the given host and port on the local side.

`-L` is a local tunnel (YOU <-- CLIENT). If a site was blocked, you can forward the traffic to a server you own and view it. For example, if imgur was blocked at work, you can do `ssh -L 9000:imgur.com:80 user@example.com`. Going to `localhost:9000` on your machine, will load imgur traffic using your other server.

-R is a remote tunnel (YOU --> CLIENT). You forward your traffic to the other server for others to view. Similar to the example above, but in reverse.

## HYDRA
### BRUTE FORCE WEB FORM
`hydra -s <port> -L </path/to/namelist> -P </path/to/passwordlist> <TARGET_IP> http-post-form '<route_uri>:<field1>=^USER^&<field2>=^PASS^:<invalid value returned>' -f -o <output_file>`
