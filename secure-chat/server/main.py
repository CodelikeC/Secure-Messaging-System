from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

from websocket_server import websocket_router 
from routes.auth_routes import router as auth_router 
from database import init_db 

app = FastAPI(
    title= "Secure Messaging System", 
    version = "1.0.0"
)

#initialize database 

init_db()

#CORS 
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"]
)

# Routes 
app.include_router(auth_router)
app.include_router(websocket_router)

@app.get("/")
async def root():
    return {
        "status": "Secure messaging Server Running"
    }