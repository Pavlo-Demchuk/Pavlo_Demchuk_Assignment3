import json

deposit_account = {
    "client_id": "C1025",
    "balance": 5000.0,
    "currency": "UAH",
    "interest_rate": 0.08,  # 8% річних
    "is_active": True
}

deposit_account["balance"] += deposit_account.get("balance") * deposit_account.get("interest_rate")
deposit_account["last_update_type"] = "interest accrual"
deposit_account["is_active"] = False

dumped_json = json.dumps(deposit_account, indent=2)
print(dumped_json)
