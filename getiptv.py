import requests
import chardet  # pip install chardet

url = "http://file.91kds.cn/tvlist/2025030711/kds_all_lnyd.txt"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114 Safari/537.36",
    "Referer": "http://file.91kds.cn/",
    "Connection": "Keep-Alive"
}

def fetch_and_save():
    try:
        print(f"正在请求：{url}")
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        # 自动检测编码
        detected = chardet.detect(response.content)
        encoding = detected["encoding"]
        print(f"📦 检测到编码：{encoding}")

        # 解码并保存为 UTF-8
        content = response.content.decode(encoding)
        with open("user_local.txt", "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ 已保存为 UTF-8 编码的 user_local.txt")

    except requests.exceptions.RequestException as e:
        print(f"❌ 请求失败：{e}")
    except UnicodeDecodeError as e:
        print(f"❌ 解码失败：{e}")

if __name__ == "__main__":
    fetch_and_save()
