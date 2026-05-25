"""
AIDEOM-VN — máy chủ web tĩnh đơn giản.

Trang web (index.html) là file HTML tự chứa: mọi tính toán & biểu đồ chạy
bằng JavaScript trong trình duyệt, KHÔNG cần backend Python. File app.py này
chỉ làm nhiệm vụ "phục vụ" (serve) file đó qua HTTP để bạn mở trên trình duyệt.

Cách chạy:
    pip install -r requirements.txt
    python app.py
Sau đó mở: http://127.0.0.1:5000

Ghi chú: Bạn cũng có thể chạy KHÔNG cần Flask bằng máy chủ tĩnh có sẵn của Python:
    python -m http.server 5000
rồi mở http://127.0.0.1:5000
"""
import os
from flask import Flask, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, static_folder=BASE_DIR, static_url_path="")


@app.route("/")
def home():
    return send_from_directory(BASE_DIR, "index.html")


@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(BASE_DIR, filename)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n  AIDEOM-VN đang chạy tại:  http://127.0.0.1:{port}\n  Nhấn Ctrl+C để dừng.\n")
    app.run(host="0.0.0.0", port=port, debug=False)
