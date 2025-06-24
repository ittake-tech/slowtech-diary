# GitHub Actionsでsitemap.txtを自動生成する仕組みを作った話

最近、ブログ記事を追加するたびに `sitemap.txt` を手動で更新していたのだけど、「これ、自動化できるんじゃない？」と思って、GitHub Actions を使ってみることにした。

結果としては…  
**無事に自動化できた！**  
でも、ちょっとだけつまずいたので、記録として残しておくことにする🌱

---

## 🎯 やりたかったこと

- ブログ記事は `articles/` フォルダに `.md` 形式で保存している
- それらを元に `sitemap.txt` を自動で生成
- 記事を追加・更新するたびに `sitemap.txt` も更新される仕組みを作りたかった

---

## ⚙ やったこと

`.github/workflows/` フォルダに、以下のような `generate-sitemap.yml` を追加。

```yaml
name: Generate sitemap.txt

on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3

      - name: Generate sitemap.txt
        run: |
          echo "https://www.minimal-peil.com/" > sitemap.txt
          for file in articles/*.md; do
            name=$(basename "$file" .md)
            echo "https://www.minimal-peil.com/#/articles/$name" >> sitemap.txt
          done

      - name: Commit and push sitemap
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "github-actions[bot]@users.noreply.github.com"
          git add sitemap.txt
          git commit -m "Auto-update sitemap.txt"
          git push

❌ 最初に出たエラー

最初の実行では、sitemap.txt の生成自体はうまくいったものの、push に失敗してしまった。

エラーメッセージはこちら：

remote: Permission to ittake-tech/slowtech-diary.git denied to github-actions[bot]
fatal: unable to access 'https://github.com/ittake-tech/slowtech-diary.git/': The requested URL returned error: 403

✅ 解決方法

GitHub Actions の設定で「書き込み権限」がオフになっていたのが原因だった。

設定手順：
	1.	リポジトリの「⚙ Settings」へ
	2.	左側の「Actions」→「General」タブを選択
	3.	「Workflow permissions」を下にスクロール
	4.	Read and write permissions に変更して「Save」！

⸻

🎉 結果！

この設定変更だけで、以後のコミット時に sitemap.txt が自動生成＆更新されるようになった✨

⸻

✍ おわりに

ちょっとした自動化だけど、ブログをスマホで運営している私にとってはかなり大きな前進。
これで記事を投稿するたびに sitemap.txt を手でいじる必要はなくなったし、SEO 的にも一歩前進だと思う🌿

同じように Docsify や GitHub Pages を使っている人の参考になればうれしいな。

⸻

この記事は、ChatGPT（ミナリ）との対話をもとにまとめました。
