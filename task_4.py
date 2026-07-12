employees = [
    {"name": "Олена", "department": "Marketing", "salary":
        25000},
    {"name": "Ігор", "department": "IT", "salary": 55000},
    {"name": "Наталія", "department": "Marketing", "salary":
        28000},
    {"name": "Олег", "department": "HR", "salary": 22000},
    {"name": "Андрій", "department": "IT", "salary": 48000},
    {"name": "Марія", "department": "IT", "salary": 52000},
]

def get_department_stats(employee_list, target_dept):
    department_stats = []
    for employee in employee_list:
        if employee["department"] == target_dept:
            department_stats.append(employee)

    length = len(department_stats)
    average = sum(employee["salary"] for employee in department_stats) / length

    department_stats = sorted(department_stats, key=lambda x: x["salary"], reverse=True)
    best_name = department_stats[0]["name"]

    return {
        "department": target_dept,
        "average": round(average, 2),
        "best_name": best_name,
        "count": length
    }


it = get_department_stats(employees, "IT")
marketing = get_department_stats(employees, "Marketing")
print(it)
print(marketing)
