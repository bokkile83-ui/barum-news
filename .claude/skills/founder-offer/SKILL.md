---
name: founder-offer
description: >-
  Builds an offer too good to refuse. Lists every problem the buyer hits on the way
  to the result they want, turns each into a solution, trims to what is cheap to
  deliver and valuable to the buyer, and stacks it with honest bonuses, a guarantee
  the CFO can afford, real urgency and a clear name. Scores it on the value
  equation (outcome, likelihood, time, effort) and re-tests it on a quick buyer
  panel. Use when the user says "make my offer better", "why won't people buy",
  "what should I include", "guarantee", "bonuses", "grand slam offer", or after the
  panel shows people passing.
argument-hint: "[what you sell]"
---

## 바름 규칙 (이 스킬 원문보다 우선)

- 바름지점(보험 설계사, 부산·창원)용이다. 답은 한국어, 고객 말은 해요체로 쓴다. 말투는 `instagram/voice.md` 를 따른다.
- 고객 실명·전화번호는 쓰지 않는다(김O자). 화면·문서에 개인 이름 대신 「BARUM 바름지점」.
- 숫자·제도는 출처가 있는 것만 쓴다. 모르면 [확인].
- 보험료는 보험사가 정한다. 가격을 새로 정하는 제안은 하지 않는다.
- 보험업법상 특별이익 제공(금품·선물·보험료 대납·할인 약속 등)은 제한된다. 덤 선물·현금성 혜택·「보장 약속」을 제안에 넣지 않는다. 한도는 [확인].
- 「무조건 보장」「100% 지급」 같은 단정 표현 금지. 약관·상품마다 다른 것은 「상품별로 달라요」.
- 오퍼 = 상담에서 무엇을 해 주는지(무료 보장분석·청구 점검·리포트 등) 정리하는 것까지만. 보너스·보증·긴급성은 법에 걸리지 않는 정보성 서비스로만 만든다.


# founder-offer

Most businesses sell a product. Good ones sell an offer: the product plus
everything that makes buying it an easy yes. This skill builds that, using the
Offers lens in `lenses.md (이 폴더)` as the method (a summary of the
framework in Alex Hormozi's *$100M Offers*; never present it as his words).

## Step 1: read what is already known

- `founder/idea.md` and `founder/pitch.md`: what is sold today.
- `founder/panel/results.md`: why buyers pass, in their words. This is the raw
  material: every top objection should be answered by something in the offer.
- `founder/numbers.json`: what each extra costs, so the stack stays profitable.
- `founder/board.md`: the board's conditions.

## Step 2: the problem list

Write every obstacle between the buyer and the result they want, in the buyer's
words: before buying (doubt, price, effort to switch), during (waiting, learning,
inconvenience), after (does it last, what if it fails). Aim for 15 to 30. Pull
from the panel objections and the competitor complaints first.

## Step 3: solutions, trimmed and stacked

Turn each problem into a solution (a feature, a service, a guarantee, a format).
Score each on value to the buyer (1 to 5) and cost to deliver (1 to 5, from the
CFO's numbers). Keep high value, low cost. Stack what is left into:

- **The core**: the thing itself, described by the outcome, not the ingredients.
- **Bonuses**: two or three, each killing one specific objection.
- **The guarantee**: what happens if it does not deliver. Model what it costs at a
  realistic claim rate with the CFO's tool before promising it.
- **Urgency and scarcity**: only if they are true (a launch week, a limited first
  batch). Never fake a countdown or a "only 3 left".
- **The name**: a clear, specific name for the offer, not the company.

## Step 4: score it

On the value equation, before and after, 1 to 10 each: dream outcome, perceived
likelihood of getting it, time to the result, effort and sacrifice. Say which
element of the stack moves which score.

## Step 5: re-test it

Write the new offer into `founder/pitch.md` (keep the old one as
`founder/pitch-v1.md`) and run `/founder-consumer --quick` with the same seed.
Report the buy rate before and after and which objections dropped. If nothing
moved, say so: the problem may be the market or the price, not the offer.

## Rules

- Every promise must be deliverable and affordable; check costs with the CFO.
- No fake reviews, testimonials, scarcity, discounts or "as seen on".
- Follow the advertising and consumer-protection rules of the user's market for
  guarantees and claims (health claims especially). Not legal advice.

## Output

`founder/offer.md` (problem list, the stack, costs, the value-equation scores, the
re-test result) and the updated `founder/pitch.md`. Next: `/founder-cfo` to re-run
the numbers with the stack, then `/founder-marketing`.
