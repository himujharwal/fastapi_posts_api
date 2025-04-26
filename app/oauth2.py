
from jose import JWTError, jwt
from app import schemas, database, models
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status 
from sqlalchemy.orm import Session


ouath2_schem = OAuth2PasswordBearer(tokenUrl='login')
# It only tells FastAPI:
# "Clients will eventually get a token from /login, and once they have it, they'll send it as //Authorization: Bearer <token>// in every request that needs auth."


SECRET_KEY = '$2b$12$yQ.p7uKsAiOx/CbJrkWxGOuY.YTF.ssggvi'
ALOGIRTHM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTE = 60



def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTE)
    to_encode.update({"exp":expire})

    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALOGIRTHM)

    return  encoded_jwt


def verify_access_token(token: str, credentials_exception):

    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALOGIRTHM])

        id =  str(payload.get("user_id"))  # do not use type here you have to enforce the it i mean not id:str = payload(...)

        if id is None:
            raise credentials_exception
        
        token_data = schemas.TokenData(id = id)

    except JWTError:
        raise credentials_exception
    
    return token_data

def get_current_user(token:str = Depends(ouath2_schem), db:Session = Depends(database.get_db)):

    credentials_exception  = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"could not validate credentials",
                                           headers={"WWW-Authenticate":"Bearer"})
    
    token = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user




