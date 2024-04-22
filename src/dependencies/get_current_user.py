# dependencies/get_current_user.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session
from models.user import UserModel
from database import get_db
import jwt
from jwt import DecodeError
from jwt import ExpiredSignatureError
#from jwt import (jwt, DecodeError, ExpiredSignatureError)
#from jwt import DecodeError, ExpiredSignatureError # We import specific exceptions to handle them explicitly (DecodeError,)
from config.environment import secret

# HTTP Bearer scheme for Authorization header
http_bearer = HTTPBearer()

def get_current_user(db: Session = Depends(get_db), token: str = Depends(http_bearer)):
    

    try:
       
        payload = jwt.decode(token.credentials, secret, algorithms=["HS256"])

        
        user = db.query(UserModel).filter(UserModel.id == payload.get("sub")).first()

        
        if not user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Invalid username or password")

    
    except DecodeError as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail=f'Could not decode token: {str(e)}')

    #If the token has expired, we also raise an HTTP 403 Forbidden error
    except ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail='Token has expired')

    # If everything is successful, we return the user
    return user


