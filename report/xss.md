# Reflected XSS in /echo

## 요약

사용자 입력값이 필터링 없이 HTML에 그대로 출력되어 JavaScript 실행이 가능합니다.

## 재현 방법

1. 서버 실행:

   ```bash
   python3 app.py

## 브라우저 접속

<http://127.0.0.1:5000/echo?msg=><script>alert("XSS")</script>

## alert 팝업 확인

영향

공격자는 피해자 브라우저에서 임의의 JavaScript를 실행할 수 있습니다.
예: 세션 탈취, 피싱 페이지 삽입, 관리자 권한 탈취 가능

## 참고

OWASP Top 10 - Cross Site Scripting

원인

msg 파라미터가 escape 없이 HTML에 그대로 삽입됨.

대응 방안

출력 시 escape 처리 또는 템플릿 엔진의 auto-escape 사용.
