# -*- coding: utf-8 -*-
"""Build the BEC lexicon used by the app.

Headwords at Preliminary level come from the publicly posted Cambridge
English: Business Preliminary wordlist. Example sentences in that PDF are
not copied. Chinese glosses are shortened from the MIT-licensed ECDICT.
Etymologies, root families, legends and lessons are original text in
content/curriculum.py.
"""

from __future__ import annotations

import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "content"))

from curriculum import EXTRA, ETYM, GERMANIC, GLOSS, LEGENDS, LESSONS, ROOTS  # noqa: E402
from scenes import SCENES  # noqa: E402
from books import BOOKS, PAIRS  # noqa: E402

PDF = Path(r"C:\Users\zanda\AppData\Local\Temp\yyx-build\bec-preliminary.pdf")
ECDICT = Path(r"C:\Users\zanda\AppData\Local\Temp\yyx-build\ecdict.csv")
OUT = ROOT / "docs" / "data.js"

POS_PARTS = {
    "n", "v", "adj", "adv", "prep", "pron", "conj", "det", "exclam", "abbrev",
    "int", "num", "art", "modal", "aux", "phr", "phr v", "prep phr", "n pl",
    "pl", "excl", "adv phr", "conj phr", "det phr", "pron phr",
}
KEEP_PARTICLE = {
    "of", "up", "on", "out", "off", "for", "to", "in", "down", "away", "with",
    "over", "back", "into", "from",
}

PHRASES = {
    "advice note": "通知单",
    "after-sales service": "售后服务",
    "air-conditioning": "空调",
    "application form": "申请表",
    "assembly plant": "装配厂",
    "assembly point": "集合点",
    "bank balance": "银行存款余额",
    "bank charge": "银行手续费",
    "bank loan": "银行贷款",
    "bank statement": "银行对账单",
    "bank transfer": "银行转账",
    "board meeting": "董事会会议",
    "board room": "会议室",
    "booking desk": "订票处",
    "booking form": "预订单",
    "business hours": "营业时间",
    "business plan": "商业计划",
    "business school": "商学院",
    "c": "摄氏；大约",
    "cable television": "有线电视",
    "call centre": "呼叫中心",
    "cash book": "现金账",
    "cash sale": "现金销售",
    "cm": "厘米",
    "co": "公司",
    "coffee-shop": "咖啡馆",
    "computer program(me)": "计算机程序",
    "computer programmer": "程序员",
    "connecting": "转机的；衔接的",
    "cross out": "划掉",
    "date-stamp": "日期戳",
    "direct cost": "直接成本",
    "direct debit": "直接借记",
    "dotted line": "虚线",
    "e": "东",
    "electronic mail": "电子邮件",
    "employment agency": "职业介绍所",
    "eu": "欧盟",
    "exchange controls": "外汇管制",
    "final demand": "最后付款通知",
    "financial advisor": "财务顾问",
    "fixed-term contract": "固定期限合同",
    "flotation": "发行上市",
    "foreign currency": "外币",
    "free gift": "赠品",
    "free sample": "免费样品",
    "free trade": "自由贸易",
    "funding": "资金筹措",
    "health and safety": "健康与安全",
    "hourly fee": "按小时计的费用",
    "hourly rate": "小时费率",
    "hr": "小时",
    "import duty": "进口关税",
    "in difficulties": "处于困境",
    "in ink": "用墨水（书写）",
    "in pencil": "用铅笔",
    "in town": "在城里",
    "information technology": "信息技术",
    "job description": "职位说明",
    "job security": "工作保障",
    "km": "公里",
    "laptop": "笔记本电脑",
    "laser disk": "激光光盘",
    "leisure industry": "休闲产业",
    "lost property": "失物",
    "m": "米",
    "mailing list": "通讯名单",
    "mass production": "大规模生产",
    "max": "最大",
    "md": "总经理",
    "middle management": "中层管理",
    "misc": "杂项",
    "n": "北",
    "no.": "号码",
    "north east": "东北",
    "north west": "西北",
    "nw": "西北",
    "on a journey": "在旅途中",
    "own brand": "自有品牌",
    "paid leave": "带薪假",
    "personnel management": "人事管理",
    "plc": "公开上市有限公司",
    "ps": "附言",
    "public holiday": "公共假日",
    "public limited company": "公开上市有限公司",
    "quality control": "质量控制",
    "r & d": "研发",
    "rd": "路",
    "retail outlet": "零售网点",
    "retail price": "零售价",
    "s": "南",
    "sec": "秒",
    "selling price": "售价",
    "south east": "东南",
    "south west": "西南",
    "st": "街；圣",
    "stay behind": "留下",
    "turn around": "周转；扭转",
    "w": "西",
    "who, whom": "谁",
    "window display": "橱窗陈列",
    "work permit": "工作许可",
    "working hours": "工作时间",
    "yr": "年",
    "internet": "互联网",
    "co-ordinate": "协调",
    "co-ordination": "协调",
    "network": "网络；人脉",
    "p./pp.": "页",
    "train": "火车；训练",
    "may": "可以；也许；五月",
    "will": "将；会；意愿",
    "mine": "我的；矿",
    "miss": "错过；想念",
    "us": "我们",
    "it": "它",
    "as": "如同；作为；当",
    "at": "在；向",
    "be": "是",
    "by": "被；由；在旁边",
    "do": "做",
    "go": "去",
    "if": "如果",
    "in": "在内；向内",
    "no": "不；没有",
    "of": "的；属于",
    "on": "在上面；继续",
    "or": "或者",
    "so": "所以；如此",
    "to": "到；向",
    "up": "向上",
    "we": "我们",
    "my": "我的",
    "me": "我",
    "mr": "先生",
    "ms": "女士",
}


