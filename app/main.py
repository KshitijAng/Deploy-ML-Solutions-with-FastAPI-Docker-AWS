from sentence_transformers import SentenceTransformer
from app.functions import returnSearchResultIndexes
from fastapi import FastAPI
from sklearn.metrics import DistanceMetric

import polars as pl
import numpy as np

# Define Embedding Model
model_name = "all-MiniLM-L6-v2"
path = "app/data/" + model_name
model = SentenceTransformer(path)

# Load Video Index
df = pl.scan_parquet('app/data/video-index.parquet') # Loads a lazy frame (LazyFrame), which does not load the data immediately.

# Create FastAPI Object
app = FastAPI()

@app.get("/")
def health_check():
    return {'health_check' : 'OK'}

@app.get("/info")
def info():
    return {'name' : 'yt-search', 'description': "Search API for Shaw Talebi's YouTube videos"}

@app.get("/search")
def search(query: str):
    idx_res = returnSearchResultIndexes(query,df, model)
    return df.select(['title', 'video_id']).collect()[idx_res].to_dict(as_series=False)
