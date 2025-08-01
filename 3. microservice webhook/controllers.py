from fastapi import HTTPException
from typing import List
import logging

from storage import storage
from schemas import WebhookRequest, WebhookResponse, WebhookLogResponse

logger = logging.getLogger(__name__)

class WebhookController:
    @staticmethod
    async def receive_webhook(webhook_data: WebhookRequest):
        try:
            webhook_log = storage.add_webhook(
                webhook_data.event,
                webhook_data.message,
                webhook_data.timestamp
            )
            
            logger.info(f"Webhook received and saved: {webhook_data.event}")
            
            return WebhookResponse(
                status="ok",
                received=webhook_data
            )
            
        except Exception as e:
            logger.error(f"Error processing webhook: {str(e)}")
            raise HTTPException(status_code=500, detail="Internal server error")

    @staticmethod
    async def get_webhook_logs(skip: int = 0, limit: int = 100):
        try:
            webhooks = storage.get_webhooks(skip, limit)
            return webhooks
        except Exception as e:
            logger.error(f"Error retrieving webhook logs: {str(e)}")
            raise HTTPException(status_code=500, detail="Internal server error")

    @staticmethod
    async def get_webhook_log(webhook_id: int):
        try:
            webhook = storage.get_webhook_by_id(webhook_id)
            if not webhook:
                raise HTTPException(status_code=404, detail="Webhook log not found")
            return webhook
        except HTTPException:
            raise
        except Exception as e:
            logger.error(f"Error retrieving webhook log: {str(e)}")
            raise HTTPException(status_code=500, detail="Internal server error") 