def is_pos(raw: str) -> bool:
    s = re.sub(r"\s+", " ", raw.strip().lower())
    s = s.replace("phrase", "phr").replace("exclamation", "exclam")
    if not s or len(s) > 48:
        return False
    parts = [p.strip() for p in re.split(r"\s*[&/,]\s*", s) if p.strip()]
    if not parts:
        return False
    return all(p in POS_PARTS for p in parts)


def parse_entry(text: str):
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace("( ", "(").replace(" )", ")")
    if not text or text.startswith("•") or "UCLES" in text or text.startswith("Cambridge"):
        return None
    spans = list(re.finditer(r"\(([^)]*)\)", text))
    pos_span = None
    for span in reversed(spans):
        if is_pos(span.group(1)):
            pos_span = span
            break
    if not pos_span:
        return None
    word = text[: pos_span.start()].strip(" -–")
    pos = re.sub(r"\s+", " ", pos_span.group(1).strip())
    if not word:
        return None
    particle = re.search(r"\s+\(([^)]+)\)$", word)
    if particle and particle.group(1).lower() not in KEEP_PARTICLE and not is_pos(particle.group(1)):
        word = word[: particle.start()].strip()
    word = re.sub(r"\s+", " ", word).strip()
    if not word or len(word) > 55 or len(word.split()) > 7:
        return None
    if re.search(r"[?!£$]", word):
        return None
    if word.endswith(".") and " " in word:
        return None
    if not re.match(r"^[A-Za-z0-9]", word):
        return None
    return word, pos


def normalize_head(word: str):
    word = re.sub(r"\s+", " ", word).strip()
    if re.search(r"\((?:n|v|adj|adv|prep|pron|phr|abbrev)\)", word, flags=re.I):
        return None
    if re.search(r"(?:^|\s)(?:n|v|adj|pron)\)", word, flags=re.I):
        return None
    word = re.sub(r"\s*\(abbrev\)\s*", " ", word, flags=re.I)
    word = re.sub(r"\s+", " ", word).strip(" ;")
    lowered = word.lower()
    if lowered.startswith("no.") and "number" in lowered:
        return "no."
    if "managing director" in lowered:
        return "MD"
    if not word or len(word) > 48:
        return None
    return word


