Add-Type -AssemblyName System.Runtime.WindowsRuntime

# Helper to await UWP async operations
function Await-Task {
    param([object]$Task)
    $asTask = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
        $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1'
    })[0]
    $genericMethod = $asTask.MakeGenericMethod($Task.GetType().GetInterfaces()[0].GenericTypeArguments[0])
    $task = $genericMethod.Invoke($null, @($Task))
    $task.Wait()
    return $task.Result
}

# Load OCR engine for Japanese
[Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Graphics.Imaging.BitmapDecoder, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.StorageFile, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null
[Windows.Storage.Streams.RandomAccessStream, Windows.Foundation, ContentType = WindowsRuntime] | Out-Null

$lang = New-Object Windows.Globalization.Language("ja")
$ocrEngine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromLanguage($lang)

if (-not $ocrEngine) {
    Write-Host "Japanese OCR not available, trying default..."
    $ocrEngine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
}

if (-not $ocrEngine) {
    Write-Error "No OCR engine available"
    exit 1
}

Write-Host "OCR Engine loaded"

$imageDir = "c:\Users\杢之助\2nd-Brain\.agent\temp_ocr"
$allText = ""

for ($i = 0; $i -lt 15; $i++) {
    $fileName = "page_{0:D2}.png" -f $i
    $filePath = Join-Path $imageDir $fileName
    
    Write-Host "Processing $fileName..."
    
    # Open file
    $storageFile = Await-Task ([Windows.Storage.StorageFile]::GetFileFromPathAsync($filePath))
    $stream = Await-Task ($storageFile.OpenAsync([Windows.Storage.FileAccessMode]::Read))
    $decoder = Await-Task ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream))
    $bitmap = Await-Task ($decoder.GetSoftwareBitmapAsync())
    
    # OCR
    $result = Await-Task ($ocrEngine.RecognizeAsync($bitmap))
    $text = $result.Text
    
    Write-Host "  -> $($text.Length) chars extracted"
    $allText += "--- Page $($i+1) ---`n$text`n`n"
    
    $stream.Dispose()
}

$outputPath = "c:\Users\杢之助\2nd-Brain\.agent\temp_ocr\extracted_text.txt"
$allText | Out-File -FilePath $outputPath -Encoding UTF8
Write-Host "`nAll text saved to: $outputPath"
Write-Host "`nTotal length: $($allText.Length) chars"
