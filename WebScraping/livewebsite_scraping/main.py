from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
# print(response.text)
yc_news_site = response.text

soup = BeautifulSoup(yc_news_site,"html.parser")
print(soup.title)

# story_list = soup.select(selector=" .titleline a")
# print(story_list)

# for story in story_list:
#     print(story.getText())

first_story = soup.select_one(selector=".titleline>a")
# print(first_story)
article_text = first_story.getText()
article_link = first_story.get("href")

articlue_sub_text = soup.select_one(selector=".subtext .subline .score")
article_upvote = articlue_sub_text.getText()

# print(f"Article Title : {article_text} \n article link : {article_link} \n article upvote : {article_upvote}")


all_stories = soup.select(selector=".titleline>a")
all_stories_sub_text = soup.select(selector=".subtext .subline .score")
article_texts = []
article_links = []
for story in all_stories:
    article_texts.append(story.getText())
    article_links.append(story.get("href"))
votes= []
for sub_text in all_stories_sub_text:
    votes.append(sub_text.getText())

# if len(article_links) == len(article_texts) == len(votes):
# print(len(article_links))
# print(len(article_texts))
# print(len(votes))
# print(article_links)
# print(article_texts)


# unsorted_up_votes = [int(item.split(' ')[0]) for item in votes]
# copy_of_sorted_up_votes = unsorted_up_votes.copy()
# copy_of_sorted_up_votes.sort()
# #print(copy_of_sorted_up_votes)
# # print(unsorted_up_votes)
# largest_vote = copy_of_sorted_up_votes[-1]
# print(unsorted_up_votes.index(largest_vote))
# topper = unsorted_up_votes.index(largest_vote)
# print(f"Top Article : \n title:{article_texts[topper]}\n link:{article_links[topper]}\n votes:{votes[topper]}")

#alternatively

upvotes = [int(item.split(' ')[0]) for item in votes]
largest = max(upvotes)
topper = upvotes.index(largest)
print(f"Top Article : \n title:{article_texts[topper]}\n link:{article_links[topper]}\n votes:{votes[topper]}")


# for i in range(len(article_links)):
#     print(f"article title : {article_texts[i]}\n article link : {article_links[i]} \n up votes : {votes[i]}")
