import requests
from typing import Dict, List, Optional
from config import BASE_URL, HEADERS
from models import PostsResponse, PostResponse


class JSONPlaceholderAPI:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(HEADERS)
    
    def get_posts_by_user(self, user_id: int) -> PostsResponse:
        try:
            url = f"{BASE_URL}/posts"
            params = {'userId': user_id}
            
            print(f"Fetching posts for user ID: {user_id}")
            response = self.session.get(url, params=params)
            response.raise_for_status()
            
            posts = response.json()
            print(f"Successfully retrieved {len(posts)} posts for user {user_id}")
            return PostsResponse(posts)
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching posts: {e}")
            return PostsResponse([], str(e))
    
    def add_new_post(self, title: str, content: str, user_id: int = 1) -> PostResponse:
        try:
            url = f"{BASE_URL}/posts"
            post_data = {
                'title': title,
                'body': content,
                'userId': user_id
            }
            
            print(f"Adding new post for user {user_id}...")
            print(f"Title: {title}")
            
            response = self.session.post(url, json=post_data)
            response.raise_for_status()
            
            result = response.json()
            print("Post added successfully!")
            return PostResponse(result)
            
        except requests.exceptions.RequestException as e:
            print(f"Error adding post: {e}")
            return PostResponse(None, str(e))
    
    def update_post_title(self, post_id: int, new_title: str) -> PostResponse:
        try:
            url = f"{BASE_URL}/posts/{post_id}"
            
            print(f"Fetching current post data for ID: {post_id}")
            get_response = self.session.get(url)
            get_response.raise_for_status()
            current_post = get_response.json()
            
            updated_data = current_post.copy()
            updated_data['title'] = new_title
            
            print(f"Updating post {post_id} title to: {new_title}")
            
            response = self.session.put(url, json=updated_data)
            response.raise_for_status()
            
            result = response.json()
            print("Post title updated successfully!")
            return PostResponse(result)
            
        except requests.exceptions.RequestException as e:
            print(f"Error updating post: {e}")
            return PostResponse(None, str(e)) 