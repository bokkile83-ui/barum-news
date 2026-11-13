---
name: founder-competitors
description: >-
  Maps every competitor and the gap they leave. Finds the direct competitors,
  indirect ones and the substitutes a buyer would use instead, from public
  sources only, and records what each sells, at what price, how they position
  themselves and what their customers complain about in public reviews, every fact
  with a link. Ends with a positioning map and the gap the new business can own.
  Use when the user says "who are my competitors", "is this market crowded", "what
  else is out there", "competitor analysis", "find the gap", or "who am I up
  against".
argument-hint: "[city or market]"
---

## 바름 규칙 (이 스킬 원문보다 우선)

- 바름지점(보험 설계사, 부산·창원)용이다. 답은 한국어, 고객 말은 해요체로 쓴다. 말투는 `instagram/voice.md` 를 따른다.
- 고객 실명·전화번호는 쓰지 않는다(김O자). 화면·문서에 개인 이름 대신 「BARUM 바름지점」.
- 숫자·제도는 출처가 있는 것만 쓴다. 모르면 [확인].
- 보험료는 보험사가 정한다. 가격을 새로 정하는 제안은 하지 않는다.
- 보험업법상 특별이익 제공(금품·선물·보험료 대납·할인 약속 등)은 제한된다. 덤 선물·현금성 혜택·「보장 약속」을 제안에 넣지 않는다. 한도는 [확인].
- 「무조건 보장」「100% 지급」 같은 단정 표현 금지. 약관·상품마다 다른 것은 「상품별로 달라요」.
- 공개 자료만 쓴다. 다른 설계사 개인을 겨냥한 기록(이름·연락처·사생활)은 만들지 않는다. 회사·채널 단위로만 정리한다.
- 경쟁사 문구·디자인은 원리만 참고하고 베끼지 않는다.


# founder-competitors

Every buyer already solves this problem somehow. This skill finds out how, what
they pay, and what they hate about it, so the new business starts with a gap
instead of a guess.

## The rules

- **Public sources only, every fact linked.** Websites, price pages, menus, app
  store and Google Maps listings, review sites, Reddit, news. If a source cannot be
  reached, say so. Never invent a competitor, a price, a rating or a review.
- **Read, do not scrape.** Read pages as a person would. Respect each site's terms.
- **Quotes are verbatim**, short, with the link. They are research, never
  testimonials.

## Step 1: who is there

From `founder/idea.md` (write it first if missing; see `/founder-board` step 0):

| type | what it means | example for a matcha café |
| --- | --- | --- |
| Direct | sells the same thing to the same buyer | other matcha bars within walking distance |
| Indirect | a different product for the same job | the coffee shops on the same street |
| Substitute | how buyers solve it without a business | matcha powder at home, canned drinks |

Aim for 5 to 10 direct and indirect, plus the main substitutes. For a local
business, search the map for the exact area; for online, search how a buyer would
("best <thing> for <who>", "<thing> alternative").

## Step 2: the facts

One row per competitor in `founder/competitors.csv`:

`name,type,url,location_or_channel,price_of_comparable_item,what_it_sells,positioning_line,rating,review_count,source_date`

`positioning_line` is their own headline or tagline, copied. Price is for the item
closest to what the new business sells, with what it includes.

## Step 3: what their customers say

For the top 3 to 5, read their reviews (1 to 3 stars first, then the "love it,
but..." 4 stars). Note recurring complaints as themes with counts and one or two
linked quotes each. Mark a theme thin if it has under three reviews.

## Step 4: the map and the gap

Write `founder/competitors.md`:

1. The table (from the CSV), sorted by how directly each competes.
2. Price range: lowest, median, highest for the comparable item.
3. A positioning map in text: two axes that matter to this buyer (price and
   convenience, quality and speed...), where each competitor sits.
4. The complaints, ranked, with links.
5. **The gap**: what nobody does well that this business could, tied to the
   evidence. If there is no gap, say so plainly; that is the most useful result
   this skill can give.
6. The threat: who could copy the new business fastest, and how.

## Output

`founder/competitors.csv`, `founder/competitors.md`. Next: `/founder-consumer`
uses the complaints to write real objections; `/founder-pricing` uses the price
range.
