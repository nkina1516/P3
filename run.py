import os
import time
import requests
from openai import OpenAI  # For interacting with the OpenAI API, specifically GPT models.
from Module1.mod1 import scrape_article_content, read_article_urls_from_file

# Define your OpenAI API key
OPENAI_API_KEY = "*"  # Replace with your actual OpenAI API key

def useLLMApi(article_text):
    client = OpenAI(api_key=OPENAI_API_KEY)
    # Define the prompt with the article text
    prompt = f"Please make the article concise, up to 50 words. The article is: {article_text}"
    
    # Use OpenAI's GPT to generate a summary based on the article text.
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Adjust based on available models
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": ""}
        ]
    )
    return completion.choices[0].message.content if completion.choices else "No summary available."

# Define a function to summarize an article
def summarize_article_from_url(url, output_file):
    try:
        # Scrape article content
        title, content = scrape_article_content(url)
        
        if title and content:
            # Summarize the article
            summary = useLLMApi(content)
            # Write summary to file
            with open(output_file, 'a') as f:
                f.write(f"URL: {url}\nTitle: {title}\nSummary: {summary}\n\n")
        else:
            print(f"Error: Unable to scrape content from {url}")
    except Exception as e:
        print(f"Error occurred while summarizing article from {url}: {str(e)}")

if __name__ == "__main__":
    # Read article URLs from file
    article_urls = read_article_urls_from_file()
    output_folder = "/Users/niatekina/Desktop/Article-Scraper/Project3/Data/returned"
    output_file = os.path.join(output_folder, "summaries.txt")
    
    # Summarize articles
    for url in article_urls:
        summarize_article_from_url(url, output_file)
