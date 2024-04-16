# Article-Summarizer using LLM

## Overview

Article summarizer is a python script that summarizes articles using a Open AI's LLM. The script scrapes articles from the `articles.txt` file located in the Data folder as follows: `Data/raw/articles.txt.` After scraping the articles, the script goes through and identifies each article's url,title, and content, then uses that information to create a summary for each individual article, and stores each article's summary along with its url, and title in the `summaries.txt` file.

## Installation

To use Article-Summarizer, follow these steps:

1. Create a new enviornemt using my `requirements.yaml` file

Be sure that you are in the location where you stored this yaml file! 

If you dont know, enter cd into the terminal. Once you've done this, say you had it stored on your dekstop inside of your 
cs325 folder, you would enter this following information to the terminal:

```
cd
cd desktop/cs325
conda env create -n new_env_name -f requirements.yaml

```
2. Activate the enviornament:

Notice how I am activating the one that got created in step 1

```
conda activate new_env_name 

```

2. Enter the command "conda list" to the terminal:
 
```
conda list

```

3. Check to see that the package newspaper3k is downloaded 

Example of what your output should look like after entering the command from step 2:

```
ncurses                   6.4                  h313beb8_0  
newspaper3k               0.2.8                    pypi_0    pypi
nltk                      3.8.1                    pypi_0    pypi
openssl                   3.0.13               h1a28f6b_0  

```
If it is not downloaded, enter the following to the terminal:

```
pip install newspaper3k

```

### Run the script

4. Navigate to the place (location) where you stored `run.py`
Ex: I stored my `run.py` in my cs325 folder

You'd enter this to the terminal:

```
cd 
cd desktop/cs325

```
5. Enter this command to run the script:

```
python run.py

```
Example of my path:

```
/Users/niatekina/envs/cs325/bin/python3 "run.py"

```
If you dont know your path enter this command:

```
pwd

```

Example of what your output shoud look like:

```

URL: https://www.cbsnews.com/news/drake-1-15-million-super-bowl-bet-chiefs-to-win/
Title: Drake places $1.15 million Super Bowl bet on the Chiefs to win
Summary: Drake bet $1.15 million on the Kansas City Chiefs to win the Super Bowl, inspired by Taylor Swift's connection with the team. The wager was shared on his Instagram, stirring up fears of the "Drake curse." The Super Bowl will air on Feb. 11 with Usher headlining the halftime show.

URL: https://www.cbsnews.com/news/drake-1-15-million-super-bowl-bet-chiefs-to-win/
Title: Drake places $1.15 million Super Bowl bet on the Chiefs to win
Summary: Drake bets $1.15 million on Chiefs for Super Bowl, sparking concern over his 'curse'. Nearly 68 million Americans plan to bet on the game. Super Bowl LVIII on Feb. 11 features Usher, Reba McEntire, and Andra Day.

URL: https://www.cbsnews.com/news/do-super-bowl-halftime-performers-get-paid/
Title: Do Super Bowl halftime performers get paid? How much Usher stands to make for his 2024 show
Summary: Super Bowl halftime performers like Usher don't get paid by the NFL, receiving only union scale wages, typically around $1,000 a day. Major stars perform for free to reach over 100 million viewers, promote their music, and have the NFL cover production costs. This exposure can outweigh financial compensation.

URL: https://www.cbsnews.com/news/who-is-grammys-host-2024-trevor-noah/
Title: Who hosted the 2024 Grammy Awards? All about Trevor Noah
Summary: Trevor Noah hosted the 2024 Grammys, his fourth consecutive time. Known for "The Daily Show" and as a bestselling author, he shared hosting nerves and thrill for being live. From South Africa, he starred in "Black Panther" and U.S. late-night shows before gaining global fame.

etc...

```

#### Creating a LLM account and generate keys to use for calls/requests

1. Create an account on a LLM site

Example using Chat GPT:

```
https://auth0.openai.com/u/signup/identifier?state=hKFo2SBwbVJWUFE1X1QtenZQa3NHNl9zaUhwNE1HSl9VXzRDV6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHg4cmwwNkFrLTB1UEtnaVB1NDFaa0VEbTFfMWo5RTlJo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q

```

2. Generate an API key

- Navigate to the far left of your screen, just past the Documentation heading, and you should see a set of icons that you can select
- The first icon you should see is Playground, followed by Assistants, then Fine Tuning, and finally API keys
- Select the one that says API keys 
- Then you should  be redirected to another page titled API keys, select generate API key
- Now you should see a message that says phone verification, enter your phone number and press enter
- You should recieve a message on your phone, enter the code from your phone in the box that asks for the sms code
- Now you should be able to title your API key, title it whatever you want
- After doing so, you should now have your very own API key, keep track of it!

3. Implement your API key

```
OPENAI_API_KEY = "your generated API key"

def useLLMApi(article_text):
    #position yourself (the client in this case) to make a request to Chat GPT's LLM
    client = OpenAI(api_key=OPENAI_API_KEY)
    
    # Define the prompt (what you're asking GPT) with the article text
    prompt = f"Please make the article concise, up to 50 words. The article is: {article_text}"
    
    # Use OpenAI's GPT to generate a summary based on the article text.
    # completion is the respone that gets returned from GPT
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # model that allows for client & response interactions
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": ""}
        ]
    )
    return completion.choices[0].message.content if completion.choices else "No summary available."
```

