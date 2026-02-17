---
description: Note記事や長文コンテンツを「工場生産ライン」のように高品質かつ効率的に作成するオーケストレーター・ワークフロー。
---

# Content Factory Orchestrator

**「Content Factory」**は、企画から執筆、推敲までを分業化・自動化し、高品質なNote記事やブログを量産するためのワークフローです。
各フェーズで専門家プロンプト（Architect, Writer, Editor）を呼び出し、あなたの「文体（my_writer）」を注入しながら進めます。

## Workflow Structure
各フェーズの指示に従い、順番に実行してください。

---

## Phase 1: Architecture (設計)

**Goal**: 読者を熱狂させる「コンセプト」と「構成案（Design）」の確定。

1.  **Call Architect**:
    - 以下のプロンプトを読み込み、対信形式で企画を固めてください。
    - Prompt: `00_システム/01_Prompts/ContentFactory/01_content_architect.md`
    - **Artifact**: `Content_Design.md` (設計図)

---

## Phase 2: Production (執筆)

**Goal**: 設計図に基づき、各パーツ（導入、本文）を執筆する。
**Important**: 各工程の前に、必ず `my_writer` スキルで最新の文体を注入すること。

1.  **Lead Writing (導入部)**:
    - **Style Injection**:
      - `python .agent/skills/my_writer/scripts/style_injector.py --topic "記事の導入"`
    - **Execution**:
      - Prompt: `00_システム/01_Prompts/ContentFactory/02_lead_writer.md`
      - Output: `00_Intro.md`

2.  **Body Writing (本文)**:
    - `Content_Design.md` の各セクション（Body 1, Body 2, Body 3...）ごとに以下を繰り返してください。
    - **Style Injection**:
      - `python .agent/skills/my_writer/scripts/style_injector.py --topic "[セクションのテーマ]"`
    - **Execution**:
      - 変数 `Target Section` と `Section Goal` を指定してプロンプトを実行。
      - Prompt: `00_システム/01_Prompts/ContentFactory/03_body_writer.md`
      - Output: `01_Body_1.md`, `02_Body_2.md` ...

---

## Phase 3: Quality Assurance (品質管理)

**Goal**: 全パーツを統合し、編集長視点で最終品質を担保する。

1.  **Call Editor in Chief**:
    - 全てのパーツ（Intro + Body files）をコンテキストに読み込んでから実行してください。
    - Prompt: `00_システム/01_Prompts/ContentFactory/04_editor_qa.md`
    - Output: `Final_Draft.md`, `Quality_Report.md`

---

## Tips
- **文体のブレ**: もし出力された文章が自分らしくないと感じたら、`style_injector.py` のトピックをより具体的に書き換えて再実行してください。
- **柔軟性**: `01_content_architect.md` で作成した構成案は絶対ではありません。執筆中に「こっちの方が面白い」と思ったら、柔軟に変更してください。
