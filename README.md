# Oberstaff Technical Test

This repository contains three distinct technical assessments demonstrating different aspects of software development and API integration.

## Overview

The technical test consists of three independent projects, each showcasing different skills and technologies:

1. **Bayma Clients Python Script** - Data processing and CSV manipulation
2. **External API Consumer** - REST API integration and interactive CLI
3. **Microservice Webhook** - FastAPI microservice with in-memory storage

## Quick Start Guide

### Prerequisites
- Python 3.8+
- pip (Python package manager)

### Running All Tests

## Project Structure

```
Oberstaff-technical-test/
├── 1. bayma-clients-python-script/     # data processing
├── 2. external-api-consuming/          # API integration
├── 3. microservice webhook/            # FastAPI microservice
└── README.md
```
## Test 1: Bayma Clients Python Script

**Location:** `1. bayma-clients-python-script/`

### How to Run
```bash
cd "1. bayma-clients-python-script"
pip install -r requirements.txt
python bayma_clients.py
```

## Test 2: External API Consumer

**Location:** `2. external-api-consuming/`

### How to Run
```bash
cd "2. external-api-consuming"
pip install -r requirements.txt
python api_consumer.py
```

## Test 3: Microservice Webhook

**Location:** `3. microservice webhook/`

### How to Run
```bash
cd "3. microservice webhook"
pip install -r requirements.txt

python main.py

python test_webhook.py
```

### API Endpoints
- `GET /` - Health check
- `POST /webhook` - Receive webhook notifications
- `GET /webhooks` - Get all webhook logs
- `GET /webhooks/{id}` - Get specific webhook

### Postman Collection
Import `docs/Bayma_Webhook_Collection.json` into Postman for comprehensive API testing.

## Testing Each Project

### Test 1: CSV Processing
```bash
cd "1. bayma-clients-python-script"
python test_script.py
```

### Test 2: API Consumer
```bash
cd "2. external-api-consuming"
python test_api.py
```

### Test 3: Webhook Service
```bash
cd "3. microservice webhook"
python main.py  # Start server
python test_webhook.py  # Test API
```
## Notes for Reviewers

1. **Each project is independent** - they can be reviewed separately
2. **Focus on code quality** - clean, maintainable, and well-documented
3. **Check error handling** - robust error management is crucial
4. **Evaluate architecture** - proper separation of concerns
5. **Test functionality** - ensure all features work as expected

## Support

If you encounter any issues or have questions about the implementation, please refer to the individual README files in each project directory for detailed instructions. 