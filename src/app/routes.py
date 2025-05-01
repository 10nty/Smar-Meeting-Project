from fastapi import APIRouter, UploadFile, Form, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.services import process_text, process_audio
from app.auth import verify_password, create_access_token
from app.models import fake_users_db

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")

@router.post("/upload_text/")
async def upload_text(content: str = Form(...)):
    notes = await process_text(content)
    return {"meeting_notes": notes}

@router.post("/upload_audio/")
async def upload_audio(file: UploadFile):
    notes = await process_audio(file)
    return {"meeting_notes": notes}

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = create_access_token(data={"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}
