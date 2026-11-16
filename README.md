# Option Pricing & Portfolio Risk Model

A quantitative finance script in Python (`NumPy`, `SciPy`) that prices a European call option and estimates 1-day tail risk for a $1M portfolio position.

## Features
- **Black-Scholes Analytical Pricing:** Computes closed-form European call prices.
- **Monte Carlo Simulation (GBM):** Simulates 100,000 Geometric Brownian Motion paths to verify convergence against the analytical price.
- **Market Risk Metrics:** Calculates 1-Day 99% Value-at-Risk (VaR) and Conditional VaR (CVaR / Expected Shortfall).

## Sample Output
- **Black-Scholes vs. Monte Carlo:** `BS: $8.0214 | MC: $8.0416 | Error: $0.0203 (0.25%)`
- **Risk Metrics:** `1D 99% VaR: $28,651.44 | 1D 99% CVaR: $32,776.43`
