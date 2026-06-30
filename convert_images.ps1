Add-Type -AssemblyName System.Drawing

$artifactDir = "C:\Users\manu1\.gemini\antigravity-ide\brain\472e8c5c-43cd-4f41-8c39-de6b5166d623"
$outDir = "c:\Users\manu1\OneDrive\Desktop\Wearable Technology\images"

if (!(Test-Path $outDir)) {
    New-Item -Path $outDir -ItemType Directory -Force
}

$mappings = @{
    "hero_wearable_1782728122390.png" = "hero-wearable.webp"
    "about_wearable_1782728134813.png" = "about-wearable.webp"
    "product_smartwatch_1782728147686.png" = "product-smartwatch.webp"
}

foreach ($entry in $mappings.GetEnumerator()) {
    $srcPath = Join-Path $artifactDir $entry.Key
    $dstPath = Join-Path $outDir $entry.Value
    
    if (Test-Path $srcPath) {
        $img = [System.Drawing.Image]::FromFile($srcPath)
        
        # Resize to reduce file size (max 800px width)
        $maxWidth = 800
        if ($img.Width -gt $maxWidth) {
            $ratio = $maxWidth / $img.Width
            $newWidth = [int]($img.Width * $ratio)
            $newHeight = [int]($img.Height * $ratio)
            $resized = New-Object System.Drawing.Bitmap($newWidth, $newHeight)
            $graphics = [System.Drawing.Graphics]::FromImage($resized)
            $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
            $graphics.DrawImage($img, 0, 0, $newWidth, $newHeight)
            $graphics.Dispose()
            $img.Dispose()
            $img = $resized
        }
        
        # Save as PNG first (webp not natively supported in .NET Framework)
        $pngPath = $dstPath -replace '\.webp$', '.png'
        $img.Save($pngPath, [System.Drawing.Imaging.ImageFormat]::Png)
        $img.Dispose()
        
        Write-Host "Saved $($entry.Key) -> $($entry.Value -replace '\.webp$', '.png')"
    } else {
        Write-Host "Source not found: $srcPath"
    }
}

Write-Host "Done! Images saved as PNG (will use in website)."
