"""유튜브 자막 받기 (지점장 PC 전용 — 클라우드는 유튜브 접속이 막혀 있다).
쓰는 법:  python yt_transcript.py <영상주소 또는 ID> [...]
결과: 같은 폴더 yt_txt/<ID>.txt (한국어 자막 우선, 없으면 자동 생성 자막).
필요: pip install youtube-transcript-api   (API 키 필요 없음)"""
import sys, os, re
from youtube_transcript_api import YouTubeTranscriptApi

def vid(s):
    m = re.search(r'(?:v=|youtu\.be/|shorts/)([\w-]{11})', s)
    return m.group(1) if m else s.strip()

def main(args):
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'yt_txt')
    os.makedirs(out, exist_ok=True)
    api = YouTubeTranscriptApi()
    for a in args:
        i = vid(a)
        try:
            t = api.fetch(i, languages=['ko', 'en'])
            text = '\n'.join(s.text for s in t)
            open(os.path.join(out, i + '.txt'), 'w', encoding='utf-8').write(text)
            print('OK', i, len(text), '자')
        except Exception as e:
            print('FAIL', i, type(e).__name__, str(e)[:120])

if __name__ == '__main__':
    main(sys.argv[1:])
