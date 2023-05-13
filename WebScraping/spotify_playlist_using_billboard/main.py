from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100/"
CLIENT_ID = ""
CLIENT_SECRET = ""
ID = ''



date = input("Enter a date in YYYY-MM-DD format")
# date = "2020-06-01"
request_url = BILLBOARD_BASE_URL+date
print(request_url)
bill_board_response = requests.get(request_url)

soup = BeautifulSoup(bill_board_response.text,"html.parser")


raw_song_list = soup.select(selector=".lrv-u-width-100p #title-of-a-story")

test_list = [item.getText().replace('\n','').replace('\t','') for item in raw_song_list]
final_list = test_list[:100]

#------------------------ Artist List ----------------------#
# raw_artist_list = soup.select(selector="div.pmc-paywall > div > div > div > div.chart-results-list.\/\/.lrv-u-padding-t-150.lrv-u-padding-t-050\@mobile-max > div> ul > li.lrv-u-width-100p > ul > li.o-chart-results-list__item.\/\/.lrv-u-flex-grow-1.lrv-u-flex.lrv-u-flex-direction-column.lrv-u-justify-content-center.lrv-u-border-b-1.u-border-b-0\@mobile-max.lrv-u-border-color-grey-light.lrv-u-padding-l-050.lrv-u-padding-l-1\@mobile-max > span")
# test_artist_list = [item.getText().replace('\n','').replace('\t','') for item in raw_artist_list]
# first_artist = soup.select(selector="div.pmc-paywall > div > div > div > div.chart-results-list.\/\/.lrv-u-padding-t-150.lrv-u-padding-t-050\@mobile-max > div:nth-child(2) > ul > li.lrv-u-width-100p > ul > li.o-chart-results-list__item.\/\/.lrv-u-flex-grow-1.lrv-u-flex.lrv-u-flex-direction-column.lrv-u-justify-content-center.lrv-u-border-b-1.u-border-b-0\@mobile-max.lrv-u-border-color-grey-light.lrv-u-padding-l-1\@mobile-max > span")
# for a in first_artist:
#     top_artist = a.getText().replace('\n','').replace('\t','')
#     print(top_artist)

# final_artist_list = []
# final_artist_list.append(top_artist)
# for item in test_artist_list:
#     final_artist_list.append(item)



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID, client_secret=CLIENT_SECRET,redirect_uri="http://localhost:8888/callback", scope="playlist-modify-private",show_dialog=True, cache_path='WebScraping/spotify_playlist_using_billboard/token.txt'))
user_id = sp.current_user()
print(user_id)
# sp.user_playlist_create(user=ID,name="BillBoardTop2020BySangeeth",public=False,description="A playlist of 2020 top billboard songs")
res = sp.user_playlist_create(user=ID,name=f"BillBoardTop{date}BySangeeth",public=False,description="A playlist of 2020 top billboard songs")
# print(res)
playlist_id = res.get('id')
# print(playlist_id)
song_uri_list = []
for songs in final_list:
    try:
        result = sp.search(q=f"track:{songs} year:{date.split('-')[0]}", limit=1)
        song_uri_list.append(result.get("tracks").get("items")[0].get("uri"))
    except Exception:
        pass

sp.playlist_add_items(playlist_id=playlist_id, items=song_uri_list)



