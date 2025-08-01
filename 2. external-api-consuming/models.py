from typing import Dict, List, Optional
from dataclasses import dataclass


@dataclass
class Post:
    id: int
    title: str
    body: str
    userId: int


@dataclass
class CreatePostRequest:
    title: str
    body: str
    userId: int


@dataclass
class UpdatePostRequest:
    id: int
    title: str
    body: str
    userId: int


class APIResponse:
    def __init__(self, success: bool, data: Optional[Dict] = None, error: Optional[str] = None):
        self.success = success
        self.data = data
        self.error = error


class PostsResponse(APIResponse):
    def __init__(self, posts: List[Dict], error: Optional[str] = None):
        super().__init__(success=bool(posts), data={'posts': posts}, error=error)
        self.posts = posts


class PostResponse(APIResponse):
    def __init__(self, post: Optional[Dict], error: Optional[str] = None):
        super().__init__(success=bool(post), data=post, error=error)
        self.post = post 