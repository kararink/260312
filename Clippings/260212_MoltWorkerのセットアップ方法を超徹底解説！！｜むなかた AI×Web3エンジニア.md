---
title: "MoltWorkerのセットアップ方法を超徹底解説！！｜むなかた AI×Web3エンジニア"
source: "https://note.com/munakata_souri/n/n69c194b057de"
author:
  - "[[むなかた AI×Web3エンジニア]]"
published: 2026-02-06
created: 2026-02-12
description: "こんにちは、むなかたです。  今回は「MoltWorker」と呼ばれる仕組みを使ってOpenClawをセキュアに運用しよう！という記事なのですが、正直ボリュームが多すぎて途中で心が折れかけました（笑）  何回か試して、ちゃんとうまくいく手順を解説しているつもりですが、記載の誤りやうまく行かないところなどあれば教えていただけると嬉しいです。  また、今回はWeb上のダッシュボード上でエージェントとやり取りするところまでの解説となっており、メッセージサービスとの連携のところの解説は 力尽き 省略させていただいているのでご了承ください…！  MoltWorkerって何？  OpenClawを"
tags:
  - "clippings"
---
![見出し画像](https://assets.st-note.com/production/uploads/images/249473457/rectangle_large_type_2_baaaf366460604c155adc040ac1c2d57.png?width=1280)

## MoltWorkerのセットアップ方法を超徹底解説！！

[むなかた AI×Web3エンジニア](https://note.com/munakata_souri)

こんにちは、むなかたです。

今回は「MoltWorker」と呼ばれる仕組みを使ってOpenClawをセキュアに運用しよう！という記事なのですが、正直ボリュームが多すぎて途中で心が折れかけました（笑）

何回か試して、ちゃんとうまくいく手順を解説しているつもりですが、記載の誤りやうまく行かないところなどあれば教えていただけると嬉しいです。

また、今回はWeb上のダッシュボード上でエージェントとやり取りするところまでの解説となっており、メッセージサービスとの連携のところの解説は ~~力尽き~~ 省略させていただいているのでご了承ください…！

## MoltWorkerって何？

OpenClawをCloudflare Workers上で動かすための仕組みで、Cloudflareの認証機能やサンドボックスを活用し、 **セキュリティ面としては最高の環境** を提供してくれています。

詳細はGithubページ [https://github.com/cloudflare/moltworker](https://github.com/cloudflare/moltworker) もご一読くださいね。

### 運用にかかるコスト

- CloudflareのWorkers Paid planの加入... 月5ドル
- その他Cloudflare機能... 無料枠内で収まるらしい
- AIサービスのAPIキー... 使った分だけ

Cloudflareのサーバ費用自体は月5ドルですが、AIをAPI経由で呼び出す必要があるため、その分の従量課金でコストが変化しそうです。

AIとのやり取りをどれだけ行うかにもよりますが10〜20ドルかかるくらいで考えておくのが無難ですね。準備も大変なので、始める前にコスト面を把握したうえでスタートしましょう。

## 必要なプログラムのインストール

### 1\. エディタのインストール

今回は直接プログラムを編集することは無いのですが、「ターミナル」を使いやすい、問題があったときにファイルを見ながらAIに聞ける、というメリットからエディタと呼ばれるメモ帳アプリを使う前提で解説していきます。

以下のようなものがインストール済みであればいずれも同じ手順で進めることができます。まだの場合は「VSCode」か「Antigravity」  
あたりをインストールしておくのがオススメです。

- VSCode
- Cursor
- Windsurf
- Antigravity

### 2\. MoltWorkerプログラムのダウンロード

MoltWorkerプログラムをダウンロードしていきます。 [https://github.com/cloudflare/moltworker](https://github.com/cloudflare/moltworker) にアクセスしてください。

緑色の「Code」というボタンを選択して「Download ZIP」をクリックします。ZIPファイルがダウンロードされるので解凍しましょう。

![画像](https://assets.st-note.com/img/1770313190-c7EraT0XQWK6NPFpMxJ4hlVy.png?width=1200)

解凍すると「moltworker」というフォルダが作成されるので、好きな場所に移動しておいてください。

続けてエディタを起動して、上部メニューの「ファイル」>「フォルダーを開く」から、「moltworker」フォルダを開いてください。

![画像](https://assets.st-note.com/img/1770313220-d31jvoCwXYRF7Ot2napufHU4.png?width=1200)

画像のように画面左側にファイル一覧が表示されていればOKです。

![画像](https://assets.st-note.com/img/1770313227-Zlkd3zxYjBWg9tJ7KnXfFGaL.png?width=1200)

### 3\. node.jsのインストール

続いて必要なプログラムのインストールや、Cloudflareへのデータアップロードに必要な「node.js」というプログラムのインストールです。

上部のメニューから「ターミナル」>「新しいターミナル」をクリックしましょう。画面下に「ターミナル」というビューが表示されるので、こちらでコマンドを入力していきます。

![画像](https://assets.st-note.com/img/1770313237-pjQeTb4lk0zHD3wn5LdCZ7sq.png?width=1200)

まずはnode.jsがインストールされているかを確認するために、以下のコマンドを実行してください。

```
node -v
```

ここでプログラムが見つからないようなエラーが発生した場合はインストールが必要です。バージョンが表示された場合はスキップして次に進んでOKです。

Node.jsのダウンロードページ [https://nodejs.org/ja/download](https://nodejs.org/ja/download) からインストーラーをダウンロードできます。画面下部からお使いのPCの環境にあったものを選択して「●●インストーラー」ボタンを押してください。

![画像](https://assets.st-note.com/img/1770313246-Wz6iR5ZUNmT291db7jl0opFX.png?width=1200)

インストーラーを起動して画面の指示に従って進めればnode.jsのインストールは完了です。

再度 「node −v」コマンドを入力してバージョン番号が出たら次に進んでください。インストールしてもまだエラーが出る場合、一度ターミナルを閉じて開き直してみてください。

### 4\. DockerDesktopのインストール

手元で設定した情報を元に、Cloudflareにプログラムをアップロードするために「Docker」というツールが必要です。

[https://www.docker.com/ja-jp/products/docker-desktop/](https://www.docker.com/ja-jp/products/docker-desktop/)

こちらのサイトから「Docker Desktop」をダウンロードしましょう。

![画像](https://assets.st-note.com/img/1770313255-MjDeoHnQL5Fc89RBWGNt3YXZ.png?width=1200)

ダウンロードしてきたインストーラを起動して、インストールと起動まで行っておいてください。

起動すると「Sign in」画面が表示されるので、アカウントの作成かログインを行っておきましょう。

![画像](https://assets.st-note.com/img/1770313262-BnkiXOTMlI9dHRVmKg6r0eu5.png?width=1200)

ログイン済み、かつアプリは起動したままの状態で次の作業に進みましょう。

![画像](https://assets.st-note.com/img/1770313267-THACzBd19tn7sXocWqgIewrF.png?width=1200)

## Cloudflareの初期設定

### 1\. アカウント作成

まずはCloudflareのアカウントから作成していきましょう。

[https://www.cloudflare.com/ja-jp/](https://www.cloudflare.com/ja-jp/) にアクセスして、「無料で始める」をクリックしてください。

![画像](https://assets.st-note.com/img/1770313275-IPLKqB8cwse64VlXDtZyNHpm.png?width=1200)

GoogleやAppleのアカウントを使って進めることもできますし、メールアドレスとパスワードの形式でもOKです。お好きな方法でアカウントを作成しましょう。

![画像](https://assets.st-note.com/img/1770313282-2kj60cnHmsxqNAuYL7PVeEOt.png?width=1200)

アカウントの作成完了後、ダッシュボード画面が表示されたらOKです。

![画像](https://assets.st-note.com/img/1770313289-yr7kfY6RLGJoXd3Cq2wtbQN4.png?width=1200)

### 2\. プランの切り替え

MoltWorkerの裏側で動いている仕組みを使うためには **月5ドルの「Workers Paid plan」に加入する必要があります** 。

アカウントの作成が完了したら続けてプラン変更をしていきます。左メニューの「Compute & AI」>「Workers plans」を選択しましょう。

2つプランが表示されていて、現在は「Free」に加入している状態なので、右側の「Purchase Workers Paid」をクリックしてください。支払い情報を入力したらプランの切り替えは完了です。

![画像](https://assets.st-note.com/img/1770313301-e7bFlktpMKmjzDx40va5Vn2S.png?width=1200)

### 3\. R2の有効化

次に、会話履歴や設定データなどを保存するための「R2」というストレージ機能を有効にします。

左メニューの「Storage & databases」>「R2 object storage」 >「Overview」を選択しましょう。

プラン加入時に使った支払い情報が表示されているはずなので、そのまま「Add R2 subscription to my account」からR2を有効にしたらOKです。

![画像](https://assets.st-note.com/img/1770313309-uYNgWfJkcSEint49BoU8jwLP.png?width=1200)

### 4\. workers.devの作成

続いて、実行に必要なworkers.devというドメインを作る必要があります。左メニューの「Compute & AI」>「Workers & Pages」というページを開いてください。

こちらのページを開いた瞬間に裏側で必要な設定が完了するので、開くだけでOKです。

![画像](https://assets.st-note.com/img/1770313315-sI7SowbXaKr9CDPlzJnEpNUv.png?width=1200)

### 5\. Cloudflare AI Gatewayの設定

続いてAIのAPIキーを管理するためのAI Gatewayの設定を進めていきます。

ダッシュボードの左メニューから「Compute & AI」>「AI Gateway」>「Create Gateway」を順に選択しましょう。

![画像](https://assets.st-note.com/img/1770313333-YH3TErNpfGzJukFDgSjeXqw1.png?width=1200)

「Gateway ID」には任意のIDを入力して、それ以下の選択肢は任意でOKです。それぞれの内容とおすすめの設定は以下のとおりです。

- Collect Logs: **「ON」**
	- ログ収集するかどうか
	- 利用状況分析や動作チェックに使えるのでONが良さそう
	- 不特定多数に使ってもらったり、個人情報が入るような場合はOFFを検討
- Cache Responses: **「OFF」**
	- 同じ質問に関して同じ返答をするかどうか
	- Botでのやり取りの場合は文脈で返答が変わる可能性があるのでOFFがオススメ
- Rate Limit Requests: **「ON」**
	- リクエスト制限を設けるかどうか
	- バグや不正での大量アクセスを防止するために念のため設定しておくと良さそう
- Authenticated Gateway:**「ON」**
	- 認証を必須にするか
	- 不正防止のためにこれはONを強くオススメ
![画像](https://assets.st-note.com/img/1770313379-2LZYBcivX6OAo9H5wG4jt3NC.png?width=1200)

Gatewayが作成されたらダッシュボード画面に遷移します。上部のタブから「Provider Keys」を選択しましょう。

AIサービスが一覧表示されるので、使いたいものを選んで「+Add」からAPIキーを登録していきます。

> APIキーの発行方法はAIサービスによって異なるので説明は省略します。登録したAPIキーはあとでも使うので控えておきましょう。

![画像](https://assets.st-note.com/img/1770313389-8M3Ea7FZglVXc6YNxvseR9B1.png?width=1200)

APIキーの登録が完了したら「Overview」タブを開いてください。「Native API/SDK Examples」を開き、画面下の選択肢からAPIキーを登録したAIを選択しましょう。

![画像](https://assets.st-note.com/img/1770313397-DLiuGTeJ12AjgpnyFvzRQUho.png?width=1200)

表示されるプログラムの中の **「baseURI」** の部分のURLをコピーしておいてください（「 **"** 」部分は不要です）。

> URLの末尾は「/anthropic」などAIのサービス名に対応しているものが必要です。「Unified API Examples」の方を選んでしまうと共有のURLが表示されてしまうので、「Native API/SDK Examples」を選ぶよう注意しましょう、

## MoltWorkerのセットアップ

それではMoltWorkerの設定を行っていきます。再度エディタに戻って、ターミナルを開いておきましょう。

### 1\. 必要なプログラムのインストール

まずは必要なプログラムをインストールします。以下のコマンドを実行しましょう。

```
npm install
```

少し待ってエラーなく終了したら完了です。

### 2\. Cloudflareへのログイン

続いて作業しているターミナルとCloudflareを紐づけるためにログインをします。以下のコマンドを実行してください。

ブラウザが自動で開かれ、アクセス許可してよいかどうかを聞かれるので「Allow」をクリックしましょう。

![画像](https://assets.st-note.com/img/1770313464-P68eQXf5YpgKhjJLADESGwVt.png?width=1200)

ターミナルに戻って以下のようなメッセージが表示されていればログイン成功です。

```javascript
Successfully logged in.
```

### 3\. APIキーの登録

続けて、Cloudflareに登録する値の設定です。先ほどの「Cloudflare AI Gateway」のところで使った値を登録していきます。

![画像](https://assets.st-note.com/img/1770313497-ZcE7FAxTgRwJGz4NlbIkYaUC.png?width=1200)

ターミナルで以下のコマンドを実行しましょう。

```
npx wrangler secret put AI_GATEWAY_API_KEY
```

値を入力するように指示されるので、CloudFlareで登録したAPIキーを貼り付けてEnterを押してください。

```
⛅️ wrangler 4.60.0 (update available 4.61.1)
─────────────────────────────────────────────
? Enter a secret value: ›
```

このように成功メッセージが表示されたらOKです。

```swift
🌀 Creating the secret for the Worker "moltbot-sandbox" 
✨ Success! Uploaded secret AI_GATEWAY_API_KEY
```

続けてbaseURLの設定を行います。以下のコマンドを実行してください。

```
npx wrangler secret put AI_GATEWAY_BASE_URL
```

こちらも値を入力するように指示されるので、baseURIに記載されていた **「https://gateway.ai.cloudflare.com/v1/...」** のようなURLを貼り付けて登録しましょう。

### 4\. アクセス用のトークンを生成

次にアクセス用トークンを作成します。以下のコマンドをまとめてターミナルに貼り付けて実行しましょう。

```javascript
export MOLTBOT_GATEWAY_TOKEN=$(openssl rand -hex 32)
echo "Your gateway token: $MOLTBOT_GATEWAY_TOKEN"
echo "$MOLTBOT_GATEWAY_TOKEN" | npx wrangler secret put MOLTBOT_GATEWAY_TOKEN
```

実行すると、このような結果が表示されるはずです。 **「Your gateway token:」** の後のランダムな文字列は **「ゲートウェイトークン」** というもので、初回URLアクセス時に使うので控えておいてください。

```
Your gateway token: [ランダムな文字列が表示される]
```

また、その下に設定が完了した旨のメッセージが表示されていればOKです。

```
⛅️ wrangler 4.60.0 (update available 4.61.1)
─────────────────────────────────────────────
🌀 Creating the secret for the Worker "moltbot-sandbox" 
✨ Success! Uploaded secret MOLTBOT_GATEWAY_TOKEN
```

### 5\. デプロイ

ここまで設定した内容をCloudFlare上に反映する「デプロイ」という作業を行います。以下のコマンドを実行しましょう。

```
npm run deploy
```

ここではしばらく待つ必要があります。最終的に以下のようなメッセージが表示されたら完了です。

```java
Deployed moltbot-sandbox triggers (2.66 sec)
  https://moltbot-sandbox.xxxxxxxxxxxxxx.workers.dev
  schedule: */5 * * * *
Current Version ID: xxxxxxxxxxxxxx
```

> 設定や事前準備が完了していないとエラーが出るので、その場合は「エラーが出たら」を参考に対応をお願いします。

最後のメッセージ内に表示されている「 **https://moltbot-sandbox.xxxxxx.workers.dev** 」がダッシュボードのURLです。

また、実際にアクセスするときにはURLの末尾に 「**?token=\[ゲートウェイトークン\]** 」を付与する必要があります。以下のようなURLになると思うので、この完全系のURLをしっかりメモしておきましょう。

```javascript
https://moltbot-sandbox.xxxxxx.workers.dev?token=[ゲートウェイトークン]
```

ただし、現状で開いても設定が完了していないというメッセージが表示されてしまいます。 値の登録をする必要があるので、次の「管理ページの設定」から情報の取得と登録を行いましょう。

![画像](https://assets.st-note.com/img/1770313629-2814pNhmBbDoHPM5naK3vZdI.png?width=1200)

### デプロイ時にエラーが出たら

**1\. Dockerが起動していない**

→ DockerDesktopがインストールされていないか起動していない状態です

```python
✘ [ERROR] The Docker CLI could not be launched. Please ensure that the Docker CLI is installed and the daemon is running.

  Other container tooling that is compatible with the Docker CLI and engine may work, but is not yet
  guaranteed to do so. You can specify an executable with the environment variable
  WRANGLER_DOCKER_BIN and a socket with DOCKER_HOST.
```

**2\. R2が無効になっている**

→ 初期設定の「R2の有効化」を再度確認ください

```javascript
✘ [ERROR] A request to the Cloudflare API (/accounts/xxxxxxxxxxxx/r2/buckets/moltbot-data) failed.

  Please enable R2 through the Cloudflare Dashboard. [code: 10042]
  
  If you think this is a bug, please open an issue at:
  https://github.com/cloudflare/workers-sdk/issues/new/choose
```

**3\. workers.devサブドメインが作られていない**

→ 初期設定の「workers.devの作成」を再度確認ください

## 管理ページの設定

ここからは管理ページの表示に必要な変数と呼ばれる値の取得と設定を行っていきます。合計5つの値を後でまとめて登録することになるので、1つずつ必ずメモを取るようにお願いします。

![画像](https://assets.st-note.com/img/1770313645-SkzJdhXToF53Yrgx7LnlUNE0.png?width=1200)

### ① CF\_ACCESS\_AUD を取得

Cloudflareの左メニュー「Compute & AI」>「Workers & Pages」に選択してください。

「moltbot-sandbox」という項目が自動で作成されているはずなので、右の「⋮」から「View settings」をクリックしましょう。

![画像](https://assets.st-note.com/img/1770313663-qfVx01TJ8bHiZ92CNrU7wKkB.png?width=1200)

設定画面に移動するので、「Domains & Routes」内の「workers.dev」の行、「⋮」から「Cloudflare Access」をONにしましょう。

![画像](https://assets.st-note.com/img/1770313670-f74AJBcbvTyu3Z6YokqXaN2d.png?width=1200)

有効にするとすぐに「Cloudflare Access Enabled」というダイアログと、トークン文字列が表示されます。

上の方の「Audience(aud)」という文字列が、「 **① CF\_ACCESS\_AUD** 」の値となります。

![画像](https://assets.st-note.com/img/1770313688-uWrYOpfoykAsB4G0JVnhSUZ5.png?width=1200)

### ② CF\_ACCESS\_TEAM\_DOMAIN を取得

続いてCloudflare Oneのページに移動します。左メニューの「Zero Trust」という項目をクリックしてください。

![画像](https://assets.st-note.com/img/1770313742-z0Lmp54h2oWySuAtixeQlPCb.png?width=1200)

左側のメニューから「Settings」をクリックして表示される「Team domain」という欄に書かれているドメインが 「 **② CF\_ACCESS\_TEAM\_DOMAIN** 」 の値となります。

![画像](https://assets.st-note.com/img/1770313762-mGtPz16vBJR9kOMu7qZ8IELo.png?width=1200)

### ③ R2\_ACCESS\_KEY\_IDと④ R2\_SECRET\_ACCESS\_KEYを取得

CloudflareのDashboardに戻り、左メニューの「Storage & databases」>「R2 object storage」>「Overview」と進みましょう。

画面右にある「Account Details」という欄の「API Tokens」の右側「Manage」 をクリックしてください。

![画像](https://assets.st-note.com/img/1770313774-moBLZ2igJXPG16ysbarYDpul.png?width=1200)

トークン一覧画面に移動するので「Account API Tokens」の「Create Account API token」をクリックしましょう。

![画像](https://assets.st-note.com/img/1770313781-ljbOgFZhKGNVpqsMTenxXoSr.png?width=1200)

トークン作成画面が表示されます。Permissionsは「Object Read & Write」を選択し、Specify bucket(s)は「Apply to specific buckets only」を選択した後、プルダウンから「moltbot-data」を選択しましょう。

![画像](https://assets.st-note.com/img/1770313789-OZA9DosLwztu4BQhdlmjpJPV.png?width=1200)

それ以外の項目はデフォルトのままで良いので、そのまま「Create Account API Token」をクリックしてください。

![画像](https://assets.st-note.com/img/1770313802-uqVO8jtm7v5ikIhBec6dCp4o.png?width=1200)

「Use the following credentials for S3 clients:」という欄の2つの文字列を控えておきましょう。

- Access Key ID... 「 **③ R2\_ACCESS\_KEY\_ID** 」
- Secret Access Key... 「 **④ R2\_SECRET\_ACCESS\_KEY** 」
![画像](https://assets.st-note.com/img/1770313826-Nc1Il5oXKDTyL72khBUmvRFA.png?width=1200)

### ⑤ CF\_ACCOUNT\_IDを取得

最後に左メニューの「Accont home」からホーム画面に遷移し、アカウント名右の「⋮」から「Copy account ID」をクリックしてください。

ここで取得できるのが「 **⑤ CF\_ACCOUNT\_ID** 」となります。

![画像](https://assets.st-note.com/img/1770313843-Rla6xyJY1QeBAi39bn8DMgfW.png?width=1200)

### 値を設定

それでは最後に取得した値をまとめて登録していきましょう。対応付けは以下のとおりです。

![画像](https://assets.st-note.com/img/1770313650-VglmpC7TfBNdPor41kz6qEDX.png?width=1200)

登録時には以下のように「npx wrangler secret put」の後に変数名を入れたものをコマンド実行してください。

```
npx wrangler secret put CF_ACCESS_AUD
```

以下のような入力モードになったら、控えておいた文字列を貼り付けて登録すればOKです。

```
⛅️ wrangler 4.60.0 (update available 4.62.0)
─────────────────────────────────────────────
? Enter a secret value: ›
```

これを5つ分繰り返したら登録完了です。

```
npx wrangler secret put CF_ACCESS_AUD
npx wrangler secret put CF_ACCESS_TEAM_DOMAIN
npx wrangler secret put R2_ACCESS_KEY_ID
npx wrangler secret put R2_SECRET_ACCESS_KEY
npx wrangler secret put CF_ACCOUNT_ID
```

再度デプロイを行って値を反映させましょう。以下のコマンドを実行してください。

```
npm run deploy
```

## 管理ページにアクセス

それでは管理ページにアクセスしましょう。デプロイ後に表示されたURLとゲートウェイトークンを使った、以下のようなURLにアクセスしましょう。

```javascript
https://[あなたのURL].workers.dev/?token=[ゲートウェイトークン]
```

ここまでの設定がうまく出来ていたら以下のような画面が表示されます。起動までに時間がかかるのでしばらく待ちましょう。

![画像](https://assets.st-note.com/img/1770313859-h4NMvSbwYG2X8ztiL3P6n1kT.png?width=1200)

ダッシュボードが表示されますが、最初にペアリングという作業が必要のためエラーが出ています。エラー文の中に表示されているURLにアクセスしてみましょう。

![画像](https://assets.st-note.com/img/1770313868-xvDUaoizrOfXNIjVTSBu21ZH.png?width=1200)

Adminページに遷移したら画面下に「Pending Pairing Requests」という欄が表示されます。こちらの項目の「Approve」をクリックしてください。

![画像](https://assets.st-note.com/img/1770313886-yvHTJlk45apcIdOXz6KeftAQ.png?width=1200)

承認が完了したら元のページに戻ってOKです。

あとはAIエージェントに何か挨拶してみて返答が帰ってきたら無事セットアップは完了です！お疲れ様でした。

> ここでうまくAIエージェントが返答してくれない場合は、AI\_GATEWAY\_API\_KEYやAI\_GATEWAY\_BASE\_URLの設定が誤っている可能性があります。

このあとのメッセージサービスとの連携を書きたかったのですが、ここまでの道のりが長すぎたので力尽きました…笑

  

MoltWorkerのセットアップ方法を超徹底解説！！｜むなかた AI×Web3エンジニア