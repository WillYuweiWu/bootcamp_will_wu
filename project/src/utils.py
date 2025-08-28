import pandas as pd

def get_summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    num = df.select_dtypes(include = 'number')
    desc = num.describe().T
    desc['missing'] = num.isna().sum().values
    return desc.reset_index().rename(columns = {'index': 'column'})

def pick_category_column(df: pd.DataFrame):
    preferred = ['category', 'categorical', 'group', 'class', 'segment', 'type', 'species']
    cols_lower = {c.lower(): c for c in df.columns}
    for p in preferred:
        if p in cols_lower:
            return cols_lower[p]
    non_num = df.select_dtypes(exclude = 'number').columns.tolist()
    return non_num[0] if non_num else None
