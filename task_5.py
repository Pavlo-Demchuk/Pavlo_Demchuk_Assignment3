import json

sales_data = [
    {"product": "Смартфон", "category": "Електроніка",
     "quantity": 1, "price": 15000},
    {"product": "Книга 'Python для всіх'", "category":
        "Книги", "quantity": 2, "price": 700},
    {"product": "Навушники", "category": "Електроніка",
     "quantity": 2, "price": 2500},
    {"product": "Чайник", "category": "Побутова техніка",
     "quantity": 1, "price": 1200},
    {"product": "Книга 'Алгоритми'", "category": "Книги",
     "quantity": 1, "price": 900},
    {"product": "Ноутбук", "category": "Електроніка",
     "quantity": 1, "price": 32000}
]

category_report = {}
for c in sales_data:
    category = c["category"]
    if category not in category_report.keys():
        category_report[category] = {"total_revenue": 0, "total_items_sold": 0}
    revenue = c["quantity"] * c["price"]
    category_report[category]["total_revenue"] += revenue
    category_report[category]["total_items_sold"] += c["quantity"]

dumped_json = json.dumps(category_report, indent=4, ensure_ascii=False)
print(dumped_json)
