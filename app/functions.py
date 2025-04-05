import numpy as np
import polars
from sklearn.metrics import pairwise_distances
from sentence_transformers import SentenceTransformer

# Helper function
def returnSearchResultIndexes(query: str, 
                        df: polars.lazyframe.frame.LazyFrame, 
                        model: SentenceTransformer) -> np.ndarray:
    """
    Function to return indexes of top search results
    """
    
    # Embed query
    query_embedding = model.encode(query).reshape(1, -1)
    
    # Convert LazyFrame to DataFrame for computation
    df_materialized = df.collect()
    
    # Compute distances between query and titles/transcripts
    dist_arr = (
        pairwise_distances(df_materialized.select(df.columns[4:388]).to_numpy(), query_embedding, metric="manhattan") +
        pairwise_distances(df_materialized.select(df.columns[388:]).to_numpy(), query_embedding, metric="manhattan")
    )

    # Search parameters
    threshold = 40  # Eyeballed threshold for Manhattan distance
    top_k = 5

    # Evaluate videos close to query based on threshold
    idx_below_threshold = np.argwhere(dist_arr.flatten() < threshold).flatten()
    # Keep top k closest videos
    idx_sorted = np.argsort(dist_arr[idx_below_threshold], axis=0).flatten()

    # Return indexes of search results
    return idx_below_threshold[idx_sorted][:top_k]
