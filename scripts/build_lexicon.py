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
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "content"))

from curriculum import (  # noqa: E402
    EXTRA,
    ETYM,
    EXTRA_KIND,
    GERMANIC,
    GLOSS,
    LEGENDS,
    LESSONS,
    MORE_ETYM,
    MORE_GERMANIC,
    ROOTS,
)
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
    if re.search(r"\b(int|exclam)\b", text) and not has_noun:
        return "small"
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


def line_key(text: str) -> str:
    return " ".join((text or "").split()).lower()


def line_audio_rel(text: str) -> str:
    digest = hashlib.sha1(line_key(text).encode("utf-8")).hexdigest()[:16]
    return f"audio/lines/{digest}.mp3"


# First ECDICT sense is sometimes a noun, or the wrong verb. The example uses a
# sense that can actually be said as the translation of the English sentence.
SENSE = {
    "apply": "应用",
    "communicate": "传达",
    "cut down (on)": "削减",
    "exclude": "排除",
    "fill in": "填写",
    "go for": "努力获取",
    "impress": "留下印象",
    "insure": "确保",
    "keep": "保持",
    "lead": "领导",
    "look after": "照顾",
    "pick up": "捡起",
    "propose": "建议",
    "protect": "保护",
    "put on": "穿上",
    "reclaim": "回收",
    "refer": "提交",
    "represent": "代表",
    "seem": "似乎",
    "take over": "接管",
    "thank": "感谢",
    "wear out": "用坏",
    "wrap": "包起来",
}


def gloss_for_sentence(entry: dict) -> str:
    forced = SENSE.get((entry.get("w") or "").lower())
    if forced:
        return forced
    gloss = short_zh(entry.get("zh") or "").strip("「」 ")
    return gloss or "这个"


def as_predicate(gloss: str) -> str:
    if gloss.endswith("的"):
        return "是" + gloss
    return "很" + gloss


