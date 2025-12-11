#!/bin/bash

# Bu script'in bulunduğu dizini al
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

input_file="$SCRIPT_DIR/script_output.txt"  # Giriş dosyasının adı
output_file="$SCRIPT_DIR/clean_rofi_output.txt"  # Çıkış dosyasının adı


# Çıkış dosyasını sıfırla
> "$output_file"

# Giriş dosyasını satır satır okuma
while IFS= read -r line; do
    # Satırdaki "Kategori"yi, "Türkçe"yi ve "İngilizce"yi yakala
    if [[ "$line" =~ \|[[:space:]]*([0-9]+)[[:space:]]*\|[[:space:]]*([a-zA-ZğüşöçİĞÜŞÖÇ]+)[[:space:]]*\|[[:space:]]*(.*)[[:space:]]*\|[[:space:]]*(.*)[[:space:]]*\| ]]; then
        # Çekilen verileri ilgili değişkenlere ata
        no="${BASH_REMATCH[1]}"
        kategori="${BASH_REMATCH[2]}"
        turkce="${BASH_REMATCH[3]}"
        ingilizce="${BASH_REMATCH[4]}"
        
        # Çıktıya formatlanmış şekilde yaz
        echo "$no. $kategori" >> "$output_file"
        echo "- $turkce" >> "$output_file"
        echo " -> $ingilizce" >> "$output_file"
    fi
done < "$input_file"

echo "Dönüştürme tamamlandı! Çıktı: $output_file"
