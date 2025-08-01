import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:8000"

def test_health_check():
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Health check: {response.status_code} - {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

def test_webhook_receiver():
    webhook_data = {
        "event": "user.created",
        "message": "New user registered successfully",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/webhook",
            json=webhook_data,
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Webhook test: {response.status_code}")
        if response.status_code == 200:
            result = response.json()
            print(f"Response: {json.dumps(result, indent=2)}")
            return True
        else:
            print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"Webhook test failed: {e}")
        return False

def test_get_webhooks():
    try:
        response = requests.get(f"{BASE_URL}/webhooks")
        print(f"Get webhooks: {response.status_code}")
        if response.status_code == 200:
            webhooks = response.json()
            print(f"Found {len(webhooks)} webhook logs")
            return True
        else:
            print(f"Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"Get webhooks failed: {e}")
        return False

def main():
    print("Testing Bayma Webhook Receiver...")
    print("=" * 40)
    
    if not test_health_check():
        print("Health check failed. Make sure the server is running.")
        return
    
    if test_webhook_receiver():
        print("Webhook receiver test passed!")
    else:
        print("Webhook receiver test failed!")
    
    if test_get_webhooks():
        print("Get webhooks test passed!")
    else:
        print("Get webhooks test failed!")
    
    print("=" * 40)
    print("Testing completed!")

if __name__ == "__main__":
    main() 