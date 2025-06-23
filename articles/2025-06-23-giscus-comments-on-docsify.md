# 🌱 DocsifyブログにGiscusでコメント機能をつけた話

最近、私の静的ブログ「Minimal Peil」に、  
**コメント機能（Giscus）** を導入しました📝

使っているのは、スマホでも完結できる**Docsify**というシンプルなドキュメント系サイトジェネレーターです。

---

## 💭 どうしてコメント機能をつけたの？

いままでは「書くこと」に集中してたけど、  
ふと「誰かの声をやさしく受け取れたらうれしいな」って思ったんです🌸

とはいえ、フォームやサーバーを使うのは大げさすぎるし…  
**GitHub Pagesで完結できる、軽やかなコメント機能がほしい！**  
そんなときに見つけたのが **Giscus（ギスカス）** でした。

---

## 🛠 Giscusって何？

Giscusは、GitHub Discussions（ディスカッション機能）を活用した  
**コメントウィジェット**です。

- 💬 GitHubアカウントでログインしてコメントできる
- 🌍 静的サイトでも使える
- ✨ リアクションや絵文字もOK
- 🌙 ダークモードにも対応（テーマで切り替え可）

個人ブログにぴったりの、**ゆるくて気軽な雰囲気**が気に入りました。

---

## 📦 実装した手順（ざっくり）

```plaintext
1. GitHub Discussionsを有効にする
   → 「Settings > Features > Discussions」からONに

2. カテゴリをつくる
   → とりあえず "General" という名前でOK

3. Giscus公式で設定を生成
   → [giscus.app](https://giscus.app) でリポジトリやカテゴリを指定して、
      スクリプトタグをコピー

4. index.htmlに貼り付ける
   → Docsifyの`<div id="app"></div>`の下にペタッと

<!-- コメント表示のためのGiscus -->
<script src="https://giscus.app/client.js"
        data-repo="ittake-tech/slowtech-diary"
        data-repo-id="●●●●●●●●"
        data-category="General"
        data-category-id="●●●●●●●●"
        data-mapping="pathname"
        data-reactions-enabled="1"
        data-theme="light"
        data-lang="ja"
        crossorigin="anonymous"
        async>
</script>

💡 data-theme="light" にしておけば、やさしいライトモードになります。

⸻

🌼 やってみた感想

実際に導入してみて……
	•	記事の下に、ちゃんとコメント欄が表示された！
	•	表示も軽くて、スマホでも見やすい◎
	•	「GitHubアカウントでログインして書く」って、ちょうどいい距離感🌱

なにより、「声を受け取れる窓」ができたことがうれしい。

⸻

✍️ おわりに

ミニマルな暮らしの中で、こうして少しずつ
「人とやさしく繋がる仕組み」を整えていくのも悪くないなって思います。

このブログを訪れた方が、気軽に一言コメントを残してくれたら、
とってもうれしいです☺️🌸

⸻

🛠 実装したリポジトリはこちら：
👉 minimal-peil.com
