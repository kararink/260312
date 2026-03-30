$word = New-Object -ComObject Word.Application
$doc = $word.Documents.Open('C:\Users\杢之助\2nd-Brain\Clippings\260330_水技C　懸案等整理票③（人事）.docx', $false, $true)
$text = $doc.Content.Text
$doc.Close($false)
$word.Quit()
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($word)
$text | Out-File -Encoding utf8 "C:\Users\杢之助\2nd-Brain\Clippings\doc.txt"
