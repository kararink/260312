---
title: "GoogleAppsScript(GAS)って何？｜むなかた AI×Web3エンジニア"
source: "https://note.com/munakata_souri/n/n34eae854320f"
author:
  - "[[むなかた AI×Web3エンジニア]]"
published: 2026-01-06
created: 2026-02-03
description: "こんにちは。今回はぼくがAIプログラミング入門者に激推しさせていただいている、「GAS（ガス）」について紹介をさせていただきます！  今回の記事では「GASとはどんなものでどんなことができるか」について解説していますが、具体的な操作方法が知りたい、という方はこちらの記事もぜひご覧になってくださいね。  GoogleAppsScript（GAS）とは  GoogleAppsScriptとは、Googleサービスをプログラム経由で操作できる仕組みで、頭文字を取って 「GAS（ガス）」 と呼ばれます。  GASにはこのような特徴があり、開発初心者に非常に優しい仕組みとなっています。"
tags:
  - "clippings"
---
[

投稿

](https://note.com/signup)

[

ログイン

](https://note.com/login?redirectPath=https%3A%2F%2Fnote.com%2Fmunakata_souri%2Fn%2Fn34eae854320f)

[

会員登録

](https://note.com/signup)

![見出し画像](https://assets.st-note.com/production/uploads/images/241854464/rectangle_large_type_2_5737f5e838edc1bc7595a25a5e4ba939.png?width=1280)

# GoogleAppsScript(GAS)って何？

[![むなかた AI×Web3エンジニア](https://assets.st-note.com/production/uploads/images/193696386/profile_14da9b7986bc45201f2141c017ff6778.png?width=60)](https://note.com/munakata_souri)

[むなかた AI×Web3エンジニア](https://note.com/munakata_souri)

2026年1月6日 20:22

##   

## 目次

1. 
2. 
3. 
4. 
5. 
6. 
7. 
8. 
9. 
10.

こんにちは。今回はぼくがAIプログラミング入門者に激推しさせていただいている、「GAS（ガス）」について紹介をさせていただきます！

今回の記事では「GASとはどんなものでどんなことができるか」について解説していますが、具体的な操作方法が知りたい、という方はこちらの記事もぜひご覧になってくださいね。

<iframe class="note-embed" scrolling="no" style="border: 0px; display: block; max-width: 99%; width: 494px; padding: 0px; margin: 10px 0px; position: static; visibility: visible;" loading="lazy" data-src="https://note.com/embed/notes/n6cc6c3d5c17f" src="https://note.com/embed/notes/n6cc6c3d5c17f" height="233px" data-ready="true"></iframe>## GoogleAppsScript（GAS）とは

GoogleAppsScriptとは、**Googleサービスをプログラム経由で操作できる仕組み**で、頭文字を取って **「GAS（ガス）」** と呼ばれます。

GASにはこのような特徴があり、開発初心者に非常に優しい仕組みとなっています。

- Googleアカウントがあれば**無料**で使える
- **環境構築が一切不要**でハードルが低い
- サーバなどを自分で準備する必要がない
- 便利なGoogleサービスをプログラム経由でもっと便利に使える
![画像](https://assets.st-note.com/img/1767698468-v5q9pfEykc80sMgNwL3RnWHU.png?width=1200)

## 開発初心者がGASを使うべき理由

### 1\. ハードルがとにかく低い

プログラミングを始めるときには、ツールのインストールやサービスの登録など、事前準備が必要なものが多いです。

GASはGoogleアカウントさえあれば無料で使うことができ、操作するのはすべてWebページ上となるため**事前準備が一切不要**で始めることができます。

### 2\. AIが大量に学習済み

GASは実は15年以上前から存在している仕組みのため、すでにAIがGASのプログラムの書き方や設定手順を大量に学習しています。

AIにお願いするときにも正式名称ではなく「**●●するプログラムをGASで作って**」のように言ってあげるだけで、「GAS = GoogleAppsScipt」ということを理解してコードを作ってくれるので、非常にやり取りがスムーズです。

### 3\. 実用性が高い

GASで操作できるサービスはGmailやスプレッドシート、Googleフォームといった普段の生活でお世話になっているサービスばかりです。

これらのサービスをプログラムから操作できるようになるだけで

- スプレッドシートにニュースを自動集約
- Googleカレンダーの予定を自動登録
- Googleフォームを自在に作成
- 条件を満たしたらメールを自動送信

といったことができるようになり、何かしら普段の作業で必ず役に立つ場面が出てきます！

## GASプロジェクトの作成方法

### 1\. ファイルを直接作成（スタンドアロン）

1つ目はGoogleドライブ上から直接作成する方法です。

右クリック or 左上の「新規」ボタンを押した後に、「その他」>「Google Apps Script」から作成することが可能です。

![画像](https://assets.st-note.com/img/1767697313-aVcbN43DQTy2jPmGeLnRrl6h.png?width=1200)

### 2\. Googleサービス内メニューから作成（コンテナバインド）

2つ目はスプレッドシートやGoogleフォームなどのサービス内のメニューから作成する方法です。

プロジェクトを作った時点でサービスと紐づいているので、サービスの操作が簡単にできるようになります。

**スプレッドシートの場合**

![画像](https://assets.st-note.com/img/1767697382-utSYojn2lqUsDh8B3MWpaI1V.png?width=1200)

**Googleフォームの場合**

![画像](https://assets.st-note.com/img/1767697368-ERKcDuqSjC4Z61yfdotxVpek.png?width=1200)

> サービスによって微妙に呼び出し場所が違うので注意しましょう。

## GASの特徴

### GASで操作できるサービス

GASではGoogleが提供しているサービスをプログラム経由で操作することが出来ますが、おそらくどれかひとつは使ったことがあるのではないでしょうか！

- Googleフォーム
- Googleカレンダー
- Googleドライブ
- Googleスライド
- Gmail
- スプレッドシート
- Googleマップ

### トリガー

GASの機能で特に便利なのが「トリガー」です。これは、**特定の条件を満たしたとき**にGASのプログラムを**自動で起動する**仕組みです。

- Googleフォームに回答があったら実行
- 毎日12時になったら実行
- スプレッドシートが編集されたら実行　などなど

一見そこまですごくなさそうに見えるのですが、作業の自動化・効率化を実現するためにとても便利な仕組みなので、ぜひ試してみてください！

### 実行上限

GASは無料で使えるのがメリットなのですが、**操作の種類ごとに回数の上限**が設けられているのでそこだけ注意しましょう。

特にメール送信回数や、トリガーの1回あたりの実行時間の上限が引っかかりやすいので要注意です。

ちなみに、無料で作成できるGoogleアカウントよりも、ビジネス用の**有料のGoogle Workspaceアカウントの方が上限がゆるめ**に設定されています。

**代表的な上限**

![画像](https://assets.st-note.com/img/1767698065-2pyZd4I3hrYqUgtK8Q5fVo0x.png?width=1200)

▼上限のリストはこちらから確認できます  
[https://developers.google.com/apps-script/guides/services/quotas?utm\_source=chatgpt.com&hl=ja](https://developers.google.com/apps-script/guides/services/quotas?utm_source=chatgpt.com&hl=ja)

---

いかがでしたでしょうか？

この説明だけだとイマイチ何がすごいのかが伝わりにくいと思うので、よろしければ実用編の記事もお読みくださいね！

<iframe class="note-embed" scrolling="no" style="border: 0px; display: block; max-width: 99%; width: 494px; padding: 0px; margin: 10px 0px; position: static; visibility: visible;" loading="lazy" data-src="https://note.com/embed/notes/n6cc6c3d5c17f" src="https://note.com/embed/notes/n6cc6c3d5c17f" height="233px" data-ready="true"></iframe>  

  

  

###   

## いいなと思ったら応援しよう！

- [
	#初心者
	](https://note.com/hashtag/%E5%88%9D%E5%BF%83%E8%80%85)
- [
	#GAS
	](https://note.com/hashtag/GAS)
- [
	#GoogleAppsScript
	](https://note.com/hashtag/GoogleAppsScript)
- [
	#AIプログラミング
	](https://note.com/hashtag/AI%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0)

[![むなかた AI×Web3エンジニア](https://assets.st-note.com/production/uploads/images/193696386/profile_14da9b7986bc45201f2141c017ff6778.png?width=80&height=80&dpr=2&crop=1:1,smart)](https://note.com/munakata_souri)

[むなかた AI×Web3エンジニア](https://note.com/munakata_souri)

▼ 自己紹介note [https://note.com/munakata\_souri/n/n919513d0bde8](https://note.com/munakata_souri/n/n919513d0bde8) ✅️ 毎日音声配信 ✅️ Discordコミュニティ紹介 ✅️ Udemy講座（割引リンクあり）

- - ## 人気記事### 【2025年7月最新版】ClaudeCodeをWindowsPCで動かすための完全マニュアル

71

![](https://assets.st-note.com/production/uploads/images/202240030/square_middle_b59a63be19446ef1b7510cd6780329d0.png?width=80&height=56&fit=crop&dpr=2&frame=1)### 【中・上級者向け】 Codexで始めるAIプログラミング〜Codex CLI編〜

28

![](https://assets.st-note.com/production/uploads/images/215702329/square_middle_b20c401f1ac49a42a3a35a4a467814ca.png?width=80&height=56&fit=crop&dpr=2&frame=1)### AIで作成したプログラムを公開するために必須の「Git」と「GitHub」の解説とインストール手順

159

![](https://assets.st-note.com/production/uploads/images/199150604/square_middle_50c2f02e6fbcd485e08a7251f5c6ea01.png?width=80&height=56&fit=crop&dpr=2&frame=1)

[もっとみる](https://note.com/munakata_souri?sort=popular)

[

前の記事

【無料でAIプログラミング入門!!】Antigravityの使い方をできるだけやさしく紹介

](https://note.com/munakata_souri/n/nb7e6c3ea605e)

[

次の記事

【初心者でもできる】 Googleフォームをプログラムに作らせてみよう

](https://note.com/munakata_souri/n/n6cc6c3d5c17f)

## コメント

コメントするには、 [ログイン](https://note.com/login?redirectPath=%2Fmunakata_souri%2Fn%2Fn34eae854320f) または [会員登録](https://note.com/signup?redirectPath=%2Fmunakata_souri%2Fn%2Fn34eae854320f) をお願いします。

## こちらもおすすめ

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)

![](https://note.com/munakata_souri/n/)![](https://assets.st-note.com/production/uploads/images/244423776/rectangle_large_type_2_ccc4ef48da5fbf4d5ecfe96d0050fc57.png?width=302&dpr=2&frame=1&format=jpg)

### 「GASって結局、何ができるの？」がわかる10の活用例と自動化のはじめ方

 [![](https://assets.st-note.com/production/uploads/images/243902165/profile_bec79f5d1a9be0e5f2b173a0a19045db.png?width=18&dpr=2) くろぬこ。｜世の中の「めんどうくさい」をAIと仕組みで減らす人｜123 design works](https://note.com/123designworks)

2週間前

2![](https://assets.st-note.com/production/uploads/images/238907147/rectangle_large_type_2_513ad8c9a8b7ba89c387696876785ea6.png?width=302&dpr=2&frame=1&format=jpg)

### 【保存版】コピペでOK！スプレッドシートGAS「超」入門。まずはこの7つだけで業務は変わる

 [![](https://d2l930y2yx77uc.cloudfront.net/assets/default/default_profile_5-043439195e40e86fd7641a3a1daf982637d77ec6f14b67d3fc98ab92374404ac.png?width=18&dpr=2) もにか](https://note.com/monika_dev)

1か月前を使ってみよう")

![](https://assets.st-note.com/production/uploads/images/240819359/rectangle_large_type_2_79f8707b45c0371f9b5a382e1fd59a03.png?width=302&dpr=2&frame=1&format=jpg)

### GAS(Google Apps Script)を使ってみよう

 [![](https://note.com/munakata_souri/n/) K先生 ＠AI業務改善](https://note.com/cozy_echium728)

1か月前

2を学ぶためにおすすめの本/書籍7選")

![](https://assets.st-note.com/production/uploads/images/243294017/rectangle_large_type_2_99590207c6ec8ff0207a36866355541a.png?width=302&dpr=2&frame=1&format=jpg)

### GAS(Google Apps Script)を学ぶためにおすすめの本/書籍7選

 [![](https://note.com/munakata_souri/n/) EducDrawer](https://note.com/educdrawer)

2週間前

25![](https://assets.st-note.com/production/uploads/images/245769200/rectangle_large_type_2_b8352dccfa0b3dbedff3dc78f660f88e.png?width=302&dpr=2&frame=1&format=jpg)

### GASのチャレンジ実録　個別差し込みメール一括送信

¥1,980

 [![](https://note.com/munakata_souri/n/) さな＠AI活用で副業から在宅ワークを実現](https://note.com/hip_oriole1535)

11日前

2![](https://note.com/munakata_souri/n/)

### Googleフォームに回答が来たら、下書きのメールを自動で送る方法

 [![](https://note.com/munakata_souri/n/) みっちゃんのSuisochaと幸福道](https://note.com/suisocha)

5日前

1![](https://assets.st-note.com/production/uploads/images/240025060/rectangle_large_type_2_71522962b769f571844d07d2fe554e55.jpeg?width=302&dpr=2&frame=1&format=jpg)

### Excelマクロより100倍楽。Google Apps Script × AIで業務自動化

 [![](https://note.com/munakata_souri/n/) てんちょー | 非エンジニアがAI開発で週末起業を爆速化](https://note.com/questceo_ai)

4週間前

4![](https://assets.st-note.com/production/uploads/images/246251238/rectangle_large_type_2_56a845e5491c2daef653618789ab0ea6.png?width=302&dpr=2&frame=1&format=jpg)

### UI/UXを最低限意識したWebアプリをGoogleアカウントだけで作る

 [![](https://note.com/munakata_souri/n/) 灯里/郁](https://note.com/akari_iku)

9日前

6![](https://assets.st-note.com/production/uploads/images/243536692/rectangle_large_type_2_cd7afec51ec909bea36bab267d463db4.png?width=302&dpr=2&frame=1&format=jpg)

### プログラミング知識ゼロでOK！AIに「魔法のボタン」を作らせて仕事を自動化するコツ

 [![](https://note.com/munakata_souri/n/) 色鉛筆｜非エンジニアのひとりAI推進室](https://note.com/giovanniai)

2週間前

1![](https://assets.st-note.com/production/uploads/images/240437226/rectangle_large_type_2_3d22ac7b2e15e28b77dccbd970d368ae.png?width=302&dpr=2&frame=1&format=jpg)

### 【AI学習記】「まだCanvasからコピペしてるの？」Claude CodeでGAS開発を劇的に変えてみた件

 [![](https://note.com/munakata_souri/n/) おかかき](https://note.com/gay_orchid5021)

1か月前

5![](https://assets.st-note.com/production/uploads/images/248030629/rectangle_large_type_2_a5148f210b981a59ebf049514a7e6e07.png?width=302&dpr=2&frame=1&format=jpg)

### 「まだ手作業してる？」Googleの無料ツールだけで作る、寝ている間に仕事が片付く"自分専用AI"の作り方

 [![](https://note.com/munakata_souri/n/) ずんだもんAI](https://note.com/zunda_ai)

2日前

1![](https://assets.st-note.com/production/uploads/images/247695823/rectangle_large_type_2_c9662b7833bfd8d4266b91ea1c63a481.jpg?width=302&dpr=2&frame=1&format=jpg)

### 【30分で完成】Googleカレンダーの記録を「ボタン一発」でスプレッドシートに出力する魔法のスイッチを作ってみた

 [![](https://note.com/munakata_souri/n/) DGFL＠K-PaPa](https://note.com/dgfl)

4日前

7![](https://assets.st-note.com/img/1768815764-QnTxlmB3iCAHpsFaKh6vNeO8.png?width=302&dpr=2&frame=1&format=jpg)

### GAS開発を楽にする方法「clasp × AIエージェント」

 [![](https://note.com/munakata_souri/n/) HIRO\_英語とAIとライフハック](https://note.com/kiyohiro0728)

2週間前

2![](https://assets.st-note.com/production/uploads/images/241288640/rectangle_large_type_2_ca1fd247deefa7bfb796c8bc7115417e.png?width=302&dpr=2&frame=1&format=jpg)

### 【GAS超入門】Geminiに聞いたら一瞬でできた！Googleカレンダーの予定をスプレッドシートに自動抽出する方法

 [![](https://note.com/munakata_souri/n/) 石原愛信 │ 石川県金沢市のDX講座・研修 生成AI ChatGPT セミナー講師](https://note.com/solobizjourney)

1か月前

59![](https://assets.st-note.com/production/uploads/images/243268304/rectangle_large_type_2_a9e643101f7deebe3546473278b9f68b.png?width=302&dpr=2&frame=1&format=jpg)

### clasp×Antigravity で楽々GAS開発

 [![](https://note.com/munakata_souri/n/) 御手洗梢](https://note.com/witty_roses242)

3週間前

10![](https://assets.st-note.com/production/uploads/images/248078713/rectangle_large_type_2_35f3a1c98aa1865ada06e601ba86496a.png?width=302&dpr=2&frame=1&format=jpg)

### 【実践】AI連携実践④：スプレッドシートが「AIチャット」になる！自動回答ツールの作成【学習132日目】

 [![](https://note.com/munakata_souri/n/) やぎ](https://note.com/bunkei_yagi_ai01)

2日前

1![](https://assets.st-note.com/production/uploads/images/238635206/rectangle_large_type_2_23624ab2bc211d01c5ddcd0ea0a5b527.png?width=302&dpr=2&frame=1&format=jpg)

### 教員のためのGAS入門②　GASの基本的な書き方

 [![](https://note.com/munakata_souri/n/) 佐良土　賢樹](https://note.com/fifthstage)

1か月前

13![](https://assets.st-note.com/production/uploads/images/247434027/rectangle_large_type_2_351d2d4276a221edc4d7ea5b8f5ee035.png?width=302&dpr=2&frame=1&format=jpg)

### gog入門：Google Workspaceを完全制御するCLIツールの決定版

 [![](https://note.com/munakata_souri/n/) アイドリ | AI-Driven Lab](https://note.com/ai_driven)

5日前

3![](https://assets.st-note.com/production/uploads/images/245474610/rectangle_large_type_2_2bcc7fa54ed247f6f846c7637c856ae5.png?width=302&dpr=2&frame=1&format=jpg)

### 【コピペでOK】GASとGemini APIで、画像も理解する「自分専用AIアシスタント」をLINEに作る

 [![](https://note.com/munakata_souri/n/) だいあろごす。](https://note.com/dialogs_develop)

13日前

25![](https://assets.st-note.com/production/uploads/images/243570305/rectangle_large_type_2_13e9918763329753fde888e6df33be5a.png?width=302&dpr=2&frame=1&format=jpg)

### 【2026年最新版】AIでスプレッドシートの自動化を「5秒」で実現する方法

 [![](https://note.com/munakata_souri/n/) かわさき楽AIサポート【公式note】](https://note.com/arukuwa)

2週間前

1![](https://assets.st-note.com/production/uploads/images/248249868/rectangle_large_type_2_49cacc093467f667e88504c4622cd7a4.png?width=302&dpr=2&frame=1&format=jpg)

### エージェントマネージャーでGAS開発環境をセットアップし、サンプルアプリをプッシュ・デプロイするまでの流れ｜バイブコーディング｜Google AntiGravity

 [![](https://note.com/munakata_souri/n/) 岩崎修｜SIMONE INC.](https://note.com/_osamu_iwasaki_)

3週間前

3![](https://assets.st-note.com/production/uploads/images/242607050/rectangle_large_type_2_3f7987f227afdb1680f6b300cfa1a38e.png?width=302&dpr=2&frame=1&format=jpg)

### GASで「自動メール送信」スクリプトを作るAIプロンプト

¥200

 [![](https://note.com/munakata_souri/n/) 東雲ミナト](https://note.com/minato_shinonome)

2週間前![](https://assets.st-note.com/production/uploads/images/241114402/rectangle_large_type_2_5f6ab5582f789486d07cd5cf43636498.png?width=302&dpr=2&frame=1&format=jpg)

### 【完全保存版💥】「コードが書ける」は最強の武器になる。非IT職のためのプログラミング超入門

¥1,980

 [![](https://note.com/munakata_souri/n/) こうじ](https://note.com/glad_avocet314)

1か月前

7![](https://assets.st-note.com/production/uploads/images/245233667/rectangle_large_type_2_347183492972431b82bccc6a13b794a3.png?width=302&dpr=2&frame=1&format=jpg)

### GASとAIで月10万円の副業を実現する自動化システム構築法

 [![](https://note.com/munakata_souri/n/) ロボくま｜AIで「何もしない」副業](https://note.com/robokuma1234)

2週間前

6![](https://assets.st-note.com/production/uploads/images/245780099/rectangle_large_type_2_45383586936d6ba9210259b3a3079dc3.jpeg?width=302&dpr=2&frame=1&format=jpg)

### 【初心者必見】０からわかるAntigravity

 [![](https://note.com/munakata_souri/n/) データ分析｜コピペで動くAIアプリ｜\[ゆき\]](https://note.com/jazzy_orchid7415)

12日前

12![](https://assets.st-note.com/production/uploads/images/248385587/rectangle_large_type_2_6c734cd25fb1cbecddea9a584599850e.png?width=302&dpr=2&frame=1&format=jpg)

### 無駄な時間を削減！YouTube動画管理アプリを作ろう！

 [![](https://note.com/munakata_souri/n/) あーさ](https://note.com/a_sa_note)

1日前![](https://assets.st-note.com/production/uploads/images/248688627/rectangle_large_type_2_252008462cd2dde3467236d6a7c063eb.png?width=302&dpr=2&frame=1&format=jpg)

### 在宅で時給が高い仕事を探してたら、GASにたどり着いた話

 [![](https://note.com/munakata_souri/n/) 村井いと](https://note.com/irodori_8_)

13日前

6![](https://assets.st-note.com/production/uploads/images/240511100/rectangle_large_type_2_897e87c7941045d878a7e8d1337a250c.jpeg?width=302&dpr=2&frame=1&format=jpg)

### GASで作る「LINE自動返信」

 [![](https://note.com/munakata_souri/n/) 1daylesson](https://note.com/1daylesson)

1か月前![](https://assets.st-note.com/production/uploads/images/238060919/rectangle_large_type_2_306101070347f3b1fe0f4adfc271f544.png?width=302&dpr=2&frame=1&format=jpg)

### Gasって何？中小不動産屋が最初に誤解する話（第1話）

 [![](https://note.com/munakata_souri/n/) 田辺領平｜不動産エンジニア（現役の不動産屋 + AI活用）](https://note.com/gakumon88)

1か月前

1![](https://assets.st-note.com/production/uploads/images/247285855/rectangle_large_type_2_2ac943585a5c0e8202f9b5a014ed1e8f.jpeg?width=302&dpr=2&frame=1&format=jpg)

### 面倒な確定申告、自動化しませんか？

¥0〜

割引あり

 [![](https://note.com/munakata_souri/n/) ボイストレーナーみか](https://note.com/micarp)

5日前

3![](https://assets.st-note.com/production/uploads/images/246935574/rectangle_large_type_2_f6304d1fd254915d17c69a7551e890b5.jpg?width=302&dpr=2&frame=1&format=jpg)

### それは絶対ではない

 [![](https://note.com/munakata_souri/n/) 本邑 柊彩（もとむら ひいろ）](https://note.com/namake_naru)

7日前

4![](https://assets.st-note.com/production/uploads/images/240873697/rectangle_large_type_2_40139e8dd7492b88cd830d8ea6ba6c85.png?width=302&dpr=2&frame=1&format=jpg)

### Amazon運用を効率化するために、Google Apps Scriptで仕組み化する　―― ツールに頼りきらない分析と自動化の第一歩

 [![](https://note.com/munakata_souri/n/) アイムバディ｜ EC運用の実験室](https://note.com/9499oyama)

1か月前

3![](https://assets.st-note.com/production/uploads/images/242322117/rectangle_large_type_2_715ed90b0b544d1e97e560e842bf81a9.png?width=302&dpr=2&frame=1&format=jpg)

### 文系でもGoogle WorkspaceだけでWebアプリを作れる：現実的な方法

 [![](https://note.com/munakata_souri/n/) 平山秀樹](https://note.com/hidekihirayama)

3週間前

27![](https://assets.st-note.com/production/uploads/images/248283489/rectangle_large_type_2_cc1a37a84f4f9154fbb9885fbce73742.png?width=302&dpr=2&frame=1&format=jpg)

### 【2026年版】Google Antigravityって何ができるの？初心者でもわかる使い方と実例ガイド

 [![](https://note.com/munakata_souri/n/) 倖狼(ころう)キリ🐺🌸✨Vtuber](https://note.com/kiri_korou)

2日前

1![](https://assets.st-note.com/production/uploads/images/246631855/rectangle_large_type_2_5df617248fd2a79920e41e8f87dc86e0.png?width=302&dpr=2&frame=1&format=jpg)

### 🟪今すぐ始めよう→グーグルスキルのすすめ

 [![](https://note.com/munakata_souri/n/) 杉にい (Sugi Nii)](https://note.com/noble_sloth4123)

8日前

8![](https://assets.st-note.com/production/uploads/images/206406275/rectangle_large_type_2_a2c51da2d62e2538f324ad99a1d5131b.png?width=302&dpr=2&frame=1&format=jpg)

### 名刺に「E-mail」の表記は不要かも…という話

 [![](https://note.com/munakata_souri/n/) 鷹野 雅弘](https://note.com/swwwitch)

6か月前

129

[![むなかた AI×Web3エンジニア](https://assets.st-note.com/production/uploads/images/193696386/profile_14da9b7986bc45201f2141c017ff6778.png?fit=bounds&format=jpeg&quality=85&width=330)](https://note.com/munakata_souri) [むなかた AI×Web3エンジニア](https://note.com/munakata_souri "むなかた AI×Web3エンジニア")

▼ 自己紹介note [https://note.com/munakata\_souri/n/n919513d0bde8](https://note.com/munakata_souri/n/n919513d0bde8) ✅️ 毎日音声配信 ✅️ Discordコミュニティ紹介 ✅️ Udemy講座（割引リンクあり）

- [noteプレミアム](https://premium.lp-note.com/)
- [note pro](https://pro.lp-note.com/?utm_source=notecom&utm_medium=footer)
- [よくある質問・noteの使い方](https://help-note.com/hc/ja)
- [プライバシー](https://terms.help-note.com/hc/ja/articles/44948981050649)
- [クリエイターへのお問い合わせ](https://note.com/munakata_souri/message)
- [フィードバック](https://help-note.com/hc/ja/requests/new?ticket_form_id=360000081181)
- [ご利用規約](https://terms.help-note.com/hc/ja/articles/44943817565465)
- [通常ポイント利用特約](https://note.com/terms/paid_point)
- [加盟店規約](https://note.com/terms/seller_creators)
- [資⾦決済法に基づく表⽰](https://note.com/terms/payment_service_act)
- [特商法表記](https://note.com/munakata_souri/terms/specified)
- [投資情報の免責事項](https://note.com/terms/investment_disclaimer)

GoogleAppsScript(GAS)って何？｜むなかた AI×Web3エンジニア