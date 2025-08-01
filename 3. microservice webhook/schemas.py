from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class WebhookRequest(BaseModel):
    event: str = Field(..., description="Event type")
    message: str = Field(..., description="Event message")
    timestamp: str = Field(..., description="Event timestamp")

class WebhookResponse(BaseModel):
    status: str = Field(default="ok", description="Response status")
    received: WebhookRequest = Field(..., description="Received webhook data")

class WebhookLogResponse(BaseModel):
    id: int
    event: str
    message: str
    timestamp: str
    received_at: str
    
    class Config:
        from_attributes = True 