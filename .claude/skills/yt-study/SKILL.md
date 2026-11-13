---
name: yt-study
description: 유튜브 보험 강의 영상의 자막을 받아 실제 내용으로 공부 글·유튜브 칸 카드·HELPER 지식책 후보를 만들 때 사용. 지점장 PC가 연결돼 있을 때만 된다.
---

# yt-study — 유튜브를 「보고」 공부하기

클라우드 작업 공간은 youtube.com 접속이 막혀 있다. 자막은 지점장 PC에서만 받는다.

1. PC 연결 확인(원격 PC 도구 mcp__remote-devices__device_bash 가 있어야 한다). 없으면 「PC를 켜고 Claude 앱을 열어 주세요」 한 줄로 끝낸다.
2. PC에서: `pip install youtube-transcript-api` (한 번만) → 이 저장소의 `tools/yt_transcript.py` 를 PC 바탕화면 클로드 폴더에 두고 `python yt_transcript.py <영상주소...>` → `yt_txt/<ID>.txt`.
3. 자막 파일을 작업 공간으로 가져와 읽는다. 자막에 나온 말이라도 숫자·제도는 공식 자료(금감원·금융위·보험협회·심평원·건보공단·보험사 공식 안내)로 한 번 더 확인하고, 확인 안 되면 쓰지 않거나 [확인 필요].
4. 결과: yt/YYYY-MM-DD.md 의 「한 줄」을 영상 실제 내용 요약으로 바꾸고 「영상에서 들은 핵심 3가지」(자막 근거 · 몇 분쯤) 추가 → 유튜브 카드(스토리 1080×1920, 간단하게) → helper/daily 에 Q&A 3개.
5. 영상 원문(자막)을 그대로 앱에 옮기지 않는다(저작권). 요약과 시간 표시만.
