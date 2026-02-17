---
name: ritsuto_writer
description: Injects Ritsuto's writing STYLE context (tone, rhythm, vocabulary) into the agent. Use when generating content "as Ritsuto". Structure/format is determined by workflows, not this skill.
---

# Ritsuto Writer Skill (Style Injector)

**リツトの「文体」を注入するスキル。**

このスキルは、リツトの価値観・トーン・語彙・縦のリズムといった「書き方のスタイル」をAIに注入します。
**「型（構造・フォーマット）」はワークフローが決定するため、このスキルでは扱いません。**

## 責務の分離

| レイヤー | 責務 |
|---|---|
| **このスキル** | 文体（トーン、リズム、禁止ワード、語彙） |
| **ワークフロー** | 型（構造テンプレート、媒体固有ルール） |

## When to Use (使いどころ)

- **Situation**: ワークフロー内で「リツトの文体で書く」必要がある時
- **Benefit**: 最新の価値観・スタイルガイドを自動注入し、文体の一貫性を保証

## Workflow

1.  **Load Style Context**:
    - Run the style injector script to retrieve Ritsuto's style context.
    - Command: `python .agent/skills/ritsuto_writer/scripts/style_injector.py --topic "Your Topic"`

2.  **Write with Style**:
    - The script outputs:
      - User Profile (Master Context, Core Values, Style Guidelines)
      - Style Examples (Few-shots for tone/rhythm mimicry)
      - Writing Task with the topic
    - **Apply these style rules when writing.** The structure/format comes from the workflow.

## Usage Example

**In a workflow** (e.g., `note-and-imagen.md`):

```markdown
1. **文体コンテキスト取得**:
   - `python .agent/skills/ritsuto_writer/scripts/style_injector.py --topic "[トピック]"` を実行
   - 出力された文体ルールを理解する

2. **型フューショット参照**:
   - `00_システム/01_Prompts/Note記事作成ワークフロー/few_shots/` 内の記事を参照
   - 構造とフォーマットを学習する

3. **執筆**:
   - 文体（スキルから）と型（フューショットから）を組み合わせて記事を執筆
```

## Files Loaded

The script automatically loads:
- `00_UserProfile/00_マスター(Master_Context).md`
- `00_UserProfile/01_価値観(Core_Values).md`
- `00_UserProfile/03_執筆スタイル(Style_Guidelines).md`
- `resources/style_examples/*.md` (縦のリズム、弱みの開示、感情表現の実例)

## Tips

- **Structure is NOT here**: If you need Note/X/Newsletter structure, refer to the workflow's `few_shots/` folder.
- **Single Source of Truth**: This skill pulls from `00_UserProfile`, so you always use the latest persona.
