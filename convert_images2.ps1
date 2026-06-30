Add-Type -AssemblyName System.Drawing

$artifactDir = "C:\Users\manu1\.gemini\antigravity-ide\brain\472e8c5c-43cd-4f41-8c39-de6b5166d623"
$outDir = "c:\Users\manu1\OneDrive\Desktop\Wearable Technology\images"

if (!(Test-Path $outDir)) {
    New-Item -Path $outDir -ItemType Directory -Force
}

$mappings = @{
    "product_fitness_1782728263780.png" = "product-fitness.png"
    "product_arglasses_1782728417059.png" = "product-arglasses.png"
    "blog_1_1782728244678.png" = "blog-1.png"
    "blog_2_1782728428267.png" = "blog-2.png"
    "blog_3_1782728440729.png" = "blog-3.png"
    "service_dev_1782728459842.png" = "service-dev.png"
    "service_health_1782728482288.png" = "service-health.png"
    "service_enterprise_1782728493019.png" = "service-enterprise.png"
    "team_1_1782728504982.png" = "team-1.png"
    "team_2_1782728557272.png" = "team-2.png"
    "team_3_1782728525327.png" = "team-3.png"
    "login_bg_1782728537534.png" = "login-bg.png"
}

foreach ($entry in $mappings.GetEnumerator()) {
    $srcPath = Join-Path $artifactDir $entry.Key
    $dstPath = Join-Path $outDir $entry.Value
    
    if (Test-Path $srcPath) {
        $img = [System.Drawing.Image]::FromFile($srcPath)
        
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
        
        $img.Save($dstPath, [System.Drawing.Imaging.ImageFormat]::Png)
        $img.Dispose()
        
        Write-Host "Saved $($entry.Key) -> $($entry.Value)"
    } else {
        Write-Host "Source not found: $srcPath"
    }
}

Write-Host "Done!"
