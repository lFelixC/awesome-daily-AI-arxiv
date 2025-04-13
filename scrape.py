import os
import re
import time
from collections import defaultdict
from datetime import UTC, datetime, timedelta

import requests
import yaml
from bs4 import BeautifulSoup

DATE = (datetime.now(UTC) - timedelta(days=1)).strftime("%Y-%m-%d")


def update_category(categories):
    arxiv_list = defaultdict(list)
    for cat, meta in categories.items():
        while True:
            try:
                response = requests.get(f"https://arxiv.org/list/{cat}/new")
                if response.status_code != 200:
                    time.sleep(3)
                    continue
            except:
                time.sleep(10)
                continue
            break

        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all(id="articles")
        for article in articles:
            for dt, dd in list(zip(article.find_all("dt"), article.find_all("dd")))[::-1]:
                arxiv_id = dt.find("a", href=lambda x: x and x.startswith("/abs/"))["href"].split("/")[-1]
                link = f"https://arxiv.org/abs/{arxiv_id}"

                title = dd.find("div", class_="list-title").get_text(strip=True).replace("Title:", "").strip()
                authors = [a.get_text(strip=True) for a in dd.find("div", class_="list-authors").find_all("a")]
                authors = authors[:6] + ["et al."] if len(authors) > 6 else authors
                authors = ", ".join([author.name if type(author) is not str else author for author in authors])
                abstract = dd.find("p", class_="mathjax").get_text(strip=True)

                category_div = dd.find("div", class_="list-subjects")
                primary_category = re.findall(
                    r"\(([^()]*)\)",
                    category_div.find("span", class_="primary-subject").get_text(strip=True),
                )[0]
                if primary_category != cat:
                    continue
                all_categories = re.findall(
                    r"\(([^()]*)\)",
                    "".join(text for text in category_div.stripped_strings),
                )
                if any(cat not in categories for cat in all_categories):
                    continue
                arxiv_list[cat].append((title, authors, link, abstract, all_categories))

        arxiv_len = len(arxiv_list[cat])
        arxiv_list_str = "\n".join(
            [
                f"- **[{title}]({link})**  `arXiv:{link.split('/')[-1].split('v')[0]}`  \n  _{authors}_\n  <details><summary>Abstract</summary>\n  {abstract.strip().replace('\n', '')}\n  </details>\n"
                for title, authors, link, abstract, _ in arxiv_list[cat]
            ]
        )

        if arxiv_len == 0:
            print("No papers found for", meta["name"])
            continue

        meta["count"] = arxiv_len

        with open("README.md", "r", encoding="utf-8") as f:
            lines = f.readlines()

        target_header = f"### {meta['name']}"
        start_index = -1
        for i, line in enumerate(lines):
            if target_header.strip() in line:
                start_index = i
                break

        if start_index == -1:
            start_index = len(lines) - 1

        end_index = len(lines)
        for i in range(start_index + 1, len(lines)):
            if lines[i].startswith("### "):
                end_index = i
                break

        new_lines = (
            lines[: start_index + 1]
            + ["\n"]
            + ["<details open><summary>Click to Collapse</summary>\n\n"]
            + [arxiv_list_str.strip() + "\n\n"]
            + ["[↑ Back to Top](#-full-archive)\n\n"]
            + ["</details>\n\n"]
            + lines[end_index:]
        )

        if start_index == len(lines) - 1:
            new_lines = new_lines[: start_index + 1] + [f"### {meta['name']}\n"] + new_lines[start_index + 1 :]

        with open("README.md", "w", encoding="utf-8") as f:
            f.writelines(new_lines)

        print("Updated README.md for", meta["name"])

    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    target_header = "Full Archive"
    start_index = -1
    for i, line in enumerate(lines):
        if target_header.strip() in line:
            start_index = i
            break

    if start_index == -1:
        raise ValueError("could not find header")

    end_index = len(lines)
    for i in range(start_index + 1, len(lines)):
        if lines[i].startswith("### "):
            end_index = i
            break

    new_lines = (
        lines[: start_index + 1]
        + ["\n"]
        + ["| Category                                                                                | Count |\n"]
        + ["| --------------------------------------------------------------------------------------- | ----- |\n"]
        + [
            f"| [{meta['name']}](#{meta['name'].replace(' ', '-').lower()[:-1]}) | {meta['count']:<5} |\n"
            for meta in categories.values()
        ]
        + ["\n"]
        + lines[end_index:]
    )

    total_papers = sum(meta["count"] for meta in categories.values())
    new_lines[2] = f"[![Total Papers](https://img.shields.io/badge/paper_today-{total_papers}+-red)]()\n"

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print("Updated README.md for Full Archive")
    return arxiv_list


