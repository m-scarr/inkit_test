import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000","http://127.0.0.1:3000"], allow_methods=["*"], allow_headers=["*"])

generated_uuids = set()

@app.get("/getData")
def root():
    new_uuid = str(uuid.uuid4())
    while new_uuid in generated_uuids:
        new_uuid = str(uuid.uuid4())
    generated_uuids.add(new_uuid)
    return {
            "uuid": new_uuid,
            "document_name": "example.pdf",
            "created_at": datetime.now(),
            "description": "This is an example description!",
            "expires_at": datetime.now() + relativedelta(months=+1)
            }