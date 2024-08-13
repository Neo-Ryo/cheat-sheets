### POWERSHELL
`(Get-ADOrganizationalUnit -Filter *).Name`\
`(Get-ADOrganizationalUnit -Filter {Name -eq "Servers"}).Count`\
`(Get-ADOrganizationalUnit -Filter {Name -eq “Workstations”}).Count`

`$Searchbase = (Get-ADOrganizationalUnit -Filter {Name -eq "People"}).DistinguishedName`\
`(Get-ADOrganizationalUnit -Filter * -SearchBase $Searchbase).Count`

` (Get-ADUser <user name> -Properties *).Description`

`Get-ADUser -Identity <user.name> -Server <domaine.name> -Properties *`

`Get-ADUser -Filter 'Name -like "*<partialname>"' -Server <domain.name> | Format-Table Name,SamAccountName -A`

`Get-ADGroup -Identity Administrators -Server <domain.name>`

`Get-ADGroupMember -Identity Administrators -Server <domain.name>`

##### AD object that where changed after a certain date
`$ChangeDate = New-Object DateTime(2022, 02, 28, 12, 00, 00)`
`Get-ADObject -Filter 'whenChanged -gt $ChangeDate' -includeDeletedObjects -Server <domaine.name>`
