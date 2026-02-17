"""
LINE Messaging API を使ったプッシュ通知スクリプト
==============================================
コマンドラインまたは他のPythonスクリプトから LINE にメッセージを送信する。

使用例:
  python line_notify.py "今日のタスク完了！"
  python line_notify.py "リマインダー" "買い物リスト：牛乳、卵"

他スクリプトからの利用:
  from line_notify import send_line_message
  send_line_message("通知テスト")
"""

import sys
import os
import io
import json
import urllib.request
import urllib.error
from pathlib import Path

# Windows コンソール（cp932）で日本語出力が崩れないようにする
if sys.stdout and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")


def _load_env(env_path: Path) -> dict[str, str]:
    """簡易 .env パーサー（python-dotenv が無くても動作する）"""
    env_vars: dict[str, str] = {}
    if not env_path.exists():
        return env_vars
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, value = line.split("=", 1)
                env_vars[key.strip()] = value.strip()
    return env_vars


def _get_config() -> tuple[str, str]:
    """Channel Access Token と User ID を取得する"""
    # 環境変数を優先、なければ .env ファイルから読む
    env_path = Path(__file__).parent / ".env"
    file_env = _load_env(env_path)

    token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN") or file_env.get("LINE_CHANNEL_ACCESS_TOKEN", "")
    user_id = os.environ.get("LINE_USER_ID") or file_env.get("LINE_USER_ID", "")

    if not token or token.startswith("ここに"):
        print("[ERROR] LINE_CHANNEL_ACCESS_TOKEN が設定されていません。")
        print(f"  .env ファイル ({env_path}) にトークンを設定してください。")
        sys.exit(1)

    if not user_id or user_id.startswith("ここに"):
        print("[ERROR] LINE_USER_ID が設定されていません。")
        print(f"  .env ファイル ({env_path}) にユーザーIDを設定してください。")
        sys.exit(1)

    return token, user_id


def send_line_message(message: str) -> bool:
    """
    LINE Messaging API で自分にプッシュメッセージを送信する。

    Args:
        message: 送信するテキストメッセージ

    Returns:
        True: 送信成功, False: 送信失敗
    """
    token, user_id = _get_config()

    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }
    body = json.dumps({
        "to": user_id,
        "messages": [
            {
                "type": "text",
                "text": message,
            }
        ],
    }).encode("utf-8")

    req = urllib.request.Request(url, data=body, headers=headers, method="POST")

    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                preview = message[:50] + ("..." if len(message) > 50 else "")
                print(f"[OK] 送信成功: {preview}")
                return True
            else:
                print(f"[WARN] 予期しないステータスコード: {response.status}")
                return False
    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        print(f"[FAIL] 送信失敗 (HTTP {e.code}): {error_body}")
        return False
    except urllib.error.URLError as e:
        print(f"[FAIL] 接続エラー: {e.reason}")
        return False


def main() -> None:
    if len(sys.argv) < 2:
        print("使い方: python line_notify.py <メッセージ> [追加メッセージ...]")
        print('例:     python line_notify.py "今日のタスク完了！"')
        sys.exit(1)

    # 複数引数はスペースで結合
    message = " ".join(sys.argv[1:])
    success = send_line_message(message)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
