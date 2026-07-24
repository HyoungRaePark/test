# =====================================================
# 프롬프트 비교 실습 - 미션 1. 대충 요청해 보기 (1차 시도) 
# =====================================================
# 1) "로그 파싱하는 파이썬 코드 줘" 를 AI에게 그대로 보내세요.
# 2) AI가 준 코드를 아래에 붙여넣고 실행해 보세요.
#
# 실행 후 기록해 보기:
# - AI가 어떤 로그 형식을 가정했나? Apache/Nginx를 가정하고 로그를 파싱했습니다.
# - 외부 라이브러리를 쓰라고 하지는 않았나? re 정규표현식 사용했다.
# - 내가 원하는 값(IP, 시각, URL, 상태코드)이 나오나? 한번에 몸통으로 줬다. 

# TODO: AI가 준 코드를 여기에 붙여넣으세요.
import re
from pathlib import Path

log_path = Path(__file__).parent / "access_mini.log"

log_pattern = re.compile(
    r'(?P<ip>\S+)\s+-\s+-\s+'
    r'\[(?P<datetime>[^\]]+)\]\s+'
    r'"(?P<method>\S+)\s+'
    r'(?P<path>\S+)\s+'
    r'(?P<protocol>[^"]+)"\s+'
    r'(?P<status>\d{3})\s+'
    r'(?P<size>\d+)'
)

with open(log_path, "r", encoding="utf-8") as f:
    for line_number, line in enumerate(f, start=1):
        line = line.strip()

        if not line:
            continue

        match = log_pattern.fullmatch(line)

        if match:
            print(match.groupdict())
        else:
            print(f"{line_number}번째 줄 파싱 실패: {line}")