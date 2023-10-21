import uuid
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = FastAPI()

origins = ["http://localhost:3000", "http://127.0.0.1:3000"]

app.add_middleware(CORSMiddleware, allow_origins=origins,
                   allow_methods=["*"], allow_headers=["*"])

#generated_uuids = set()


@app.get("/docInfo")
def getDocInfo():
    # guarantees a unique uuid each time, but this is terrible design, a better way to guarantee uniqueness would be a system that increments an integer.
    # new_uuid = str(uuid.uuid4())
    # while new_uuid in generated_uuids:
    #     new_uuid = str(uuid.uuid4())
    # generated_uuids.add(new_uuid)
    return {
        "uuid": str(uuid.uuid4()),
        "document_name": "an example document",
        "created_at": datetime.now(),
        "description": "This is an example description!",
        "expires_at": datetime.now() + relativedelta(months=+1)
    }
