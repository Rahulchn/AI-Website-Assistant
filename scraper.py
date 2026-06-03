import requests
from bs4 import BeautifulSoup
import pickle
import re

def clean_content(text):


    text = re.sub(r'\s+', ' ', text)

    return text.strip()

def scrape_website(url):

    try:

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "html.parser")


        for tag in soup(["script", "style"]):
            tag.extract()

        website_text = soup.get_text(separator=" ")

        cleaned_text = clean_content(website_text)

        return cleaned_text

    except Exception as e:
        print("Error:", e)
        return None


website_url = input("Enter Website URL: ")

website_data = scrape_website(website_url)

if website_data:

    data_dictionary = {
        "context": website_data
    }

    with open("data_store.pkl", "wb") as file:

        pickle.dump(data_dictionary, file)

    print("\nWebsite data stored successfully!")
