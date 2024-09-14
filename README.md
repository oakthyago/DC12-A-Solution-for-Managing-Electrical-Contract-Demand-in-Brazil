**My undergraduate thesis (TCC)**

# DC12

DC12 is a data-driven solution for managing Electrical Contract Demand in Brazil, with a focus on optimizing power usage and costs for industrial sectors.

## Introduction

This project marks an initial step into the world of machine learning and data science. The data has been organized and modeled effectively to deliver actionable insights.



## Understanding Electrical Demand

In Brazil, industrial sectors face a unique billing system based on electrical demand. While energy consumption is easy to grasp — for example, a 100W lamp consumes 100W/h (watts per hour) — demand is slightly more complex.

### Example:
If you use a 100W lamp for 8 hours a day over 30 days, the total consumption is:
- **100W × 8 hours/day × 30 days = 24,000W (24 kWh) per month**.

## What is Demand?

Demand refers to the peak power required over a specific period, usually the maximum in a given month. For instance, if you have 8 lamps rated at 100W each, but only ever turn on 4 lamps at once, your demand for the month is 400W. However, if at any moment you turn on all 8 lamps, even for just a second, your peak demand for that month would be 800W.

## Annual Demand Contract

Electricity providers in Brazil require companies to sign an annual demand contract, which predicts how much power your business will require. This is critical for ensuring supply reliability and comes with specific billing rules.

For instance, if your company signs a 100kW demand contract:
- If your actual demand is **100kW or lower**, you'll be charged for the contracted 100kW.
- If your demand exceeds **100kW**, you'll incur a penalty. This is usually 3 times the rate for each kilowatt over the contracted amount.

### Example:
If your demand for a month reaches **120kW**, you'll pay for:
- 100kW (contracted) + (20kW × 3) = 160kW total.

---

This repository presents a foundation for analyzing and managing electrical demand more efficiently, leveraging data science and automation for better decision-making.
