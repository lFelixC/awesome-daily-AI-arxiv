import os
import time

import arxiv
import yaml


def update_category(client: arxiv.Client, categories):
    for cat, meta in categories.items():
        while True:
            try:
                search = arxiv.Search(query=f"cat:{cat}", max_results=800, sort_by=arxiv.SortCriterion.LastUpdatedDate)
                if not client.results(search):
                    time.sleep(3)
                    continue
            except:
                time.sleep(10)
                continue
            break

        arxiv_list = []

        newest_day = None
        for result in client.results(search):
            if result.primary_category != cat:
                continue
            link = result.entry_id
            title = result.title
            abstract = result.summary
            authors = result.authors
            authors = authors[:6] + ["et al."] if len(authors) > 6 else authors
            authors = ", ".join([author.name if type(author) is not str else author for author in authors])
            update_time = result.updated
            publish_time = result.published

            if newest_day is None:
                newest_day = update_time.date()
            if update_time.date() != newest_day:
                break

            arxiv_list.append((title, authors, link, abstract, publish_time))
        arxiv_len = len(arxiv_list)
        arxiv_list = sorted(arxiv_list, key=lambda x: x[-1], reverse=True)
        arxiv_list = "\n".join(
            [
                f"- **[{title}]({link})**  `arXiv:{link.split('/')[-1].split('v')[0]}`  \n  _{authors}_\n  <details><summary>Abstract</summary>\n  {abstract.strip().replace('\n', '')}\n  </details>\n"
                for title, authors, link, abstract, _ in arxiv_list
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
            + [arxiv_list.strip() + "\n\n"]
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
    return newest_day


def update_hot_topic(client: arxiv.Client, categories, topics, newest_day):
    def parse_query(meta: dict):
        assert "keywords" in meta
        assert "filters" in meta

        query = "(" + " OR ".join([f"cat:{cat}" for cat in categories]) + ") AND ("

        for keyword in meta["keywords"]:
            query += f'"{keyword}"OR'
        query = query[:-2] + ") "

        filter_query = ""
        if meta["filters"] is not None:
            for filter in meta["filters"]:
                filter_query += f'"{filter}"OR'
            filter_query = filter_query[:-2]

        query += f"ANDNOT ({filter_query})" if filter_query else ""
        return query

    for topic, meta in topics.items():
        query = parse_query(meta)
        while True:
            try:
                search = arxiv.Search(
                    query=query,
                    max_results=800,
                    sort_by=arxiv.SortCriterion.LastUpdatedDate,
                )
                if not client.results(search):
                    time.sleep(3)
                    continue
            except:
                time.sleep(10)
                continue
            break

        arxiv_list = []

        for result in client.results(search):
            link = result.entry_id
            title = result.title
            abstract = result.summary
            category = list(set([result.primary_category] + result.categories))
            authors = result.authors
            authors = authors[:6] + ["et al."] if len(authors) > 6 else authors
            authors = ", ".join([author.name if type(author) is not str else author for author in authors])
            update_time = result.updated
            publish_time = result.published

            if not all([cat in categories for cat in category]):
                continue

            if update_time.date() != newest_day:
                break

            arxiv_list.append((title, authors, link, abstract, category, publish_time))
        arxiv_len = len(arxiv_list)
        arxiv_list = sorted(arxiv_list, key=lambda x: x[-1], reverse=True)
        arxiv_list = "\n".join(
            [
                f"- **[{title}]({link})**  `arXiv:{link.split('/')[-1].split('v')[0]}`  `{'` `'.join(categories)}`  \n  _{authors}_\n  <details open><summary>Abstract</summary>\n  {abstract.strip().replace('\n', '')}\n  </details>\n"
                for title, authors, link, abstract, categories, _ in arxiv_list
            ]
        )

        meta["count"] = arxiv_len

        if arxiv_len == 0:
            print("No papers found for", topic)
            continue

        os.makedirs("hot_topic", exist_ok=True)
        with open(f"hot_topic/{topic}.md", "w", encoding="utf-8") as f:
            f.write(f"# 🔍 {topic} Papers · {newest_day}\n\n")
            f.write(f"[![Total Papers](https://img.shields.io/badge/Papers-{arxiv_len}-2688EB)]()\n")
            f.write(
                "[![Last Updated](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/repos/tavish9/awesome-daily-AI-arxiv/commits/main&query=%24.commit.author.date&label=updated&color=orange)]()\n\n"
            )
            f.write("---\n\n")
            f.write("## 📌 Filter by Category\n")
            f.write(f"**Keywords**: `{'` `'.join(meta['keywords'])}`  \n")
            f.write(f"**Filter**: `{'` `'.join(meta['filters']) if meta['filters'] else 'None'}`\n\n")
            f.write("---\n\n")
            f.write("## 📚 Paper List\n\n")
            f.write(arxiv_list)

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
    client = arxiv.Client()
    newest_day = update_category(client, categories)
    update_hot_topic(client, categories, topics, newest_day)
