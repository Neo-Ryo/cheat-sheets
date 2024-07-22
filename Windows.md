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
