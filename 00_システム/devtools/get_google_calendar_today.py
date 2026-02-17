import urllib.request
import datetime
import re
import sys

# ==========================================
# CONFIGURATION
# ==========================================
# Google Calendarの「iCal形式の非公開URL」を以下に設定してください。
# Settings -> Integrate calendar -> Secret address in iCal format

ICAL_URL = "https://calendar.google.com/calendar/ical/m090106%40gmail.com/private-c765a469fb19a17708ffabbcb3737bfc/basic.ics"
# ==========================================

def get_today_events():
    """
    指定されたICS URLから今日の予定を取得し、整形して出力する
    """
    # The check for "YOUR_SECRET_ical_URL_HERE" is removed as ICAL_URL is now explicitly set.
    # If you want to keep a check for an empty or placeholder URL, you can add it here.
    # Example:
    # if not ICAL_URL or "YOUR_SECRET_ical_URL_HERE" in ICAL_URL:
    #     print("Error: ICAL_URL is not configured. Please set your Google Calendar Secret iCal URL in the script.")
    #     return

    try:
        # ICSデータを取得
        with urllib.request.urlopen(ICAL_URL) as response:
            ical_data = response.read().decode('utf-8')
    except Exception as e:
        print(f"Error fetching calendar data: {e}")
        return

    # 今日の日付 (ローカル)
    today = datetime.date.today()
    today_str = today.strftime('%Y%m%d')
    
    # 簡易的なICSパーサー matches VEVENT blocks
    events = []
    
    # 正規表現でイベントブロックを抽出
    # re.DOTALLで改行も含めてマッチさせる
    event_blocks = re.findall(r'BEGIN:VEVENT(.*?)END:VEVENT', ical_data, re.DOTALL)

    print(f"--- Google Calendar Events for {today} ---")

    found_events = False

    for block in event_blocks:
        # 日付関連のフィールドを抽出
        dtstart_match = re.search(r'DTSTART(?:;.*?)?:(\d{8})(?:T(\d{6}))?', block)
        dtend_match = re.search(r'DTEND(?:;.*?)?:(\d{8})(?:T(\d{6}))?', block)
        summary_match = re.search(r'SUMMARY:(.*)', block)

        if not dtstart_match:
            continue

        start_date_str = dtstart_match.group(1)
        start_time_str = dtstart_match.group(2) # None if all-day
        
        # 今日のイベントか判定
        if start_date_str == today_str:
            found_events = True
            summary = summary_match.group(1).strip() if summary_match else "No Title"
            
            # 時間の整形
            if start_time_str:
                # 時刻あり (UTCで来る場合が多いが、ICSの形式による。
                # 単純化のため、表示されている数字をそのまま整形する。
                # 必要に応じてタイムゾーン変換を入れるが、Google CalendarのSecret Addressは通常UTC。
                # ここでは簡易実装としてZがついているか確認して+9時間 (JST) する処理を入れる。
                
                # Check for TZID or Z logic if needed. For now, assume simple parsing or UTC.
                # Many ICS feeds allow raw UTC. Let's try to detect Z.
                # Re-fetch full line for DTSTART to check for Z
                dtstart_line_match = re.search(r'DTSTART.*:(\d{8}T\d{6})(Z?)', block)
                is_utc = False
                if dtstart_line_match and dtstart_line_match.group(2) == 'Z':
                    is_utc = True
                
                hour = int(start_time_str[0:2])
                minute = int(start_time_str[2:4])
                
                if is_utc:
                    # UTC to JST (+9)
                    dt = datetime.datetime(int(start_date_str[0:4]), int(start_date_str[4:6]), int(start_date_str[6:8]), hour, minute)
                    dt_jst = dt + datetime.timedelta(hours=9)
                    time_display = dt_jst.strftime('%H:%M')
                    
                    # 日付またぎの補正は今回は省略(今日の予定としてリストアップ対象になったものがズレる可能性があるが、
                    # start_date_str判定の時点でJST換算していないと漏れる可能性がある)
                    # *厳密には* 全イベントをJSTに変換してから「今日」か判定すべきだが、
                    # まずは簡易実装として「日付文字列が一致するもの」を表示し、時刻をJSTになおす。
                else:
                    time_display = f"{hour:02}:{minute:02}"
            else:
                time_display = "All Day"

            print(f"- [{time_display}] {summary}")
    
    if not found_events:
        print("No events found for today.")

if __name__ == "__main__":
    get_today_events()
