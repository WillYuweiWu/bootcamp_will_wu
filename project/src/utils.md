# `get_summary_stats`

## Purpose

This function generates a statistical summary of all numeric columns in a DataFrame and also reports the number of missing values.

## Rationale

- Filters only numeric columns using `select_dtypes(include='number')`
- Runs `.describe()` to compute standard summary statistics
- Transposes the result so that each row corresponds to a column, making it easier to read.
- Adds a new column called `missing` showing how many values are `NaN` for each numeric column
- Resets the index and renames the column label from `'index'` to `'column'` for clarity

## Output

A DataFrame where each row represents one numeric column, with summary statistics and the count of missing values. 

# `pick_category_column`

## Purpose

This function automatically selects a likely categorical column from a DataFrame, which is often useful for grouping or classification tasks.

## Rationale

- Defines a preferred list of common categorical names
- Converts column names to lowercase for easier matching
- If one of the preferred names exists in the DataFrame, it returns that column name
- If not, it looks for the first non-numeric column in the DataFrame and returns it
- If no non-numeric column exists, returns `None`

## Output

The name of a column most likely representing categories or `None` if none are found. 