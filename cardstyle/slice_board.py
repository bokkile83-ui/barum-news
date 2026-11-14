"""3×3 일러스트 판(흰 바탕)을 칸별로 잘라 배경을 지우고 cardstyle/art/<이름>.webp 로 저장한다.
사용: python3 cardstyle/slice_board.py <판 png> <이름1,이름2,…,이름9>
배경 지우기 = 가장자리에서 이어진 흰색(밝기 차 18 이내)만 투명으로. 물체 안의 흰색은 남는다."""
import sys, os
from collections import deque
from PIL import Image, ImageFilter

def cut(cell, tol=18):
    im = cell.convert('RGBA'); w, h = im.size; px = im.load()
    bg = [px[0, 0], px[w-1, 0], px[0, h-1], px[w-1, h-1]]
    br = tuple(sum(c[i] for c in bg)//4 for i in range(3))
    near = lambda p: max(abs(p[0]-br[0]), abs(p[1]-br[1]), abs(p[2]-br[2])) <= tol
    seen = bytearray(w*h); q = deque()
    for x in range(w):
        q.append((x, 0)); q.append((x, h-1))
    for y in range(h):
        q.append((0, y)); q.append((w-1, y))
    while q:
        x, y = q.popleft()
        if x < 0 or y < 0 or x >= w or y >= h: continue
        i = y*w+x
        if seen[i]: continue
        seen[i] = 1
        if not near(px[x, y]): continue
        px[x, y] = (255, 255, 255, 0)
        q.extend(((x+1, y), (x-1, y), (x, y+1), (x, y-1)))
    a = im.split()[3].filter(ImageFilter.GaussianBlur(0.8))
    im.putalpha(a)
    box = im.getbbox()
    return im.crop(box) if box else im

if __name__ == '__main__':
    src, names = sys.argv[1], sys.argv[2].split(',')
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'art')
    os.makedirs(out, exist_ok=True)
    b = Image.open(src).convert('RGB'); W, H = b.size; cw, ch = W//3, H//3
    for k, n in enumerate(names):
        r, c = divmod(k, 3)
        pad = int(cw*0.02)
        cell = b.crop((c*cw+pad, r*ch+pad, (c+1)*cw-pad, (r+1)*ch-pad))
        im = cut(cell)
        im.thumbnail((640, 640))
        im.save(os.path.join(out, n + '.webp'), 'WEBP', quality=90)
        print(n, im.size)
