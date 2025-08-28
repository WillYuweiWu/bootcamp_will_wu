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

## Stage 05 - Data Storage

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

## Stage 06 - Data Preprocessing

In `cleaning.py`, I create 3 functions for my cleaning strategy:

1. `fill_missing_median`
    - **Purpose**: replace `NaN` values in a numeric column with that column's median. 
    - **Return**: a new dataframe with missing data filled.  

2. `drop_missing`
    - **Purpose**: remove rows with missing values. 
    - In this case, use `thresh = 0.1`: drop the rows that has more than 10% values missing. 
    - **Return**: a new dataframe with these rows removed. 
    
3. `normalize_data`
    - **Purpose**: scale numeric data so columns are comparable. 
    - Uses the `zscore` method so that a column $\sim \mathcal{N} (\mu = 0, \sigma = 1)$. 
    - **Return**: a new dataframe that's normalized. 

When handling the actual dataset, I only use the first 2 functions, since no column needs to be normalized at this stage. 

## Stage 07 - Outlier Analysis

### Outlier Assumptions

- The IQR method assumes that the distribution is reasonably symmetric and that values lying beyond 1.5 × IQR from the quartiles are unusually extreme. It works well for skewed but not heavily tailed distributions.

- The Z-Score method assumes normality of the data. Values more than $3\sigma$ from $\mu$ are flagged as outliers. This method may mis-identify points if the underlying distribution is skewed. 

- Winsorization assumes that extreme values are likely noise or errors, not genuine signals, and caps them into a centrain boundary, in this case the 5th – 95th percentile. This prevents extreme values from dominating summary statistics, but assumes trimming extremes does not discard meaningful information.

### Potential Risks

- High trading volumes for the S&P 500 might not always be errors but rather reflections of market events. Treating them as outliers risks discarding meaningful signals.

- The cutoff values are arbitrary. Different thresholds may classify different observations as outliers, leading to inconsistent results.

- Removing or winsorizing outliers alters the distribution, variance, and correlation structure. This can understate the true volatility of trading activity.

## Stage 09 - Feature Engineering

### Rationale

1. `log_sp500_close`

    - Financial indices are typically non-stationary and could grow exponentially over time. Taking the log stabilizes variance, compresses large values, and makes percentage changes additive.
    - Since the VIX is often seen as the panic index, it tends to spike when equity markets fall. Looking at `log_sp500_close` makes the relationship between changes in VIX and the S&P more interpretable in scatterplots.

2. `vix_delta`, `sp500_delta`

    - Instead of absolute price levels, daily changes capture the market’s short-term movement.
    - The scatterplot of `vix_delta` v.s. `sp500_delta` highlights the inverse relationship: when the S&P 500 drops, the VIX usually jumps. This captures the core dynamic: volatility rises during downturns and falls during rallies.

3. `vix_spread`, `sp500_spread`

    - The high-low spread within a day reflects market volatility and trading range. These features measure the “turbulence” of each index, independent of closing direction.
    - The scatterplot of `vix_spread` v.s. `sp500_spread` helps explore whether days of high uncertainty in the VIX coincide with wide trading ranges in the S&P 500. If a positive relationship exists, it suggests that intraday instability in equities and perceived volatility move together.

### Connecion to Problem

The problem is to understand the relationship between VIX and S&P 500.

- Log transformation normalizes the scale, ensuring the relationship isn’t distorted by long-term S&P growth.
- Delta features directly test the short-term inverse correlation.
- Spread features capture market instability, helping identify whether volatility manifests as wider trading ranges in both indices simultaneously.

## Repo Plan

- `data`: raw and processed data of VIX and S&P 500
- `notebooks`: Jupyter notebooks for causal analyses
- `docs`: documents such as stakeholder memo, reports, and presentations 
- `deliverables`: plots, outputs, and other data visualization forms
- `src`: useful functions and explanation markdown files
- `README.md`, `.env`, `.gitignore`, and other required & system files