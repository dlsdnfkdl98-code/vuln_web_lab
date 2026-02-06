# PortSwigger Lab - Reflected XSS into HTML context with nothing encoded

## 요약

검색 파라미터가 HTML에 인코딩 없이 그대로 반영되어, 임의의 HTML/JS 실행이 가능함(Reflected XSS).

## 재현

1. Lab 실행 후 검색 기능 사용
2. 검색 입력이 결과 페이지에 그대로 HTML로 렌더링되는지 확인(예: `<h1>AAA</h1>`가 제목으로 렌더링됨)
3. 브라우저에서 JavaScript 실행이 가능함을 확인(팝업 등)

## 원인

사용자 입력값이 서버 응답 HTML에 escape/encode 없이 삽입되어 브라우저가 HTML로 해석함.

## 영향

피해자 브라우저에서 공격자 스크립트 실행 가능(세션 탈취, 피싱 UI 삽입 등).

## 대응 방안(실무)

- 출력 컨텍스트에 맞는 escaping/encoding 적용(HTML, attribute, JS, URL 컨텍스트 구분)
- 템플릿 엔진 auto-escape 사용
- 추가 방어로 CSP 적용
