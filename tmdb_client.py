import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "a93968a6d7a5e1a0b5a89566dd70f8cb"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    print(response)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