def update_hot_topic(arxiv_list, topics):
    def filter_strings(raw_list, keywords, filter_words):
        def check_condition(s, condition):
            if isinstance(condition, list):
                return all(sub.lower() in s.lower() for sub in condition)
            else:
                return condition.lower() in s.lower()

        return [
            item
            for item, content in raw_list
            if any(check_condition(content, cond) for cond in keywords)
            and not any(check_condition(content, f_cond) for f_cond in filter_words)
        ]

    arxiv_list = [(item, item[0] + " " + item[3]) for sublist in arxiv_list.values() for item in sublist]
    for topic, meta in topics.items():
        topic_list = filter_strings(arxiv_list, meta["keywords"], meta["filters"] or [])

        arxiv_len = len(topic_list)
        topic_list = sorted(topic_list, key=lambda x: x[-1], reverse=True)
        topic_list = "\n".join(
            [
                f"- **[{title}]({link})**  `arXiv:{link.split('/')[-1].split('v')[0]}`  `{'` `'.join(categories)}`  \n  _{authors}_\n  <details open><summary>Abstract</summary>\n  {abstract.strip().replace('\n', '')}\n  </details>\n"
                for title, authors, link, abstract, categories in topic_list
            ]
        )

        meta["count"] = arxiv_len

        if arxiv_len == 0:
            print("No papers found for", topic)
            continue

        os.makedirs("hot_topic", exist_ok=True)
        with open(f"hot_topic/{topic}.md", "w", encoding="utf-8") as f:
            f.write(f"# 🔍 {topic} Papers · {DATE}\n\n")
            f.write(f"[![Total Papers](https://img.shields.io/badge/Papers-{arxiv_len}-2688EB)]()\n")
            f.write(
                "[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()\n\n"
            )
            f.write("---\n\n")
            f.write("## 📌 Filter by Category\n")
            keywords = [",".join(keyword) if type(keyword) is list else keyword for keyword in meta["keywords"]]
            filter_words = [
                ",".join(filter_word) if type(filter_word) is list else filter_word
                for filter_word in (meta["filters"] or [])
            ]
            f.write(f"**Keywords**: `{'` `'.join(keywords)}`  \n")
            f.write(f"**Filter**: `{'` `'.join(filter_words) if filter_words else 'None'}`\n\n")
            f.write("---\n\n")
            f.write("## 📚 Paper List\n\n")
            f.write(topic_list)

        print("Updated hot_topic for", topic)

    hot_topic = sorted(topics.items(), key=lambda x: x[1]["count"], reverse=True)
    hot_topic = "\n".join([f"  - [{topic}](hot_topic/{topic}.md)" for topic, _ in hot_topic])

    with open("README.md", "r", encoding="utf-8") as f:
        lines = f.readlines()

    target_header = "Hot Topic"
    start_index = -1
    for i, line in enumerate(lines):
        if target_header.strip() in line:
            start_index = i
            break

    if start_index == -1:
        raise ValueError("could not find header")

    end_index = len(lines)
    end_header = "Active Platform"
    for i in range(start_index + 1, len(lines)):
        if end_header.strip() in lines[i]:
            end_index = i
            break

    new_lines = lines[: start_index + 1] + [hot_topic] + ["\n"] + lines[end_index:]

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(new_lines)

    print("Updated README.md for Hot Topic")


if __name__ == "__main__":
    config = yaml.load(open("config.yml", "r"), Loader=yaml.FullLoader)
    categories = {key: {"name": value} for key, value in config["category"].items()}
    topics = config["topic"]
    arxiv_list = update_category(categories)
    update_hot_topic(arxiv_list, topics)
