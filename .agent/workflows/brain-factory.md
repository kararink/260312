---
description: Brain教材制作の全工程（設計・集客・執筆・仕上げ）を、専門家プロンプトを指揮して完遂するオーケストレーター・ワークフロー。
---

# Brain Factory Orchestrator

Brain教材制作を工場生産ラインのように管理するオーケストレーターです。
各フェーズごとに、成功法則（Success Principles）を学習済みの「専門家プロンプト（Specialist Prompt）」を呼び出し、高品質なアウトプットを保証します。

## Workflow Structure
各フェーズで、対応するプロンプトファイルを読み込み、実行させてください。

---

## Phase 1: Architecture (建築)

**Goal**: コンセプト、ターゲット、タイトル、目次（Roadmap）の確定。

1.  **Call Architect**:
    - 以下のプロンプトを読み込み、ユーザーと対話しながら企画を固めてください。
    - Prompt: `c:\Users\杢之助\2nd-Brain\00_システム\01_Prompts\BrainFactory\01_concept_architect.md`
    - **Artifact**: `Brain_Concept.md`（またはチャットログでの合意）

---

## Phase 2: Marketing (集客)

**Goal**: 読者を惹きつける「無料プレビュー（LP）」の作成。

1.  **Call Copywriter**:
    - 以下のプロンプトを読み込み、LPを執筆させてください。
    - Prompt: `c:\Users\杢之助\2nd-Brain\00_システム\01_Prompts\BrainFactory\02_lp_writer.md`
    - **Artifact**: `00_FreePreview.md`

---

## Phase 3: Production (量産)

**Goal**: 目次に沿ったコンテンツ（全章）の執筆。

1.  **Prologue**:
    - Prompt: `c:\Users\杢之助\2nd-Brain\00_システム\01_Prompts\BrainFactory\03_prologue_writer.md`
    - Output: `01_Prologue.md`

2.  **Chapter Loop**:
    - 目次にある各章（Day 1, Day 2...）に対して、以下の手順を繰り返してください。
    - **Step A**: 以下のプロンプトを読み込み、執筆を実行。
        - Prompt: `c:\Users\杢之助\2nd-Brain\00_システム\01_Prompts\BrainFactory\04_chapter_writer.md`
        - Variable: `Topic` = 章のテーマ, `Goal` = 章のゴール
    - Output: `02_Day1.md`, `03_Day2.md` ...

---

## Phase 4: Closing (仕上げ)

**Goal**: エピローグと特典案内によるLTV向上。

1.  **Call Closer**:
    - 以下のプロンプトを読み込み、感動的な締めくくりと特典案内を作成してください。
    - Prompt: `c:\Users\杢之助\2nd-Brain\00_システム\01_Prompts\BrainFactory\05_epilogue_writer.md`
    - Output: `Final_Epilogue.md`, `Bonus_Offer.md`

    - 全体の整合性を確認し、完了宣言を行ってください。

---

## Phase 5: Quality Assurance (品質保証)

**Goal**: コンテンツの抜け漏れがないか、設計図と照らし合わせて最終監査を行う。

1.  **Call CQO (Chief Quality Officer)**:
    - 以下のプロンプトを読み込み、作成した全ファイルと設計図を照合させてください。
    - **重要**: ここで「FAIL」が出た場合、必ず修正を行ってからリリースしてください。
    - Prompt: `c:\Users\杢之助\2nd-Brain\00_システム\01_Prompts\BrainFactory\06_consistency_checker.md`
    - Output: `Quality_Report.md`
