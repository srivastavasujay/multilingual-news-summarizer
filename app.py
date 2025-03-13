from flask import Flask, render_template, request
import requests
import cohere
import json
import time

app = Flask(__name__)

# Your News API key
NEWS_API_KEY = '94ec949e93bc45faa132a0b6dde20b59'
# Your Cohere API key
COHERE_API_KEY = 'Fcj3y7CAsrhs9yHvvXxpLYowYdX5z02APwZJtzuv'

# Initialize Cohere client
co = cohere.Client(COHERE_API_KEY)

# Load language options from JSON file
with open('templates/languages.json') as f:
    languages = json.load(f)

# Function to fetch news articles
def fetch_articles(query, language):
    category = query
    url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={NEWS_API_KEY}'
    
    # Measure the time before making the API request
    start_time = time.time()
    
    response = requests.get(url)
    
    # Measure the time after receiving the response
    end_time = time.time()
    
    # Calculate the response time
    response_time = end_time - start_time
    print(f"API response time: {response_time} seconds")
    
    articles = response.json().get('articles', [])[:20]  # Limit to 20 articles
    
    if language != 'en':
        articles = translate_articles(articles, language)
    
    return articles

# Function to translate articles using Cohere
def translate_articles(articles, target_language):
    translated_articles = []
    for index, article in enumerate(articles):
        try:
            translated_title = translate_text(article['title'], target_language)
            translated_description = translate_text(article['description'], target_language)
                        
            translated_article = {
                'title': translated_title,
                'description': translated_description,
                'url': article['url'],
                'source': article['source'],
                'publishedAt': article['publishedAt']
            }
            translated_articles.append(translated_article)
        except Exception as e:
            error_message = f"Error translating article {index}: {e}"
            print(error_message)
            translated_article = {
                'title': error_message,
                'description': error_message,
                'url': article['url'],
                'source': article['source'],
                'publishedAt': article['publishedAt']
            }
            translated_articles.append(translated_article)
    return translated_articles

# Function to translate text using Cohere
def translate_text(text, target_language):
    if not text:
        return ""
        
    try:
        response = co.generate(
            model='command',
            prompt=f"Translate the following text to {target_language}: {text}",
            max_tokens=512,
            temperature=0.5,
            stop_sequences=["--"]
        )
        translated_text = response.generations[0].text.strip()
        return translated_text
    except Exception as e:
        error_message = f"Error translating text: {e}"
        print(error_message)
        return error_message  # Return error details if translation fails

# Route to display the homepage
@app.route('/')
def index():
    # Get query parameter or default to 'technology'
    query = request.args.get('query', 'technology')
    language = request.args.get('language', 'en')
    
    articles = fetch_articles(query, language)
    return render_template('index.html', articles=articles, query=query, language=language, languages=languages)

if __name__ == '__main__':
    app.run(debug=True)