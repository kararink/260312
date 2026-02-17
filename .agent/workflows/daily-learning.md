---
description: 毎日1つのテーマ（進化心理学、行動経済学、AI/Tech、脳科学、健康）を科学的に学び、アクションに落とし込むワークフロー。
---

# Daily Learning Workflow

このワークフローは、ユーザーが指定した5つのテーマからランダムに1つを選び、
1.  **リサーチAI**: 科学的根拠のある理論を特定
2.  **教授AI**: Cool Architectスタイルで解説
3.  **トレーナーAI**: 今日できるアクションと習慣を設計
というプロセスを実行して、日誌に追記します。

## Steps

1.  **Select Theme & Check Log**
    - 以下のスクリプトを実行して、今日のテーマを決定し、過去の学習ログを取得します。
    - **Themes**:
        - Evolutionary Psychology
        - Behavioral Economics
        - AI & Technology
        - Neuroscience
        - Health & Bio-hacking
    - **Log File**: `c:\Users\杢之助\2nd-Brain\05_日誌\learning_log.json`

    ```powershell
    # PowerShell Script to select theme and read log
    $themes = @("Evolutionary Psychology", "Behavioral Economics", "AI & Technology", "Neuroscience", "Health & Bio-hacking")
    $logFile = "c:\Users\杢之助\2nd-Brain\05_日誌\learning_log.json"
    
    if (-not (Test-Path $logFile)) {
        Set-Content -Path $logFile -Value "[]" -Encoding UTF8
    }

    $logContent = Get-Content $logFile -Raw | ConvertFrom-Json
    
    # Get recent topics to avoid repetition of specific theories
    $recentTopics = $logContent | Sort-Object -Property Date -Descending | Select-Object -First 5 -ExpandProperty Topic -ErrorAction SilentlyContinue
    
    # Get last theme to avoid consecutive same theme
    $lastTheme = $logContent | Sort-Object -Property Date -Descending | Select-Object -First 1 -ExpandProperty Theme -ErrorAction SilentlyContinue

    # Filter out the last theme from the pool to ensure variety
    if ($lastTheme) {
        $themes = $themes | Where-Object { $_ -ne $lastTheme }
    }

    $selectedTheme = $themes | Get-Random
    
    # Store variables for next steps
    $env:SelectedTheme = $selectedTheme
    $env:RecentLog = ($recentTopics -join ", ")
    
    Write-Output "Selected Theme: $selectedTheme"
    Write-Output "Recent Topics: $env:RecentLog"
    ```

2.  **Research Phase**
    - **Role**: Research AI
    - **Prompt**: `c:\Users\杢之助\2nd-Brain\00_システム\01_Prompts\DailyLearning\01_research_ai.md`
    - **Input**:
        - Theme: `$env:SelectedTheme`
        - Log: `$env:RecentLog`
    - **Output**: `research_result.json` (Save this content for next steps)

3.  **Professor Phase**
    - **Role**: Professor AI
    - **Prompt**: `c:\Users\杢之助\2nd-Brain\00_システム\01_Prompts\DailyLearning\02_professor_ai.md`
    - **Input**:
        - ResearchJSON: `{{research_result.json}}`
    - **Output**: `professor_explanation.md`

4.  **Trainer Phase**
    - **Role**: Trainer AI
    - **Prompt**: `c:\Users\杢之助\2nd-Brain\00_システム\01_Prompts\DailyLearning\03_trainer_ai.md`
    - **Input**:
        - ProfessorExplanation: `{{professor_explanation.md}}`
    - **Output**: `action_plan.md`

5.  **Compile & Save**
    - `professor_explanation.md` と `action_plan.md` を結合し、今日の日誌ファイルの末尾に追記します。
    - また、学習したトピックを `learning_log.json` に追記します。

    ```powershell
    # PowerShell Script to save results
    $researchJson = Get-Content "research_result.json" -Raw | ConvertFrom-Json
    $professorText = Get-Content "professor_explanation.md" -Raw
    $trainerText = Get-Content "action_plan.md" -Raw
    
    $today = Get-Date -Format "yyyy-MM-dd"
    $dailyNotePath = "c:\Users\杢之助\2nd-Brain\05_日誌\$today.md"
    
    # Append to Daily Note
    $finalOutput = "`n`n## Daily Learning: $($researchJson.topic)`n`n" + $professorText + "`n" + $trainerText
    Add-Content -Path $dailyNotePath -Value $finalOutput -Encoding UTF8
    
    # Update Log
    $logFile = "c:\Users\杢之助\2nd-Brain\05_日誌\learning_log.json"
    $currentLog = Get-Content $logFile -Raw | ConvertFrom-Json
    if ($currentLog -is [System.Array]) {
        $userLog = [System.Collections.Generic.List[PSObject]]::new($currentLog)
    } else {
        $userLog = [System.Collections.Generic.List[PSObject]]::new()
    }

    $newEntry = [PSCustomObject]@{
        Date = $today
        Theme = $researchJson.theme
        Topic = $researchJson.topic
    }
    
    $userLog.Add($newEntry)
    $userLog | ConvertTo-Json -Depth 2 | Set-Content -Path $logFile -Encoding UTF8
    
    Write-Output "Daily Learning completed and saved to $dailyNotePath"

    # Send Discord Notification
    $pythonScript = "C:\Users\杢之助\2nd-Brain\00_システム\devtools\discord_notify.py"
    $notifyMessage = "✅ Daily Learning Completed! Theme: $($researchJson.theme) - Topic: $($researchJson.topic)"
    python $pythonScript $notifyMessage
    ```
