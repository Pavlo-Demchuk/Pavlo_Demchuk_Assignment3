import json

exam_results = [
    {"student_name": "Анна", "score": 91},
    {"student_name": "Богдан", "score": 58},
    {"student_name": "Вікторія", "score": 75},
    {"student_name": "Григорій", "score": 45}
]
passing_score = 60  # Прохідний бал

for s in exam_results:
    if s["score"] >= passing_score:
        s["score"] = True
    else:
        s["score"] = False

dumped_json = json.dumps(exam_results, indent=2, ensure_ascii=False)
print(dumped_json)
