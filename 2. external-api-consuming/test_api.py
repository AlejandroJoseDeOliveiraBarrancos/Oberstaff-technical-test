#!/usr/bin/env python3
from datetime import datetime

from api_client import JSONPlaceholderAPI
from utils import display_post_titles, display_json_response


def test_api_functionality():
    print("Testing JSONPlaceholder API Consumer...")
    print("=" * 60)
    
    api = JSONPlaceholderAPI()
    
    print("\nTesting: Get posts from user (userId=1)")
    response = api.get_posts_by_user(1)
    
    if response.success:
        print(f"Retrieved {len(response.posts)} posts")
        
        print("\nTesting: Display post titles")
        display_post_titles(response.posts)
        
        print("\nTesting: Add new post")
        demo_title = f"Test Post - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        demo_content = "This is a test post created by the API consumer test script."
        
        add_response = api.add_new_post(demo_title, demo_content, 1)
        if add_response.success and add_response.post:
            print("New post created successfully")
            display_json_response(add_response.post, "New Post Response")
        
        print("\nTesting: Update post title")
        if response.posts:
            first_post_id = response.posts[0]['id']
            new_title = f"Updated Title - {datetime.now().strftime('%H:%M:%S')}"
            
            update_response = api.update_post_title(first_post_id, new_title)
            if update_response.success and update_response.post:
                print("Post title updated successfully")
                display_json_response(update_response.post, "Updated Post Response")
    
    print("\nAll tests completed successfully!")
    print("=" * 60)


def test_error_handling():
    print("\nTesting error handling...")
    print("=" * 60)
    
    api = JSONPlaceholderAPI()
    
    print("\nTesting invalid user ID...")
    response = api.get_posts_by_user(999)
    if not response.success:
        print("Correctly handled invalid user ID")
    
    print("\nTesting invalid post ID for update...")
    update_response = api.update_post_title(999, "Test Title")
    if not update_response.success:
        print("Correctly handled invalid post ID")
    
    print("Error handling tests completed!")


if __name__ == "__main__":
    try:
        test_api_functionality()
        test_error_handling()
        print("\nAll tests passed!")
        
    except Exception as e:
        print(f"\nTest failed with error: {e}")
        import traceback
        traceback.print_exc() 