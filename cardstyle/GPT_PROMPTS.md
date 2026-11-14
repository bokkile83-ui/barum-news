# GPT 디자인 감각 — 다시 쓰는 프롬프트 (2026.11.14 GPT 바름 프로젝트에서 받음)

## 1. 그림 프롬프트 (영문) — [SUBJECT] 만 바꿔 넣는다
같은 그림체를 정확히 맞추려면 cardstyle/art/ 의 그림 몇 장을 참조 이미지로 같이 준다(GPT 권고).

Create a premium, cohesive 3D editorial icon illustration of [SUBJECT], matching a sophisticated Korean insurance news card aesthetic. Use softly rounded, dimensional forms with polished satin-gloss surfaces, smooth bevels, subtle reflections, and realistic yet friendly proportions. Maintain a consistent palette of bright insurance blue (#3182F6), soft powder blue (#D9E9FF), warm white (#FFFFFF), and restrained metallic gold (#F5C45E), with small natural skin-tone or medical accents only when needed. Render the object from a gentle three-quarter front perspective, with soft studio lighting coming diagonally from the upper left, delicate ambient occlusion, a faint contact shadow directly beneath the object, and clean high-quality material shading. Place one centered object or a tightly integrated small object group on a pure white background, fully contained within its frame with generous margins. The result should look like a premium 3D product render used in an elegant financial lifestyle magazine, not a flat vector, emoji sticker, clipart, or exaggerated cartoon. No text, letters, numbers, logos, watermark, borders, or decorative background.

여러 개를 한 번에: 「3×3 격자 한 장(1:1), 흰 바탕, 칸마다 물체 하나 가운데, 글자 없음」을 덧붙이고, 받은 판은 `python3 cardstyle/slice_board.py <판> <이름 9개>` 로 잘라 art/ 에 넣는다.

## 2. 카드 디자인 지시문 (GPT 원문 요약)
목표: 30~60대 일반 고객이 카톡·인스타에서 편하게 읽고 저장하고 싶은 프리미엄 생활 금융 뉴스.
1. 1080×1080, 제목 위치·출처 위치·하단 띠 높이 통일. 보험사 광고·자극적 썸네일처럼 만들지 않는다. 밝고 고급스러운 금융 생활 매거진.
2. 색: 기본 #FAFCFF · 보조 #EAF4FF / #FFF6EB / #E6F7F1 · 핵심 파랑 #3182F6 · 제목 #191F28 · 보조 글자 #6B7684 · 골드 #F5C45E. 검은 외곽선·네온·과한 채도 금지.
3. 글자: 제목 76~96px 900 · 큰 숫자 190~275px 900(한 장에서 가장 강한 요소) · 본문 34~44px · 출처 24~28px. 제목 2~3줄.
4. 3D 일러스트: 둥근 입체·부드러운 광택·블루/화이트/골드·왼쪽 위 조명·약한 접지 그림자. 주제에 맞는 물체 2~4개를 한 장면으로. 이모지 스티커·평면 벡터·과장 캐릭터 금지. 글자·숫자를 가리지 않게.
5. 배치: 위 = 꼬리표(말풍선) + 날짜 / 가운데 위 = 제목 / 가운데 = 큰 숫자 또는 비교 / 가운데 아래 = 설명 + 일러스트 / 아래 = 출처 + 하단 띠(연파랑 90~100px, 위쪽 완만한 곡선, 오른쪽 n/N).
6. HTML 자동 발행: 글자는 HTML 로(이미지에 굽지 않음), 일러스트는 미리 만든 그림. 제목 최소 64px. 숫자 없는 뉴스는 비교 카드나 핵심 문장. 날짜·수치·출처·시행 여부 검증. 좌우 여백 60px 이상.
7. 금지: 수익·절감 보장 · 과장 · 확인 안 된 통계 · 가짜 후기 · 보험사 로고 · 개인 이름 · 서로 다른 질감 그림 섞기 · 과한 그림자 · 글자 외곽선 · 원색 배경.