def spoken_verb(surface: str) -> str:
    """Put a verb where a person can say it. Phrasal verbs keep a real object."""
    bare = {
        "break down", "break up", "come down", "get back", "get in", "get off",
        "get on", "get up", "give in", "give up", "go down", "go off",
        "go on", "go out", "hang up", "keep on", "look ahead", "look out",
        "set off", "set out", "slow down", "stay behind", "turn around", "wake up",
    }
    parts = surface.split()
    if surface in bare or len(parts) < 2:
        return surface
    if len(parts) >= 3:
        return surface + " it"
    verb, particle = parts
    separable = {
        "up", "down", "off", "on", "out", "away", "back", "in", "over",
        "through", "forward", "aside", "together",
    }
    if particle in separable and verb not in {"go", "come", "sit", "stand", "stay", "be"}:
        return f"{verb} it {particle}"
    return surface + " it"


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
    "conference": [
        {"k": "办公", "en": "The conference starts at nine. Please sit near the door.", "zh": "会议九点开始。请坐得靠门一点。"},
        {"k": "日常", "en": "We watched the game, then argued as if it were a conference.", "zh": "我们看完比赛，然后吵得像在开会。"},
        {"k": "搞笑", "en": "The conference had a dress code. The cat wore a tie.", "zh": "会议有着装要求。猫打了领带。"},
    ],
    "chair": [
        {"k": "办公", "en": "Please chair the meeting. I will take the minutes.", "zh": "请你主持会议。我来做记录。"},
        {"k": "日常", "en": "I bought a new chair and had nowhere to put the old one.", "zh": "我买了新椅子，旧的没地方放。"},
        {"k": "搞笑", "en": "She was asked to chair the meeting. She sat on the table.", "zh": "大家请她主持。她坐到了桌子上。"},
    ],
    "airport": [
        {"k": "办公", "en": "The client will meet you at the airport, not at the hotel.", "zh": "客户会在机场见你，不是在酒店。"},
        {"k": "日常", "en": "We reached the airport and remembered the tickets were at home.", "zh": "到了机场才想起票在家里。"},
        {"k": "搞笑", "en": "The airport called our flight. Our flight did not answer.", "zh": "机场呼叫我们的航班。航班没接。"},
    ],
    "bill": [
        {"k": "办公", "en": "Please check the bill before you pay it.", "zh": "付款前请先核对账单。"},
        {"k": "日常", "en": "The electricity bill arrived on a Sunday.", "zh": "电费账单星期天到了。"},
        {"k": "搞笑", "en": "The bill was longer than the meal.", "zh": "账单比那顿饭还长。"},
    ],
    "quote": [
        {"k": "办公", "en": "Can you quote a price before Friday?", "zh": "周五之前能报价吗？"},
        {"k": "日常", "en": "I quoted my mother. She said I had the words wrong.", "zh": "我引用了我妈的话。她说我引用错了。"},
        {"k": "搞笑", "en": "He quoted a very low price, then quoted a second one.", "zh": "他报了一个很低的价，然后又报了第二个。"},
    ],
    "business": [
        {"k": "办公", "en": "Business was quiet in August.", "zh": "八月的生意很清淡。"},
        {"k": "日常", "en": "She talked business all through lunch.", "zh": "午饭从头到尾她都在谈生意。"},
        {"k": "搞笑", "en": "We opened a business. The cat became head of complaints.", "zh": "我们开了家公司。猫成了投诉部主管。"},
    ],
    "law": [
        {"k": "办公", "en": "The contract has to follow the law.", "zh": "合同得符合法律。"},
        {"k": "日常", "en": "He explains the law better after coffee.", "zh": "喝完咖啡，他把法律讲得更清楚。"},
        {"k": "搞笑", "en": "The law was clear. Our excuse was creative.", "zh": "法律很清楚。我们的借口很有创意。"},
    ],
    "visa": [
        {"k": "办公", "en": "The visa arrived the day before the flight.", "zh": "签证在航班前一天到了。"},
        {"k": "日常", "en": "I checked the visa twice, then checked it again on the train.", "zh": "签证我查了两遍，上了火车又查一遍。"},
        {"k": "搞笑", "en": "The visa was ready. The passport was in another city.", "zh": "签证好了。护照在另一座城市。"},
    ],
    "payroll": [
        {"k": "办公", "en": "Payroll goes out on the last Friday.", "zh": "工资在最后一个周五发。"},
        {"k": "日常", "en": "We said we would not discuss payroll at dinner. We failed.", "zh": "我们说晚饭不谈工资。没做到。"},
        {"k": "搞笑", "en": "Payroll was late. The cat still expected lunch.", "zh": "工资晚了。猫仍然等着午饭。"},
    ],
    "team": [
        {"k": "办公", "en": "The team meets at half past eight.", "zh": "团队八点半开会。"},
        {"k": "日常", "en": "Our family team lost at cards.", "zh": "我们家这个队打牌输了。"},
        {"k": "搞笑", "en": "The team had five people and six opinions.", "zh": "团队五个人，六种意见。"},
    ],
    "project": [
        {"k": "办公", "en": "The project needs one more week.", "zh": "这个项目还要一周。"},
        {"k": "日常", "en": "I called washing the windows a project.", "zh": "我把擦玻璃叫成一个项目。"},
        {"k": "搞笑", "en": "The project plan was perfect. Nobody started.", "zh": "项目计划完美。没有人开工。"},
    ],
    "value": [
        {"k": "办公", "en": "The value of the stock fell on Monday.", "zh": "周一股价跌了。"},
        {"k": "日常", "en": "We argued about the value of a second coffee.", "zh": "我们争论第二杯咖啡值不值。"},
        {"k": "搞笑", "en": "The report said high value. The coffee disagreed.", "zh": "报告写着价值很高。咖啡并不同意。"},
    ],
    "net": [
        {"k": "办公", "en": "The net price does not include tax.", "zh": "净价不含税。"},
        {"k": "日常", "en": "I caught three apples in a shopping net.", "zh": "我用购物袋网兜装了三个苹果。"},
        {"k": "搞笑", "en": "Please send the net figure. He sent a picture of a fishing net.", "zh": "请把净额发来。他发来一张渔网的照片。"},
    ],
    "fair": [
        {"k": "办公", "en": "We will see you at the trade fair in March.", "zh": "三月的交易会上见。"},
        {"k": "日常", "en": "The fair was crowded, and the apples were cheap.", "zh": "集市很挤，苹果很便宜。"},
        {"k": "搞笑", "en": "The trade fair gave me a bag, three pens, and no customers.", "zh": "交易会给了我一个袋子、三支笔，没有客户。"},
    ],
    "minute": [
        {"k": "办公", "en": "Please send the minutes before the end of the day.", "zh": "请在今天下班前把会议记录发来。"},
        {"k": "日常", "en": "Give me a minute. I am looking for the house key.", "zh": "等我一分钟。我在找家门钥匙。"},
        {"k": "搞笑", "en": "The minutes were short. The meeting was not.", "zh": "会议记录很短。会议本身不短。"},
    ],
    "career": [
        {"k": "办公", "en": "She left the firm to change her career.", "zh": "她离开公司，是为了换一条职业路。"},
        {"k": "日常", "en": "My uncle still calls cooking a career.", "zh": "我舅舅仍然把做饭叫成一项事业。"},
        {"k": "搞笑", "en": "His career plan was one page. The doubts took three.", "zh": "职业计划只有一页。犹豫写了三页。"},
    ],
    "charge": [
        {"k": "办公", "en": "There is no delivery charge on this order.", "zh": "这张订单不收运费。"},
        {"k": "日常", "en": "Who is in charge of feeding the cat?", "zh": "谁负责喂猫？"},
        {"k": "搞笑", "en": "They charged me for water. The water was free on the sign.", "zh": "他们收了我的水钱。牌子上写着水是免费的。"},
    ],
    "firm": [
        {"k": "办公", "en": "The firm will reply by Thursday.", "zh": "公司周四前回复。"},
        {"k": "日常", "en": "Be firm. The child has already had two biscuits.", "zh": "坚定一点。这孩子已经吃了两块饼干。"},
        {"k": "搞笑", "en": "The firm has a mission statement. The cat has the desk.", "zh": "公司有使命宣言。猫占着桌子。"},
    ],
    "board": [
        {"k": "办公", "en": "The board meets on the first Monday.", "zh": "董事会在第一个星期一开会。"},
        {"k": "日常", "en": "I carried the board up the stairs by myself.", "zh": "我自己把木板扛上了楼。"},
        {"k": "搞笑", "en": "The board approved the plan. Nobody could find a pen.", "zh": "董事会通过了计划。没有人找得到笔。"},
    ],
    "data": [
        {"k": "办公", "en": "The data arrived, but the labels were missing.", "zh": "数据到了，标签没到。"},
        {"k": "日常", "en": "I keep the family data in one notebook.", "zh": "家里的数据我记在一个本子上。"},
        {"k": "搞笑", "en": "The data was confidential. Someone had left it on the train.", "zh": "数据是保密的。有人把它落在火车上了。"},
    ],
    "scale": [
        {"k": "办公", "en": "We cannot raise salaries on this scale.", "zh": "按这个级别，工资加不了。"},
        {"k": "日常", "en": "I stood on the scale and then had a biscuit.", "zh": "我站上秤，然后吃了块饼干。"},
        {"k": "搞笑", "en": "The pay scale was fair. The biscuit scale was not.", "zh": "工资等级很公平。饼干的秤并不公平。"},
    ],
}