def extract_heads(pdf_path: Path):
    from pypdf import PdfReader

    reader = PdfReader(str(pdf_path))
    found = []
    for index, page in enumerate(reader.pages):
        if index < 3:
            continue
        chunks = []

        def visitor(text, cm, tm, font_dict, font_size):
            if text and text.strip():
                chunks.append((round(tm[4], 1), round(tm[5], 1), text.replace("\n", " ").strip()))

        page.extract_text(visitor_text=visitor)
        by_y = defaultdict(list)
        for x, y, text in chunks:
            by_y[y].append((x, text))
        for y, items in by_y.items():
            items.sort()
            origins = [72.0, 315.6]
            for x, text in items:
                if 324 <= x <= 346 and re.match(r"^[A-Za-z]", text) and not text.startswith("•"):
                    origins.append(x)
            for origin in origins:
                limit = 300.0 if origin < 200 else 560.0
                if not any(abs(x - origin) < 8 for x, _text in items):
                    continue
                parts = [text for x, text in items if origin - 2 <= x < limit]
                parsed = parse_entry(" ".join(parts))
                if parsed:
                    found.append(parsed)
    deduped = {}
    for word, pos in found:
        word = normalize_head(word)
        if not word:
            continue
        key = word.lower()
        if key not in deduped:
            deduped[key] = {"w": word, "pos": pos}
        elif pos.lower() not in deduped[key]["pos"].lower():
            deduped[key]["pos"] = deduped[key]["pos"] + " & " + pos
    return list(deduped.values())


def expand_keys(word: str):
    base = word.lower().replace("’", "'").strip()
    keys = []

    def add(value: str):
        value = re.sub(r"\s+", " ", value).strip(" /")
        if value and value not in keys:
            keys.append(value)

    add(base)
    for part in re.split(r"\s*/\s*", base):
        add(part)

    def explode(value: str):
        match = re.search(r"\(([^)]+)\)", value)
        if not match:
            return [value]
        inner = match.group(1)
        left, right = value[: match.start()], value[match.end() :]
        options = [left + right, left + inner + right]
        out = []
        for option in options:
            out.extend(explode(option))
        return out

    for key in list(keys):
        for option in explode(key):
            add(option)
    return keys


def clean_gloss(translation: str, word: str = "") -> str:
    if not translation:
        return ""
    translation = translation.replace("\\n", "\n")
    lines = []
    for line in translation.splitlines():
        line = re.sub(r"^\[.*?\]\s*", "", line).strip()
        line = re.sub(r"^(n|vt|vi|v|a|adj|adv|prep|pron|conj|art|int|aux|num|abbr)\.\s*", "", line)
        line = re.sub(r"\[.*?\]", "", line).strip(" ;；")
        if line and not line.startswith("网络"):
            lines.append(line)
    text = lines[0] if lines else ""
    text = re.sub(r"\s+", " ", text).strip("；; ")
    parts = [part.strip() for part in re.split(r"[；;]", text) if part.strip()]
    text = "；".join(parts[:2])
    if len(word) <= 4:
        bits = [bit.strip() for bit in re.split(r"[，,]", text) if bit.strip()]
        text = "，".join(bits[:3])
    if len(text) > 56:
        text = text[:56].rstrip("；;，, ") + "…"
    return text


def clean_phonetic(value: str) -> str:
    if not value:
        return ""
    value = value.strip().strip("'").replace("ә", "ə").replace(":", "ː")
    value = value.replace("ɑ:", "ɑː").replace("ɔ:", "ɔː").replace("i:", "iː").replace("u:", "uː").replace("ə:", "ɜː")
    return value


def load_ecdict(path: Path, wanted: set[str]):
    found = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            word = (row.get("word") or "").lower()
            if word in wanted and word not in found:
                found[word] = {
                    "ph": clean_phonetic(row.get("phonetic") or ""),
                    "zh": clean_gloss(row.get("translation") or "", word),
                }
            if len(found) == len(wanted):
                break
    return found


def short_zh(text: str) -> str:
    piece = re.split(r"[；;，,]", text or "")[0].strip().replace("…", "")
    return piece or "这个"


def surface_word(word: str) -> str:
    text = re.sub(r"\([^)]*\)", "", word)
    text = text.split("/")[0].strip()
    return re.sub(r"\s+", " ", text) or word


def pos_kind(pos: str) -> str:
    text = (pos or "").lower()
    has_noun = bool(re.search(r"\bn\b", text))
    if re.search(r"\bphr v\b|\bv\b", text) and not has_noun:
        return "v"
    if re.search(r"\badj\b", text) and not has_noun:
        return "adj"
    if re.search(r"\badv\b", text) and not has_noun and "adj" not in text:
        return "adv"
    if re.search(r"\b(prep|conj|pron|det|int|exclam|abbrev)\b", text) and not has_noun:
        return "small"
    return "n"


