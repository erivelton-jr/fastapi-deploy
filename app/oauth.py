from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException

oauthscheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauthscheme)):
    if not token == 'usuario':
        raise HTTPException(
            status_code=401,
            detail="Token não é valido.",
            headers={"WWW-Authenticate": "Basic"},
        )
