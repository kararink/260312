# 🎨 プロンプトのコツ集

高品質な画像を生成するためのプロンプト構築ガイドです。

---

## 基本ルール

1. **英語で書く** — 現時点では英語プロンプトの方が品質が高い
2. **具体的に書く** — 「かっこいい画像」ではなく「何が、どこで、どう見えるか」を書く
3. **スタイルを指定する** — 「anime style」「cinematic」「watercolor」等
4. **照明を指定する** — 「golden hour」「neon lighting」「studio lighting」等

---

## 目的別テンプレート

### 📺 YouTubeサムネイル（16:9）

インパクトがあり、クリックしたくなるサムネを作るテンプレート:

```
Low angle shot, wide angle lens (16mm), dynamic composition.
[主題の描写].
Cinematic lighting, golden hour backlight, rim lighting.
Bold vibrant colors, high contrast, [スタイル] style.
YouTube thumbnail aesthetic, eye-catching, professional quality.
```

例:
```
Low angle shot, wide angle lens (16mm), dynamic composition.
A young Japanese man in a black happi coat, standing confidently
in front of glowing holographic AI interfaces.
Cinematic lighting, golden hour backlight, rim lighting.
Bold vibrant colors, high contrast, cyberpunk anime style.
YouTube thumbnail aesthetic, eye-catching, professional quality.
```

---

### 🐦 Xポスト画像（16:9 or 1:1）

スクロールを止めさせる「フック画像」のテンプレート:

```
[感情を引き起こすシーン].
[キャラクターの描写とアクション].
Dramatic lighting, [色のコントラスト指定].
Social media post style, high impact, attention-grabbing.
[スタイル] illustration.
```

例:
```
A person sitting at a desk late at night, surrounded by
floating screens showing code and AI interfaces.
The person has a look of determination, illuminated by
the blue glow of the screens.
Dramatic lighting, blue and orange color contrast.
Social media post style, high impact, attention-grabbing.
Anime production quality illustration.
```

---

### 📝 Note記事バナー（16:9）

整理された情報を伝えつつ、クリックを誘うバナー:

```
Japanese promotional banner design, 16:9 aspect ratio.
[テーマの描写].
Main title in very large bold golden Japanese characters
with metallic sheen: "[日本語タイトル]".
3D metallic chrome sheen, intense golden glow.
Premium information product aesthetic, [スタイル].
Cinematic lighting, floating particles.
```

例:
```
Japanese promotional banner design, 16:9 aspect ratio.
AI and technology theme with abstract neural network visualization.
Main title in very large bold golden Japanese characters
with metallic sheen: "AIで画像生成".
3D metallic chrome sheen, intense golden glow, sharp black outline.
Premium information product aesthetic, dark luxury background.
Cinematic lighting, floating particles, bokeh effect.
```

---

### 🎨 一般イラスト

6要素フレームワーク（この順番で書くと品質が安定します）:

```
[1. 主題] + [2. アクション] + [3. 場所・背景] +
[4. 照明] + [5. カメラ] + [6. スタイル]
```

例:
```
A cat wearing a tiny wizard hat,
casting a spell with sparkling particles from its paw,
in a cozy magical library filled with floating books,
warm candlelight with purple magical glow,
eye-level shot, medium close-up,
watercolor fantasy illustration style.
```

---

## アスペクト比の使い分け

| 比率 | 用途 | コマンド |
|:---|:---|:---|
| **16:9** | YouTubeサムネ / Xカード / Noteバナー | `--aspect_ratio 16:9` |
| **1:1** | Xポスト正方形 / プロフィール画像 | `--aspect_ratio 1:1` |
| **9:16** | スマホ壁紙 / ストーリー | `--aspect_ratio 9:16` |
| **3:4** | ポートレート / 書籍表紙 | `--aspect_ratio 3:4` |
| **4:3** | プレゼン資料 / ブログ記事 | `--aspect_ratio 4:3` |

---

## ❌ やってはいけないこと

### 1. キーワードの羅列
```
❌ cat, cute, beautiful, anime, colorful, HDR, 8K, masterpiece
✅ A cute orange tabby cat sitting on a windowsill, looking outside
   at a rainy day. Cozy warm lighting. Anime illustration style.
```

キーワードの羅列は品質が不安定になります。
**シーンを物語るように、文章で書く** のが正解です。

### 2. 背面ショット
```
❌ Over-the-shoulder looking back at the camera
```
背面から振り向くポーズは、首や体の歪みが頻発します。
キャラクターの全体像が必要なら **サイドプロフィール** を使ってください。

### 3. 曖昧な指示
```
❌ かっこいい画像を作って
✅ A samurai standing on a cliff at sunset, wind blowing through his hair,
   dramatic silhouette against orange sky, cinematic wide shot.
```

AIは「かっこいい」の定義を知りません。
**何が、どこで、どのように見えるか** を具体的に伝えましょう。

### 4. テキストの過信
日本語テキストは比較的うまくレンダリングされますが、
長い文章や複雑なレイアウトは崩れることがあります。

- **2〜4文字**: かなり正確
- **5〜10文字**: まあまあ
- **10文字以上**: 崩れやすい

バナー等でテキストが必要な場合は、
AIで画像を生成した後にCanva等で文字を載せるのも手です。
