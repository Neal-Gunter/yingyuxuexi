# -*- coding: utf-8 -*-
"""Hand-written examples for high-frequency words whose templates sounded wrong.

These replace only the listed headwords. The other generated sentences stay.
"""

def _three(office, daily, funny):
    return [
        {"k": "办公", "en": office[0], "zh": office[1]},
        {"k": "日常", "en": daily[0], "zh": daily[1]},
        {"k": "搞笑", "en": funny[0], "zh": funny[1]},
    ]


HAND_MORE = {
    "desk": _three(
        ("Please leave the report on my desk.", "请把报告放在我的桌上。"),
        ("The cat has taken the sunny spot on the desk.", "猫占了桌上有阳光的地方。"),
        ("I cleared the desk. The cat put the pen back.", "我把桌子收拾干净了。猫把笔放了回去。"),
    ),
    "arrive": _three(
        ("The client will arrive at nine.", "客户九点到。"),
        ("We arrived home after the rain.", "雨停以后我们到了家。"),
        ("I arrived early. The meeting arrived late.", "我到得早。会议到得晚。"),
    ),
    "office": _three(
        ("I will be in the office until six.", "我在办公室待到六点。"),
        ("She works in a small office above a shop.", "她在一家商店楼上的小办公室上班。"),
        ("The office was quiet. The printer was not.", "办公室很安静。打印机不是。"),
    ),
    "door": _three(
        ("Please close the door during the call.", "打电话时请关上门。"),
        ("I left the door open and the cat walked in.", "我没关门，猫走进来了。"),
        ("Someone knocked. The cat answered. The door stayed shut.", "有人敲门。猫应了。门还关着。"),
    ),
    "window": _three(
        ("The meeting-room window does not open.", "会议室的窗户打不开。"),
        ("Rain came in through the open window.", "雨从开着的窗户飘进来。"),
        ("The window was clean until the cat inspected it.", "窗户本来是干净的，直到猫去检查了一下。"),
    ),
    "house": _three(
        ("The company bought the house next to the factory.", "公司买下了工厂旁边的那栋房子。"),
        ("We got home and found the house dark.", "我们到家时，房子是黑的。"),
        ("I locked the house. The key was still inside.", "我把房子锁上了。钥匙还在里面。"),
    ),
    "home": _three(
        ("I will finish this at home tonight.", "今晚我在家把这个做完。"),
        ("The bus was late, so I walked home.", "公交晚了，所以我走路回家。"),
        ("I work from home. The cat is the manager.", "我在家办公。猫是经理。"),
    ),
    "room": _three(
        ("Is the meeting room free at three?", "三点会议室有空吗？"),
        ("This room is too small for six people.", "这个房间坐六个人太小。"),
        ("We booked a quiet room. The room next door did not.", "我们订了一间安静的房间。隔壁没有。"),
    ),
    "city": _three(
        ("Our city office closes at five.", "城里的办公室五点关门。"),
        ("I like this city early in the morning.", "我喜欢清晨的这座城市。"),
        ("The city never sleeps. I do, badly.", "这座城市不睡觉。我睡，而且睡不好。"),
    ),
    "people": _three(
        ("Twelve people are coming to the meeting.", "十二个人来开会。"),
        ("Too many people got on the bus.", "上车的人太多了。"),
        ("People called the plan simple. They had not read page four.", "大家都说计划很简单。他们没看第四页。"),
    ),
    "time": _three(
        ("We do not have time for another draft.", "我们没有时间再改一稿。"),
        ("What time does the shop close?", "商店几点关门？"),
        ("I was on time. The bus was on some other time.", "我准时到了。公交在另一个时间里。"),
    ),
    "day": _three(
        ("Please send it by the end of the day.", "请在今天下班前发来。"),
        ("It was a long day, and the soup helped.", "这一天很长，汤帮了忙。"),
        ("The calendar said it was a short day. The inbox disagreed.", "日历说这一天很短。收件箱不同意。"),
    ),
    "year": _three(
        ("Sales were higher than last year.", "销售额比去年高。"),
        ("This year I will remember his birthday.", "今年我会记得他的生日。"),
        ("The report covers the whole year. Page one covers January.", "报告覆盖全年。第一页只写了一月。"),
    ),
    "week": _three(
        ("Can we move the meeting to next week?", "会议能改到下周吗？"),
        ("I do the washing on Sunday and plan it for the rest of the week.", "我周日洗衣服，一周里的其他日子则在计划洗衣服。"),
        ("It felt like a short week. The inbox did not notice.", "感觉这周很短。收件箱没看出来。"),
    ),
    "weather": _three(
        ("Bad weather delayed the delivery.", "坏天气耽误了送货。"),
        ("The weather looks fine, so I will walk.", "天气看起来不错，所以我走路去。"),
        ("The weather forecast promised sun. My shoes did not believe it.", "天气预报保证有太阳。我的鞋不信。"),
    ),
    "problem": _three(
        ("The problem is the date on the invoice.", "问题出在发票的日期上。"),
        ("The only problem is the missing house key.", "唯一的问题是家门钥匙不见了。"),
        ("We solved the problem. The solution invented a new one.", "我们解决了问题。这个办法又造出一个新问题。"),
    ),
    "question": _three(
        ("I have one question about the contract.", "关于合同我有一个问题。"),
        ("She asked a question and then answered it herself.", "她问了一个问题，然后自己回答了。"),
        ("Any questions? The cat raised a paw. Nobody called on it.", "有问题吗？猫举起一只爪子。没人点它。"),
    ),
    "company": _three(
        ("The company will pay for the train.", "公司会付火车票的钱。"),
        ("I enjoy his company, not his singing.", "我喜欢有他作伴，不喜欢他唱歌。"),
        ("The company has a vision. The vision has no budget.", "公司有愿景。愿景没有预算。"),
    ),
    "work": _three(
        ("The work is due on Friday.", "这件工作周五到期。"),
        ("I work near the station.", "我在车站附近上班。"),
        ("I finished the work. The work had not finished with me.", "我做完了工作。工作还没做完我。"),
    ),
    "car": _three(
        ("The client came by car.", "客户是开车来的。"),
        ("The car would not start, so we took the bus.", "车发动不了，所以我们坐了公交。"),
        ("I washed the car. The rain washed the joke.", "我洗了车。雨把这个笑话洗了一遍。"),
    ),
    "train": _three(
        ("I will take the early train.", "我坐早班火车。"),
        ("The train was full, and so was my bag.", "火车满了，我的包也满了。"),
        ("The train left on time. My ticket was for the next one.", "火车准时开了。我的票是下一班。"),
    ),
    "bus": _three(
        ("The bus to the office takes twenty minutes.", "去办公室的公交要二十分钟。"),
        ("I missed the bus and met a neighbour.", "我没赶上公交，碰上了邻居。"),
        ("I ran for the bus. The bus preferred to leave.", "我追公交。公交更想开走。"),
    ),
    "leave": _three(
        ("She is on leave until Monday.", "她休假到周一。"),
        ("Please leave the light on.", "请把灯留着。"),
        ("I asked for leave. The inbox asked me to stay.", "我请了假。收件箱请我留下。"),
    ),
    "die": _three(
        ("The old contract dies at the end of March.", "旧合同在三月底失效。"),
        ("The flowers die if nobody waters them.", "没人浇水，花就会枯死。"),
        ("My phone battery died in the middle of the excuse.", "借口说到一半，手机没电了。"),
    ),
    "happen": _three(
        ("If that happens, call me at once.", "如果发生那种情况，马上打电话给我。"),
        ("It happened on the way home.", "这件事发生在回家的路上。"),
        ("Nothing happened. Then the printer happened.", "本来什么都没发生。然后打印机发生了。"),
    ),
    "cost": _three(
        ("The cost is higher than the quote.", "成本比报价高。"),
        ("These apples cost too much.", "这些苹果太贵了。"),
        ("The meeting cost two hours. The decision cost one sentence.", "会议花了两小时。决定只用了一句话。"),
    ),
    "seem": _three(
        ("The figures seem right.", "这些数字看起来是对的。"),
        ("You seem tired. Sit down.", "你看起来累了。坐下吧。"),
        ("It seemed easy until we opened the box.", "打开盒子之前，它看起来很容易。"),
    ),
    "become": _three(
        ("She became manager in May.", "她五月当上了经理。"),
        ("The sky became dark before dinner.", "晚饭前天就黑了。"),
        ("The plan became a spreadsheet. The spreadsheet became a problem.", "计划变成了表格。表格变成了问题。"),
    ),
    "table": _three(
        ("The figures are in the table on page two.", "数字在第二页的表里。"),
        ("Dinner is on the table.", "晚饭摆上桌了。"),
        ("I set the table. The cat sat in the middle of it.", "我摆好了桌子。猫坐到了桌子中间。"),
    ),
    "book": _three(
        ("Please book a room for Tuesday.", "请订周二的房间。"),
        ("I read that book twice.", "那本书我读了两遍。"),
        ("I booked a quiet seat. The person beside me booked a long call.", "我订了一个安静的座位。旁边的人订了一通很长的电话。"),
    ),
    "money": _three(
        ("The money should reach the account today.", "这笔钱今天应该到账。"),
        ("I had money for coffee and none for the bus.", "我的钱够买咖啡，不够坐公交。"),
        ("Money cannot buy time. It can buy a faster printer.", "钱买不到时间。它可以买一台更快的打印机。"),
    ),
    "man": _three(
        ("The man at reception has your badge.", "前台那位男士拿着你的证件。"),
        ("An old man held the door for me.", "一位老人替我拉住了门。"),
        ("The man wanted a refund. The receipt stayed in his other coat.", "他想退款。收据在另一件外套里。"),
    ),
    "woman": _three(
        ("The woman who called is our new client.", "打电话来的那位女士是我们的新客户。"),
        ("A woman on the bus offered me her seat.", "公交上一位女士把座位让给了我。"),
        ("The woman asked for a quiet table. The table was quiet. The kitchen was not.", "那位女士要了一张安静的桌子。桌子是安静的。厨房不是。"),
    ),
    "child": _three(
        ("She left early to collect her child.", "她提早走，去接孩子。"),
        ("The child ate the biscuit and looked innocent.", "孩子吃了饼干，一脸无辜。"),
        ("The child pressed one button. The office learned a new noise.", "孩子按了一个按钮。办公室认识了一种新声音。"),
    ),
    "friend": _three(
        ("A friend on the other team sent the file.", "另一个组的朋友把文件发来了。"),
        ("I had lunch with an old friend.", "我和一位老朋友吃了午饭。"),
        ("My friend said it would take five minutes. That was an hour ago.", "朋友说只要五分钟。这话是一小时前说的。"),
    ),
    "family": _three(
        ("He is away on family leave.", "他在休家事假。"),
        ("The whole family came for dinner.", "全家都来吃饭了。"),
        ("I told the family I was busy. They sent the cat to check.", "我跟家里说我很忙。他们派猫来核实。"),
    ),
    "food": _three(
        ("Food at the hotel is included in the price.", "酒店的餐食含在价格里。"),
        ("There is no food in the house except biscuits.", "家里除了饼干没有吃的。"),
        ("The meeting had no food. That became the real subject.", "会上没有吃的。这成了真正的议题。"),
    ),
    "morning": _three(
        ("I will send it in the morning.", "我早上发。"),
        ("The morning was cold, and the coffee was late.", "早上很冷，咖啡来得晚。"),
        ("Good morning. The inbox had already started without me.", "早上好。收件箱已经先开工了。"),
    ),
    "night": _three(
        ("The night shift answers the phone.", "夜班负责接电话。"),
        ("I read for an hour last night.", "昨晚我读了一小时书。"),
        ("I said I would answer at night. Night came. I did not.", "我说晚上回复。晚上来了。我没有。"),
    ),
    "school": _three(
        ("She joined us straight from business school.", "她从商学院一出来就到我们这里了。"),
        ("School starts again on Monday.", "周一又要上学了。"),
        ("School taught me the dates. The calendar still surprises me.", "学校教过我这些日期。日历仍然吓我一跳。"),
    ),
    "name": _three(
        ("Please write your name on the form.", "请在表格上写下你的名字。"),
        ("I forgot his name and remembered his dog's.", "我忘了他的名字，记住了他家狗的名字。"),
        ("The form asked for my name, then asked again.", "表格要了我的名字，然后又要了一次。"),
    ),
    "place": _three(
        ("Please keep my place in the meeting.", "开会请给我留个位置。"),
        ("This is a good place for lunch.", "这里适合吃午饭。"),
        ("I saved a place for the report. The cat saved it for sleeping.", "我给报告留了个地方。猫把它留来睡觉。"),
    ),
    "world": _three(
        ("We sell in three countries, not the whole world.", "我们在三个国家卖，不是卖到全世界。"),
        ("The world looks kinder after coffee.", "喝过咖啡，世界和气一些。"),
        ("The world can wait. The kettle cannot.", "世界可以等。水壶不行。"),
    ),
    "life": _three(
        ("Work and life are both on the agenda.", "工作和生活都在议程上。"),
        ("Life is easier when the bus is on time.", "公交准时的时候，日子好过一些。"),
        ("I wanted a quiet life. Then I bought a printer.", "我想过安静的日子。然后我买了打印机。"),
    ),
    "country": _three(
        ("The tax rule is different in each country.", "每个国家的税规不一样。"),
        ("We drove into the country for the day.", "我们开车去乡下待了一天。"),
        ("He knows every country on the form and none of the bus routes.", "表格上的每个国家他都知道。公交线路一条都不知道。"),
    ),
    "street": _three(
        ("The new office is on a quiet street.", "新办公室在一条安静的街上。"),
        ("I live three streets from the station.", "我住的地方离车站三条街。"),
        ("The meeting was across the street. So was the rain.", "会议在街对面。雨也在街对面。"),
    ),
    "road": _three(
        ("The factory is just off the main road.", "工厂就在大路旁边。"),
        ("This road goes all the way home.", "这条路一直通向家。"),
        ("The road was closed. My map had not heard.", "路封了。我的地图还没听说。"),
    ),
    "phone": _three(
        ("Please phone the client before noon.", "请在中午前给客户打电话。"),
        ("My phone was in the fridge. I was not.", "手机在冰箱里。我不在。"),
        ("The phone rang during the meeting. It was my reminder about the meeting.", "电话在会上响了。是我自己设的会议提醒。"),
    ),
    "computer": _three(
        ("The computer restarted and took the draft with it.", "电脑重启了，草稿也一起走了。"),
        ("I use one computer at home and one at work.", "我家里一台电脑，单位一台。"),
        ("The computer asked me to wait. I have been waiting since Tuesday.", "电脑让我等一等。我从周二等到现在。"),
    ),
    "paper": _three(
        ("Please print it on white paper.", "请用白纸打印。"),
        ("I wrote the shopping list on a scrap of paper.", "我把购物清单写在一张纸上。"),
        ("We said we would use less paper, then printed the notice.", "我们说要少用纸，然后把通知打印了出来。"),
    ),
    "idea": _three(
        ("That idea will not fit the budget.", "那个主意放不进预算。"),
        ("I had an idea in the shower and lost it on the stairs.", "我洗澡时有了个主意，在楼梯上把它弄丢了。"),
        ("It was a good idea until we tried it before coffee.", "这主意不错，直到我们在喝咖啡之前拿它试了试。"),
    ),
    "information": _three(
        ("I need more information before I sign.", "签字前我需要更多信息。"),
        ("The notice had all the information except the time.", "通知上信息很全，就是没有时间。"),
        ("For more information, ask the person who has already left.", "想知道更多，请问已经离开的那个人。"),
    ),
    "news": _three(
        ("The news about the contract came this morning.", "合同的消息是今天早上来的。"),
        ("I heard the news from a neighbour.", "这个消息我是从邻居那儿听来的。"),
        ("There is good news and bad news. The good news is short.", "有好消息，也有坏消息。好消息比较短。"),
    ),
    "order": _three(
        ("Please confirm the order by email.", "请用邮件确认订单。"),
        ("The children would not sit in the order I chose.", "孩子们不肯按我排的顺序坐。"),
        ("I ordered soup. The kitchen ordered a delay.", "我点了汤。厨房点了一份拖延。"),
    ),
    "plan": _three(
        ("The plan is to ship on Thursday.", "计划是周四发货。"),
        ("Our plan was a walk. Then we met the rain.", "我们的计划是散步。然后我们遇上了雨。"),
        ("Plan A needed a pen. Plan B needed a miracle.", "甲方案需要一支笔。乙方案需要一个奇迹。"),
    ),
    "price": _three(
        ("The price does not include delivery.", "价格不含运费。"),
        ("The price of coffee went up again.", "咖啡又涨价了。"),
        ("The price was fair. My face was less fair.", "价格很公道。我的脸色没那么公道。"),
    ),
    "job": _three(
        ("The job starts on the first of May.", "这份工作五月一日开始。"),
        ("I like the job. I do not like the alarm.", "我喜欢这份工作。我不喜欢闹钟。"),
        ("The job description was one page. The surprises took three.", "职位说明只有一页。意外写了三页。"),
    ),
    "forget": _three(
        ("Please do not forget the attachment.", "请别忘了附件。"),
        ("I forgot the bread and remembered the biscuits.", "我忘了面包，记住了饼干。"),
        ("I forgot nothing. I also forgot to check.", "我什么都没忘。我也忘了核对。"),
    ),
    "read": _three(
        ("Please read the note at the bottom.", "请读底部的那条说明。"),
        ("I read on the bus until my stop.", "我在公交上一直读到下车。"),
        ("I read the email three times. It was still about the printer.", "那封邮件我读了三遍。还是在说打印机。"),
    ),
    "speak": _three(
        ("She will speak first at the meeting.", "会上她第一个发言。"),
        ("He speaks quietly on the phone at night.", "他晚上打电话时声音很轻。"),
        ("I was about to speak. The kettle spoke first.", "我正要开口。水壶先叫了。"),
    ),
    "call": _three(
        ("I will call you after the meeting.", "会后我打电话给你。"),
        ("A neighbour called to say the window was open.", "邻居打电话来说窗户开着。"),
        ("I returned the call. The caller had already given up.", "我回了电话。对方已经放弃了。"),
    ),
    "understand": _three(
        ("I do not understand line four of the quote.", "报价单第四行我看不懂。"),
        ("She understood the joke a minute later.", "她过了一分钟才听懂那个笑话。"),
        ("Everyone understood the plan until the first question.", "第一个问题出现之前，大家都懂这个计划。"),
    ),
    "stay": _three(
        ("Please stay for the second meeting.", "请留下开第二个会。"),
        ("Stay there. I am coming down.", "待在那儿。我马上下来。"),
        ("I stayed late. The lights stayed later.", "我留到很晚。灯留得更晚。"),
    ),
    "show": _three(
        ("Can you show me the latest figures?", "能把最新的数字给我看看吗？"),
        ("The film starts at seven. I will show you the way.", "电影七点开始。我带你去。"),
        ("The chart showed growth. The biscuit tin showed the truth.", "图表显示在增长。饼干罐显示了实际情况。"),
    ),
    "water": _three(
        ("Please put a jug of water in the meeting room.", "请在会议室放一壶水。"),
        ("The water in this kettle takes a long time to boil.", "这壶水要烧很久。"),
        ("I asked for water. They brought a form about water.", "我要了水。他们拿来一张关于水的表格。"),
    ),
    "bank": _three(
        ("The payment is still with the bank.", "这笔付款还在银行那边。"),
        ("I stopped at the bank on the way home.", "回家路上我去了趟银行。"),
        ("The bank was closed. My question was still open.", "银行关门了。我的问题还开着。"),
    ),
    "shop": _three(
        ("The staff shop sells last year's samples.", "员工商店卖去年的样品。"),
        ("I will stop at the shop for bread.", "我去商店买面包。"),
        ("I went to the shop for one thing and came out with a story.", "我去商店只为买一样东西，出来时多了一个故事。"),
    ),
    "bag": _three(
        ("Put the samples in the black bag.", "把样品放进黑袋子里。"),
        ("My bag is heavier than my lunch.", "我的包比午饭还重。"),
        ("I packed the bag. The bus helped it unpack.", "我装好了包。公交帮它拆开了。"),
    ),
    "station": _three(
        ("Meet me at the station, not at the office.", "在车站见，别在办公室见。"),
        ("The station cafe already knows my order.", "车站咖啡馆已经知道我要点什么。"),
        ("I reached the station on time. The train had other plans.", "我准时到了车站。火车另有安排。"),
    ),
    "hour": _three(
        ("The call took an hour.", "这通电话打了一个小时。"),
        ("I waited an hour for the bus.", "我等了一个小时的公交。"),
        ("He said it would take an hour. Bring a book.", "他说只要一个小时。带本书去吧。"),
    ),
    "month": _three(
        ("The figures for this month are not final.", "这个月的数字还不是最终的。"),
        ("The rent is due at the start of the month.", "房租在月初交。"),
        ("This month felt long. The calendar agreed. My manager did not.", "这个月感觉很长。日历同意。我的经理不同意。"),
    ),
    "number": _three(
        ("What is the order number?", "订单号是多少？"),
        ("I saved his number and lost the name.", "我存了他的号码，把名字丢了。"),
        ("The number looked familiar. It was my own.", "这个号码很眼熟。是我自己的。"),
    ),
    "way": _three(
        ("This is the fastest way to send it.", "这是把它发出去最快的办法。"),
        ("Is this the way to the station?", "这是去车站的路吗？"),
        ("There is a right way. I found three others first.", "有一种正确的办法。我先找到了另外三种。"),
    ),
    "need": _three(
        ("We need the signed copy today.", "我们今天需要签字件。"),
        ("I need a new kettle. This one sighs.", "我需要一把新水壶。这一把会叹气。"),
        ("I need five minutes. The inbox needs me forever.", "我需要五分钟。收件箱永远需要我。"),
    ),
    "mind": _three(
        ("I do not mind which day we meet.", "我们哪天见面都行。"),
        ("Mind the step. It is darker than it looks.", "小心这个台阶。它比看上去暗。"),
        ("I made up my mind. Then I asked my mind to vote again.", "我下定了决心。然后我让脑子再投一次票。"),
    ),
    "light": _three(
        ("The light in meeting room two has gone out.", "第二会议室的灯灭了。"),
        ("Leave a light on. I will be late.", "留一盏灯。我会晚回来。"),
        ("The traffic light was green. My courage was not.", "红绿灯是绿灯。我的勇气不是。"),
    ),
    "end": _three(
        ("We need an end date on the contract.", "合同上需要一个结束日期。"),
        ("At the end of the day I want soup.", "一天结束时，我想喝汤。"),
        ("The meeting had no clear end. The biscuits did.", "会议没有清楚的结尾。饼干有。"),
    ),
    "break": _three(
        ("Let's take a ten-minute break.", "我们休息十分钟吧。"),
        ("I broke the cup and saved the coffee.", "我打碎了杯子，咖啡还在。"),
        ("The break was short. The story told during it was not.", "休息很短。休息时讲的故事不短。"),
    ),
    "care": _three(
        ("Please take care with the client's name.", "客户的名字请写仔细。"),
        ("Take care on the wet road.", "路是湿的，走慢一点。"),
        ("I handled the box with care. The cat handled it with feet.", "我小心地拿这个盒子。猫用脚拿。"),
    ),
}
