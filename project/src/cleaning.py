import pandas as pd
import numpy as np

def fill_missing_median(df: pd.DataFrame, cols = None) -> pd.DataFrame:
    out = df.copy()
    for c in _numeric_cols(out, cols):
        out[c] = out[c].fillna(out[c].median())
    return out

def drop_missing(df: pd.DataFrame, how: str = 'any', thresh: int | None = None, subset = None) -> pd.DataFrame:
    if thresh is not None:
        return df.dropna(thresh = thresh, subset = subset)
    return df.dropna(how = how, subset = subset)

def normalize_data(df: pd.DataFrame, cols = None, method: str = 'zscore') -> pd.DataFrame:
    out = df.copy()
    for c in _numeric_cols(out, cols):
        s = out[c].astype(float)
        if method == "zscore":
            mean = s.mean()
            std = s.std(ddof = 0) or 1.0
            out[c] = (s - mean) / std
        elif method == "minmax":
            mn, mx = s.min(), s.max()
            rng = (mx - mn) or 1.0
            out[c] = (s - mn) / rng
        else:
            raise ValueError("method must be 'zscore' or 'minmax'")
    return out