"""
merged_by_sample_0506.json에서
AG_localization, EG_localization 태스크를 삭제하는 스크립트
"""
import json
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "merged_by_sample_0506.json"
OUTPUT_FILE = Path(__file__).parent / "merged_by_sample_0506.json"  # 덮어쓰기

TASKS_TO_REMOVE = ["AG_localization", "EG_localization"]


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    removed_counts = {task: 0 for task in TASKS_TO_REMOVE}

    for sample_id, sample in data.items():
        tasks = sample.get("tasks", {})
        for task_name in TASKS_TO_REMOVE:
            if task_name in tasks:
                del tasks[task_name]
                removed_counts[task_name] += 1

    # 결과 저장
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"총 샘플 수: {len(data)}")
    for task_name, count in removed_counts.items():
        print(f"  {task_name} 삭제: {count}건")
    print(f"저장 완료: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
