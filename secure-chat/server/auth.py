import jwt 
from datetime import datetime, timedelta 

SECRET_KEY = "CHANGE_THIS_SECRET"
ALGORITHM = "HS256"

def create_token(username: str): 
    payload = {
        "sub": username, 
        "exp": datetime.utcnow() +timedelta(hours=12)
    }
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm = ALGORITHM
    )

def verify_token(token: str): 
    try: 
        payload = jwt.decode(
            token, 
            SECRET_KEY,
            algorithms =[ALGORITHM]
        )
        return payload["sub"]
    except jwt.PyJWTError: 
        return None 
    