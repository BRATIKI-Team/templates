from typing import Annotated
from fastapi import Depends, FastAPI, Body, Query
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.services.index_service import IndexService
from app.services.query_service import QueryService

app = FastAPI()

load_dotenv()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/index")
async def index(index_service: Annotated[IndexService, Depends(IndexService)]):
    index_service.index()

@app.get("/query")
async def query(
    query: Annotated[str, Query(...)],
    query_service: Annotated[QueryService, Depends(QueryService)]):
    return query_service.query(query)
