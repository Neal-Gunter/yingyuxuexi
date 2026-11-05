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
    if re.search(r"[?!£$]", word) or word.endswith("."):
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
            for origin, limit in ((72.0, 300.0), (315.6, 560.0)):
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
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    text = "window.YY = " + json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + ";\n"
    OUT.write_text(text, encoding="utf-8")
    print(json.dumps(counts, ensure_ascii=False, indent=2))
    if missing:
        print("missing gloss sample:", ", ".join(missing[:30]))


if __name__ == "__main__":
    main()
