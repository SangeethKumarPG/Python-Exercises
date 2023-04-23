from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")


soup = BeautifulSoup(response.text,"html.parser")
top_100_movies = soup.select(selector=".article-title-description>.article-title-description__text>.title")
movie_list = [item.getText() for item in top_100_movies]
movie_list_reversed = movie_list[::-1]
print(movie_list_reversed)
with open("WebScraping/MustWatch100Movies/movies.txt","w") as file:
    for movie in movie_list_reversed:
        file.write(movie)
        file.write("\n")
