from bs4 import BeautifulSoup
import requests
import json

# a list that will be storing the articles
articles = []  

# function to get the articles from the New York Times website and store them
def get_articles():
    try:
        url = "https://www.nytimes.com/section/world/?page=10"

        # uses get method of the requests module to fetch data from the new york times website
        page_html_data = requests.get(url)   

        # creates a parser instance
        soup = BeautifulSoup(page_html_data.content, "html.parser")  

        # retrieving all articles 
        # the html data for articles are embedded in the class "css-1l4spti".
        articles_details = soup.find_all("article", class_="css-1l4spti")    
        
        # loop through the html data of all articles to get each articles details separately
        for article_details in articles_details:
          article_description_tag = article_details.find("p", class_="css-1pga48a e15t083i1")
          if article_description_tag:
            # find the link of the article
            article_link = article_details.find("a", class_="css-8hzhxf").get('href')    

            # find the title of the article  
            article_title = article_details.find("h3", class_="css-1kv6qi e15t083i0").text.strip()     
            
            # find the description of the article
            article_description = article_details.find("p", class_="css-1pga48a e15t083i1").text.strip()     
            
            
            article_content = article_title + " - " + article_description 
           
            # create a JSON object containing article information
            article_json = {
              "link": f"https://www.nytimes.com/{article_link}",
              "title": article_title,
              "description": article_description,
              "content": article_content
            }
            
            # append the JSON object to the list of articles
            articles.append(article_json)

    except requests.exceptions.RequestException as e:
        print("Couldn't carry out the request!", e)

# call the function to get articles from the New York Times website
get_articles()

# Save articles as JSON file
with open('nyt_articles.json', 'w', encoding='utf-8') as json_file:
    json.dump(articles, json_file, ensure_ascii=False, indent=4)
