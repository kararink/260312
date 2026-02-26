"""
Discord Webhook を使ったプッシュ通知スクリプト
==============================================
コマンドラインまたは他のPythonスクリプトから Discord にメッセージを送信する。

使用例:
  python discord_notify.py "今日のタスク完了！"
  python discord_notify.py "リマインダー" "買い物リスト：牛乳、卵"

他スクリプトからの利用:
  from discord_notify import send_discord_message
  send_discord_message("通知テスト")
"""

import sys
import os
import json
import requests
import io
from pathlib import Path

# Windows コンソール（cp932）で日本語出力が崩れないようにする
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# ==========================================
# 💎 Webhook URL（環境変数から取得）
# ==========================================
def _load_webhook_url() -> str:
    """環境変数またはルート .env から DISCORD_WEBHOOK_URL を取得する"""
    url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not url:
        # ルートの .env を探す
        env_path = Path(__file__).resolve().parents[2] / ".env"
        if env_path.exists():
            with open(env_path, encoding="utf-8") as f:
                for line in f:
                    if line.startswith("DISCORD_WEBHOOK_URL="):
                        url = line.strip().split("=", 1)[1]
                        break
    if not url:
        print("[ERROR] DISCORD_WEBHOOK_URL が設定されていません。")
        print("ルートの .env に DISCORD_WEBHOOK_URL=<URL> を追記してください。")
    return url or ""

WEBHOOK_URL = _load_webhook_url()

def send_discord_message(message: str, username="Antigravity Agent") -> bool:
    """
    Discordにメッセージを送信する関数
    :param message: 送信するメッセージ内容
    :param username: 通知のアバター名（省略可）
    :return: True: 送信成功, False: 送信失敗
    """
    data = {
        "content": message,
        "username": username
    }
    
    try:
        # WebhookへのPOSTリクエスト
        response = requests.post(
            WEBHOOK_URL, 
            data=json.dumps(data), 
            headers={"Content-Type": "application/json"}
        )
        
        if 200 <= response.status_code < 300:
            preview = message[:50] + ("..." if len(message) > 50 else "")
            print(f"[OK] 送信成功: {preview}")
            return True
        else:
            print(f"[FAIL] 送信失敗: ステータスコード {response.status_code}")
            print(f"エラー内容: {response.text}")
            return False
            
    except Exception as e:
        print(f"[FAIL] エラーが発生しました: {e}")
        return False

def main() -> None:
    if len(sys.argv) < 2:
        print("使い方: python discord_notify.py <メッセージ> [追加メッセージ...]")
        print('例:     python discord_notify.py "今日のタスク完了！"')
        
        # 引数がない場合はテスト送信を行う
        print("\n--- 引数が指定されていないため、テスト送信を行います ---")
        send_discord_message("🚀 Discord通知システム：セットアップ完了テスト")
        sys.exit(0)

    # 複数引数はスペースで結合
    message = " ".join(sys.argv[1:])
    success = send_discord_message(message)
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
