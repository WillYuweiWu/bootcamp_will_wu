# Impact of VIX on Option Prices

## Problem Statement

One key attraction of options, compared to their underlying assets and other forms of financial assets, is their potential to generate returns on the volatility of the underlying. Therefore, in the pricing of options, volatility is always taken into account. However, most pricing models only consider the volatility with respect to the asssets themselves, but leave the market volatility overlooked. 

This Volatility Index (VIX) is a widely recognized quantifier of the market volatility. It also reflects investors' expectation of the future market risk. Therefore, this project seeks to explore the relationship between the VIX and the option prices with the underlying being included in the basket of the VIX. 

## Stakeholder & User

- Primary Stakeholder: hedgefunds, asset management, and trading companies. 
- End users: quantitative researchers, algorithmic traders, industrial professionals and students. 

## Useful Answer & Decision

- This project aims to explore the **causal** relationship between VIX and options prices and form a **predictive** model between the two. 
- The metric for VIX is the index itself and the metric for option prices is the nominal dollar prices. 
- The project shall explore the causal relationship using scatterplot first, followed by different types of regression models. 

## Assumptions & Constraints

- This project should assume a consistent and popular pricing method of options (e.g. Black-Scholes) that takes the asset volatility into account. Therefore, the assumptions of the pricing model also applies to this project (e.g. no arbitrage, risk-neutral, etc.). 
- The VIX is computed using a certain basket of asset volatilities (similar to CPI) that may or may not be biased towards certain industries, which means that its biggest constraint is the limit extent of representation of the whole market. 

## Known Unknowns / Risks

- It is very likely that market risk (quantified by VIX) would have an impact on options prices in the future, but the biggest unknown is the reaction time and duration of reaction. 
- Time series analysis would be used to address the uncertainty above. 

## Lifecycle Mapping

- Understand VIX and option prices → Problem Framing & Scoping (Stage 01) → A stakeholder memo in `docs`. 
- Gather VIX and option prices data → Data Aquisition, Storage, and Processing (Stage 04-06) → A clean dataset in `data`. 
- Causal analyses → Data Analysis and Visualization (Stage 07-12) → Plots, outputs, and predictive models in `deliverables`. 

## Repo Plan

- `data`: raw data of VIX and options prices
- `notebooks`: Jupyter notebooks for causal analyses
- `docs`: documents such as stakeholder memo, reports, and presentations 
- `deliverables`: plots, outputs, and other data visualization forms