def choose(word: str, salt: int, options: list[str]) -> str:
    score = salt
    for char in word.lower():
        score = (score * 33 + ord(char)) % 1000003
    return options[score % len(options)]


HAND_XS = {
    "meeting": [
        {"k": "办公", "en": "The meeting starts at ten. Please bring the agenda.", "zh": "会议十点开始。请把议程带上。"},
        {"k": "日常", "en": "I remembered the meeting only when I was already on the bus.", "zh": "我已经上了公交，才想起还有会议。"},
        {"k": "搞笑", "en": "The meeting started before anyone sat down. The cat took the first chair.", "zh": "人还没坐下，会议就开始了。猫占了第一把椅子。"},
    ],
    "invoice": [
        {"k": "办公", "en": "Please send the invoice with the delivery note.", "zh": "请把发票和送货单一起发来。"},
        {"k": "日常", "en": "I found last month's invoice in a kitchen drawer.", "zh": "我在厨房抽屉里找到了上个月的发票。"},
        {"k": "搞笑", "en": "The invoice has been 'on its way' since Monday. So has my patience.", "zh": "发票从周一起就说在路上。我的耐心也是。"},
    ],
    "budget": [
        {"k": "办公", "en": "The budget cannot cover another round of taxis.", "zh": "预算不够再报一轮出租车了。"},
        {"k": "日常", "en": "We talked about the household budget after dinner.", "zh": "晚饭后我们谈了家里的开支预算。"},
        {"k": "搞笑", "en": "Everyone nodded at the budget. Nobody had opened it.", "zh": "所有人都对预算点头。没有人打开过。"},
    ],
    "customer": [
        {"k": "办公", "en": "The customer is still waiting for a clear answer.", "zh": "客户还在等一个清楚的答复。"},
        {"k": "日常", "en": "A customer asked me the same question three times.", "zh": "一位顾客把同一个问题问了三遍。"},
        {"k": "搞笑", "en": "The customer brought a cat and introduced it as a partner.", "zh": "客户带来一只猫，并介绍说这是合伙人。"},
    ],
    "deadline": [
        {"k": "办公", "en": "The deadline is Friday at noon.", "zh": "截止日期是周五中午。"},
        {"k": "日常", "en": "I remembered the deadline halfway home.", "zh": "走到半路我才想起截止日期。"},
        {"k": "搞笑", "en": "The deadline did not move. My excuse did.", "zh": "截止日期没动。我的借口动了。"},
    ],
    "salary": [
        {"k": "办公", "en": "Salary is paid on the last working day.", "zh": "工资在最后一个工作日发。"},
        {"k": "日常", "en": "We checked the salary and then chose a cheaper dinner.", "zh": "我们看了工资，然后选了更便宜的晚饭。"},
        {"k": "搞笑", "en": "The cat has no salary and still expects lunch.", "zh": "猫没有工资，仍然等着午饭。"},
    ],
    "contract": [
        {"k": "办公", "en": "Please read the contract before you sign.", "zh": "签字前请先读合同。"},
        {"k": "日常", "en": "The phone contract ends in March.", "zh": "手机合约三月到期。"},
        {"k": "搞笑", "en": "We shook hands. The contract was still in the other room.", "zh": "我们已经握手了。合同还在另一个房间。"},
    ],
    "luggage": [
        {"k": "办公", "en": "Please keep the samples in your hand luggage.", "zh": "请把样品放在手提行李里。"},
        {"k": "日常", "en": "My luggage arrived one day after I did.", "zh": "行李比我晚到一天。"},
        {"k": "搞笑", "en": "The suitcase went to the meeting. I went to the wrong carousel.", "zh": "箱子去开会了。我去了错误的行李转盘。"},
    ],
    "delivery": [
        {"k": "办公", "en": "The delivery is due before noon.", "zh": "这批货中午之前要送到。"},
        {"k": "日常", "en": "The dinner delivery arrived during the film.", "zh": "外卖在电影放到一半时到了。"},
        {"k": "搞笑", "en": "Delivery said 'at the door'. The door disagreed.", "zh": "配送写着放在门口。门并不同意。"},
    ],
    "discount": [
        {"k": "办公", "en": "We can offer a small discount on large orders.", "zh": "大额订单可以给一点折扣。"},
        {"k": "日常", "en": "I bought the coat because of the discount, not the weather.", "zh": "我买这件外套是因为折扣，不是因为天气。"},
        {"k": "搞笑", "en": "The discount was so small it needed a magnifying glass.", "zh": "折扣小到需要放大镜。"},
    ],
    "manager": [
        {"k": "办公", "en": "Please ask the manager before you change the price.", "zh": "改价格之前请问一下经理。"},
        {"k": "日常", "en": "The shop manager helped me find a smaller size.", "zh": "店经理帮我找了小一号。"},
        {"k": "搞笑", "en": "The manager called a meeting. The cat was already there.", "zh": "经理召集会议。猫已经到了。"},
    ],
    "email": [
        {"k": "办公", "en": "I sent the email, but I forgot the attachment.", "zh": "邮件发出去了，附件忘了。"},
        {"k": "日常", "en": "Her email arrived while we were cooking.", "zh": "我们做饭的时候，她的邮件到了。"},
        {"k": "搞笑", "en": "The email said 'urgent'. It was a picture of lunch.", "zh": "邮件标题是「紧急」。内容是午饭的照片。"},
    ],
    "coffee": [
        {"k": "办公", "en": "The meeting can start when the coffee arrives.", "zh": "咖啡到了，会议就可以开始。"},
        {"k": "日常", "en": "I drink one coffee on the way to work.", "zh": "我上班路上喝一杯咖啡。"},
        {"k": "搞笑", "en": "The coffee was stronger than the decision.", "zh": "咖啡比那个决定更有劲。"},
    ],
    "flight": [
        {"k": "办公", "en": "My flight lands at 9:40. I can be in the office by noon.", "zh": "我的航班 9:40 落地。中午能到办公室。"},
        {"k": "日常", "en": "The flight was late, so we missed dinner.", "zh": "航班晚点了，晚饭没赶上。"},
        {"k": "搞笑", "en": "The flight was on time. My shoes were not.", "zh": "航班准点。我的鞋不是。"},
    ],
    "hotel": [
        {"k": "办公", "en": "The hotel is a short walk from the client.", "zh": "酒店离客户走路就到。"},
        {"k": "日常", "en": "We liked the hotel because breakfast started early.", "zh": "我们喜欢这家酒店，因为早餐开得早。"},
        {"k": "搞笑", "en": "The hotel gave me a quiet room next to a drum.", "zh": "酒店给了我一间安静的房，隔壁是一面鼓。"},
    ],
    "agenda": [
        {"k": "办公", "en": "The agenda has three items and one apology.", "zh": "议程上有三项，外加一次道歉。"},
        {"k": "日常", "en": "Our family agenda was: eat, walk, sleep.", "zh": "我们家的议程是：吃、走、睡。"},
        {"k": "搞笑", "en": "Item one on the agenda was finding the agenda.", "zh": "议程第一项是把议程找出来。"},
    ],
}


