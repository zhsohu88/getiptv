import requests

# 请求地址
url = "http://file.91kds.cn/tvlist/2025030711/kds_all_lnyd.txt"

# 请求头（模拟浏览器）
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
        content = response.text

        # 保存为 user_local.txt
        with open("user_local.txt", "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ 已保存为 user_local.txt")

    except requests.exceptions.RequestException as e:
        print(f"❌ 请求失败：{e}")

if __name__ == "__main__":
    fetch_and_save()
