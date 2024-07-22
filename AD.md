# ACTIVE DIRECTORY

### SEARCH FOR USERS IN AD
`Get-ADUser -Filter * -SearchBase "CN=Users,DC=THMREDTEAM,DC=COM"`

# ANTIVIRUS ENUM
cmd \
`wmic /namespace:\\root\securitycenter2 path antivirusproduct` \
or POWERSHELL \
`Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct` \
Note that Windows servers may not have SecurityCenter2 namespace, which may not work on the attached VM. Instead, it works for Windows workstations! \
