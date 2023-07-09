# DC12

DC12 is a solution for Electrical Contract Demand in Brazil.

## Introduction

The solution presented here is a first step towards machine learning and data science. Although I didn't spend much time on visual presentation using seaborn graphics, I was able to organize and model the data.

As the philosopher said, "It's better to get it done late than even later."

## Electrical Demand

In Brazil, the industrial sector has to deal with a different billing fee for electrical demand. Understanding electrical consumption is straightforward: if you light a lamp with a power rating of 100W, it means it will consume 100W/h (watts per hour). So, if the lamp is on for 8 hours a day and 30 days a month, the consumption will be 8 * 30 * 100W = 24,000W or 24kW per month for that lamp.

## Demand

Demand refers to the power required over a specific time period, typically the maximum demand within a month. For example, if you have 8 lamps rated at 100W/h each in your house, but you only light a maximum of 4 lamps simultaneously throughout the month, your demand for that month would be 400W. However, if for just one second during that month, you turn on all 8 lamps simultaneously, your demand for that month would be 800W.

## Annual Contract for Demand

Electricity distribution companies need to know how much energy your company will demand, which is a logistical challenge. To address this, a contract is made for a year. For example, if you have a 100kW demand contract:
- If your demand is 100kW or less, you will pay for the 100kW demand for that month.
- If your demand exceeds 100kW, you will pay a fee of 3 times (3x) for each unit of demand that exceeds the contracted amount.
  * For example, if your demand consumption for a month is 120kW, you will pay for 100kW + (20 * 3)kW = 160kW.
