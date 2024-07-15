## Find file
`Get-ChildItem -Path <path\to\check> -Recurse | Select-Object -Property Name, Directory | Where-Object -Property Name -Contains <filename>`
## Find file and get content
`Get-ChildItem “*<type of file (eg: .txt)>*” -Path C:\ -Recurse -ErrorAction SilentlyContinue | Get-Content`
## Decode base64
`[System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String(<stringToDecode>))`
## List Connection
`Get-NetTCPConnection`
## List connection and filter
`Get-NetTCPConnection | Where-Object {($_.State -eq “<STATE>”) -and ($_.LocalPort -eq “<PORT>”)}`
