#!/usr/bin/env python3
"""Play YouTube videos with mpv and yt-dlp."""

import argparse
import shutil
import subprocess
import sys
from urllib.parse import urlparse


def is_youtube_url(value):
    parsed = urlparse(value)
    hostname = (parsed.hostname or "").lower()
    return (
        parsed.scheme == "https"
        and (hostname == "youtu.be" or hostname == "youtube.com" or hostname.endswith(".youtube.com"))
    )


def main(argv=None):
    parser = argparse.ArgumentParser(description="YouTube videolarını mpv ile oynatır.")
    parser.add_argument("url", nargs="?", help="YouTube video bağlantısı")
    args = parser.parse_args(argv)
    url = args.url or input("YouTube video bağlantısını girin: ").strip()

    if not is_youtube_url(url):
        print("Hata: https://youtube.com veya https://youtu.be bağlantısı girin.", file=sys.stderr)
        return 2

    missing = [name for name in ("mpv", "yt-dlp") if shutil.which(name) is None]
    if missing:
        print(
            "Eksik program(lar): "
            + ", ".join(missing)
            + ". Kurulum için README.md dosyasına bakın.",
            file=sys.stderr,
        )
        return 1

    try:
        return subprocess.run(["mpv", "--", url], check=False).returncode
    except OSError as error:
        print(f"mpv başlatılamadı: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
