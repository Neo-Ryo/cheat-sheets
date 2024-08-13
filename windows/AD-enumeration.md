### POWERSHELL
`(Get-ADOrganizationalUnit -Filter *).Name`\
`(Get-ADOrganizationalUnit -Filter {Name -eq "Servers"}).Count`\
`(Get-ADOrganizationalUnit -Filter {Name -eq “Workstations”}).Count`

`$Searchbase = (Get-ADOrganizationalUnit -Filter {Name -eq "People"}).DistinguishedName`\
`(Get-ADOrganizationalUnit -Filter * -SearchBase $Searchbase).Count`