def example_sentences(entry: dict) -> list[dict]:
    hand = HAND_XS.get(entry["w"].lower())
    if hand:
        rows = [dict(item) for item in hand]
        if entry.get("ex"):
            rows.insert(0, {"k": "商务", "en": entry["ex"], "zh": "这是这个词在商务语境里的一句。"})
        return rows[:4]
    word = surface_word(entry["w"])
    gloss = short_zh(entry.get("zh") or "")
    kind = pos_kind(entry.get("pos") or "")
    if "." in word or len(word) <= 2 or kind == "small":
        office = choose(word, 1, [
            'Please do not delete the word "{w}" from the email.',
            'The note says "{w}", and nobody knows why.',
            'She wrote "{w}" at the top of the agenda.',
        ]).format(w=word)
        daily = choose(word, 2, [
            'He texted one word: "{w}".',
            'I heard "{w}" twice on the way home.',
            'The sign still says "{w}".',
        ]).format(w=word)
        funny = choose(word, 3, [
            'The meeting stopped when someone shouted "{w}!"',
            'My cat stepped on the keyboard and produced "{w}".',
            'The coffee machine displayed "{w}" and refused to explain.',
        ]).format(w=word)
        office_zh = f"请不要把邮件里的「{gloss}」删掉。"
        daily_zh = f"他只发来一个意思：{gloss}。"
        funny_zh = f"有人突然喊了一声，会议室停住了。那个意思是：{gloss}。"
    elif kind == "v":
        office = choose(word, 1, [
            "We still need to {w} before the client calls.",
            "They agreed to {w} after the meeting.",
            "It took all morning to {w}.",
            "Someone has to {w} before Friday.",
        ]).format(w=word)
        daily = choose(word, 2, [
            "I will {w} after dinner.",
            "She asked me not to {w} on the bus.",
            "He promised to {w} tomorrow morning.",
            "We can {w} when we get home.",
        ]).format(w=word)
        funny = choose(word, 3, [
            "He stood up to {w}, then sat down and ordered coffee.",
            "Nobody wanted to {w}, so the job stayed open.",
            "I was ready to {w}. The printer was not.",
            "They tried to {w} and ended up laughing.",
        ]).format(w=word)
        office_zh = f"客户来电话之前，这件事还得做：{gloss}。"
        daily_zh = f"晚饭后再说这件事：{gloss}。"
        funny_zh = f"大家本来要去{gloss}，结果先笑了。"
    elif kind == "adj":
        office = choose(word, 1, [
            "The client says the plan is too {w}.",
            "This report looks {w} on page two.",
            "We need a less {w} solution before Friday.",
            "Her email was short and {w}.",
        ]).format(w=word)
        daily = choose(word, 2, [
            "The weather is {w}, so I am staying in.",
            "This soup tastes {w}, and I still ate it.",
            "He looked {w} after the long meeting.",
            "The bus was late and the driver was {w}.",
        ]).format(w=word)
        funny = choose(word, 3, [
            "My boss called the idea {w}. The idea looked proud.",
            "The cat finds your slides {w} and went to sleep.",
            "Even the printer thinks this font is {w}.",
            "The cake was {w}. We still put it in the minutes.",
        ]).format(w=word)
        office_zh = f"客户觉得这个方案太{gloss}了。"
        daily_zh = f"日常生活里，这件东西给人的感觉是{gloss}。"
        funny_zh = f"老板说这个主意很{gloss}，主意本身看起来还挺得意。"
    elif kind == "adv":
        office = choose(word, 1, [
            "Please reply {w} and copy the manager.",
            "She explained the numbers {w}.",
            "We should decide {w}, before the client arrives.",
            "He read the contract {w}.",
        ]).format(w=word)
        daily = choose(word, 2, [
            "She answered {w} and then laughed.",
            "Walk {w}. The floor is wet.",
            "He closed the door {w}.",
            "I will call you {w}.",
        ]).format(w=word)
        funny = choose(word, 3, [
            "The cat entered {w}, as if it owned the budget.",
            "He apologised {w}, while still holding the invoice.",
            "The lift doors opened {w}, and the meeting was inside.",
            "She nodded {w}. The coffee did not.",
        ]).format(w=word)
        office_zh = f"请这样回复：{gloss}，并抄送经理。"
        daily_zh = f"她是这样回答的：{gloss}。"
        funny_zh = f"猫以一种「{gloss}」的方式走进来，好像预算是它的。"
    else:
        office = choose(word, 1, [
            "We need to sort out the {w} today.",
            "Who is looking after the {w}?",
            "The {w} came up in this morning's meeting.",
            "There is still no decision on the {w}.",
            "I left a note about the {w}.",
        ]).format(w=word)
        daily = choose(word, 2, [
            "I was still thinking about the {w} on the bus home.",
            "She explained the {w} in ordinary words.",
            "We talked about the {w} after dinner.",
            "He called me about the {w} while I was cooking.",
            "The {w} can wait until tomorrow.",
        ]).format(w=word)
        funny = choose(word, 3, [
            "Everyone avoided the {w}, so it stayed on the agenda all week.",
            "I tried to forget the {w}. It was waiting in my inbox.",
            "The {w} has been 'nearly finished' since Monday.",
            "We blamed the {w}. The {w} did not attend the meeting.",
            "The cat sat on the papers and guarded the {w}.",
        ]).format(w=word)
        office_zh = f"今天得把{gloss}这件事理清楚。"
        daily_zh = f"回家的路上我还在想{gloss}。"
        funny_zh = f"大家都躲着{gloss}，所以它在议程上待了一整周。"
    rows = [
        {"k": "办公", "en": office, "zh": office_zh},
        {"k": "日常", "en": daily, "zh": daily_zh},
        {"k": "搞笑", "en": funny, "zh": funny_zh},
    ]
    if entry.get("ex"):
        rows.insert(0, {"k": "商务", "en": entry["ex"], "zh": f"商务例句，关键词是{gloss}。"})
    return rows[:4]


