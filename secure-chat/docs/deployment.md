# Deployment Guide

## Requirements

Python 3.11+

---

## Install Dependencies

pip install -r requirements.txt

or

pip install .

---

## Start Server

cd server

uvicorn main:app --reload

---

## Start Client

cd client

python app.py

---

## Production Notes

Use:

- HTTPS
- Reverse Proxy
- TLS Certificates
- Dedicated Database

Do not use SQLite in production.