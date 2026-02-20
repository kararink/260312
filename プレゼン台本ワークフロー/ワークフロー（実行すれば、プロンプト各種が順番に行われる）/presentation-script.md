---
description: プレゼンテーション・フロントセミナーの台本とスライド生成プロンプトを、メソッドに基づいて自動生成するワークフロー。
---

# プレゼン台本生成ワークフロー (Presentation Script Factory)

メソッド（未来→問題→原因→解決ループ）を活用し、指定された分数に合わせたプレゼン台本 ＋ スライド生成プロンプトを一括出力します。

// turbo-all

## 入力受付

ユーザーから以下の情報を受け取ってください:

| 項目 | 必須 | 例 |
|------|------|-----|
| テーマ / トピック | ○ | 「Antigravityの教科書を売るフロントセミナー」 |
| 分数 | ○ | 10 / 30 / 60 / 90 |
| 教材データ（メンション） | △ | `@[ファイルパス]` で教材内容が添付される |

## Step 0: 文体コンテキスト取得 (Style Injection)

**このステップは全ての執筆ステップの前提となります。**

1. **文体コンテキスト取得**:
   - `python .agent/skills/ritsuto_writer/scripts/style_injector.py --topic "[入力テーマ]"` を実行
   - 出力された文体ルール（トーン、リズム、語彙、禁止ワードなど）を理解し、Step 3 の台本執筆に適用する

2. **メソッドリファレンス読み込み**:
   - `c:\Users\PC_User\product\Ritsuto_Brain\03_知識ベース\プロフェッショナルスピーカーのノウハウ\method_reference.md` を読み込む
   - 21の核心原則、MPCSループテンプレート、Few-shot を理解する

## Step 1: 戦略設計 (Strategy Design)

1. 以下のプロンプトを読み込んで実行してください。
   - `c:\Users\PC_User\product\Ritsuto_Brain\00_システム\01_Prompts\プレゼン台本ワークフロー\01_strategy_designer.md`
2. 戦略設計書を出力してください（テーマ定義、ペルソナ、エンロールクエスチョン、時間配分、MPCSループ設計）。
3. **ユーザーへの確認は行わず、戦略設計書を保持して Step 2 へ進んでください。**

## Step 2: 構成・シナリオ作成 (Scenario Building)

1. 以下のプロンプトを読み込んで実行してください。
   - `c:\Users\PC_User\product\Ritsuto_Brain\00_システム\01_Prompts\プレゼン台本ワークフロー\02_scenario_builder.md`
2. Step 1 の戦略設計書を入力として、セクション単位の詳細構成表を作成してください。
3. **構成表を保持して Step 3 へ進んでください。**

## Step 3: 台本執筆 (Script Writing)

1. 以下のプロンプトを読み込んで実行してください。
   - `c:\Users\PC_User\product\Ritsuto_Brain\00_システム\01_Prompts\プレゼン台本ワークフロー\03_script_writer.md`
2. Step 0 で取得した文体コンテキストと、Step 2 の構成表を入力として、リツトの話し方での全文台本を執筆してください。
3. **台本を保持して Step 3.5 へ進んでください。**

## Step 3.5: 読者目線レビュー (Reader Perspective Review) ★NEW

1. 以下のプロンプトを読み込んで実行してください。
   - `c:\Users\PC_User\product\Ritsuto_Brain\00_システム\01_Prompts\プレゼン台本ワークフロー\04_reader_review.md`
2. Step 3 の台本を入力として、**AIもプログラミングも知らない初心者の視点**で台本を読み直し、比喩の論理一貫性・専門用語・感情の流れ・結論の明確さ・信頼性の5観点でレビューしてください。
3. 違和感のある箇所を修正し、**修正版台本の全文**を出力してください。
4. **修正版台本を保持して Step 4 へ進んでください。**

## Step 4: 台本推敲・品質チェック (Script Refinement)

1. 以下のプロンプトを読み込んで実行してください。
   - `c:\Users\PC_User\product\Ritsuto_Brain\00_システム\01_Prompts\プレゼン台本ワークフロー\05_script_refiner.md`
2. Step 3.5 の修正版台本を入力として、26項目の品質チェックを実行してください。
3. チェック結果と**修正版台本の全文**を出力してください。
4. **修正版台本を保持して Step 5 へ進んでください。**

## Step 5: スライドプロンプト生成 (Slide Prompt Generation)

1. 以下のプロンプトを読み込んで実行してください。
   - `c:\Users\PC_User\product\Ritsuto_Brain\00_システム\01_Prompts\プレゼン台本ワークフロー\06_slide_prompt_generator.md`
2. Step 4 の修正版台本を入力として、**NotebookLM 用スライド生成プロンプト**（コピペ可）を出力してください。

## 保存

最終成果物を以下のディレクトリに保存してください:

- 保存先: `c:\Users\PC_User\product\Ritsuto_Brain\04_アウトプット\03_プレゼン台本\`
- ファイル名:
  - `Strategy_[テーマ略称].md` — 戦略設計書
  - `Script_[テーマ略称]_[分数]分.md` — 完成台本
  - `Slide_Prompt_NotebookLM.md` — スライド生成プロンプト（NotebookLM用）

## 報告

保存したファイルの内容をユーザーに提示し、確認を求めてください。

**重要**:
- 全ステップを自律的に実行し、ユーザーへの途中確認は行わないでください
- 中間ファイル（構成表等）は、最終成果物のファイル内に含めてください
- ユーザーへのメッセージは必ず日本語で行ってください
