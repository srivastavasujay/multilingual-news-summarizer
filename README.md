# Multilingual News Summarizer

This web application fetches news articles using an open-source News API and allows users to select a language for summarizing and translating the news articles using the Aya model.

## Features

- Fetches top news articles based on a query.
- Supports multiple languages for translation.
- Uses the Aya model for summarizing and translating news articles.

## Prerequisites

- Python 3.6 or higher
- Flask
- Requests
- Cohere Python SDK

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/multilingual-news-summarizer.git
    cd multilingual-news-summarizer
    ```

2. **Create a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up your API keys:**

    - Open [app.py](http://_vscodecontentref_/1) and replace `'your_news_api_key'` and `'your_cohere_api_key'` with your actual API keys.

5. **Run the application:**

    ```sh
    python app.py
    ```

6. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:5000/
    ```

## Usage

1. Enter a query to search for news articles.
2. Select a language from the dropdown menu.
3. Click the "Search" button to fetch and translate the news articles.

## Supported Languages

The application supports the following languages:

- Afrikaans
- Amharic
- Arabic
- Azerbaijani
- Belarusian
- Bengali
- Bulgarian
- Catalan
- Cebuano
- Czech
- Welsh
- Danish
- German
- Greek
- Esperanto
- Estonian
- Basque
- Finnish
- Tagalog
- French
- Western Frisian
- Scottish Gaelic
- Irish
- Galician
- Gujarati
- Haitian Creole
- Hausa
- Hebrew
- Hindi
- Hungarian
- Armenian
- Igbo
- Indonesian
- Icelandic
- Italian
- Javanese
- Japanese
- Kannada
- Georgian
- Kazakh
- Khmer
- Kyrgyz
- Korean
- Kurdish
- Lao
- Latvian
- Latin
- Lithuanian
- Luxembourgish
- Malayalam
- Marathi
- Macedonian
- Malagasy
- Maltese
- Mongolian
- Maori
- Malay
- Burmese
- Nepali
- Dutch
- Norwegian
- Northern Sotho
- Chichewa
- Oriya
- Punjabi
- Persian
- Polish
- Portuguese
- Pashto
- Romanian
- Russian
- Sinhala
- Slovak
- Slovenian
- Samoan
- Shona
- Sindhi
- Somali
- Southern Sotho
- Spanish
- Albanian
- Serbian
- Sundanese
- Swahili
- Swedish
- Tamil
- Telugu
- Tajik
- Thai
- Turkish
- Twi
- Ukrainian
- Urdu
- Uzbek
- Vietnamese
- Xhosa
- Yiddish
- Yoruba
- Chinese
- Zulu

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [News API](https://newsapi.org/)
- [Cohere](https://cohere.ai/)
