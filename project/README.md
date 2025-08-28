# Impact of VIX on Stock Index (S&P 500)

## Problem Statement

This Volatility Index (VIX) is a widely recognized quantifier of the market volatility, reflecting investors' expectation of the future market risk. It is also referred to as the "panic index". Therefore, this project seeks to explore the relationship between the VIX and the most famous stock index in the world (S&P 500) to see if the panic effect manifested through VIX impacts the overall stock market performance, and if the VIX is indeed a good indicator and predictor of the stock market. 

## Stakeholder & User

- Primary Stakeholder: hedgefunds, asset management, and trading companies. 
- End users: quantitative researchers, algorithmic traders, industrial professionals and students. 

## Useful Answer & Decision

- This project aims to explore the **causal** relationship between VIX and S&P 500 and form a **predictive** model between the two. 
- The metrics for VIX and for S&P 500 are the indicies themselves. 
- The project shall explore the causal relationship using scatterplot first, followed by different types of regression models. 

## Assumptions & Constraints

- Both the VIX and the S&P 500 are computed using a certain basket of assets that may or may not be biased towards certain industries, which means that its biggest constraint is the limit extent of representation of the whole market. 

## Known Unknowns / Risks

- It is very likely that market risk (quantified by VIX) would have an impact on stock prices in the future, but the biggest unknown is the reaction time and duration of reaction. 
- Time series analysis would be used to address the uncertainty above. 

## Lifecycle Mapping

- Understand VIX and S&P 500 → Problem Framing & Scoping (Stage 01) → A stakeholder memo in `docs`
- Gather VIX and S&P 500 data → Data Aquisition, Storage, and Processing (Stage 04-06) → A clean dataset in `data` and useful functions in `src`
- Causal analyses → Data Analysis and Visualization (Stage 07-12) → Plots, outputs, and predictive models in `deliverables`

## Data Storage

### Folder Structure

- `data`
    - `raw`: storage place for raw data (CSV files)
    - `processed`: storage place for processed data (Parquet files)

### Formats Used

- **CSV**: used for raw data
    - Easy to read, widely supported by various languages and tools, friendly for sharing and inspection
    - Larger file size and subsequent slower read/write speed, everything becomes text until parsed
- **Parquet**: used for processed data
    - Highly compressed, faster read/write speed, optimized for analytics
    - Not readable, requires extra libraries, more complex to set up

### Read / Write

- **CSV** files: read with `.read_csv()` and written with `.to_csv()`
- **Parquet** files: read with `.read_parquet()` and written with `.to_parquet()`

## Repo Plan

- `data`: raw and processed data of VIX and S&P 500
- `notebooks`: Jupyter notebooks for causal analyses
- `docs`: documents such as stakeholder memo, reports, and presentations 
- `deliverables`: plots, outputs, and other data visualization forms
- `src`: useful functions and explanation markdown files
- `README.md`, `.env`, `.gitignore`, and other required & system files