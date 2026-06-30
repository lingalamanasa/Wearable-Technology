Add-Type -AssemblyName System.Drawing

$imgDir = "c:\Users\manu1\OneDrive\Desktop\Wearable Technology\images"
$files = Get-ChildItem $imgDir -Filter "*.png"

foreach ($file in $files) {
    $img = [System.Drawing.Image]::FromFile($file.FullName)
    
    # Resize to max 500px width for aggressive compression
    $maxWidth = 500
    $ratio = 1
    if ($img.Width -gt $maxWidth) {
        $ratio = $maxWidth / $img.Width
    }
    $newWidth = [int]($img.Width * $ratio)
    $newHeight = [int]($img.Height * $ratio)
    
    $resized = New-Object System.Drawing.Bitmap($newWidth, $newHeight)
    $graphics = [System.Drawing.Graphics]::FromImage($resized)
    $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $graphics.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
    $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $graphics.DrawImage($img, 0, 0, $newWidth, $newHeight)
    $graphics.Dispose()
    $img.Dispose()
    
    # Save as JPEG with quality 50 to get under 100KB
    $jpegCodec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
    $qualityParam = [System.Drawing.Imaging.Encoder]::Quality
    $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
    $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter($qualityParam, 45L)
    
    $jpgPath = $file.FullName -replace '\.png$', '.jpg'
    $resized.Save($jpgPath, $jpegCodec, $encoderParams)
    $resized.Dispose()
    
    # Remove original PNG
    Remove-Item $file.FullName -Force
    
    $newSize = [math]::Round((Get-Item $jpgPath).Length / 1024, 1)
    Write-Host "$($file.Name) -> $([System.IO.Path]::GetFileName($jpgPath)) : $newSize KB"
}

Write-Host "`nDone! All images compressed."
