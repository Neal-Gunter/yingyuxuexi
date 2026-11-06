# -*- coding: utf-8 -*-
"""Topic books and pairs that are easy to confuse."""

BOOKS = [
    {
        "id": "meet",
        "title": "会议",
        "blurb": "开会、议程、截止日期、确认和取消",
        "words": ["meeting", "agenda", "minutes", "deadline", "manager", "staff", "report", "email", "appointment", "cancel", "confirm", "arrange", "conference", "chair", "copy", "decision", "proposal", "schedule"],
    },
    {
        "id": "money",
        "title": "钱",
        "blurb": "工资、发票、预算、付款和账户",
        "words": ["salary", "wage(s)", "invoice", "payment", "budget", "cash", "receipt", "refund", "discount", "price", "tax", "account", "balance", "credit", "debit", "bonus", "overtime", "insurance", "bank", "cost", "profit", "loss", "cheque"],
    },
    {
        "id": "travel",
        "title": "旅行",
        "blurb": "航班、酒店、行李、票和延误",
        "words": ["flight", "hotel", "luggage", "ticket", "passport", "reserve", "delay", "travel", "trip", "visitor", "guest", "journey", "booking", "airport"],
    },
    {
        "id": "people",
        "title": "人事",
        "blurb": "雇主、培训、部门、面试和合同",
        "words": ["employer", "employee", "staff", "salary", "training", "department", "interview", "candidate", "recruitment", "contract", "manager", "colleague", "director"],
    },
    {
        "id": "office",
        "title": "办公",
        "blurb": "桌子、电脑、电话、打印机和信",
        "words": ["office", "desk", "computer", "phone", "printer", "email", "fax", "copy", "file", "calendar", "clock", "chair", "letter", "report"],
    },
    {
        "id": "papers",
        "title": "单据",
        "blurb": "发票、收据、支票、表格和护照",
        "words": ["invoice", "receipt", "bill", "cheque", "form", "contract", "ticket", "passport", "stamp", "signature", "envelope", "parcel"],
    },
    {
        "id": "trip",
        "title": "出行",
        "blurb": "航班、火车、出租车、酒店和早餐",
        "words": ["flight", "train", "taxi", "bus", "car", "hotel", "passport", "ticket", "luggage", "breakfast", "restaurant", "menu"],
    },
    {
        "id": "trade",
        "title": "买卖",
        "blurb": "顾客、商店、产品、折扣和现金",
        "words": ["customer", "shop", "product", "discount", "order", "delivery", "cash", "money", "receipt", "bill", "price", "supplier"],
    },
]

PAIRS = [
    {
        "id": "meet-conference",
        "title": "meeting / conference",
        "left": "meeting",
        "right": "conference",
        "note": "两个词都能说会议。meeting 来自日耳曼语 meet「遇见」。conference 来自拉丁语 conferre「带到一起」。日常会常用 meeting，更正式的会常用 conference。",
    },
    {
        "id": "customer-client",
        "title": "customer / client",
        "left": "customer",
        "right": "client",
        "note": "都是客户。customer 来自拉丁语 consuetudo「习惯」，原是常来买的人。client 来自拉丁语 cliens，原是听从庇护人的人，现在多指把专业服务托给你的一方。",
    },
    {
        "id": "salary-wage",
        "title": "salary / wage",
        "left": "salary",
        "right": "wage(s)",
        "note": "都是报酬。salary 来自拉丁语 sal「盐」，传统上和买盐的津贴有关，多按月发。wage 来自日耳曼语里的「抵押、保证」，多按小时或按周发。",
    },
    {
        "id": "buy-purchase",
        "title": "buy / purchase",
        "left": "buy",
        "right": "purchase",
        "note": "都是买。buy 是日耳曼本族词。purchase 经法语来自拉丁语「向前抓取」，语气更正式，合同和报表里更常见。",
    },
    {
        "id": "contact-contract",
        "title": "contact / contract",
        "left": "contact",
        "right": "contract",
        "note": "只差一个字母。contact 是拉丁语 tangere「触摸」，碰到一起。contract 是拉丁语 trahere「拉」，把双方拉到同一张契约上。",
    },
    {
        "id": "law-legal",
        "title": "law / legal",
        "left": "law",
        "right": "legal",
        "note": "都和法有关。law 来自古诺斯语，是日耳曼词。legal 来自拉丁语 lex「法」。句子里可以同时出现：The contract is legal under Chinese law.",
    },
    {
        "id": "worth-value",
        "title": "worth / value",
        "left": "worth",
        "right": "value",
        "note": "都是价值。worth 是日耳曼词。value 来自拉丁语 valere「值钱」。worth 常放在 be 后面，value 更能作名词和动词。",
    },
    {
        "id": "wholesale-retail",
        "title": "wholesale / retail",
        "left": "wholesale",
        "right": "retail",
        "note": "批发和零售。wholesale 是日耳曼词 whole「整」加上 sale「卖」。retail 来自古法语「切成小块」，是一小份一小份地卖。",
    },
    {
        "id": "borrow-lend",
        "title": "borrow / lend",
        "left": "borrow",
        "right": "lend",
        "note": "都是日耳曼词，方向相反。borrow 来自古英语 borgian，是把东西借进来。lend 来自古英语 lænan，是把东西借出去。",
    },
    {
        "id": "say-tell",
        "title": "say / tell",
        "left": "say",
        "right": "tell",
        "note": "都是日耳曼词。say 来自古英语 secgan，着重说出来的那句话。tell 来自古英语 tellan，原是点数，后来是告诉某一个人。",
    },
    {
        "id": "price-cost",
        "title": "price / cost",
        "left": "price",
        "right": "cost",
        "note": "都和钱有关，来路不同。price 来自古法语 pris，拉丁语 pretium「价钱」。cost 来自古法语，拉丁语 constare「停在某个数目上」，是花掉的成本。",
    },
    {
        "id": "staff-stuff",
        "title": "staff / stuff",
        "left": "staff",
        "right": "stuff",
        "note": "只差一个字母。staff 来自古英语 stæf「杆」，后来是一班人。stuff 来自古法语 estoffe，是材料、东西。",
    },
    {
        "id": "personal-personnel",
        "title": "personal / personnel",
        "left": "personal",
        "right": "personnel",
        "note": "同一条拉丁语 persona「面具、人」。personal 是私人的。personnel 经法语表示一批人员。",
    },
    {
        "id": "affect-effect",
        "title": "affect / effect",
        "left": "affect",
        "right": "effect",
        "note": "都来自拉丁语 facere「做」。affect 是 ad + facere，对某事发生作用。effect 是 ex + facere，做出来的结果。",
    },
]
