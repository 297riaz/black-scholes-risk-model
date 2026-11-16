import numpy as np
from scipy.stats import norm

np.random.seed(42)
S0, K, T, r, sigma, n_sims, port_val = 100.0, 105.0, 1.0, 0.05, 0.20, 100_000, 1_000_000

# Black-Scholes Analytical Price
d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = d1 - sigma * np.sqrt(T)
bs_price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

# Monte Carlo European Call (GBM)
Z = np.random.standard_normal(n_sims)
ST = S0 * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)
payoffs = np.exp(-r * T) * np.maximum(ST - K, 0)
mc_price = np.mean(payoffs)
error = abs(mc_price - bs_price)

# 1-Day 99% VaR & CVaR ($1M Position)
dt = 1 / 252
S_1d = port_val * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * np.random.standard_normal(n_sims))
pnl = S_1d - port_val
var_99 = -np.percentile(pnl, 1)
cvar_99 = -np.mean(pnl[pnl <= -var_99])

print(f"BS: ${bs_price:.4f} | MC: ${mc_price:.4f} | Error: ${error:.4f} ({error/bs_price:.2%})")
print(f"1D 99% VaR: ${var_99:,.2f} | 1D 99% CVaR: ${cvar_99:,.2f}")