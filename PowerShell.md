## Find file
`Get-ChildItem -Path <path\to\check> -Recurse | Select-Object -Property Name, Directory | Where-Object -Property Name -Contains <filename>`

## Decode base64
`[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String(<stringToDecode>))`
