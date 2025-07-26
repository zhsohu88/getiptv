# 导入 requests 库，用于发送 HTTP 请求
import requests

# 导入 chardet 库，用于自动检测网页内容的编码格式
import chardet  # 如果未安装，请运行：pip install chardet

# 要请求的 IPTV 列表文件地址
url = "http://file.91kds.cn/tvlist/2025030711/kds_all_lnyd.txt"

# 设置请求头，模拟浏览器访问，避免被服务器拒绝
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114 Safari/537.36",
    "Referer": "http://file.91kds.cn/",  # 来源页面，部分服务器会校验
    "Connection": "Keep-Alive"           # 保持连接，提高效率
}

# 定义主函数：请求 IPTV 文件并保存为 UTF-8 编码
def fetch_and_save():
    try:
        print(f"正在请求：{url}")
        
        # 发送 GET 请求，设置超时时间为 30 秒
        response = requests.get(url, headers=headers, timeout=30)
        
        # 如果响应状态码不是 200，则抛出异常
        response.raise_for_status()

        # 使用 chardet 自动检测响应内容的编码格式
        detected = chardet.detect(response.content)
        encoding = detected["encoding"]
        print(f"📦 检测到编码：{encoding}")

        # 将原始内容按检测到的编码解码为字符串
        content = response.content.decode(encoding)

        # 将内容保存为 UTF-8 编码的文本文件
        with open("user_local.txt", "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ 已保存为 UTF-8 编码的 user_local.txt")

    # 捕获请求异常（如网络错误、超时等）
    except requests.exceptions.RequestException as e:
        print(f"❌ 请求失败：{e}")

    # 捕获解码异常（如编码识别错误）
    except UnicodeDecodeError as e:
        print(f"❌ 解码失败：{e}")

# 如果当前脚本是主程序入口，则执行 fetch_and_save 函数
if __name__ == "__main__":
    fetch_and_save()
