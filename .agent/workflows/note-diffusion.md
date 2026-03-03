---
description: /note-diffusion - マスターワークフロー。PDF（またはテキスト）を起点に、Note記事、Sunoプロンプト、SNS拡散文（X, FB, IG）を一括生成します。
---

# Note記事完全自動化（SNS拡散）ワークフロー (Master Controller)

このワークフローは、入力ソース（PDFの中身やテキスト）から、Note記事とその拡散用コンテンツを一気通貫で生成します。

**各フェーズで必ず中間ファイルを確認し、ステップをスキップせずに順次実行してください。抽象的な指示ではなく、以下の具体的なプロンプトファイルを必ず読み込んで実行してください。**

## Phase 1: 入力ソースの確定 (Input)
1. **ソースの指定**: ユーザーが入力ファイル（スキャンしたPDFのテキストやマークダウンファイル）を指定した場合。
   - Target: そのファイルを `TARGET_SOURCE` とする。

## Phase 2: コアテーマの抽出 (Extraction)
1. **抽出実行**
   - Tool: `read_file` -> `.\00_システム\01_Prompts\Note拡散ワークフロー\1_Note拡散_抽出プロンプト.md`
   - Action: プロンプトを実行し、`TARGET_SOURCE` から重要なインサイト（骨子）を抽出。
   - Output: `.\04_アウトプット\NoteDiffusion_Extraction.md`

## Phase 3: コンテンツ一括生成 (Generation)
1. **一括生成実行**
   - Tool: `read_file` -> `.\00_システム\01_Prompts\Note拡散ワークフロー\2_Note拡散_生成プロンプト.md`
   - Action: Phase 2で抽出した骨子（`EXTRACTION_RESULT`）と `TARGET_SOURCE` を入力としてプロンプトを実行し、5つのコンテンツを一気に生成。
   - Output: `.\04_アウトプット\NoteDiffusion_Draft.md`

## Phase 4: 品質チェックと推敲 (Review & Refine)
1. **推敲**
   - Action: 生成された `NoteDiffusion_Draft.md` の内容全体（Note記事のトーン＆マナー、SNSの誘導リンク枠が正しく入っているか等）をAI自身で確認し、微調整を行う。
   - Output: `.\04_アウトプット\NoteDiffusion_Refined.md`

## Phase 5: 画像生成と落款印（キャラクター）の合成 (Image & Stamp)
1. **Note見出し画像の生成**
   - Tool: `generate_image`
   - Action: Phase 3で出力された「見出し画像生成用プロンプト」を使用して画像を生成する。
   - Output: `.\04_アウトプット\04_Note画像\NoteDiffusion_BaseImage.png` （またはjpg等）
2. **スタンプ（落款印）の合成**
   - Tool: `run_command`
   - Action: 以下のコマンドを実行し、生成した見出し画像にキャラクタースタンプをランダムに合成する。
     ```powershell
     python .\00_システム\devtools\add_stamp.py ".\04_アウトプット\04_Note画像\NoteDiffusion_BaseImage.png" ".\04_アウトプット\04_Note画像\NoteDiffusion_StampedImage.png"
     ```
   - Output: スタンプ合成済みの見出し画像 `NoteDiffusion_StampedImage.png`
3. **Instagram用画像の生成（3枚）**
   - Tool: `generate_image` (3回実行)
   - Action: Phase 3で出力されたInstagram用画像指示書（1〜3枚目）をもとに、各スライド画像を生成する。
   - **命名規則**: `NoteDiffusion_[YYYYMMDD]_IG_01.png`, `_IG_02.png`, `_IG_03.png`
   - **Output先**: `.\04_アウトプット\05_Instagram\`
   - 生成後、`.\04_アウトプット\05_Instagram\NoteDiffusion_[YYYYMMDD]_Instagram.md` にインデックスファイルを作成し、各画像への参照と再生成用プロンプトを記録する。

## Phase 6: ユーザーへの引き渡し (Finalize)
1. **最終確認・アウトプット格納**
   - Action: `NoteDiffusion_Refined.md` の冒頭（タイトルの下）に、Markdown形式でスタンプ合成画像を挿入する。
     `![見出し画像](../04_Note画像/NoteDiffusion_StampedImage.png)`
   - Action: 【5】Instagram用セクションに、生成した画像への参照を挿入する。
     `![1枚目](../05_Instagram/NoteDiffusion_[YYYYMMDD]_IG_01.png)` 等
   - **Move to Output**: 最終稿を `.\04_アウトプット\03_Note\NoteDiffusion_[YYYYMMDD]_Final.md` に移動/保存。
   - ユーザーに「出力が完了しました。Noteへの投稿と、各SNSへの拡散準備が整っています。」と報告。
2. **中間ファイルの削除 (必須)**
   - **Command**: `Remove-Item` または `del` を使用。
   - **Delete Targets**: `.\04_アウトプット\NoteDiffusion_Extraction.md` および `.\04_アウトプット\NoteDiffusion_Draft.md`
   - **Verify**: `04_アウトプット` 直下に中間ファイルが残っていないことを確認。

---
**使用方法**:
「/note-diffusion [ファイルパス]」
**AIへの指示**: 各ステップでツールを実行するたびに、必ず `task_boundary` を更新し、進捗を明示すること。勝手に文章を作成せず、必ず指定されたプロンプトファイルの内容に従うこと。
