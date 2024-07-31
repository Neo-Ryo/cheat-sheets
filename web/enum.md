## WEB ENUM
### GOBUSTER
`gobuster dir -u http://<IP_TARGET> -w </path/to/wordlist> -x php,sh,txt,html`

### FFUF
`ffuf -u http://<IP_TARGET>/FUZZ -w /path/to/wrdlist`
#### FFUF subdomain
`ffuf -u http://domain.name -w /path/to/wrdlist -H "Host:FUZZ.domain.name"`
#### FFUF brute force
`ffuf -u 'http://domain.name/post' -X POST -d 'username=FUZZ&password=admin' -H 'Content-Type: application/x-www-form-urlencoded' -w /usr/share/wordlists/rockyou.txt -mc all -t 100 -fr "Error message"`
#### FFUF brute force multiple input
`ffuf -u 'http://cherryontop.thm/content.php?facts=IDS&user=USER' -w <(seq 1 100):IDS -w base32-usernames.txt:USER`
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
