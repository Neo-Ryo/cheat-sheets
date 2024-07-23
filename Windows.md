# ACTIVE DIRECTORY

### SEARCH FOR USERS IN AD
`Get-ADUser -Filter * -SearchBase "CN=Users,DC=THMREDTEAM,DC=COM"`

# ANTIVIRUS ENUM
cmd \
`wmic /namespace:\\root\securitycenter2 path antivirusproduct` \
or POWERSHELL \
`Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct` \
Note that Windows servers may not have SecurityCenter2 namespace. Instead, it works for Windows workstations! \

### Windows defender
PS \
`Get-Service WinDefend` \

#### Windows defender status
PS \
`Get-MpComputerStatus | select RealTimeProtectionEnabled`

# FIREWALL
### get firewall infos/status
`Get-NetFirewallProfile | Format-Table Name, Enabled` \
if we have privelges we can disable firewall \
`Set-NetFirewallProfile -Profile Domain, Public, Private -Enabled False` \
### check rules
`Get-NetFirewallRule | select DisplayName, Enabled, Description`
### test connections
`Test-NetConnection -ComputerName 127.0.0.1 -Port 80` \
`(New-Object System.Net.Sockets.TcpClient("127.0.0.1", "80")).Connected` \
# EVENT LOGS
`Get-EventLog -List`
### CHECK SYSMON
`Get-Process | Where-Object { $_.ProcessName -eq "Sysmon" }`\
`Get-CimInstance win32_service -Filter "Description = 'System Monitor service'"`\
`Get-Service | where-object {$_.DisplayName -like "*sysm*"}`\
`reg query HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\WINEVT\Channels\Microsoft-Windows-Sysmon/Operational`\
`findstr /si '<ProcessCreate onmatch="exclude">' C:\tools\*`

#  RUNNING SERVICES

### ENUMERATE
`net start`
### GET DETAILS ON A SPECIFIC ONE
`wmic service where "name like '<SERVICE_NAME>'" get Name,PathName`\
`Get-Process -Name <process_exe>`
#### LISTENNING PORT
`netstat -noa |findstr "LISTENING" |findstr <ID>`

# DNS

### DNS TRANSFERT
`nslookup.exe`\
Provide the DNS to ask (local machine or other)\
`>server <IP>`\
DNS zone transfer on the domain we find in the AD environment.\
`>ls -d <DOMAIN>`
