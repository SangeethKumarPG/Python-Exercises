import requests
class Post:

    def __init__(self):
        self.response = requests.get("https://api.npoint.io/66a01db051fc5b17179b")
        self.all_posts = self.response.json()


    def get_all(self):
        return self.all_posts

    def get_a_post(self,id):
        for post in self.all_posts:
            if post.get("id") == id:
                return post
        