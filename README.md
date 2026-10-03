# restaurant-budget-allocation
Data-driven allocation of a ₹2,00,000 raw material budget across restaurant ingredients using Pandas, NumPy, Seaborn and Matplotlib.



# Restaurant Raw Material Budget Allocation

Allocating a fixed purchasing budget (₹2,00,000) across 12 raw items based on dish sales data, instead of splitting it equally.

## Problem
Splitting a budget equally across all ingredients ignores customer demand. This leads to wasted stock, tied-up capital and poor decisions. The budget should follow demand.

## Dataset
- Synthetic data of 2,000 restaurant orders, generated with NumPy
- Columns: `Gender`, `Ordered_dishes`, `Base_Price`, `Total_bill`
- 9 dishes, with `Total_bill` being the base price plus an extra charge
- Because the data is synthetic, the findings illustrate the method and are not real business results

## Method
1. Group orders by dish to get total revenue and number of orders
2. Calculate each dish's revenue share and order share
3. Dish budget = (0.7 × revenue share + 0.3 × order share) × total budget
4. Split each dish's budget across raw items using an estimated recipe table
5. Add up each raw item's budget across all dishes

The 70/30 weights and the recipe percentages are assumptions. They can be changed at the top of the notebook.

## Key Observations
- Mutton Biryani earns the highest revenue (18.5%) but has low order volume (9.8%), so a revenue-only allocation would overstate its budget
- Paneer Butter Masala and Chicken Biryani are the most-ordered dishes, with similar but not identical sales
- Mean and median are close, so the sales values are roughly symmetric. Bill amounts are not normally distributed, because fixed menu prices create several peaks (Shapiro-Wilk p ≈ 0)

## Result
| Raw item | Budget (₹) | Share |
|---|---|---|
| Chicken | 42,717 | 21.4% |
| Mutton | 36,306 | 18.2% |
| All spices | 19,943 | 10.0% |
| Paneer | 16,976 | 8.5% |
| Butter | 16,579 | 8.3% |
| Basmathi rice | 13,446 | 6.7% |
| Dal | 11,955 | 6.0% |
| Maida Flour | 10,253 | 5.1% |
| Browies | 9,445 | 4.7% |
| Corn Flour | 7,743 | 3.9% |
| Ice Cream | 7,728 | 3.9% |
| Biriyani Spices | 6,912 | 3.5% |

## Tech Stack
Python, Pandas, NumPy, Seaborn, Matplotlib

## How to Run
```bash
pip install -r requirements.txt
jupyter notebook Budget_allocation_to_items_based_on_data.ipynb
```

## Limitations and Future Work
- Replace the estimated recipe split with real ingredient costs from purchase bills
- Add wastage and shelf-life into the allocation
- Test different revenue/order weights and compare the outcomes

## Author
[Eswar sai ] · [https://www.linkedin.com/in/eswarsai-ootla/]
