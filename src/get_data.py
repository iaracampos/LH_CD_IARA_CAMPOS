import pandas as pd
import requests
from tqdm import tqdm  
import os
from dotenv import load_dotenv

def get_tmdb_data(title, year):
    url = "https://api.themoviedb.org/3/search/movie"
    
    load_dotenv()  
    api_key = os.getenv("TMDB_API_KEY")

    response = requests.get(url, params={
        "api_key": api_key,
        "query": title,
        "year": year,
    })

    data = response.json()

    if data['results']:
        tmdb_id = data["results"][0]["id"]
        details_url = f"https://api.themoviedb.org/3/movie/{tmdb_id}"
        details_response = requests.get(details_url, params={
            "api_key": api_key,
            "language": "en-US"
        })
        details = details_response.json()

        return {
            "budget": details.get('budget'),
            "popularity": details.get('popularity'),
            "vote_count": details.get('vote_count'),
            "revenue": details.get('revenue'),
        }
    return None
    

def main():

    df = pd.read_csv("./data/processed/movies_processed.csv")
    #inicializando com null
    df['tmdb_budget'] = None
    df['tmdb_popularity'] = None
    df['tmdb_vote_count'] = None
    df['tmdb_revenue'] = None

    for i, row in tqdm(df.iterrows(), total=len(df)):
        title = row['Title']
        year = row['Year']
        movie_feat= get_tmdb_data(title, year)
        
        if movie_feat:
            df.at[i, 'tmdb_budget'] = movie_feat['budget']
            df.at[i, 'tmdb_popularity'] = movie_feat['popularity']
            df.at[i, 'tmdb_vote_count'] = movie_feat['vote_count']
            df.at[i, 'tmdb_revenue'] = movie_feat['revenue']

    df.to_csv("./data/processed/movies_with_tmdb.csv", index=False)


if __name__ == "__main__":
    main()