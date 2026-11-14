# feed — 재무 소식을 앱마다 나눠 보여 주는 목록

- `apps.json` — 통합앱 도구 탭 · 자료 탭 · LIFE PLAN 첫 화면의 「💰 오늘의 재무 소식」 칸이 바로 읽는다(e3d/finfeed.js, 허브 v593~). 앱 zip 을 다시 올리지 않아도 바뀐다.
- 한 줄 = `{"d":"YYYY-MM-DD","app":["tools","jaryo","life","helper"],"t":"제목 25자 안팎","s":"요지 한 줄 60자 안팎","src":"출처 기관·매체","url":"출처 주소","f":"fin/…md"}`
- app 고르기: life = 연금·노후·세액공제·저축·달러·상속·증여·가계 재무 / tools = 계산기 값(금리·환율·공제 한도·물가)과 바로 쓰는 숫자 / jaryo = 상담 때 설명할 제도·개념 / helper = 설계사 질문에 답할 사실(HELPER 지식책 후보 → helper/daily/YYYY-MM-DD-fin.md)
- 최근 30줄만 남긴다(오래된 줄은 빼도 fin/ 원문은 지우지 않는다). 글은 fin 원문에 있는 문장·숫자만 — 새로 만들지 않는다.
- `hub_todo.md` — 앱 안 고정 값(계산기 기본값·자료 글 판·LIFE PLAN 기준표)을 바꿔야 하는 것. 허브 zip 배포 때 반영한다.
