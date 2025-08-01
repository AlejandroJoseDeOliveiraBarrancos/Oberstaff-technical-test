from fastapi import APIRouter
from typing import List

from controllers import WebhookController
from schemas import WebhookRequest, WebhookResponse, WebhookLogResponse

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Bayma Webhook Receiver is running"}

@router.post("/webhook", response_model=WebhookResponse)
async def receive_webhook(webhook_data: WebhookRequest):
    return await WebhookController.receive_webhook(webhook_data)

@router.get("/webhooks", response_model=List[WebhookLogResponse])
async def get_webhook_logs(skip: int = 0, limit: int = 100):
    return await WebhookController.get_webhook_logs(skip, limit)

@router.get("/webhooks/{webhook_id}", response_model=WebhookLogResponse)
async def get_webhook_log(webhook_id: int):
    return await WebhookController.get_webhook_log(webhook_id) 