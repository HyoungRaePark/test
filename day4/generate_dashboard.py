# -*- coding: utf-8 -*-
# =====================================================
# 차트 만들기 실습 - generate_dashboard.py
#  - 같은 폴더에 results.json, dashboard_template.html 필요
# ★ 꾸미기는 index.html이 아니라 dashboard_template.html을 수정!
#   (index.html은 생성물이라 다음 실행 때 덮어써집니다)
# =====================================================
import json


# 1. 집계 결과 읽기
with open("results.json", "r", encoding="utf-8") as f:
    results = json.load(f)

# 2. 템플릿 읽기
with open("dashboard_template.html", "r", encoding="utf-8") as f:
    html = f.read()

# 3. 상태코드 데이터 삽입 (완성된 예시)
status_counts = results["status_counts"]

# 상태 코드 숫자 기준으로 오름차순 정렬
sorted_status = sorted(status_counts.items(), key=lambda x: int(x[0]))

status_labels = [status for status, count in sorted_status]
status_data = [count for status, count in sorted_status]

html = html.replace("__STATUS_LABELS__", json.dumps(status_labels))
html = html.replace("__STATUS_DATA__", json.dumps(status_data))

# 4. TODO: 시간대별 데이터 삽입
#    results["hourly_counts"] 를 시(hour) 순서로 정렬해
#    __HOURLY_LABELS__ 와 __HOURLY_DATA__ 를 치환하세요.
hourly_counts = results["hourly_counts"]
sorted_hours = sorted(hourly_counts.items())

hourly_labels = [hour for hour, count in sorted_hours]
hourly_data = [count for hour, count in sorted_hours]

html = html.replace("__HOURLY_LABELS__", json.dumps(hourly_labels))
html = html.replace("__HOURLY_DATA__", json.dumps(hourly_data))

# 5. TODO: 에러 URL TOP 5 데이터 삽입
#    results["top_error_urls"] 는 [URL, 횟수] 쌍의 리스트입니다.
#    URL 리스트와 횟수 리스트로 나눠
#    __ERROR_LABELS__ 와 __ERROR_DATA__ 를 치환하세요.
error_counts = results["top_error_urls"]

error_labels = [url for url, count in error_counts]
error_data = [count for url, count in error_counts]

html = html.replace("__ERROR_LABELS__", json.dumps(error_labels))
html = html.replace("__ERROR_DATA__", json.dumps(error_data))

# 의심 IP 차트 데이터 분리
ip_counts = results["top_ip"]

ip_labels = [ip for ip, count in ip_counts]
ip_data = [count for ip, count in ip_counts]

html = html.replace("__IP_LABELS__", json.dumps(ip_labels))
html = html.replace("__IP_DATA__", json.dumps(ip_data))

# 6. 작성자 이름 삽입  ★ "본인 이름"을 실제 이름으로 바꾸세요
html = html.replace("__AUTHOR__", "박형래")

# 7. 완성본 저장
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html 생성 완료. 브라우저로 열어 확인하세요.")