def fill_pair(english: str, chinese: str, word: str, gloss: str, verb: str) -> dict:
    en = (
        english.replace("{w}", word)
        .replace("{v}", verb)
        .replace("{W}", (word[:1].upper() + word[1:]) if word else word)
    )
    if word.endswith(".") and en.endswith(word + "."):
        en = en[:-1]
    return {
        "en": en,
        "zh": chinese.replace("{g}", gloss).replace("{p}", as_predicate(gloss)),
    }


def example_sentences(entry: dict) -> list[dict]:
    hand = HAND_XS.get(entry["w"].lower())
    if hand:
        return [dict(item) for item in hand][:4]
    if entry["w"].lower() == "used to":
        return [
            {"k": "办公", "en": "We used to send the invoice on Friday.", "zh": "我们以前都在周五寄发票。"},
            {"k": "日常", "en": "I used to walk home.", "zh": "我以前都是走回家。"},
            {"k": "搞笑", "en": "The cat used to wait by the door. Now it waits on the keyboard.", "zh": "猫以前在门口等。现在它在键盘上等。"},
        ]
    word = surface_word(entry["w"])
    gloss = gloss_for_sentence(entry)
    kind = pos_kind(entry.get("pos") or "")
    verb = spoken_verb(word)
    if "." in word or len(word) <= 1 or kind == "small":
        office_pairs = [
            ("The line begins with {w}.", "这一行以{g}开头。"),
            ("Please don't leave {w} out.", "请不要把{g}漏掉。"),
            ("She wrote {w} and then stopped.", "她写了{g}，然后停住了。"),
        ]
        daily_pairs = [
            ("I heard someone say {w} on the bus.", "我在公交上听见有人说{g}。"),
            ("The form still has {w} on it.", "表格上还留着{g}。"),
            ("He texted me {w} and nothing else.", "他只给我发了{g}。"),
        ]
        funny_pairs = [
            ("The coffee machine showed {w} and refused to explain.", "咖啡机显示了{g}，拒绝解释。"),
            ("My cat walked across the keyboard and left {w}.", "猫从键盘上走过，留下了{g}。"),
            ("Everyone looked at {w} on the screen, then at the cat.", "大家都看着屏幕上的{g}，然后看向猫。"),
        ]
    elif kind == "v":
        office_pairs = [
            ("We still need to {v} before Friday.", "周五之前我们还得{g}。"),
            ("They asked me to {v} today.", "他们让我今天就{g}。"),
            ("I will {v} after the meeting.", "会后我会{g}。"),
        ]
        daily_pairs = [
            ("I can {v} when I get home.", "到家之后我可以{g}。"),
            ("She will {v} tomorrow morning.", "她明天早上会{g}。"),
            ("We can {v} after dinner.", "晚饭后我们可以{g}。"),
        ]
        funny_pairs = [
            ("I was about to {v} when the phone rang.", "我正要{g}，电话响了。"),
            ("Nobody wanted to {v}, so we had coffee.", "没人愿意{g}，于是我们喝了咖啡。"),
            ("I was ready to {v}. The printer was not.", "我准备好{g}了。打印机没有。"),
        ]
    elif kind == "adj":
        office_pairs = [
            ("They called the plan {w}.", "他们说这个方案{p}。"),
            ("I would not call this draft {w}.", "我不会说这份草稿{p}。"),
            ("The email sounded {w}.", "那封邮件听上去{p}。"),
        ]
        daily_pairs = [
            ("The soup was {w}, and I still ate it.", "汤{p}，我还是喝了。"),
            ("He looked {w} after the long day.", "忙了一天，他看上去{p}。"),
            ("It felt {w} on the way home.", "回家的路上，那种感觉{p}。"),
        ]
        funny_pairs = [
            ("My boss called it {w}. The cat stayed quiet.", "老板说它{p}。猫没吭声。"),
            ("The cake was {w}. We still put it on the table.", "蛋糕{p}。我们还是把它放上了桌。"),
            ("Even the sign looked {w}.", "连招牌看上去都{p}。"),
        ]
    elif kind == "adv":
        office_pairs = [
            ("Could you say that {w}?", "你能{g}说这句话吗？"),
            ("Please read the numbers {w}.", "请{g}把数字读一下。"),
            ("She explained it {w}.", "她{g}作了解释。"),
        ]
        daily_pairs = [
            ("She answered {w}, then smiled.", "她{g}回答，然后笑了。"),
            ("I will call you {w}.", "我会{g}给你打电话。"),
            ("He closed the door {w}.", "他{g}关上了门。"),
        ]
        funny_pairs = [
            ("The cat walked in {w}, as if it paid the rent.", "猫{g}走了进来，好像房租是它付的。"),
            ("She nodded {w}. The coffee did not.", "她{g}点了头。咖啡没有。"),
            ("He apologised {w}, still holding the invoice.", "他{g}道了歉，手里还拿着发票。"),
        ]
    else:
        office_pairs = [
            ("Can we talk about {w} before lunch?", "午饭前我们能谈谈{g}吗？"),
            ("I left a note about {w} on your desk.", "我在你桌上留了张关于{g}的条子。"),
            ("{W} is still on my list for today.", "{g}还在我今天的单子上。"),
        ]
        daily_pairs = [
            ("I was still thinking about {w} on the way home.", "回家的路上我还在想{g}。"),
            ("She mentioned {w} while we were eating.", "吃饭的时候她提起了{g}。"),
            ("We can leave {w} until tomorrow.", "我们可以把{g}留到明天。"),
        ]
        funny_pairs = [
            ("I tried to forget about {w}. My inbox would not let me.", "我想忘掉{g}。收件箱不让。"),
            ("The cat sat on the only note about {w}.", "猫坐在唯一那张关于{g}的条子上。"),
            ("Everyone nodded about {w}, then changed the subject.", "大家就{g}点了点头，然后换了话题。"),
        ]
    office = fill_pair(*choose(word, 1, office_pairs), word, gloss, verb)
    daily = fill_pair(*choose(word, 2, daily_pairs), word, gloss, verb)
    funny = fill_pair(*choose(word, 3, funny_pairs), word, gloss, verb)
    return [
        {"k": "办公", **office},
        {"k": "日常", **daily},
        {"k": "搞笑", **funny},
    ]


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
    more_germanic = {word.lower() for word in MORE_GERMANIC}
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
        loan = MORE_ETYM.get(key)
        if loan:
            entry["et"] = loan
            entry["ek"] = "traced"
            continue
        kind_note = EXTRA_KIND.get(key)
        if kind_note:
            entry["ek"], entry["et"] = kind_note
            continue
        if key in germanic:
            entry["et"] = (
                f"{entry['w']} 是英语的日耳曼本族词，来自古英语这一支，不是从拉丁语或希腊语借来的。"
                "商务英语里，句子的骨架（冠词、代词、介词、助动词）大多是这类词；"
                "拉丁语和希腊语更多出现在合同、财务和抽象概念里。"
            )
            entry["ek"] = "germanic"
            continue
        if key in more_germanic:
            entry["et"] = (
                f"{entry['w']} 是英语里的日耳曼本族词，不是从拉丁语或希腊语整词借来的。"
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
        for row in entry["xs"]:
            rel = line_audio_rel(row["en"])
            audio_file = ROOT / "docs" / rel
            if audio_file.exists() and audio_file.stat().st_size > 500:
                row["au"] = rel
            else:
                row.pop("au", None)
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
        scene_copy = {**scene, "words": kept, "lines": [dict(line) for line in scene.get("lines") or []]}
        for line in scene_copy["lines"]:
            rel = line_audio_rel(line.get("en") or "")
            audio_file = ROOT / "docs" / rel
            if line.get("en") and audio_file.exists() and audio_file.stat().st_size > 500:
                line["au"] = rel
        scenes.append(scene_copy)

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
