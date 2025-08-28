# Stakeholder Memo - Predicting S&P with VIX

## 1. Overview of Project and Purpose
This project analyzed the relationship between the VIX and the S&P 500 index, focusing on feature engineering, outlier detection, time-series modeling, and risk evaluation. The purpose was to test predictive relationships between volatility and equity performance, while developing a reproducible pipeline (data ingestion, feature engineering, modeling, evaluation, and deployment setup). The final outputs include notebooks, APIs/dashboards, and documentation to support decision-making and stakeholder review.

## 2. Key Findings and Recommendations

### Findings

- Strong negative correlation between VIX and S&P 500 returns, consistent with market risk theory.  
- Outlier analysis flagged extreme volume days as potential distortions, especially around crisis events.  
- Regression models performed reasonably, but errors widened in high-volatility regimes.  
- Scenario and sensitivity analyses showed performance drop-offs when market conditions deviated significantly from training data.  

### Recommendations

- Use this model as a diagnostic tool rather than a standalone predictor.  
- Prioritize monitoring drift and outlier events in production to avoid misleading signals.  
- Consider ensemble methods or regime-switching models for robustness in volatile periods.  
- Maintain monthly retraining, with additional triggers tied to data drift (e.g. PSI ≥ 0.3) and error spikes (e.g. RMSE +20% above baseline).  

## 3. Assumptions and Limitations

### Assumptions 

- Historical relationships between VIX and S&P 500 remain partially stable in future contexts.  
- Data feeds remain reliable and schema-consistent (column naming, frequency).  
- Market behavior is approximated well enough by linear/TS models for short-term horizon evaluation.  

### Limitations

- Models are sensitive to structural breaks (e.g. COVID-19 shock).  
- Outliers and data gaps can heavily influence results if not continuously monitored.  
- Model scope is market specific but not directly generalizable to other asset classes without rework.  

## 4. Risks and Potential Issues

- **Schema drift**: Vendor changes in data format or missing fields.  
- **Increased nulls**: Data incompleteness may distort forecasts.  
- **Concept drift**: Crisis-driven regime shifts could break historical relationships.  
- **System reliability**: Deployment issues such as port conflicts, uptime failures.  
- **Business impact**: Misinterpretation of results during extreme volatility may lead to poor trading decisions.  

## 5. Instructions for Using Deliverables

- **Data and Features**: Use the merged VIX + S&P 500 dataset for consistent analysis. Pre-cleaning steps are included in notebooks.  
- **Notebooks**: Stages 07–11 walk through outlier detection, feature engineering, regression, and risk evaluation. Stages 13+ include deployment setup.  
- **APIs/Dashboards**: Flask service supports visualization of `log_sp500_close` and `vix_close` trends over time. Ensure `jinja2` compatibility patches are applied before running.  
- **Documentation**: Markdown guides detail how to rerun notebooks, assumptions/risks, and how to interact with outputs.  

## 6. Suggested Next Steps

-  **Productionization**: Deploy the API with load testing and containerization to ensure scalability.  
-  **Monitoring setup**: Implement four-layer monitoring (Data, Model, System, Business) with alerting thresholds.  
-  **Model enhancement**: Explore non-linear and regime-switching approaches to better capture crisis dynamics.  
-  **Stakeholder integration**: Connect dashboards to business workflows, ensuring clarity for non-technical audiences.  
-  **Governance**: Establish retraining cadence, ownership roles and issue-logging process.  
