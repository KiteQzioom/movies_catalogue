import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhOTM5NjhhNmQ3YTVlMWEwYjVhODk1NjZkZDcwZjhjYiIsInN1YiI6IjYxYTgwM2FiMDU4MjI0MDA0MmI3MjYxMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lYzSUgWc5e7VirADMqvF98a3Hm3nqaAZJYqyp9tppEk"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    print(response)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"
