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
]
