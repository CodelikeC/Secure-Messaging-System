from fastapi import APIRouter, WebSocket, WebSocketDisconnect

import json
import time

websocket_router = APIRouter()

# Active connections
connected_clients = {}

# Replay protection
used_nonces = set()

async def relay_message(receiver, packet):

    if receiver in connected_clients:
        ws = connected_clients[receiver]
        await ws.send_text(json.dumps(packet))

@websocket_router.websocket("/ws/{username}")
async def websocket_endpoint(
    websocket: WebSocket,
    username: str
):

    await websocket.accept()

    connected_clients[username] = websocket

    print(f"[+] {username} connected")

    try:
        while True:

            data = await websocket.receive_json()

            # Basic validation
            required_fields = [
                "sender",
                "receiver",
                "ciphertext",
                "nonce",
                "signature",
                "timestamp"
            ]

            for field in required_fields:
                if field not in data:
                    await websocket.send_json({
                        "error": f"Missing field: {field}"
                    })
                    continue

            # Replay protection
            nonce = data["nonce"]

            if nonce in used_nonces:
                await websocket.send_json({
                    "error": "Replay attack detected"
                })
                continue

            used_nonces.add(nonce)

            # Timestamp validation
            current_time = int(time.time())

            if abs(current_time - data["timestamp"]) > 60:
                await websocket.send_json({
                    "error": "Packet expired"
                })
                continue

            # Store encrypted message only
            print(f"""
            Encrypted Message:
            From: {data['sender']}
            To: {data['receiver']}
            Ciphertext: {data['ciphertext']}
            """)

            # Relay encrypted packet
            await relay_message(
                data["receiver"],
                data
            )

    except WebSocketDisconnect:

        print(f"[-] {username} disconnected")

        if username in connected_clients:
            del connected_clients[username]
