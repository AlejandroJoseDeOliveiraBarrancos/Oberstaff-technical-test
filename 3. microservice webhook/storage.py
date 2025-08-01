from typing import List, Dict, Optional
from datetime import datetime
import uuid

class InMemoryStorage:
    def __init__(self):
        self.webhooks: List[Dict] = []
        self.max_webhooks = 1000
    
    def add_webhook(self, event: str, message: str, timestamp: str) -> Dict:
        webhook_id = len(self.webhooks) + 1
        webhook_data = {
            "id": webhook_id,
            "event": event,
            "message": message,
            "timestamp": timestamp,
            "received_at": datetime.utcnow().isoformat()
        }
        
        self.webhooks.append(webhook_data)
        
        if len(self.webhooks) > self.max_webhooks:
            self.webhooks.pop(0)
        
        return webhook_data
    
    def get_webhooks(self, skip: int = 0, limit: int = 100) -> List[Dict]:
        return self.webhooks[skip:skip + limit]
    
    def get_webhook_by_id(self, webhook_id: int) -> Optional[Dict]:
        for webhook in self.webhooks:
            if webhook["id"] == webhook_id:
                return webhook
        return None

storage = InMemoryStorage() 