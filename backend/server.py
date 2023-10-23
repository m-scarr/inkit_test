from uuid import uuid4
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = FastAPI()

origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(CORSMiddleware, allow_origins=origins)


@app.get("/doc_info")
def get_doc_info():
    return {
        "uuid": str(uuid4()),
        "document_name": "an example document",
        "created_at": datetime.now(),
        "description": "This is an example description!",
        "expires_at": datetime.now() + relativedelta(months=+1)
    }
