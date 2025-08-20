# Stage 05 - Data Storage

## Folder Structure

- `data`
    - `raw`: storage place for raw data (CSV files)
    - `processed`: storage place for processed data (Parquet files)
- `README.md`: this markdown file
- `stage05_data-storage.ipynb`: the Jupyter notebook that completes the required tasks

## Formats Used

- **CSV**: used for raw data
    - Easy to read, widely supported by various languages and tools, friendly for sharing and inspection
    - Larger file size and subsequent slower read/write speed, everything becomes text until parsed
- **Parquet**: used for processed data
    - Highly compressed, faster read/write speed, optimized for analytics
    - Not readable, requires extra libraries, more complex to set up

## Reads/Writes

- **CSV** files: read with `.read_csv()` and written with `.to_csv()`
- **Parquet** files: read with `.read_parquet()` and written with `.to_parquet()`

## Validation Checks

- `shape_equal`: checks if the reloaded dataframe has the same shape as the original
- `date_is_datetime`: checks if the dates are parsed as class `datetime64`
- `price_is_numeric`: checks if the prices are numeric
