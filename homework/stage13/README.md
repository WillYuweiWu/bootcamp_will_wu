# Stage 13 - Productization

## Project Overview and Objectives

This project investigates the relationship between the VIX and the S&P 500 Index, moving from raw data collection to productized services. This stage extends the project from exploratory notebooks into a productized environment with:

- A Flask API that exposes predictive functionality and visualization endpoints.
- Two visualization functions and API routes:
  - `log_sp500_close vs time`
  - `vix_close vs time`
- Integration of outlier handling, feature engineering, and evaluation into reproducible services.

## How to Rerun Scripts / Notebooks

1. **Environment Setup**

    - Install requirements:
     ```
     pip install -r requirements.txt
     ```
    - Ensure data file `VIX_S&P500_features.csv` exists in `../data/processed/`.

2. **Rerun Notebooks**

    - Run each notebook in order. 
    - Use “Restart & Run All” in Jupyter to guarantee clean, reproducible runs.

3. **Launching Flask API**
    
    - Run the Step 6 cell in `stage13_productization.ipynb`.
    - Guard is in place to prevent “address already in use” errors; API will remain active on `http://127.0.0.1:5005`.

## Assumptions, Risks, and Lifecycle Mapping

- **Assumptions**

    - Input data follows the schema used during training (`log_sp500_close`, `vix_close`, etc.).
    - Features are numeric and aligned to the same scale as in model development.

- **Risks**

    - Model performance may degrade in high-volatility regimes (market shocks).
    - Imputation assumptions may underrepresent uncertainty when missing values are not random.
    - API endpoints assume trusted internal use; no authentication is included.

## Instructions for Using APIs / Dashboards

### API Endpoints
Once the Flask server is running:

- **Health Check**

    - `GET /health`: returns API status and available features.

- **Prediction**

    - `POST /predict` with JSON:
    ```json
    {
      "features": {"vix_close": 15.2, "sp500_close": 5200.0}
    }
    ```
    - Returns predicted value.

- **Time-Series Plots**
    - `GET /plot/sp500`: returns inline chart for `log_sp500_close vs time`.
    - `GET /plot/vix`: returns inline chart for `vix_close vs time`.

### Dashboards

- The `/plot/...` endpoints serve HTML with inline `.png` charts.
- Save the returned HTML locally (`plot_sp500.html`, `plot_vix.html`) and open in a browser for inspection.
- Extendable to a simple dashboard framework if needed.
