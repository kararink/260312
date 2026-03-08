# Googleカレンダー連携のシステム化

## 概要
Googleカレンダー（m090106@gmail.com）の「今日の予定」を取得し、日次スタートアップワークフロー（`/today-start`）で作成される日誌に自動的に反映させる。

## アーキテクチャ

1.  **データソース**: Google Calendar (iCal形式の非公開URL)
2.  **取得スクリプト**: `00_システム\devtools\get_google_calendar_today.py` (Python)
    *   標準ライブラリのみ使用 (`urllib`, `datetime`, `re`)
    *   iCalデータをパースし、当日のイベントを抽出・整形して標準出力する。
3.  **ワークフロー統合**: `.agent\workflows\today-start.md`
    *   日誌作成前にスクリプトを実行。
    *   出力結果をプロンプトコンテキスト（秘書へのブリーフィング等）に渡す。

## セットアップ手順
1.  **URL取得**: Googleカレンダー設定画面から「iCal形式の非公開URL」を取得。
2.  **設定**: `get_google_calendar_today.py` の `ICAL_URL` 変数にURLを記述。

## 使用方法
コマンドラインまたはワークフローから以下を実行：
```powershell
python 00_システム\devtools\get_google_calendar_today.py
```
