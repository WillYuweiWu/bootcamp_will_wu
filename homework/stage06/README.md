# Stage 06 - Data Processing

## Cleaning Strategy

1. `fill_missing_median(df, cols = None)`
    - **Purpose**: replace `NaN` values in a numeric column with that column's median. 
    - **Return**: a new dataframe with missing data filled.  

2. `drop_missing(df, how = 'any', thresh = None, subset = None)`
    - **Purpose**: remove rows with missing values. 
    - In this case, use `thresh = 0.5`: drop the rows that has more than 50% values missing. 
    - **Return**: a new dataframe with these rows removed. 

3. `normalize_data(df, cols = None, method = 'zscore'`
    - **Purpose**: scale numeric data so columns are comparable. 
    - Uses the `zscore` method so that a column $\sim \mathcal{N} (\mu = 0, \sigma = 1)$. 
    - **Return**: a new dataframe that's normalized. 

The cleaning strategy follows the order listed. 
