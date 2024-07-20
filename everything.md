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


## REVERSE SHELL
### Upgrade reverse shell (according to python avalaible version)
`python -c 'import pty; pty.spawn("/bin/bash")'`


## CHECK IMAGES
### HIDDEN DATA (bmp, jpeg, wav and au files)
`steghide extract -sf <file.extension>`
