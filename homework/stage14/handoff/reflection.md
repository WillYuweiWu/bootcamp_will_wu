# Stage 14 - Model Deployment Reflection

## Credible Failure Modes

- **Schema drift**: upstream data feed changes column names, order, or data types (e.g. `sp500_volume` missing).  
- **Increased nulls**: unexpected rise in missing values in `vix_close` or `sp500_close`.  
- **Concept drift**: statistical relationship between VIX and S&P 500 shifts during market crises.  
- **Label delay**: lag in receiving updated S&P 500 closing data from the vendor.  
- **System reliability**: API endpoint fails or experiences port conflicts.  

## Monitoring Metrics & Thresholds

- **Schema drift** → automated schema validation; trigger alert if required column missing or type mismatch.  
- **Increased nulls** → null percentage per column; warning at > 0.5%, critical at > 2%.  
- **Concept drift** → Population Stability Index (PSI) on `vix_close` and `sp500_close`; threshold > 0.3.  
- **Label delay** → freshness check on latest timestamp; alert if >1 business day behind.  
- **System reliability** → uptime/latency monitoring; warning if p95 latency > 300 ms, critical if > 500 ms or > 1% error rate.  

## Alert Recipients & Runbook First Step

- **Schema/nulls** → Data Engineering team. *Runbook step*: inspect data ingestion job, rerun or backfill missing values.  
- **Concept drift** → Data Science team. *Runbook step*: pause new deployments, run drift diagnostics, compare with baseline distributions.  
- **Label delay** → Data Engineering & DS jointly. *Runbook step*: verify ETL schedule, trigger manual refresh if needed.  
- **System reliability** → MLOps/SRE team. *Runbook step*: restart Flask container, check for port conflicts, redeploy if required.  

## Retraining Cadence & Triggers

- **Scheduled monthly retrain** with updated data.  
- **Immediate retrain** if:  
    - PSI > 0.3 on key features for 3+ consecutive days.  
    - Rolling 2-week RMSE > baseline by > 20%.  
    - Sustained spike in volatility (e.g. VIX in 90th percentile for 5+ trading days).  
    - Schema or pipeline modification.  

## Ownership & Handoffs
- **Data Engineering**: responsible for ingestion reliability, schema checks, logging issues in Jira.  
- **Data Science**: owns model dashboards, retraining pipeline, drift analysis, and rollback proposals.  
- **MLOps/SRE**: ensures API uptime, CI/CD pipelines, system health monitoring, and logs incidents in monitoring tools.  
- **Product/Risk stakeholders**: approve major rollbacks or strategy changes and receive weekly summary reports.  

## Monitoring Layers

- **Data layer**: schema validation, nulls %, freshness (lag in days), PSI for drift detection.  
- **Model layer**: RMSE, MAE, directional hit-rate, feature importance shifts, calibration curves.  
- **System layer**: API uptime, latency, memory/CPU utilization, container restarts, error codes.  
- **Business layer**: decision accuracy vs market outcomes, hedging/trading cost of false positives/negatives, financial value of predictions.  
