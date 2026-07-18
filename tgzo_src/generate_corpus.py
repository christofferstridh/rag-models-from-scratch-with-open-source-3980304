import os
import re
import wikipedia

def sanitize_filename(filename):
    return re.sub(r'[^a-zA-Z0-9]', "_", filename)


def generate_corpus(search_term="human rights", num_articles=1000, output_dir="all_articles"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    articles = []
    search_results = wikipedia.search(search_term, results=num_articles)
    print("hej")
    for i,title in enumerate(search_results,1):
        try:
            page = wikipedia.page(title, auto_suggest=False)
            articles.append((title, page.content))
            
            filename = sanitize_filename(title) + ".txt"
            
            with open(os.path.join(output_dir, filename), "w", encoding="utf-8") as f:
                f.write(content)

        except Exception as e:
            print(f"Error processing '{title}': {str(e)}")
            continue

    print(f"Saved {len(articles)} articles to {output_dir}")

    return articles

if __name__ == "__main__":
    generate_corpus()
