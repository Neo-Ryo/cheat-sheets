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
`Get-NetFirewallProfile | Format-Table Name, Enabled`
if we have privelges we can disable firewall
`Set-NetFirewallProfile -Profile Domain, Public, Private -Enabled False`
