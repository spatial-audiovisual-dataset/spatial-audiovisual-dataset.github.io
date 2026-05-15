"""
merged_by_sample_0506.json에서 특정 샘플의 특정 태스크만 삭제하는 스크립트
"""
import json
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "merged_by_sample_0506.json"
OUTPUT_FILE = INPUT_FILE

# {샘플ID: [삭제할 태스크들]}
TASKS_TO_REMOVE = {
    "00800-TEEsavR23oF_003_011": ["AG_direction", "AG_distance"],
    "00802-wcojb4TFT35_004_008": ["RR_hidden_source"],
    "00802-wcojb4TFT35_005_007": ["AG_direction", "AG_distance", "RR_proximity"],
    "00810-CrMo8WxCyVb_007_007": ["RR_hidden_source"],
    "00813-svBbv1Pavdk_010_011": ["RR_hidden_source"],
    "00824-Dd4bFSTQ8gi_007_012": ["AG_direction", "AG_distance", "RR_proximity"],
    "00831-yr17PDCnDDW_011_011": ["RR_loudness"],
    "00832-qyAac8rV8Zk_007_013": ["RR_loudness"],
    "00839-zt1RVoi7PcG_006_004": ["RR_loudness"],
    "00844-q5QZSEeHe5g_012_001": ["RR_loudness"],
    "00877-4ok3usBNeis_005_014": ["RR_hidden_source"],
    "00878-XB4GS9ShBRE_008_012": ["RR_hidden_source"],
}


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    total_removed = 0

    for sample_id, task_list in TASKS_TO_REMOVE.items():
        if sample_id not in data:
            print(f"  ✗ 샘플 없음: {sample_id}")
            continue
        tasks = data[sample_id].get("tasks", {})
        for task_name in task_list:
            if task_name in tasks:
                del tasks[task_name]
                print(f"  ✓ {sample_id} → {task_name} 삭제")
                total_removed += 1
            else:
                print(f"  ✗ {sample_id} → {task_name} 없음")

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\n총 {total_removed}개 태스크 삭제 완료")
    print(f"저장: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