def root_sentence(word: str, root: dict) -> str:
    return (
        f"{word} 可以放进「{root['title']}」这一族。"
        f"{root['meaning']}。"
        f"{root['pattern']}"
    )


def main():
    if not PDF.exists():
        raise SystemExit(f"missing wordlist pdf: {PDF}")
    if not ECDICT.exists():
        raise SystemExit(f"missing ecdict: {ECDICT}")

    heads = extract_heads(PDF)
    words = {}
    for item in heads:
        words[item["w"].lower()] = {
            "w": item["w"],
            "lv": "P",
            "pos": item["pos"],
            "ph": "",
            "zh": "",
            "et": "",
            "ek": "",
            "rs": [],
            "lg": "",
            "ex": "",
        }

    for item in EXTRA:
        key = item["w"].lower()
        if key in words:
            current = words[key]
            if item.get("zh"):
                current["zh"] = item["zh"]
            if item.get("et"):
                current["et"] = item["et"]
                current["ek"] = "traced"
            if item.get("ex"):
                current["ex"] = item["ex"]
            if item.get("pos") and len(item["pos"]) > len(current["pos"]):
                current["pos"] = item["pos"]
            continue
        words[key] = {
            "w": item["w"],
            "lv": item.get("lv", "H"),
            "pos": item.get("pos", ""),
            "ph": "",
            "zh": item.get("zh", ""),
            "et": item.get("et", ""),
            "ek": "traced" if item.get("et") else "",
            "rs": [],
            "lg": "",
            "ex": item.get("ex", ""),
        }

    root_by_id = {root["id"]: root for root in ROOTS}
    for root in ROOTS:
        for member in root["members"]:
            key = member.lower()
            if key not in words:
                words[key] = {
                    "w": member,
                    "lv": "V",
                    "pos": "",
                    "ph": "",
                    "zh": "",
                    "et": "",
                    "ek": "",
                    "rs": [],
                    "lg": "",
                    "ex": "",
                }
            if root["id"] not in words[key]["rs"]:
                words[key]["rs"].append(root["id"])

    legend_by_id = {legend["id"]: legend for legend in LEGENDS}
    for legend in LEGENDS:
        for link in legend["words"]:
            key = link["w"].lower()
            if key not in words:
                words[key] = {
                    "w": link["w"],
                    "lv": link.get("lv", "V"),
                    "pos": link.get("pos", ""),
                    "ph": "",
                    "zh": link.get("zh", ""),
                    "et": "",
                    "ek": "",
                    "rs": [],
                    "lg": legend["id"],
                    "ex": "",
                }
            entry = words[key]
            entry["lg"] = legend["id"]
            if link.get("pos") and not entry["pos"]:
                entry["pos"] = link["pos"]

    wanted = set()
    aliases = {}
    for key, entry in words.items():
        for alias in expand_keys(entry["w"]):
            wanted.add(alias)
            aliases.setdefault(alias, key)
    dictionary = load_ecdict(ECDICT, wanted)

    for key, entry in words.items():
        if not entry["ph"] or not entry["zh"]:
            for alias in expand_keys(entry["w"]):
                hit = dictionary.get(alias)
                if not hit:
                    continue
                if not entry["ph"]:
                    entry["ph"] = hit["ph"]
                if not entry["zh"]:
                    entry["zh"] = hit["zh"]
                if entry["ph"] and entry["zh"]:
                    break
        override = GLOSS.get(key) or GLOSS.get(entry["w"].lower()) or PHRASES.get(key)
        if override:
            entry["zh"] = override
        if not entry["zh"]:
            entry["zh"] = "（词表收录；简明释义待补）"

    germanic = {word.lower() for word in GERMANIC}
    for key, entry in words.items():
        hand = ETYM.get(key)
        if hand:
            entry["et"] = hand
            entry["ek"] = "traced"
            continue
        if entry["et"]:
            entry["ek"] = entry["ek"] or "traced"
            continue
        if entry["lg"]:
            legend = legend_by_id[entry["lg"]]
            link = next(item for item in legend["words"] if item["w"].lower() == key)
            if link.get("et"):
                entry["et"] = link["et"]
                entry["ek"] = "traced"
                continue
        if entry["rs"]:
            root = root_by_id[entry["rs"][0]]
            entry["et"] = root_sentence(entry["w"], root)
            entry["ek"] = "root"
            continue
        if key in germanic:
            entry["et"] = (
                f"{entry['w']} 是英语的日耳曼本族词，来自古英语这一支，不是从拉丁语或希腊语借来的。"
                "商务英语里，句子的骨架（冠词、代词、介词、助动词）大多是这类词；"
                "拉丁语和希腊语更多出现在合同、财务和抽象概念里。"
            )
            entry["ek"] = "germanic"
            continue
        entry["et"] = (
            f"{entry['w']} 已收入词库，方便按 BEC 级别查阅。"
            "仅凭今天的拼写，不能稳妥判断它是拉丁语、希腊语还是日耳曼语传来的，所以这里不猜测词源。"
            "如果它属于已经整理好的词根或传说，会显示在对应的一族里。"
        )
        entry["ek"] = "open"

    for entry in words.values():
        entry["rs"] = [root_id for root_id in entry["rs"] if root_id in root_by_id]
        if entry["lg"] and entry["lg"] not in legend_by_id:
            entry["lg"] = ""
        entry["xs"] = example_sentences(entry)
        pic_name = surface_word(entry["w"]).lower().replace(" ", "-")
        entry.pop("pic", None)
        for ext in (".png", ".jpg"):
            pic_path = ROOT / "docs" / "pics" / f"{pic_name}{ext}"
            if pic_path.exists():
                entry["pic"] = f"pics/{pic_name}{ext}"
                break
        audio_path = ROOT / "docs" / "audio" / f"{pic_name}.mp3"
        if audio_path.exists():
            entry["audio"] = f"audio/{pic_name}.mp3"
        else:
            entry.pop("audio", None)

    known = {item["w"].lower() for item in words.values()}

    def keep_words(names):
        kept = []
        for name in names:
            if name.lower() in known and name not in kept:
                kept.append(name)
        return kept

    books = []
    for book in BOOKS:
        books.append({**book, "words": keep_words(book["words"])})
    pairs = []
    for pair in PAIRS:
        if pair["left"].lower() in known and pair["right"].lower() in known:
            pairs.append(pair)

    scenes = []
    for scene in SCENES:
        kept = [word for word in scene["words"] if word.lower() in known]
        scenes.append({**scene, "words": kept})

    ordered = sorted(words.values(), key=lambda item: item["w"].lower())
    counts = {
        "words": len(ordered),
        "P": sum(1 for item in ordered if item["lv"] == "P"),
        "V": sum(1 for item in ordered if item["lv"] == "V"),
        "H": sum(1 for item in ordered if item["lv"] == "H"),
        "traced": sum(1 for item in ordered if item["ek"] == "traced"),
        "root": sum(1 for item in ordered if item["ek"] == "root"),
        "germanic": sum(1 for item in ordered if item["ek"] == "germanic"),
        "open": sum(1 for item in ordered if item["ek"] == "open"),
        "legends": sum(1 for item in ordered if item["lg"]),
        "roots": len(ROOTS),
        "legendEntries": len(LEGENDS),
        "lessons": len(LESSONS),
        "scenes": len(scenes),
        "books": len(books),
        "pairs": len(pairs),
    }
    missing = [item["w"] for item in ordered if item["zh"].startswith("（词表收录")]
    payload = {
        "meta": {
            "title": "英语词源",
            "counts": counts,
            "missingGloss": missing[:40],
        },
        "words": ordered,
        "roots": ROOTS,
        "legends": LEGENDS,
        "lessons": LESSONS,
        "scenes": scenes,
        "books": books,
        "pairs": pairs,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = "window.YY = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n"
    OUT.write_text(text, encoding="utf-8")
    print(json.dumps(counts, ensure_ascii=False, indent=2))
    if missing:
        print("missing gloss sample:", ", ".join(missing[:30]))


if __name__ == "__main__":
    main()
