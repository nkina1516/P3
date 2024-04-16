import os
import newspaper

def scrape_article_content(url):
    # Function to scrape article content from URL
    try:
        article = newspaper.Article(url)
        article.download()
        article.parse()

        # Return the article title and content
        return article.title, article.text
    except Exception as e:
        print(f"Error occurred while scraping {url}: {str(e)}")
        return None, None

def read_article_urls_from_file():
    # Function to read article URLs from "articles.txt"
    project_directory = "/Users/niatekina/Desktop/Article-Scraper/Project3"
    raw_folder_path = os.path.join(project_directory, "Data", "raw")
    articles_file_path = os.path.join(raw_folder_path, "articles.txt")
    with open(articles_file_path, 'r') as file:
        article_urls = file.readlines()
    return [url.strip() for url in article_urls if url.strip()]
