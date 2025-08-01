#!/usr/bin/env python3
from datetime import datetime
from typing import Dict, List

from api_client import JSONPlaceholderAPI
from config import DEFAULT_USER_ID, MENU_OPTIONS
from utils import (
    print_menu_header, display_post_titles, display_json_response,
    get_user_input, validate_not_empty, validate_integer
)


class APIConsumerApp:
    def __init__(self):
        self.api = JSONPlaceholderAPI()
        self.user_id = DEFAULT_USER_ID
    
    def show_menu(self) -> None:
        print_menu_header("JSONPlaceholder API Consumer")
        for key, value in MENU_OPTIONS.items():
            print(f"{key}. {value}")
        print_menu_header("")
    
    def get_user_posts(self) -> List[Dict]:
        response = self.api.get_posts_by_user(self.user_id)
        return response.posts if response.success else []
    
    def add_post_interactive(self) -> None:
        print("\nCreating new post...")
        
        title = get_user_input(
            "Enter post title: ",
            validator=validate_not_empty,
            error_message="Title cannot be empty!"
        )
        if not title:
            return
        
        content = get_user_input(
            "Enter post content: ",
            validator=validate_not_empty,
            error_message="Content cannot be empty!"
        )
        if not content:
            return
        
        user_id_input = get_user_input(f"Enter user ID (default: {self.user_id}): ")
        if user_id_input:
            if validate_integer(user_id_input):
                user_id = int(user_id_input)
            else:
                print("Invalid user ID, using default.")
                user_id = self.user_id
        else:
            user_id = self.user_id
        
        response = self.api.add_new_post(title, content, user_id)
        if response.success and response.post:
            display_json_response(response.post, "New Post Response")
    
    def update_post_interactive(self) -> None:
        print("\nUpdating post title...")
        
        post_id_input = get_user_input(
            "Enter post ID to update: ",
            validator=validate_not_empty,
            error_message="Post ID cannot be empty!"
        )
        if not post_id_input:
            return
        
        if not validate_integer(post_id_input):
            print("Invalid post ID!")
            return
        
        post_id = int(post_id_input)
        
        new_title = get_user_input(
            "Enter new title: ",
            validator=validate_not_empty,
            error_message="New title cannot be empty!"
        )
        if not new_title:
            return
        
        response = self.api.update_post_title(post_id, new_title)
        if response.success and response.post:
            display_json_response(response.post, "Updated Post Response")
    
    def run_demo(self) -> None:
        print("\nRunning complete API demo...")
        
        posts = self.get_user_posts()
        display_post_titles(posts)
        
        demo_title = f"Demo Post - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        demo_content = "This is a demo post created by the API consumer script."
        
        response = self.api.add_new_post(demo_title, demo_content, self.user_id)
        if response.success and response.post:
            display_json_response(response.post, "New Post Response")
        
        if posts:
            first_post_id = posts[0]['id']
            new_title = f"Updated Title - {datetime.now().strftime('%H:%M:%S')}"
            
            update_response = self.api.update_post_title(first_post_id, new_title)
            if update_response.success and update_response.post:
                display_json_response(update_response.post, "Updated Post Response")
        
        print("\nDemo completed successfully!")
    
    def run(self) -> None:
        print("Starting JSONPlaceholder API Consumer...")
        
        try:
            while True:
                self.show_menu()
                choice = input("\nSelect an option (1-6): ").strip()
                
                if choice == '1':
                    posts = self.get_user_posts()
                    if posts:
                        display_json_response(posts, f"Posts for User {self.user_id}")
                
                elif choice == '2':
                    posts = self.get_user_posts()
                    display_post_titles(posts)
                
                elif choice == '3':
                    self.add_post_interactive()
                
                elif choice == '4':
                    self.update_post_interactive()
                
                elif choice == '5':
                    self.run_demo()
                
                elif choice == '6':
                    print("\nGoodbye!")
                    break
                
                else:
                    print("Invalid option. Please select 1-6.")
                
                input("\nPress Enter to continue...")
                
        except KeyboardInterrupt:
            print("\n\nApplication interrupted. Goodbye!")
        except Exception as e:
            print(f"\nUnexpected error: {e}")


def main():
    app = APIConsumerApp()
    app.run()


if __name__ == "__main__":
    main() 