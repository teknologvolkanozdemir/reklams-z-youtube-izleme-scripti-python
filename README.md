# YouTube izleme aracı (Raspberry Pi OS)

`izle.py`, YouTube bağlantılarını `mpv` oynatıcıda `yt-dlp` aracılığıyla açar.
Bu yöntem normal YouTube oynatıcısını kullanmaz; ancak YouTube'un değişiklikleri,
video içindeki sponsorlu içerikler veya başka etkenler nedeniyle reklamların hiç
çıkmayacağını garanti etmez.

## Kurulum

Raspberry Pi OS terminalinde gerekli programları kurun:

```sh
sudo apt update
sudo apt install mpv yt-dlp
```

## Kullanım

Bir video bağlantısını komut satırında verin:

```sh
python3 izle.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Bağlantıyı etkileşimli olarak girmek için:

```sh
python3 izle.py
```
