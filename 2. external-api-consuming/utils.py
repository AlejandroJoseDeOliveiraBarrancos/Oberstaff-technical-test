import json
from typing import Dict, List
from config import DISPLAY_WIDTH


def print_separator(width: int = DISPLAY_WIDTH, char: str = "=") -> None:
    print(char * width)


def print_menu_header(title: str) -> None:
    print_separator()
    print(title)
    print_separator()


def display_post_titles(posts: List[Dict]) -> None:
    if not posts:
        print("No posts to display.")
        return
    
    print("\nPost Titles:")
    print_separator()
    
    for i, post in enumerate(posts, 1):
        title = post.get('title', 'No title')
        post_id = post.get('id', 'N/A')
        print(f"{i:2d}. [{post_id}] {title}")
    
    print_separator()
    print(f"Total: {len(posts)} posts\n")


def display_json_response(data: Dict, title: str = "API Response") -> None:
    print(f"\n{title}")
    print_separator()
    print(json.dumps(data, indent=2, ensure_ascii=False))
    print_separator()


def get_user_input(prompt: str, validator=None, error_message: str = None) -> str:
    while True:
        user_input = input(prompt).strip()
        
        if validator is None:
            return user_input
        
        if validator(user_input):
            return user_input
        else:
            print(error_message or "Invalid input.d Please try again.")


def validate_not_empty(value: str) -> bool:
    return bool(value and value.strip())


def validate_integer(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False 