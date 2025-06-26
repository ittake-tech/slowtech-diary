import os
import re

category_rules = {
    "markdown|jekyll|sitemap": "ブログ運営",
    "chatgpt|ai": "AI活用",
    "facebook|sns": "SNS",
    "パーマカルチャー|農": "パーマカルチャー",
    "ミニマリズム|シンプル": "ミニマリズム"
}

posts_dir = "_posts"

for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()

        # タイトル＆本文部分からキーワード検索
        match_category = None
        for pattern, category in category_rules.items():
            if re.search(pattern, content, re.IGNORECASE):
                match_category = category
                break

        if match_category:
            # フロントマター部分を編集
            if "---" in content:
                parts = content.split("---")
                front_matter = parts[1]
                if "category:" not in front_matter:
                    front_matter += f"\ncategory: {match_category}\n"
                    new_content = f"---{front_matter}---{parts[2]}"
                    with open(filepath, "w", encoding="utf-8") as file:
                        file.write(new_content)
                    print(f"{filename}: カテゴリ '{match_category}' を追加しました！")
