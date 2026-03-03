---
name: blueprint-architect
description: Asks the user for ideas and automatically generates a perfect Markdown blueprint for Web Apps, AI Automations (prompt chains/workflows), or Agent Skills. Master architect that prevents reinventing the wheel and enforces MVP. Use when the user wants to create an app, tool, automation, or a new skill blueprint.
---

# Blueprint Architect（天才設計士）

ユーザーの「作りたいもの（アプリ、ツール、自動化ワークフロー等）」のアイデアから、エージェントが迷わず開発できる完璧な**プロ級の設計図（Markdownファイル）**を自動生成するスキルです。

## When to use this skill (使いどころ)
- **Situation**: 「設計図を書いて」「アプリを作りたい」「〇〇ツールを作りたい」「アーキテクト」などの依頼を受けた時
- **Situation**: ユーザーが何を作りたいかふわっとしているが、形にしたい時
- **Benefit**: 後から「Firebaseの無料枠を超えた」「セキュリティに欠陥があった」「APIキーが漏れた」等の手戻りや悲劇を事前に防ぐ、最強の設計図が手に入ります。

## Workflow Overview

詳細なステップ、鉄の掟（アーキテクチャ制約）、および分岐ロジックについては、必ず `resources/architect_guidelines.md` を読み込んでから実行してください。

### Execution Steps (Agent)
1. **Analyze**: ユーザーの要望を分析し、`resources/architect_guidelines.md` の **Step 1** の壁打ち（質問）を開始する。
2. **Refine**: ユーザーとやり取りし、MVPの選定と「鉄の掟（Firebase等）」の組み込みを確定させる。
3. **Generate**: 要望の種別（アプリ/自動化/新スキル）に応じた専用テンプレート（`blueprint_template.md`, `automation_template.md`, `skill_template.md` のいずれか）を読み込み、要件を埋め込んだMarkdownテキストを生成。
4. **Save & Report**: `write_to_file` で `00_[対象名]設計図.md` として保存し、「設計図を作成しました！この通りに進めてよろしいですか？」と報告する。

## Usage Instructions

### User Request Example
> 「文字起こしツールの設計図を作って」
> 「ブラウザで動くポモドーロタイマーを作りたいんだけど、アーキテクトお願い」
> 「設計図」
