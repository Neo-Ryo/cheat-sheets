# ACTIVE DIRECTORY

### SEARCH FOR USERS IN AD
`Get-ADUser -Filter * -SearchBase "CN=Users,DC=THMREDTEAM,DC=COM"`

# ANTIVIRUS ENUM
`wmic /namespace:\\root\securitycenter2 path antivirusproduct` \
or POWERSHELL \
`Get-CimInstance -Namespace root/SecurityCenter2 -ClassName AntivirusProduct`
