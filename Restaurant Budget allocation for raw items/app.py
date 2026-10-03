import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

TOTAL_BUDGET = 200000
W_REVENUE = 0.7
W_ORDERS = 1 - W_REVENUE

df = pd.read_csv(r"D:\Restaurant_customer_data (1).xls")

Total_sales = df.groupby('Ordered_dishes')['Total_bill'].sum()
Total_items_sold = df.groupby('Ordered_dishes')['Total_bill'].count()

rev_share = Total_sales / Total_sales.sum()
ord_share = Total_items_sold / Total_items_sold.sum()

dish_budget = (W_REVENUE * rev_share + W_ORDERS * ord_share) * TOTAL_BUDGET
print(dish_budget.round(0).sort_values(ascending=False))

recipe = {
    "Mutton Biriyani":        {"Mutton":55, "Basmathi rice":22, "Biriyani Spices":12, "All spices":6,  "Butter":5},
    "Mutton Curry":           {"Mutton":75, "All spices":15, "Butter":10},
    "Paneer Butter masala":   {"Paneer":65, "Butter":20, "All spices":15},
    "Chicken Biryani":        {"Chicken":50, "Basmathi rice":25, "Biriyani Spices":12, "All spices":8, "Butter":5},
    "Chicken 65":             {"Chicken":70, "Corn Flour":15, "Maida Flour":5, "All spices":10},
    "Chicken Machurian":      {"Chicken":65, "Corn Flour":20, "All spices":15},
    "Dal Makhani":            {"Dal":65, "Butter":20, "All spices":15},
    "Brownie With Ice Cream": {"Ice Cream":45, "Browies":55},
    "Butter Nan":             {"Maida Flour":80, "Butter":20},
}

for dish, ingredients in recipe.items():
    assert sum(ingredients.values()) == 100, dish

recipe_df = pd.DataFrame(recipe).T.fillna(0) / 100

raw_budget = recipe_df.mul(dish_budget, axis=0).sum().sort_values(ascending=False)
print("*" * 50)
result = pd.DataFrame({
    "Budget (Rs)": raw_budget.round(0),
    "Share %": (raw_budget / TOTAL_BUDGET * 100).round(1)
})
print("Raw Material Budget Allocation:")
print(result)
print("Total:", raw_budget.sum().round(0))

plt.figure(figsize=(9, 5))
sns.histplot(df['Total_bill'], bins=30, kde=True, color='skyblue', edgecolor='black')
plt.title('Distribution of Total Bill', fontweight='bold')
plt.xlabel('Total bill (₹)')
plt.ylabel('Number of orders')
plt.tight_layout()
plt.show()