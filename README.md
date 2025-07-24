# 🧠 Async Math Microservice

## 📌 Overview

This project is an asynchronous REST microservice built with **FastAPI** that performs key mathematical operations:
- Fibonacci sequence generation
- Factorial calculation
- Exponentiation (Power)

Each request is persisted in a **SQLite** database, logs are saved and made available via an endpoint, and results are cached for performance. It follows modern microservice practices with clear modular architecture, async worker handling, and API Key authorization.

---

## ✅ Requirements Analysis

### 1. Mathematical Operations (Required)
- **Implemented**: Fibonacci, Factorial, Power
- **Endpoints**: `/fib`, `/fact`, `/pow`
- **Worker Support**: Asynchronous logging using `asyncio.Queue`
- **Status**: ✅ Fully Implemented

### 2. Microservice with API Exposure (REST, not SOAP)
- **Framework**: FastAPI (lightweight async micro-framework)
- **API Type**: REST
- **Status**: ✅ Compliant

### 3. Database Integration
- **Tech Used**: SQLite via Tortoise ORM
- **Data Model**: `RequestLog` stores operation type, input, result, and timestamp
- **Status**: ✅ Implemented

### 4. Authorization
- **Implemented With**: API Key (`x-api-key: secret123`) via HTTP header
- **Status**: ✅ Compliant

### 5. Logging
- **Mechanism**: Logs written to `logs/app.log`
- **Endpoint**: `/logs` returns recent API calls
- **Status**: ✅ Implemented

### 6. Serialization / Deserialization
- **Library**: Pydantic models for request and response validation
- **Status**: ✅ Fulfilled

### 7. Caching / Optimization
- **Mechanism**: `functools.lru_cache` applied to math operations
- **Status**: ✅ Implemented

### 8. Code Structure (MVC/MVCS)
- **Routing Layer**: `routes.py`
- **Service Layer**: `math_ops.py`, `worker.py`, `logger.py`
- **Data Layer**: `schemas/operations.py`
- **Model Layer**: `models/request_log.py`, `db.py`
- **Status**: ✅ Clean, well-structured

### 9. Linting (flake8)
- **Config**: Present as `.flake8`
- **Check**: All files pass `flake8` checks successfully
- **Status**: ✅ Passed

---

## 🛠️ Tech Stack

- FastAPI
- SQLite + Tortoise ORM
- Pydantic
- `asyncio.Queue`
- lru_cache
- Logging module
- API Key Auth

---

## 🚀 How to Run

Make sure Python 3.10+ is installed, then run:

```bash
pip install -r requirements.txt && uvicorn main:app --reload