# REST API Reference

## POST /auth/register

Register a new user.

### Request

{
  "username": "alice",
  "password": "password",
  "public_key": "..."
}

### Response

{
  "message": "User registered successfully"
}

---

## POST /auth/login

### Request

{
  "username": "alice",
  "password": "password"
}

### Response

{
  "token": "jwt"
}

---

## GET /auth/public-key/{username}

Returns the user's public key.