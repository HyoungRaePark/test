# =====================================================
# 프롬프트 비교 실습 - 미션 2. 4원칙을 적용해 요청하기
# =====================================================
# 1) 2차 시도 프롬프트를 AI에게 보내세요. (수정해도 좋아요)
# 2) AI가 준 코드를 아래에 붙여넣고 실행해 보세요.
#
# 실행 후 기록해 보기:
# - 미션 1과 2의 가장 큰 차이 / 일단 눈에 보기 편하게 index 증가값으로 몇 줄인지 구분, 어느줄에서 에러가 뜨는지 알수있다. 또한 전체횟수에서의 성공도 알수있다.
# - 4원칙 중 결과에 가장 크게 영향을 준 것 / 로그 파싱의 파일을 정확하게 재지정 , 분석하기 편하게 재구현을 요청했다.
# - 다음에 프롬프트 쓸 때 꼭 넣을 것 / 파일을 불러온다면 해당 파일명을 미리 기재, 경로를 지정 해야한다.

# TODO: AI가 준 코드를 여기에 붙여넣으세요.

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

success = 0
fail = 0

with open(log_path, encoding="utf-8") as f:
    for line_num, line in enumerate(f, start=1):
        line = line.strip()

        if not line:
            continue

        match = log_pattern.match(line)

        if match:
            log = match.groupdict()

            print("\n")
            print(f"[{line_num}]")
            print(f"IP      : {log['ip']}")
            print(f"시간    : {log['datetime']}")
            print(f"메서드  : {log['method']}")
            print(f"URL     : {log['url']}")
            print(f"상태코드: {log['status']}")
            print(f"크기    : {log['size']}")
            print("\n")
            print("-" * 40)

            success += 1

        else:
            print(f"[{line_num}] 파싱 실패 -> {line}")
            fail += 1

# print("\n===== 결과 =====")
# print(f"성공 : {success}")
# print(f"실패 : {fail}")

# --- 미션 3: 비정상 입력 테스트 ---
# 위 코드를 붙여넣은 뒤, 아래 주석을 풀고 실행해 보세요. 
# 💥 에러가 나는 게 정상입니다!
# 에러 메시지 + 문제 입력을 "좋은 수정 요청" 형식으로 AI에게 전달하고,
# 형식에 맞지 않는 줄이 들어오면 None을 반환하도록 수정을 요청하세요.
#
# print(parse_line('127.0.0.1 - - [07/Jul/2026:10:23:45 +0900] "GET /index.html HTTP/1.1" 200 1043'))
# print(parse_line(""))                        # 빈 줄
# print(parse_line("### broken line ###"))     # 형식이 깨진 줄
