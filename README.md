# Article Clustering
## Description

The Article Clustering App is a web application that clusters news articles based on their content similarity using machine learning algorithms. The app uses scraped news articles from the New York Times, preprocesses the text data, applies a clustering algorithm, and displays the clustered articles on the web page. It provides users with an organized view of related news articles, making it easier to navigate and explore different topics.

## Features

- Clustering: The app cluster the news articles based on their content similarity.
- Display: The app displays the clustered articles on the web page, allowing users to explore related articles conveniently.

## Packages Used

This project has used some packages which have to be installed to run this web app locally present in `requirements.txt` file. 

## Installation

To run the project locally, there is a need to have Visual Studio Code (vs code) installed on your PC:

- **[vs code](https://code.visualstudio.com/download)**: It is a source-code editor made by Microsoft with the Electron Framework, for Windows, Linux, and macOS.

## Usage

1. Clone the project 

``` bash
git clone https://github.com/AdrineUWERA/article_clustering.git

```

2. Open the project with vs code

``` bash
cd article_clustering
code .
```

3. Install the required dependencies

``` bash
pip install -r requirements.txt
```


4. Run the project

``` bash
streamlit run app.py
```

5. Use the link printed in the terminal to visualise the app. (Usually `http://localhost:8501`)

## Important Notes
- The app is designed to cluster specifically with only for the already fetched articles

## Authors and Acknowledgment

- Adrine Uwera 

## License
[MIT](https://choosealicense.com/licenses/mit/)
