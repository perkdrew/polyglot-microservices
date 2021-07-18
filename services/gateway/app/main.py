from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI( 
    title="Polyglot API",
    description="These are the polyglot microservices.",
    docs_url = "/docs",
    redoc = "/redoc")

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)