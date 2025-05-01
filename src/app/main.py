from fastapi import FastAPI
from app.routes import router
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
app = FastAPI(title="Smart Meeting Notes")
app.include_router(router)