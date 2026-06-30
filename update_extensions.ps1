$files = Get-ChildItem "c:\Users\manu1\OneDrive\Desktop\Wearable Technology" -Include *.html, *.css -Recurse

foreach ($file in $files) {
    $content = Get-Content $file.FullName
    if ($content -match "\.png") {
        $content = $content -replace "\.png", ".webp"
        Set-Content -Path $file.FullName -Value $content
        Write-Host "Updated $($file.Name)"
    }
}
