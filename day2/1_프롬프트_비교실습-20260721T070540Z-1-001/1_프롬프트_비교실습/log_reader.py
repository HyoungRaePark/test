# =====================================================
# 프롬프트 비교 실습 - 심화미션. 파일 전체 파싱
# =====================================================
# 지금까지는 로그 한 줄을 처리했지만, 실제 서버 로그는 쌓여서 파일이 됩니다.
# 어제 배운 파일 읽기와 오늘 만든 parse_line을 합쳐 파일 전체를 파싱합니다.
# 직접 작성해도 좋고, AI에게 시켜도 좋습니다.
#
# 요구사항
#   - access_mini.log 파일을 한줄씩 읽어 parse_line으로 파싱한다.
#   - 결과가 none이면 건너뛰고, 전체 줄 수와 파싱 성공한 줄, 건너띈 줄을 센다.
#
# 기대 출력
#   전체 줄 수 : 15
#   파싱 성공 : 12
#   건너뛴 줄 : 3

# --- 1. 완성한 parse_line 함수 붙여넣기 ---
# TODO: log_parser_v3.py에서 완성한 parse_line 함수를 붙여넣으세요

import re
from pathlib import Path

log_path = Path(__file__).parent / "access_mini.log"

log_pattern = re.compile(
    r'(?P<ip>\S+)\s+-\s+-\s+'
    r'\[(?P<datetime>[^\]]+)\]\s+'
    r'"(?P<method>\S+)\s+'
    r'(?P<url>\S+)\s+'
    r'(?P<protocol>[^"]+)"\s+'
    r'(?P<status>\d{3})\s+'
    r'(?P<size>\d+)'
)


def parse_line(line):
    match = log_pattern.match(line.strip())

    if match:
        return match.groupdict()

    return None

# --- 2. 파일 전체 파싱하기 ---
# TODO: AI가 준 코드를 여기에 붙여넣으세요. 직접 작성해봐도 좋습니다.
total = 0
success = 0
fail = 0

print(f"\n")

with open(log_path, "r", encoding="utf-8") as f:
    for line in f:
        total += 1
        result = parse_line(line)

        if result:
            success += 1
            print(result)
            # 필요한 값만 보고 싶다면
            # print(result["ip"], result["status"], result["url"])
        else:
            print(f"\n파싱 실패: {line.strip()}\n")
            fail += 1


print(f"\n전체: {total}")
print(f"파싱성공: {success}")
print(f"건너뛴 줄: {fail}")
print(f"\n")

# git status
# git add .
# git commit -m "수정 내용"
# # git push