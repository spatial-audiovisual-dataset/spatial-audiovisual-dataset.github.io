"""
merged_by_sample_0506.json에서 지정된 샘플들을 삭제하는 스크립트
"""
import json
from pathlib import Path

INPUT_FILE = Path(__file__).parent / "merged_by_sample_0506.json"
OUTPUT_FILE = INPUT_FILE  # 덮어쓰기

SAMPLES_TO_REMOVE = [
    "00808-y9hTuugGdiq_011_006",
    "00824-Dd4bFSTQ8gi_007_000",
    "00827-BAbdmeyTvMZ_008_012",
    "00832-qyAac8rV8Zk_007_013",
    "00853-5cdEh9F2hJL_007_004",
    "00862-LT9Jq6dN3Ea_010_005",
    "00873-bxsVRursffK_008_012",
    "00877-4ok3usBNeis_004_012",
    "00891-cvZr5TUy5C5_015_006",
]


def main():
    with open(INPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    before = len(data)
    removed = []
    not_found = []

    for sample_id in SAMPLES_TO_REMOVE:
        if sample_id in data:
            del data[sample_id]
            removed.append(sample_id)
        else:
            not_found.append(sample_id)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"변경 전 샘플 수: {before}")
    print(f"삭제된 샘플 수: {len(removed)}")
    for s in removed:
        print(f"  ✓ {s}")
    if not_found:
        print(f"찾지 못한 샘플:")
        for s in not_found:
            print(f"  ✗ {s}")
    print(f"변경 후 샘플 수: {len(data)}")
    print(f"저장 완료: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
