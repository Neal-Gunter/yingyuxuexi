# -*- coding: utf-8 -*-
"""More etymologies for headwords that were still marked open.

A word is included only when its history can be stated. Looking Latin,
French, or Greek is not enough. Uncertain words stay out of these lists.
"""

GERMANIC_WORDS = """
above
across
against
ago
alike
almost
alone
along
aloud
already
although
altogether
always
among
awake
aware
away
back
bag
because
become
behind
believe
bell
belong
below
beneath
bend
birth
black
blind
blue
boat
body
bold
born
borrow
both
bottom
brain
break
bright
broad
bulk
busy
care
choose
clean
climb
cloth
clothes
clothing
club
coal
cold
cool
crop
crowd
crowded
cut
dark
deal
dear
deep
depth
die
dig
dip
door
draw
drawer
dream
drink
drive
drop
dry
each
early
east
eastern
eat
edge
either
else
empty
enough
even
ever
eye
far
fare
fast
fasten
fear
fetch
field
fight
film
fire
first
flat
fleet
flood
floor
fly
fold
follow
following
food
forbid
forget
forgive
former
free
freeze
fresh
friend
frighten
full
game
gap
gate
glad
glass
glasses
gold
green
greet
grey
ground
growth
guilty
hair
half
hall
hang
happen
happy
harbour
hard
hardly
hate
head
health
hear
heart
heat
heating
heavy
height
hers
herself
hidden
hide
highway
hill
himself
hire
hit
hole
hope
hot
hundred
ice
ill
illness
indeed
inside
instead
key
kind
lack
ladder
lady
last
later
laugh
lay
lead
leader
leadership
leading
learn
least
leave
left
lend
length
less
lie
life
lift
light
like
likely
link
listen
live
living
load
lock
locker
lonely
lose
lot
love
low
lower
luck
mad
mark
meal
middle
midnight
mind
miss
name
narrow
near
neighbour
neighbourhood
neither
never
news
next
night
none
nor
north
nose
nothing
often
once
one
open
ours
ourselves
path
pence
play
pretty
pull
quick
rather
reach
read
ready
red
rich
ride
right
ring
road
roof
room
rough
row
run
sad
sea
seat
shake
shape
sharp
sheet
shelf
shine
short
shower
shut
shy
sick
side
sight
silver
since
sing
sit
skill
skilled
sky
sleep
slight
slow
small
smell
smile
smoke
smooth
soft
soon
sorry
south
speak
speaker
speech
speed
spell
spill
spread
spring
stairs
stand
star
steal
steam
steel
steep
step
stick
still
stock
stone
storm
straight
strength
strengthen
strike
string
strong
such
summer
sun
sweep
swim
swing
talk
tap
tape
teach
tear
thank
thanks
theirs
themselves
thick
thief
thin
thing
thirst
though
thought
thousand
through
throw
thumb
tide
tie
tight
till
time
today
together
tomorrow
tonight
tool
tooth
top
toward
town
tree
trend
true
trust
truth
twice
twin
under
understand
unless
until
upon
upward
wake
walk
want
ward
warm
warn
wash
watch
water
wave
way
weak
weakness
wealth
wear
weather
web
week
weigh
weight
welcome
welfare
west
wet
wheel
when
whenever
where
whereas
whether
which
while
white
whole
whose
wide
width
willing
win
wind
window
wing
winter
wire
wise
wish
within
without
witness
woman
wonder
wood
wooden
wool
word
world
worry
wrap
wrong
yard
yesterday
yet
yours
yourself
youth
""".split()

# Compounds and phrases made of Germanic words. Not the Old English sentence,
# because the phrase itself is later English.
PHRASES = """
anybody
anyhow
anyone
anything
anyway
anywhere
at all
at the same time
backwards
background
bookkeeping
bookshop
break down
break in
break up
bring forward
buyer
by all means
by day
by hand
by land
by mistake
by name
by oneself
by sea
by sight
call for
call in
come down
cut back
cut up
daily
deadlock
door-to-door
downstairs
dry cleaning
everything
everywhere
feedback
fill in
fill up
find out
foreman
fortnight
free gift
free trade
full time
full-time
get along with
get back
get down
get in
get off
get on
get on with
get rid of
get up
give in
give out
give up
go down
go for
go off
go on
go out
go with
goodbye
hand in
hand out
handbag
handbook
handwriting
hang up
hardware
highway
holiday
how much
in half
in sight
in stock
in the end
in time
in town
indoor
indoors
instead of
keep on
keep up
key in
knock down
landlady
landlord
leave out
let’s
look after
look ahead
look forward to
look like
look out
look up
make up
maybe
midnight
next to
no one
nobody
north east
north west
not at all
nothing
nowhere
nowadays
on fire
on foot
on holiday
on sale
on time
one-way
oneself
onto
out of
out of doors
out of stock
out of work
outdoor
outdoors
overnight
overseas
overtake
own brand
put away
put back
put down
put off
put on
put out
put through
put up
ring back
ring up
run out of
set off
set out
set up
so that
so-so
somebody
someone
something
sometimes
somewhere
south east
south west
take away
take off
take out
take over
take up
thank you
throw away
wake (up)
wear out
weekday
weekend
whiteboard
workforce
workman
workplace
workshop
worldwide /world-wide
wrap up
write down
write out
""".split("\n")


def _phrase(text: str) -> str:
    shown = text.strip()
    return (
        f"{shown} 是英语里用日耳曼本族词组成的说法，不是从拉丁语或希腊语整词借来的。"
    )


# source -> {headword: what this word is in the family}
FAMILIES = {
    "拉丁语 agere「去做、推动」": {
        "act": "做出来的那一下",
        "action": "做出来的行为",
        "active": "正在做的",
        "activity": "正在做的那些事",
        "actor": "做这件事的人",
        "actual": "已经做实的，不是停在计划上",
        "agent": "替别人去做的人",
        "agency": "替别人去做的那一方",
        "react": "对着再做一次",
        "reaction": "对着做出的反应",
    },
    "拉丁语 habere「持有」，habilis 是「拿得住」": {
        "able": "拿得住、干得了",
        "ability": "拿得住这件事的程度",
    },
    "拉丁语 esse「是」，ab- 表示离开": {
        "absent": "不在场",
        "absence": "不在的那段空",
    },
    "拉丁语 cadere「落下」": {
        "accident": "落到头上的事",
        "casual": "随落随遇的，不是排定的",
        "chance": "落下来的机会。cadentia 是下落",
        "occasion": "落到眼前的一回",
    },
    "拉丁语 caput「头」": {
        "achieve": "做到头。古法语 achever 是 a chief，把事情做到头",
        "chef": "为首的人。法语 chef 就是头",
    },
    "拉丁语 computare「放到一起算」": {
        "count": "数、计算",
        "account": "把该算的算到一处",
        "accounts": "一本本算清的账",
        "accountant": "算账的人",
        "accounting": "算账这件事",
        "accountancy": "算账这一行",
    },
    "拉丁语 currere「跑」": {
        "current": "正在跑着的、现行的",
        "corridor": "跑过去的那条通道。意大利语 corridore",
        "courier": "跑腿送信的人",
        "course": "跑出来的一条路线、课程",
        "occur": "跑到眼前",
    },
    "拉丁语 facere「做」": {
        "fact": "已经做出的事",
        "factor": "参与做成结果的一项",
        "fashion": "做出来的样子。拉丁语 factio",
        "difficult": "不容易做。dis- 加上 facilis",
        "effect": "做出来的结果。ex- 加上 facere",
        "perfect": "做透了。per- 是从头到尾",
        "affect": "做到某物身上",
    },
    "拉丁语 stare「站立」": {
        "stay": "留下来站着。经古法语 ester",
        "distance": "彼此站开的那段",
        "distant": "站得远的",
        "instance": "站到眼前的一例",
        "station": "站定的地方",
        "state": "站成的样子、国家或状况",
        "stage": "站着表演或办事的一层。古法语 estage",
        "contrast": "对着站，好比较",
        "circumstance": "站在四周的那些情况",
    },
    "拉丁语 spectare「看」，specere 是同一族": {
        "expect": "向前看、等着",
        "expectation": "向前看着的那份等待",
        "inspect": "向里面看",
        "inspection": "向里面看一遍",
        "respect": "回头再看，因而敬重",
        "special": "单独拿出来看的一种",
        "specialist": "专看这一门的人",
        "specific": "指到这一种上",
    },
    "拉丁语 tendere「伸、拉紧」": {
        "attend": "把注意力伸向",
        "attendance": "人伸到了现场",
        "attention": "伸过去的注意",
        "intend": "心意伸向某一边",
        "attempt": "伸手去试",
        "extend": "向外伸",
        "extension": "伸出去的那一截",
        "tend": "照管。它是 attend 缩短后的说法",
    },
    "拉丁语 tenere「握住」": {
        "contain": "把东西握在里面",
        "content": "握在里面的东西，或已经知足",
        "continent": "连在一起的一大块陆地",
        "continue": "握住不放，接着下去",
        "entertain": "在彼此之间握住，用来待客",
    },
    "拉丁语 ferre「携带」": {
        "differ": "分头带走，于是不同",
        "difference": "分头带走之后的差别",
        "different": "被分头带走的",
        "prefer": "把一件带到更前面",
        "preference": "被带到前面的选择",
        "refer": "把事情带回去给别人看",
        "reference": "被带回去对照的材料",
        "offer": "向着某人带过去",
        "suffer": "在下面扛着",
        "transfer": "带到另一处",
    },
    "拉丁语 scribere「写」": {
        "describe": "把样子写下来",
        "description": "写下来的样子",
    },
    "拉丁语 mittere「送、放出」": {
        "admit": "送到里面，准许进入",
        "admission": "被准许进入",
        "permit": "放出许可",
        "permission": "放出来的许可",
        "commit": "交到一起，托付",
        "committee": "被托付这件事的一组人",
        "omit": "放过去，没有送上",
        "submit": "送到下面，呈上",
    },
    "拉丁语 plicare「折叠」": {
        "apply": "把一件折到另一件上，因而应用",
        "application": "递上去的申请，或应用",
        "applicant": "把申请递上来的人",
        "display": "把折着的打开给人看",
        "reply": "折回来。古法语 replier",
        "imply": "折在里面，没有直说",
    },
    "拉丁语 ponere「放下、安置」": {
        "position": "被放下的位置",
        "positive": "已经放下、可以肯定的",
        "oppose": "放在对面",
        "component": "放到一起的零件",
        "propose": "放到众人前面",
        "purpose": "预先放下的目标",
        "postpone": "放到后面",
    },
    "拉丁语 ducere「带领」": {
        "produce": "引到前面来",
        "product": "被引出来的产物",
        "production": "把产物引出来",
        "educate": "把人带出来、带大",
        "reduce": "往回带、减少",
        "introduce": "领到里面",
    },
    "拉丁语 capere「拿」": {
        "catch": "去抓住。北方法语 cachier，拉丁语 captare",
        "receive": "接住递来的东西",
        "accept": "接到手里",
        "except": "拿到外面，排除",
        "participate": "拿住其中一份",
        "occupy": "把地方拿下",
        "occupation": "拿下的营生或占领",
        "capable": "拿得住的",
    },
    "拉丁语 claudere「关闭」": {
        "close": "关上",
        "include": "关在里面",
        "exclude": "关在外面",
        "conclude": "一起关上，作结",
        "conclusion": "关上之后的结论",
    },
    "拉丁语 finis「边界、尽头」": {
        "fine": "到了尽头的、精细的。罚金也是把事情结清的那一笔",
        "final": "最后的",
        "finish": "做到尽头",
        "finance": "把账结清。古法语 finer",
        "definite": "把边界定死",
        "define": "画出边界",
    },
    "拉丁语 gradus「一步」": {
        "grade": "一个等级、一步",
        "graduate": "走完一级",
        "graduation": "走完这一级",
        "progress": "向前迈步",
        "degree": "迈下去的度数",
    },
    "拉丁语 genus「种类、出生」，gener-": {
        "general": "属于这一整类的",
        "generous": "出身宽厚的，后来指大方",
        "gender": "种类，后来特别指性别",
    },
    "希腊语 graphein「写、画」": {
        "biography": "写一生。bios 是生命",
        "geography": "写大地。ge 是地",
        "paragraph": "写在旁边的一段",
        "programme": "写给众人看的预告。希腊语 programma",
        "program": "和 programme 是同一个希腊词",
        "graph": "画出来的图",
        "diagram": "画穿过去的图。dia- 是穿过",
    },
    "希腊语 logos「话、道理」": {
        "apology": "把道理说开。apo- 是从旁边说清楚",
        "logic": "讲道理的那一门",
        "logo": "一个用来认人的词或标志",
        "catalogue": "按条说完的单子",
        "dialogue": "两个人对着说",
    },
    "希腊语 phone「声音」和 tele「远」": {
        "telephone": "远处的声音",
        "telegram": "远处写来的。gramma 是写下的字",
        "television": "远处的看见。vision 来自拉丁语 videre",
        "phone": "telephone 的缩短，仍是远处的声音",
    },
    "拉丁语 portare「携带」": {
        "export": "带到外面",
        "import": "带到里面",
        "transport": "带过一段路",
        "transportation": "把人或货带过去",
        "report": "把消息带回来",
        "support": "从下面托着带",
        "portable": "可以带走的",
    },
    "拉丁语 premere「压」": {
        "press": "压",
        "pressure": "压上来的力",
        "impress": "压进心里或纸上",
        "impression": "压出来的印记",
        "express": "压出来、说出来",
        "print": "压印出来",
    },
    "拉丁语 forma「形状」": {
        "form": "形状、表格",
        "formal": "按形状来的，正式的",
        "inform": "把形状给进去，于是通知",
        "informal": "不按正式形状的",
        "perform": "把事情做成该有的形状",
        "performance": "做出来的那场",
        "uniform": "一种形状。unus 是一",
        "reform": "重新做成一个形状",
        "format": "排成的格式",
    },
    "拉丁语 pars「一份」": {
        "part": "分出来的一份",
        "party": "站在同一份上的人",
        "particular": "这一份上的，具体的",
        "apart": "分成一份一份",
        "apartment": "分出来的一套住所",
        "depart": "从这份里离开",
        "departure": "离开",
        "department": "分出去的一块职责",
        "participate": "拿住其中一份",
        "partial": "只是其中一份",
        "portion": "分到的一截",
    },
    "拉丁语 signum「记号」": {
        "sign": "记号",
        "signal": "打出的信号",
        "significant": "这个记号有分量",
        "signature": "自己留下的记号",
        "design": "把记号画出来",
        "assign": "把记号派到某人头上",
        "resign": "把记号交回去，辞职",
    },
    "拉丁语 servire「侍奉」，servus 是仆人": {
        "serve": "侍奉、供职",
        "service": "侍奉做成的服务",
        "servant": "侍奉的人",
        "reserve": "留着伺候以后",
        "conserve": "守着，不让它散掉",
        "observe": "守着看",
        "preserve": "预先守住",
    },
    "拉丁语 videre「看见」": {
        "visit": "去看一看",
        "video": "看见的画面",
        "view": "看见的景象。经古法语",
        "review": "再看一遍",
        "visible": "可以看见的",
        "vision": "看见的东西",
        "evidence": "清楚看见、可以拿出的证据",
        "provide": "预先看见，因而供给",
        "advice": "看上去该怎么做。拉丁语 ad visum，经古法语 avis",
        "supervise": "从上面看着",
        "survey": "在上面看一遍",
        "interview": "彼此看见、当面谈",
    },
    "拉丁语 venire「来」": {
        "event": "来到的一件事",
        "prevent": "提前来到，于是挡住",
        "convention": "来到一起",
        "convenient": "来到一起、合用的",
        "convenience": "合用",
        "venture": "将要来的一场风险。adventure 的缩短",
        "invent": "走来碰上，于是发明",
    },
    "拉丁语 vertere「转」": {
        "convert": "转成另一样",
        "conversation": "转来转去地谈",
        "advertise": "把人的注意力转过来",
        "version": "转写出来的一个本子",
        "diverse": "转向不同方向",
    },
    "拉丁语 vox「声音」，voc-": {
        "voice": "声音",
        "vocabulary": "一个人拿得出来的那些词",
        "advocate": "把声音加到某一边",
        "vocation": "被声音叫去的行当",
    },
    "拉丁语 trahere「拉」，tract-": {
        "attract": "拉过来",
        "attraction": "拉过来的力量",
        "attractive": "拉得住人的",
        "contract": "拉到一起的契约",
        "treat": "拉着处理。拉丁语 tractare",
        "abstract": "从里面拉出来",
    },
    "拉丁语 struere「搭建、堆放」": {
        "structure": "搭出来的结构",
        "construct": "搭起来",
        "construction": "搭起来的工程",
        "instruct": "把该有的装备搭进人里，于是指导",
        "instruction": "指导",
        "instructor": "指导的人",
        "destroy": "把搭好的拆掉",
    },
    "拉丁语 credere「相信」": {
        "grant": "相信并给予。经古法语 graanter",
        "credit": "把信任给出",
        "incredible": "无法相信的",
        "credential": "让人相信的凭据",
    },
    "拉丁语 medius「中间」": {
        "medium": "中间的手段或媒介",
        "media": "媒介，medium 的复数",
        "immediate": "中间没有隔着东西",
        "intermediate": "停在中间的",
        "medicine": "医治。拉丁语 mederi「治疗」，和中间这条是近亲",
        "medical": "医学的",
    },
    "拉丁语 locus「地方」": {
        "local": "地方上的",
        "locate": "放到一个地方",
        "location": "所在的地方",
    },
    "拉丁语 manus「手」": {
        "manage": "用手驾驭。意大利语 maneggiare 原是驯马",
        "manager": "用手管事的人",
        "managerial": "属于管事的",
        "manner": "手上的做法",
        "manual": "用手的",
        "manufacture": "用手做成。factura 是制作",
        "maintain": "把东西保持在手里。manu tenere",
        "manuscript": "手写的。scribere 是写",
    },
    "拉丁语 magnus「大」，major 是更大": {
        "major": "更大的",
        "majority": "更大的那一部分",
        "main": "主要的。经古法语，不是日耳曼词",
        "maximum": "最大",
        "max": "maximum 的缩短",
    },
    "拉丁语 parvus「小」，minor 是更小，minimus 是最小": {
        "minor": "较小的",
        "minimum": "最小",
        "minus": "减去，更少",
        "minute": "分到很小的一份",
    },
    "拉丁语 nasci「出生」，natur-": {
        "nature": "与生俱来的样子",
        "natural": "天然的",
        "nation": "同一出生的人群",
        "national": "属于这个国家的",
        "nationality": "国籍",
        "native": "本地出生的",
    },
    "拉丁语 nota「记号」": {
        "note": "记下的记号",
        "notice": "使记号被人看见",
        "notify": "把记号告诉人",
        "notion": "心里的一个记号、念头",
    },
    "拉丁语 nuntius「信使」": {
        "announce": "把消息送出去",
        "pronounce": "向前说出",
        "pronunciation": "说出来的读法",
    },
    "拉丁语 ordo「行列、秩序」": {
        "order": "行列、命令",
        "ordinary": "排在常列里的",
        "coordinate": "排到同一序上",
        "extraordinary": "排到常列之外",
    },
    "希腊语 organon「工具」": {
        "organise": "把人当成一套工具排好",
        "organisation": "排好的组织",
        "organic": "像一个器官那样连着的",
    },
    "拉丁语 parare「准备、安排」": {
        "prepare": "预先安排",
        "preparation": "预先的安排",
        "separate": "安排到各自一边",
        "repair": "重新安排好",
        "compare": "放到一起安排、比较",
        "comparison": "比较",
        "apparatus": "准备好的一套器具",
    },
    "拉丁语 pendere「称、悬挂」，pens-": {
        "expense": "称出去的花费",
        "expenses": "称出去的那些花费",
        "expensive": "称出去很多的",
        "expenditure": "称出去的支出",
        "depend": "挂在下面，靠着",
        "independent": "不挂在别人下面",
        "spend": "称出钱去。古英语 spendan 借的就是 expendere",
    },
    "拉丁语 petere「追求、寻求」": {
        "repeat": "再寻求一次",
        "compete": "一起争着寻求",
        "competitive": "在争的",
        "petition": "正式求一件事",
        "appetite": "伸向食物的欲求",
    },
    "拉丁语 populus「人民」": {
        "people": "人、人民",
        "popular": "在人民中间受欢迎的",
        "population": "人民的数目",
        "public": "属于人民的",
        "publish": "放到人民面前",
        "publication": "放到众人面前的作品",
        "publicity": "让众人看见",
    },
    "拉丁语 primus「第一」": {
        "prime": "第一的",
        "primary": "最初的",
        "principal": "站在第一位的",
        "priority": "更前面的顺序",
        "prior": "更前面的",
    },
    "拉丁语 privus「单独的」": {
        "private": "单独放下、不公开的",
        "privilege": "单独的一条法。lex 是法",
    },
    "拉丁语 probare「检验、证明好」": {
        "prove": "证明",
        "proof": "证明",
        "probable": "经得起检验的，因而很可能",
        "approve": "检验后认为好",
        "approval": "检验后的同意",
        "probe": "拿东西去探、去试",
    },
    "拉丁语 proprius「自己的」": {
        "proper": "属于自己该有的、恰当的",
        "property": "属于自己的产业",
        "appropriate": "把某物当成自己的、合适的",
    },
    "拉丁语 punctum「点」，pungere 是刺": {
        "point": "一个点",
        "punctual": "卡在点上的",
        "punctuation": "点出来的标点",
        "punch": "打出一个点或一个孔",
    },
    "拉丁语 quaerere「询问、寻找」": {
        "question": "问出来的问题",
        "questionnaire": "一串问题",
        "query": "问一句",
        "require": "再寻找，于是要求",
        "request": "再求一次",
        "inquiry": "向里面问",
        "enquire": "向里面问",
        "acquire": "寻到手里",
    },
    "拉丁语 regere「引导、扶正」，regula 是尺": {
        "rule": "尺、规则",
        "regular": "按尺来的",
        "correct": "扶正",
        "correction": "扶正",
        "region": "被划出来引导的一片",
        "regulate": "用尺去调",
        "regime": "一套管法",
    },
    "拉丁语 salvare「保全」，salvus 是安全的": {
        "safe": "安全的。经古法语 sauf",
        "safety": "安全",
        "save": "保全下来",
        "salary": "买盐的钱。sal 是盐，后来指工资",
    },
    "拉丁语 scire「知道」": {
        "science": "成系统的知识",
        "scientific": "科学的",
        "conscious": "和别人一起知道",
        "conscience": "自己心里知道",
    },
    "拉丁语 sequi「跟随」": {
        "second": "跟着来的第二个",
        "secondary": "第二位的",
        "sequence": "一个跟着一个",
        "consequence": "跟着来的结果",
        "subsequent": "随后跟着的",
        "suit": "跟着的一套，衣服或诉讼",
        "suitable": "跟得上、合适的",
        "pursue": "在后面跟着追",
    },
    "拉丁语 sedere「坐」": {
        "president": "坐在前面的人",
        "resident": "坐下来住的人",
        "reside": "坐着住下",
        "assess": "坐到旁边去估价",
        "session": "坐在一起的一段时间",
        "size": "坐下来评定的尺寸。古法语 sise",
    },
    "拉丁语 sentire「感觉、认为」": {
        "sense": "感觉",
        "sentence": "把判断说完整的一句",
        "consent": "感觉到一起，同意",
        "sensitive": "容易感觉到的",
    },
    "拉丁语 similis「相像」": {
        "similar": "相像的",
        "similarity": "相像",
    },
    "拉丁语 sistere「站住」": {
        "assist": "站在旁边",
        "assistant": "站在旁边的人",
        "exist": "站出来，于是存在",
        "insist": "站在上面不走开",
        "consist": "站到一起，由什么组成",
        "resist": "反着站住",
    },
    "拉丁语 solvere「松开」": {
        "solve": "把结松开",
        "solution": "松开之后的解法",
        "absolute": "完全松开、不受绑的",
        "resolve": "再松开一次，下决心",
    },
    "希腊语 skhema「形状」，拉丁语 schema": {
        "scheme": "一个形状、方案",
    },
    "拉丁语 stringere「拉紧」": {
        "strict": "拉紧的",
        "district": "被拉紧划出的一片",
        "restrict": "往回拉紧",
        "stress": "拉紧的压力",
        "strain": "拉紧",
    },
    "拉丁语 tempus「时间」": {
        "temporary": "只占一段时间的",
        "contemporary": "时间叠在一起的",
        "tempo": "时间的拍子",
    },
    "拉丁语 uti「使用」，usus 是使用": {
        "use": "使用",
        "usual": "通常会用的",
        "useful": "用得上的",
        "user": "使用的人",
        "utility": "用处",
    },
    "拉丁语 valere「有力量、值钱」": {
        "valid": "还站得住、有效",
        "valuable": "值得的",
        "value": "值多少",
        "available": "此刻够得上、用得上",
        "equivalent": "力量相等",
    },
    "拉丁语 varius「变化的、有斑的」": {
        "vary": "变化",
        "various": "各种各样的",
        "variety": "多样",
        "variable": "会变的",
    },
    "拉丁语 unus「一」": {
        "unit": "一个单位",
        "union": "合成一个",
        "unite": "合成一个",
        "unique": "只有一个",
        "uniform": "一种形状",
        "universe": "转成一个整体。vertere 是转",
        "university": "一个整体的行会，后来是大学",
    },
}


# (headword, source, note) for words that need their own sentence.
ONE_OFFS = [
    ("accommodation", "拉丁语 accommodare「使合适」", "modus 是尺度。住宿是把住处调到合适。"),
    ("according to", "古法语 acorder", "和拉丁语 cor「心」有关：把说法调到一条心上。according to 就是照着这个来。"),
    ("accuracy", "拉丁语 accuratus「加以留心的」", "cura 是操心。准确是把事情照料到点上。"),
    ("accurate", "拉丁语 accuratus", "cura 是操心。准确的，就是被仔细照料过的。"),
    ("adapt", "拉丁语 adaptare", "ad- 朝向，aptus 是合适。改编、适应，都是把它配上去。"),
    ("add", "拉丁语 addere", "ad- 朝向，dare 是给。加法就是再给上去。"),
    ("addition", "拉丁语 addere「加到上面」", "加上去的那一笔。"),
    ("additional", "拉丁语 addere", "再加在上面的。"),
    ("address", "古法语 adrecier", "通俗拉丁语里是把方向摆正，directus 是直的。地址是把话送到的方向。"),
    ("adjust", "古法语 ajuster", "拉丁语 ad 加上 iuxta「靠近」。调整就是把它挪到挨着合适的位置。"),
    ("administration", "拉丁语 administrare", "minister 是服务、掌管。行政是替一件事管到实处。"),
    ("administrative", "拉丁语 administrare", "属于管事的。"),
    ("administrator", "拉丁语 administrare", "管事的人。"),
    ("admire", "拉丁语 admirari", "mirari 是惊奇。钦佩是看着而惊奇。"),
    ("adult", "拉丁语 adultus", "adolescere 是长大，alere 是喂养。成年人是已经长成的人。"),
    ("advance", "古法语 avancer", "拉丁语 abante「从前面」。前进就是再往前。"),
    ("advanced", "古法语 avancer", "已经往前走了一截的。"),
    ("advantage", "古法语 avantage", "avant 是前面。优势是占在前面的那一点。"),
    ("aeroplane", "法语 aéroplane", "希腊语 aer 是空气，plane 来自拉丁语 planus「平的」。飞机是空气里的一个平面。"),
    ("affair", "法语 à faire", "faire 来自拉丁语 facere「做」。要做的那件事，就是事务。"),
    ("afraid", "盎格鲁法语 afrayer", "更早是通俗拉丁语 *exfridare，日耳曼语 frithu 是平安。害怕是被赶出平安。"),
    ("age", "古法语 aage", "拉丁语 aetas，aevum 是年代。年龄和时代是同一条。"),
    ("aged", "古法语 aage，拉丁语 aetas", "有了年岁的。"),
    ("agricultural", "拉丁语 agricultura", "ager 是田，cultura 是耕种。"),
    ("agriculture", "拉丁语 agricultura", "ager 是田，colere 是耕种。农业就是种田。"),
    ("air", "希腊语 aer", "经拉丁语 aer、古法语 air。空气。"),
    ("airline", "希腊语 aer「空气」加上 line", "line 来自拉丁语 linea「线」。航线是空气里的一条线。"),
    ("airmail", "空气的邮袋", "air 来自希腊语 aer。mail 来自古法语 male「袋子」。航空邮件是经空气送出的那一袋。"),
    ("airplane", "希腊语 aer 加上拉丁语 planus「平的」", "和 aeroplane 是同一个说法的另一拼法。"),
    ("alarm", "意大利语 all'arme", "意思是「到武器那里去」。警报原来是一声拿起武器。"),
    ("allow", "古法语 allouer", "拉丁语里常连到 allocare「拨一个位置」或 allaudare「称赞」。商务里的 allowance 是拨出来的一份。"),
    ("allowance", "古法语 allouer", "拨出来的那一份额度或津贴。"),
    ("ambassador", "法语 ambassadeur", "拉丁语 ambactus「侍从」本身借自日耳曼语：被派去办事的人。"),
    ("ambition", "拉丁语 ambitio", "ambire 是四处走、拉票。雄心原来是到处去争取。"),
    ("amount", "古法语 amont", "拉丁语 ad montem「向着山上去」。总额是累计到的那个高度。"),
    ("announce", "拉丁语 annuntiare", "nuntius 是信使。宣布就是把消息送出去。"),
    ("annoy", "古法语 enoier", "拉丁语 in odio「处于厌烦之中」。"),
    ("anxious", "拉丁语 anxius", "angere 是勒紧、使窒息。焦虑是心里被勒住。"),
    ("apologise", "希腊语 apologia", "apo- 加上 logos「话」。把道理说开，就是道歉或辩解。"),
    ("apology", "希腊语 apologia", "把道理从旁边说清楚。"),
    ("appear", "拉丁语 apparere", "ad- 朝向，parere 是显现。出现就是被看见。"),
    ("appearance", "拉丁语 apparere", "显现出来的样子。"),
    ("appropriate", "拉丁语 appropriare", "proprius 是自己的。合适，或把它拿来自用。"),
    ("approximate", "拉丁语 approximare", "proximus 是最近的。大约就是走近，但还没到点上。"),
    ("architect", "希腊语 arkhitekton", "arkhi- 是为首，tekton 是建造的人。建筑师是建造者里头为首的。"),
    ("area", "拉丁语 area", "原是打谷的空场。后来才是一片区域。"),
    ("argue", "拉丁语 arguere", "把事情说清楚、加以证明。争论是从这里来的。"),
    ("arithmetic", "希腊语 arithmetike", "arithmos 是数。算术是数的技术。"),
    ("art", "拉丁语 ars", "技艺。它和 arm「武器」没有关系。"),
    ("article", "拉丁语 articulus", "artus 是关节。文章或物品都是从整体上分出的一节。"),
    ("assembly", "古法语 assembler", "拉丁语 ad 加上 simul「一起」。装配和集会都是聚到一起。"),
    ("associate", "拉丁语 associare", "socius 是同伴。结成一伙。"),
    ("association", "拉丁语 associare", "同伴结成的团体。"),
    ("assure", "拉丁语 ad 加上 securus「没有忧虑」", "向人保证，就是让他不必再操心。"),
    ("attach", "古法语 atachier", "和钉在桩上有关，桩是日耳曼词。attach 是钉上。attack 是后来从同一族来的。"),
    ("attack", "意大利语 attaccare，法语 attaquer", "和 attach 同族，原是钉上去、扑上去。"),
    ("attitude", "法语 attitude，意大利语 attitudine", "拉丁语 aptitudo。姿态后来变成态度。"),
    ("author", "拉丁语 auctor", "augere 是使增长。作者是把作品促成的人。"),
    ("authorise", "拉丁语 auctoritas", "由有权促成的人点头。"),
    ("authority", "拉丁语 auctoritas", "使人增长、说了算的那种权力。"),
    ("automatic", "希腊语 automatos", "autos 是自己，-matos 是愿意、动作。自动就是自己会动。"),
    ("availability", "拉丁语 valere「有力量、值钱」", "avail 加上 -able。一件东西此刻够得上。"),
    ("average", "阿拉伯语 'awar「货物的损坏」", "经意大利语 avaria、法语 avarie。海损被大家分摊，后来才是平均数。"),
    ("avoid", "古法语 evuider「倒空」", "和拉丁语 vacuus「空的」一路。避开就是把路空出来。"),
    ("award", "盎格鲁诺曼语 awarder", "来自日耳曼语 ward「看守、裁断」。奖是裁断之后给的。"),
    ("bicycle", "拉丁语 bi-「二」加上希腊语 kyklos「圆、轮」", "两只轮子。"),
    ("billion", "法语 billion", "bi- 加上 million。million 来自意大利语，拉丁语 mille「千」。"),
    ("blame", "古法语 blasmer", "拉丁语 blasphemare，希腊语 blasphemein。责备和亵渎在词源上是说重话。"),
    ("blank", "法语 blanc", "日耳曼语里「发白、发亮」的那个词。空白是还没写上的白。"),
    ("block", "法语 bloc", "中古荷兰语 bloc，日耳曼词。一块整料。"),
    ("box", "晚期拉丁语 buxis", "希腊语 pyxis，黄杨木盒子。"),
    ("branch", "古法语 branche", "晚期拉丁语 branca「爪子」。树枝像伸出去的爪，分行也是从主干伸出。"),
    ("brick", "法语 brique", "中古荷兰语 bricke，日耳曼词。"),
    ("brilliant", "法语 brillant", "briller 是发光。更早常连到拉丁语 beryllus「绿宝石」，这一步不是定论，发光本身来自法语。"),
    ("brochure", "法语 brocher「缝、装订」", "小册子原来是缝起来的几页。"),
    ("buffet", "法语 buffet", "餐柜，也指自取的一席。"),
    ("bullet", "法语 boulette「小球」", "拉丁语 bulla 是泡、圆印。子弹是一颗小圆。"),
    ("bureau", "法语 bureau", "原是铺在桌上的粗呢，后来是这张桌子，再后来是局、处。"),
    ("burglar", "中世纪拉丁语 burglator", "和 burg「住家、城」有关。入户的贼。"),
    ("burglary", "中世纪拉丁语 burglator", "入室盗窃。"),
    ("bus", "拉丁语 omnibus", "omnis 的与格复数，「给所有人的」。公共汽车是给大家的车，后来只剩 bus。"),
    ("button", "古法语 bouton", "芽、纽扣。扣上的那个小圆。"),
    ("cab", "法语 cabriolet 的缩短", "原是一种轻马车。"),
    ("cabinet", "法语 cabinet", "cabin 的小词，一间小室，后来是柜和内阁。"),
    ("cable", "古法语 cable", "晚期拉丁语 capulum「绳套」。缆绳。"),
    ("café/cafe", "法语 café", "咖啡，更早是阿拉伯语 qahwah，经土耳其语。咖啡馆用的是法语。"),
    ("calendar", "拉丁语 calendarium", "calendae 是每月的第一天。日历从这一天记起。"),
    ("calm", "意大利语 calma，希腊语 kauma「炎热」", "正午热得没有风，就是平静。"),
    ("camera", "拉丁语 camera「拱形房间」", "希腊语 kamara。相机是一个小暗室。"),
    ("campaign", "法语 campagne", "拉丁语 campus「田野」。战役和宣传活动都是拉到场地上的一仗。"),
    ("canal", "拉丁语 canalis「管道」", "和 reed 的 canna 有关。运河是一条人工的槽。"),
    ("canteen", "法语 cantine，意大利语 cantina「地窖」", "食堂是放酒食的地方。"),
    ("car", "拉丁语 carrus「车」", "更早是凯尔特语。career、cargo、charge 走的是同一辆车。"),
    ("card", "法语 carte", "拉丁语 charta，希腊语 khartes「纸草叶」。卡片是一小片纸。"),
    ("cardboard", "card 加上 board", "card 来自希腊语、拉丁语的纸草，board 是日耳曼词「木板」。硬纸板是贴成板的纸。"),
    ("carpet", "中世纪拉丁语 carpita", "拉丁语 carpere「摘、梳」。地毯原是梳过的厚毛织物。"),
    ("carry", "北方法语 carier", "拉丁语 carrus「车」。搬运是用车运。"),
    ("cash", "法语 caisse「箱子」", "拉丁语 capsa。现金原来是箱子里的钱。"),
    ("category", "希腊语 kategoria", "kata 加上 agora「在公共场合说」。范畴是说得清的一类。"),
    ("catering", "盎格鲁诺曼语 acater「购买」", "拉丁语 ad 加上 captare「去拿」。承办伙食是把吃的买来备上。"),
    ("cause", "拉丁语 causa", "原因、事由。它和 because 不是同一个词。because 是日耳曼的 by cause，cause 这一截才是拉丁语。"),
    ("ceiling", "古法语 cel", "一般认为来自拉丁语 caelum「天、华盖」。天花板是屋里的那一层天。"),
    ("celebrate", "拉丁语 celebrare", "常常来往、隆重举行。庆祝是把日子过得郑重。"),
    ("celebration", "拉丁语 celebrare", "隆重举行的那场。"),
    ("cellar", "拉丁语 cellarium", "cella 是小室。地窖是储物的小室。"),
    ("Celsius", "瑞典天文学家 Celsius 的姓", "温标以他命名。它不是一个拉丁普通名词。"),
    ("cent", "拉丁语 centum「一百」", "百分之一的货币单位。"),
    ("centigrade", "拉丁语 centum「百」加上 gradus「步、度」", "一百分度。"),
    ("centimetre", "法语", "拉丁语 centum「百」加上希腊语 metron「量」。一米的一百分之一。"),
    ("central", "希腊语 kentron，拉丁语 centrum", "圆心、中心。"),
    ("centre", "希腊语 kentron「刺点、圆心」", "拉丁语 centrum。中心原来是画圆时钉子钉住的那一点。"),
    ("century", "拉丁语 centuria", "centum 是一百。一百年，或一百人的单位。"),
    ("certain", "拉丁语 certus", "cernere 是筛、判定。确定的，就是已经筛过的。"),
    ("chain", "拉丁语 catena", "链子。"),
    ("chairman", "chair 加上 man", "chair 来自希腊语 kathedra「座位」。man 是日耳曼词。主席是坐主位的人。"),
    ("chairperson", "chair 加上 person", "chair 来自希腊语 kathedra。person 来自拉丁语 persona「面具、角色」。"),
    ("chairwoman", "chair 加上 woman", "chair 来自希腊语 kathedra。woman 是日耳曼词。"),
    ("challenge", "古法语 chalenge", "拉丁语 calumnia「诬告、责难」。挑战是把一件事正式提出来。"),
    ("change", "古法语 changier", "拉丁语 cambiare，来自凯尔特语。更换。"),
    ("chart", "拉丁语 charta", "希腊语 khartes「纸草」。图表是画在纸上的。"),
    ("charter", "古法语 chartre", "拉丁语 chartula「小文件」。特许状是一份写成的权利。"),
    ("cheat", "escheat 的缩短", "古法语 eschete，拉丁语 ex 加上 cadere「落下」。无人继承而落回国库，后来才是欺骗。"),
    ("cheerful", "cheer 加上 -ful", "cheer 来自古法语 chere「脸」，拉丁语 cara。气色好，就是高兴。"),
    ("chemical", "希腊语 khemeia", "经阿拉伯语、拉丁语的炼金术用语，后来才是化学。"),
    ("chemist", "希腊语 khemeia", "做化学或卖药的人。"),
    ("circle", "拉丁语 circulus", "circus 是圆，希腊语 kirkos。"),
    ("circular", "拉丁语 circularis", "圆的，或传阅的一封信。"),
    ("circulate", "拉丁语 circulare", "让它沿圆周转。"),
    ("city", "古法语 cite", "拉丁语 civitas「公民集体」。城市原是一群公民。"),
    ("claim", "古法语 clamer", "拉丁语 clamare「喊」。索赔和声称都是大声把权利说出来。"),
    ("clarify", "拉丁语 clarificare", "clarus 是清楚、明亮。澄清就是使它亮出来。"),
    ("class", "拉丁语 classis", "原是按财产分成的公民等级，也指舰队。班级和类别都是这一分法。"),
    ("classify", "拉丁语 classis 加上 facere「做」", "把它放进一个等级。"),
    ("classroom", "class 加上 room", "class 是拉丁语的等级，room 是日耳曼词。教室是上课的那间。"),
    ("clear", "古法语 cler", "拉丁语 clarus「明亮的」。清楚就是亮。"),
    ("clerical", "晚期拉丁语 clericus", "希腊语 kleros「签、神职的份」。文书工作和神职人员走的是同一个词。"),
    ("clerk", "晚期拉丁语 clericus", "希腊语 klerikos。能写字的人，后来是职员。"),
    ("climate", "希腊语 klima「坡度、地带」", "气候原是地球上的一个斜带。"),
    ("clock", "中古荷兰语 clocke", "中世纪拉丁语 clocca「钟、铃」。钟表从报时的铃来，不是日耳曼的 time。"),
    ("coach", "匈牙利语 kocsi", "来自匈牙利城镇 Kocs，那里造的马车。长途汽车和教练都从这辆马车来。"),
    ("coast", "古法语 coste", "拉丁语 costa「肋骨、侧面」。海岸是陆地的一侧。"),
    ("coffee", "阿拉伯语 qahwah", "经土耳其语、意大利语 caffè。"),
    ("coin", "古法语 coin「楔子、角」", "拉丁语 cuneus。硬币是打楔子压出来的。"),
    ("collection", "拉丁语 colligere", "com- 加上 legere「采集」。收集。"),
    ("colour", "古法语 colour", "拉丁语 color。"),
    ("combination", "拉丁语 combinare", "bini 是两个两个。组合是配到一起。"),
    ("combine", "拉丁语 combinare", "把两边配上。"),
    ("comfort", "晚期拉丁语 confortare", "fortis 是强。安慰原是使人强壮。"),
    ("comment", "拉丁语 commentum", "想出来的解释。评注。"),
    ("common", "拉丁语 communis", "大家共用的。"),
    ("communicate", "拉丁语 communicare", "communis 是共用。沟通就是把信息变成共用的。"),
    ("communication", "拉丁语 communicare", "把信息交到共用的地方。"),
    ("commute", "拉丁语 commutare", "整个换过。通勤是在两处之间来回换地方，刑罚的减换也是这个词。"),
    ("compact", "拉丁语 compactus", "compingere 是钉到一起。紧凑就是钉实了。"),
    ("complain", "古法语 complaindre", "拉丁语 plangere「捶胸、哀哭」。投诉是把不满说出来。"),
    ("compliment", "法语 compliment，意大利语 complimento", "拉丁语 complementum「填满」。恭维原是把礼数做满。complement「补足」是同一个拉丁词。"),
    ("composition", "拉丁语 componere", "放到一起。作文和构成都是这个。"),
    ("computer", "拉丁语 computare「计算」", "计算机就是拿来算的机器。"),
    ("computer program(me)", "拉丁语 computare 加上希腊语 programma", "程序是写出来公开展示的一套步骤，计算机负责算。"),
    ("concentrate", "法语 concentrer", "拉丁语 con- 加上 centrum「中心」。集中就是收到中心。"),
    ("concentration", "拉丁语 centrum「中心」", "收到一处。"),
    ("concern", "拉丁语 concernere", "原是一起筛。后来是与某事有关、使人担心。"),
    ("concert", "意大利语 concerto", "拉丁语 concertare「争执、协力」。音乐会是把声音调到一起。"),
    ("confidence", "拉丁语 confidere", "fidere 是信任。信心是完全信任。"),
    ("confident", "拉丁语 confidere", "信得过的。"),
    ("confidential", "拉丁语 confidere", "只交给信任的人。"),
    ("confirmation", "拉丁语 confirmare", "firmus 是牢固。确认就是把它钉牢。"),
    ("congratulations", "拉丁语 congratulari", "gratus 是可喜的。一起为喜事高兴。"),
    ("connecting", "拉丁语 conectere", "nectere 是绑。连接就是绑上。"),
    ("connection", "拉丁语 conectere「绑在一起」", "connect 的名词。"),
    ("conservative", "拉丁语 conservare", "servare 是守住。保守就是守着原样。"),
    ("consul", "拉丁语 consul", "罗马的执政官。领事沿用了这个官名。"),
    ("consulate", "拉丁语 consul", "领事的官署。"),
    ("consult", "拉丁语 consultare", "和 consul 同族，把事情拿去商量。"),
    ("consultancy", "拉丁语 consultare", "给人商量的那一行。"),
    ("consultant", "拉丁语 consultare", "被请来商量的人。"),
    ("consultation", "拉丁语 consultare", "商量的那一次。"),
    ("contest", "拉丁语 contestari", "testis 是证人。竞赛原是一起对证。"),
    ("contribute", "拉丁语 contribuere", "tribuere 是分派。捐出或贡献，是把自己的一份派进去。"),
    ("contribution", "拉丁语 contribuere", "派进去的那一份。"),
    ("co-operate", "拉丁语 cooperari", "opus 是工作。一起做。"),
    ("co-operation", "拉丁语 cooperari", "一起做的事。"),
    ("co-operative", "拉丁语 cooperari", "愿意一起做的，或合作社。"),
    ("copy", "古法语 copie", "拉丁语 copia「丰足」。抄本多起来，copia 才变成一份副本。"),
    ("corner", "古法语 corniere", "拉丁语 cornu「角」。"),
    ("corporate", "拉丁语 corporatus", "corpus 是身体。法人是被当成一个身体的组织。"),
    ("correspondence", "中世纪拉丁语 correspondere", "respondere 是应答。通信是一来一回地对上。"),
    ("cost", "古法语 coster", "拉丁语 constare「站在一起、值这么多」。成本是它站得住的那个价。"),
    ("cotton", "阿拉伯语 qutn", "经法语 coton。棉花。"),
    ("country", "古法语 contree", "拉丁语 contra「对面」。国土原是对面的那一片地。"),
    ("countryside", "country 加上 side", "country 来自拉丁语 contra。side 是日耳曼词。乡下是城外的那一侧。"),
    ("couple", "古法语 cople", "拉丁语 copula「联结」。一对就是绑在一起的两个。"),
    ("courage", "古法语 corage", "拉丁语 cor「心」。勇气是心里的那股劲。"),
    ("court", "古法语 cort", "拉丁语 cohors「围场、一队人」。法庭和宫廷都是围起来的一圈人。"),
    ("cover", "古法语 covrir", "拉丁语 cooperire「完全盖上」。"),
    ("create", "拉丁语 creare", "造出来。"),
    ("creation", "拉丁语 creare", "造出来的东西。"),
    ("creative", "拉丁语 creare", "会造的。"),
    ("crime", "拉丁语 crimen「指控、过错」", "罪。"),
    ("criminal", "拉丁语 crimen", "和罪有关的。"),
    ("criticise", "希腊语 krites「判断的人」", "krinein 是分辨。批评就是作出判断。"),
    ("culture", "拉丁语 cultura", "colere 是耕种。文化原是把心智耕出来。"),
    ("cup", "拉丁语 cuppa", "古英语就借入了这个「杯」。它不是日耳曼本族的 bowl。"),
    ("curious", "拉丁语 curiosus", "cura 是操心。好奇是特别上心。"),
    ("curriculum vitae/CV", "拉丁语 curriculum vitae", "curriculum 是跑的路程，vita 是生命。履历是一生跑过的路。CV 是这两个词的缩写。"),
    ("curve", "拉丁语 curvus「弯的」", "曲线。"),
    ("custom", "古法语 costume", "拉丁语 consuetudo「习惯」。海关 customs 是习惯上要交的那笔税。"),
    ("customs", "拉丁语 consuetudo「习惯」", "海关是按习惯征收的关口。"),
    ("customer", "custom「光顾的习惯」", "来自拉丁语 consuetudo。顾客是习惯来的人。"),
    ("damage", "古法语 damage", "拉丁语 damnum「损失」。"),
    ("danger", "古法语 dangier", "拉丁语 dominium「统治权」。危险原是落在别人权力之下。"),
    ("dangerous", "古法语 dangier", "处于别人权力之下，因而不安全。"),
    ("date", "拉丁语 data「已给出」", "dare 是给。中世纪信上写 Data Romae，意思是于罗马寄出。日期从这里来。"),
    ("decimal", "拉丁语 decimus", "decem 是十。十进制。"),
    ("declare", "拉丁语 declarare", "clarus 是清楚。宣布就是说清楚。"),
    ("decline", "拉丁语 declinare", "clinare 是倾斜。下降、谢绝，都是偏开。"),
    ("decrease", "拉丁语 decrescere", "crescere 是生长。减少是往回长。"),
    ("deduct", "拉丁语 deducere", "ducere 是带领。扣除就是领走一笔。"),
    ("defeat", "古法语 desfait", "拉丁语 disfacere「做掉、撤销」。打败就是把对方做成不成。"),
    ("defence", "拉丁语 defendere", "fendere 是击打。防御是挡开打击。defense 是同一词的另一拼法。"),
    ("defend", "拉丁语 defendere", "挡开。"),
    ("definite", "拉丁语 definire", "finis 是边界。明确就是边界画死了。"),
    ("delegate", "拉丁语 delegare", "legare 是派出。代表是被派去的人。"),
    ("delete", "拉丁语 delere「涂掉」", "删去。"),
    ("deletion", "拉丁语 delere", "涂掉的那一处。"),
    ("delighted", "拉丁语 delectare「使人高兴」", "和 delight 是同一个动词。"),
    ("demonstrate", "拉丁语 demonstrare", "monstrare 是指出。演示就是指给人看。"),
    ("demonstration", "拉丁语 demonstrare", "指给人看的那场。"),
    ("deny", "古法语 denier", "拉丁语 denegare。否定就是说不。"),
    ("depart", "古法语 departir", "拉丁语 dis- 加上 partire「分开」。离开是从这里分开。"),
    ("department store", "department 加上 store", "department 来自法语 départir「分开」。store 来自拉丁语 instaurare「备起货」。百货店是分成许多部的店。"),
    ("depressed", "拉丁语 deprimere", "premre 是压。情绪低落就是被往下压。"),
    ("depression", "拉丁语 deprimere「往下压」", "经济萧条和情绪低落用的是同一个「下压」。"),
    ("description", "拉丁语 describere", "scribere 是写。描写就是把样子写下来。"),
    ("desert", "拉丁语 deserere「放弃、离开」", "沙漠是被放弃的地方。动词 desert 是离开岗位。甜点 dessert 是另一个词。"),
    ("desk", "中世纪拉丁语 desca", "来自拉丁语 discus、希腊语 diskos「圆盘」。书桌是一块书写的板。"),
    ("desktop", "desk 加上 top", "desk 来自希腊语、拉丁语的圆盘。top 是日耳曼词。桌面，后来是电脑的案头。"),
    ("despite", "古法语 despit", "拉丁语 despectus，despicere「向下看」。尽管，语气里原有看不起。"),
    ("destination", "拉丁语 destinare「钉住、指定」", "目的地是被指定的那一点。"),
    ("develop", "法语 développer", "原是把包着的东西打开。包裹那一层再早不完全确定，这里记到法语。"),
    ("dial", "拉丁语 dies「一天」", "日晷按天的影子来拨。后来才是电话拨号。"),
    ("diary", "拉丁语 diarium", "dies 是一天。日记是按天写的。journal 是同一族。"),
    ("dictation", "拉丁语 dictare「反复说」", "dicere 是说。听写就是照着说的写。"),
    ("differ", "拉丁语 differre", "ferre 是携带，dis- 是分开。不同就是各带各的。"),
    ("digital", "拉丁语 digitus「手指」", "数字原是扳手指。"),
    ("diploma", "希腊语 diploma「折好的纸」", "diplous 是双重。文凭原是折起来的正式文书。"),
    ("direct", "拉丁语 dirigere", "regere 是引导、摆正。直接就是不拐弯地摆正。"),
    ("direction", "拉丁语 dirigere", "被摆正的方向。"),
    ("directory", "拉丁语 dirigere", "用来找方向的名册。"),
    ("disabled", "dis- 加上 able", "able 来自拉丁语 habilis「拿得住」。disabled 是拿不住、做不了的。"),
    ("disappoint", "法语 désappointer", "appoint 来自拉丁语 ad punctum「定到一个点上」。失望是把定好的点撤掉。"),
    ("disc/disk", "希腊语 diskos，拉丁语 discus", "圆盘。"),
    ("discover", "古法语 descovrir", "拉丁语 dis- 加上 cooperire「揭开盖子」。发现就是揭开。"),
    ("discussion", "拉丁语 discutere「敲开」", "discuss 的名词。讨论是把事情敲开看。"),
    ("disk drive", "希腊语 diskos 加上 drive", "盘是希腊词。drive 是日耳曼词「驱动」。磁盘驱动器是让盘转起来的装置。"),
    ("dislike", "dis- 加上 like", "like 是日耳曼词。dis- 来自拉丁语。不喜欢就是把喜欢撤掉。"),
    ("distance", "拉丁语 distantia", "stare 是站。距离是站开的那段。"),
    ("distant", "拉丁语 distare", "站得远。"),
    ("distribution", "拉丁语 distribuere", "tribuere 是分派。分销就是派到各处。"),
    ("district", "中世纪拉丁语 districtus", "distringere 是拉紧。行政区是被划紧的一片。"),
    ("disturb", "拉丁语 disturbare", "turba 是混乱的人群。打扰就是把平静搅乱。"),
    ("divide", "拉丁语 dividere", "分开。dividend「股息」是该被分开的那一份。"),
    ("division", "拉丁语 dividere", "分开的结果，或一个部门。"),
    ("doctor/Dr", "拉丁语 doctor", "docere 是教。博士和医生在词源上都是老师。Dr 是这个词的缩写。"),
    ("documentary", "拉丁语 documentum", "docere 是教。纪录文件是用来说明的。"),
    ("documentation", "拉丁语 documentum", "一套用来说明的文件。"),
    ("domestic", "拉丁语 domesticus", "domus 是家。国内的、家里的，都是这一家。"),
    ("double", "拉丁语 duplus", "duo 是二。两倍。"),
    ("doubt", "拉丁语 dubitare", "duo 是二。怀疑是心里有两个想法。"),
    ("dozen", "古法语 dozaine", "拉丁语 duodecim「十二」。一打是十二个。"),
    ("drama", "希腊语 drama", "dran 是去做。戏剧是做出来给人看的。"),
    ("dramatic", "希腊语 drama", "像戏那样的。"),
    ("dramatically", "希腊语 drama", "以很像戏的方式。"),
    ("dress", "古法语 dresser「整理、使直立」", "拉丁语 directus「直的」。穿衣服原是把仪容整理好。"),
    ("driving licence", "drive 加上 licence", "drive 是日耳曼词。licence 来自拉丁语 licere「被允许」。驾照是允许你开车的文件。"),
    ("duplicate", "拉丁语 duplicare", "duo 加上 plicare「折」。一式两份就是折成双。"),
    ("during", "拉丁语 durare「持续、变硬」", "during 是「在它持续的时候」。"),
    ("eager", "古法语 aigre", "拉丁语 acer「尖锐」。热切原是锐利。"),
    ("easy", "古法语 aise", "拉丁语 adjacens「躺在近旁」。容易就是安安稳稳挨着，不必费力。"),
    ("economical", "希腊语 oikonomia", "oikos 是家，nemein 是管理。节约是把家管好。"),
    ("economics", "希腊语 oikonomia", "治家，后来是治一地的资源。"),
    ("educate", "拉丁语 educare「养育、带大」", "和 ducere「带领」是近亲。教育先是把人带大。"),
    ("effective", "拉丁语 efficere", "ex- 加上 facere「做」。有效就是真做出来了。"),
    ("effort", "法语 effort", "拉丁语 ex- 加上 fortis「强」。努力是使出的力气。"),
    ("electric", "希腊语 elektron「琥珀」", "琥珀摩擦会生电，这个词就给了电。"),
    ("electrical", "希腊语 elektron「琥珀」", "和电有关的。"),
    ("electricity", "希腊语 elektron「琥珀」", "电。"),
    ("electronic", "希腊语 elektron", "用电子的方式工作的。"),
    ("electronics", "希腊语 elektron", "电子学，或电子设备。"),
    ("electronic mail", "希腊语 elektron 加上 mail", "mail 来自古法语 male「袋子」。电子邮件是用电送出的信。"),
    ("elementary", "拉丁语 elementum「基本成分」", "最初的、元素的。"),
    ("elevator", "拉丁语 elevare「举起」", "levis 是轻。电梯是把人举上去的装置。"),
    ("embarrass", "法语 embarrasser", "意大利语 imbarazzare，barra 是横杠。难堪就是被横杠挡住。"),
    ("embassy", "法语 ambassade", "和 ambassador 同族，拉丁语 ambactus，更早是日耳曼语「被派去的人」。大使馆是使者的驻处。"),
    ("emergency", "拉丁语 emergere「从里面冒出来」", "mergere 是沉入。紧急情况是突然冒出来的。"),
    ("employment agency", "employ 加上 agency", "employ 来自拉丁语 implicare「拿来用」。agency 来自 agere「去做」。职业介绍所是替人把工作做成的地方。"),
    ("enable", "en- 加上 able", "able 来自拉丁语 habilis。使某人做得到。"),
    ("enclose", "古法语 enclos", "拉丁语 includere「关在里面」。附上就是夹进信里。"),
    ("encourage", "法语 encourager", "拉丁语 cor「心」。鼓励是把勇气放进心里。"),
    ("engine", "古法语 engin", "拉丁语 ingenium「天赋、巧机关」。发动机原是一个巧装置。"),
    ("engineer", "古法语 engin，拉丁语 ingenium", "做巧装置的人。"),
    ("engineering", "拉丁语 ingenium「巧机关」", "工程是设计这些装置。"),
    ("English", "Angles 这个日耳曼部族的名字", "England 是他们的土地。英语不是从拉丁语来的语言名。"),
    ("enjoy", "古法语 enjoir", "拉丁语 gaudere「喜乐」。享受就是处于喜乐里。"),
    ("enormous", "拉丁语 enormis", "norma 是尺、规范。大得超出规矩。"),
    ("enrol", "法语 enrôler", "拉丁语 rotulus「小卷轴」。登记就是写进名册的卷子。"),
    ("ensure", "古法语 enseurer", "拉丁语 securus「不必操心」。确保就是使人可以放心。insure 是同一族。"),
    ("enter", "拉丁语 intrare", "走进去。"),
    ("enthusiasm", "希腊语 enthousiasmos", "en- 加上 theos「神」。热情原是神进到人里面。"),
    ("enthusiastic", "希腊语 enthousiasmos", "满是这股热的。"),
    ("entire", "拉丁语 integer「完整、没被碰过」", "整数 integer 是同一个词。"),
    ("entrance", "拉丁语 intrare「进入」", "入口。"),
    ("entry", "拉丁语 intrare", "进入，或写进去的一条。"),
    ("envelope", "法语 enveloppe", "把信包起来的那一层。动词再早的来源不算稳，这里记到法语。"),
    ("environment", "法语 environ「周围」", "环境就是四周。environ 再早不完全一致，这里记到法语。"),
    ("environmental", "法语 environ「周围」", "和四周环境有关的。"),
    ("equal", "拉丁语 aequalis", "aequus 是平的。相等就是一样平。"),
    ("equip", "古法语 esquiper", "古诺斯语 skipa「给船配人」。装备原是给船把人手配齐，是日耳曼词经法语进来。"),
    ("escalator", "近代造的词", "escalade 来自法语，和拉丁语 scala「梯子」有关，再加上 elevator「升起」。自动扶梯是会升的梯子。"),
    ("escape", "通俗拉丁语 *excappare", "cappa 是斗篷。逃走原是留下斗篷、人跑了。经古法语。"),
    ("especially", "拉丁语 specialis", "species 是种类，specere 是看。尤其就是这一类特别。"),
    ("essential", "拉丁语 essentia", "esse 是「是」。必要的，是少了它就不成立的。"),
    ("estimate", "拉丁语 aestimare「估价」", "估计就是给一个价。"),
    ("EU", "European Union 的缩写", "Europe 是希腊语 Europē，这个地名再往前没有把握。Union 来自拉丁语 unus「一」。"),
    ("Euro", "Europe", "欧洲的货币名。Europe 是希腊语 Europē，地名再早没有定论，这里只记到这个名字。"),
    ("exact", "拉丁语 exigere「称出、索取」", "agere 是做。精确就是称到刚刚好。"),
    ("exam", "examination 的缩短", "拉丁语 examinare。examen 原是天平的指针。考试是称一称。"),
    ("examination", "拉丁语 examinare", "examen 是天平指针。考试和检查都是称一称。"),
    ("examine", "拉丁语 examinare", "放到天平上称。"),
    ("example", "拉丁语 exemplum", "eximere 是取出来。例子是取出来给人看的一个。"),
    ("excellent", "拉丁语 excellere「高出来」", "出色就是高出一截。"),
    ("excess", "拉丁语 excedere", "cedere 是走。过量就是走出了限度。"),
    ("exchange", "古法语 eschangier", "拉丁语 ex- 加上 cambiare「更换」，cambiare 来自凯尔特语。交换。"),
    ("exchange rate", "exchange 加上 rate", "exchange 是更换。rate 来自拉丁语 rata「算定的一份」。汇率是换算出来的比价。"),
    ("excited", "拉丁语 excitare「叫起来」", "激动就是被叫醒。"),
    ("exciting", "拉丁语 excitare", "叫得人起来的。"),
    ("excluding", "拉丁语 excludere", "claudere 是关闭。把某物关在外面。"),
    ("excuse", "拉丁语 excusare", "causa 是事由。原谅就是把事由说开。"),
    ("executive", "拉丁语 exsequi「跟到底、执行」", "sequi 是跟随。执行官是把决定跟到底的人。"),
    ("exercise", "拉丁语 exercere「不停地做、操练」", "练习就是反复驱动。"),
    ("exhibit", "拉丁语 exhibere", "habere 是持有。展出就是拿出来给人持有、看见。"),
    ("exhibition", "拉丁语 exhibere", "拿出来的那场展示。"),
    ("exist", "拉丁语 exsistere「站出来」", "sistere 是站住。存在就是站到了这里。"),
    ("expansion", "拉丁语 expandere「铺开」", "扩张就是铺出去。"),
    ("experience", "拉丁语 experiri「试过」", "经验是试过的那些事。"),
    ("experienced", "拉丁语 experiri", "试过的。"),
    ("experiment", "拉丁语 experimentum", "拿来试的一次。"),
    ("expert", "拉丁语 expertus「试过的」", "专家是试过、因而内行的人。"),
    ("explanation", "拉丁语 explanare", "planus 是平的。解释就是把皱着的铺平。"),
    ("explore", "拉丁语 explorare", "原是猎人喊着把林子搜一遍。探索仍是这幅画面。"),
    ("external", "拉丁语 externus", "在外面的。"),
    ("extraordinary", "拉丁语 extra「在外」加上 ordo「行列」", "不在常列里的。"),
    ("extremely", "拉丁语 extremus「最外面」", "到了顶的程度。"),
    ("facilities", "拉丁语 facilitas", "facilis 是容易做的。设施是使事情好做的那些条件。"),
    ("facing", "拉丁语 facies「脸、外观」", "经古法语 face。面对就是把脸转向。"),
    ("fail", "古法语 faillir", "拉丁语 fallere「欺骗、落空」。失败就是没有兑现。"),
    ("faint", "古法语 feint", "拉丁语 fingere「塑造、假装」。昏厥和微弱，原是撑出来的样子塌了。"),
    ("faithfully", "古法语 feid，拉丁语 fides「信任」", "忠实地，就是按信任去做。"),
    ("false", "拉丁语 falsus", "fallere 是欺骗。假的就是欺骗性的。"),
    ("family", "拉丁语 familia", "原是一户里的全家，包括仆从，不是只指血亲。"),
    ("famous", "拉丁语 famosus", "fama 是传闻。有名就是传闻里有他。"),
    ("fan", "有两支", "作风扇，来自拉丁语 vannus「簸谷的扇」。作爱好者，是 fanatic 的缩短，拉丁语 fanum「神庙」，入迷原是庙里的狂热。"),
    ("fantastic", "希腊语 phantasia「显现的想象」", "好得像幻想出来的。"),
    ("farm", "古法语 ferme", "拉丁语 firmare「使固定」。农场原是定下租约的一块地，不是日耳曼的 field。"),
    ("fault", "古法语 faute", "拉丁语 fallere「落空、欺骗」。过错是没有站住的地方。"),
    ("favourite", "拉丁语 favor", "favere 是善意。最受善待的那个。"),
    ("fax machine", "fax 加上 machine", "fax 是 facsimile 的缩短，拉丁语 facere「做」和 similis「相像」。machine 来自希腊语 mekhane。传真机做出一份相像的文书。"),
    ("female", "拉丁语 femella", "femina「女人」的小词。"),
    ("festival", "拉丁语 festum「节日」", "和 fair「集市」的拉丁语 feriae 是近亲。"),
    ("fiction", "拉丁语 fictio", "fingere 是塑造。小说是塑造出来的。"),
    ("figure", "拉丁语 figura", "fingere 是塑造。数字、人影、图表都是一个造形。"),
    ("file", "拉丁语 filum「线」", "档案是穿在一条线上的文书，锉刀也是带线纹的工具。"),
    ("filing cabinet", "file 加上 cabinet", "file 来自拉丁语 filum「线」。cabinet 是法语里的小房间。档案柜是放成串文件的柜子。"),
    ("final demand", "final 加上 demand", "final 来自拉丁语 finis「尽头」。demand 来自拉丁语 demandare「交托」。最后催款是交到尽头的那一次要求。"),
    ("finalise", "拉丁语 finis「尽头」加上英语动词后缀", "把事情收到尽头。"),
    ("financial advisor", "finance 加上 advisor", "finance 来自拉丁语 finis「结清」。advisor 来自拉丁语 ad visum「看上去」。理财顾问是帮人把账看清楚的人。"),
    ("financial year", "finance 加上 year", "finance 来自拉丁语 finis。year 是日耳曼词。财政年度是结账的那一年。"),
    ("fine", "拉丁语 finis「尽头」", "作「好、精细」和作「罚金」都从尽头来：精细是到了头，罚金是把事结清。"),
    ("fix", "拉丁语 figere「钉住」", "修理、确定，都是把它钉死。"),
    ("fixed cost", "fix 加上 cost", "fix 来自拉丁语 figere「钉住」。cost 来自拉丁语 constare「值这么多」。固定成本是钉住不变的那笔。"),
    ("fixed-term contract", "fix、term 和 contract", "都是拉丁语一路：钉住的期限，再把双方拉到一起。"),
    ("flexibility", "拉丁语 flectere「弯曲」", "能弯而不折。"),
    ("flexible", "拉丁语 flexibilis", "flectere 是弯曲。"),
    ("flotation", "float 的名词", "float 是日耳曼词「浮」。股票上市用了这个「浮起来」，拼写受了拉丁语影响，来源仍是 float。"),
    ("flowchart", "flow 加上 chart", "flow 是日耳曼词。chart 来自拉丁语 charta、希腊语 khartes。流程图是把流动画在纸上。"),
    ("focus", "拉丁语 focus「炉灶」", "光学里火聚成的那一点，后来才是注意力的焦点。"),
    ("force", "古法语 force", "拉丁语 fortis「强的」。力量。"),
    ("foreign", "古法语 forain", "拉丁语 foras「在外面」。外国的就是外面的。"),
    ("foreigner", "拉丁语 foras「在外面」", "从外面来的人。"),
    ("foreign currency", "foreign 加上 currency", "foreign 来自拉丁语 foras。currency 来自拉丁语 currere「跑」。外币是在外面跑的钱。"),
    ("foreign exchange", "foreign 加上 exchange", "两者都经法语来自拉丁语。外汇是和外面兑换。"),
    ("forgetful", "forget 加上 -ful", "forget 是日耳曼词。容易忘的。"),
    ("form", "拉丁语 forma「形状、模子」", "表格是把信息放进模子。"),
    ("forward", "古英语 foreweard", "fore 是前，-ward 是朝向。向前是日耳曼词。它不是拉丁语的 forth 的借词。"),
    ("forward(s)", "日耳曼语 fore「前面」加上 -ward「朝向」", "向前。期货里的 forward 也是朝前的那一份合约。"),
    ("founder", "拉丁语 fundare", "fundus 是底。作「创立」是打底。作「沉没」是沉到底。两个都和底有关。"),
    ("fridge", "refrigerator 的缩短", "拉丁语 frigus「寒冷」。冰箱就是造冷的机器。"),
    ("front", "拉丁语 frons「额头、正面」", "前面。"),
    ("fuel", "古法语 fouaille", "拉丁语 focus「炉灶」。燃料是给炉灶的。"),
    ("function", "拉丁语 functio", "fungi 是执行、履行。功能就是它被拿来做的那件事。"),
    ("fund", "拉丁语 fundus「底、地产」", "资金原是垫底的那一笔。"),
    ("funding", "拉丁语 fundus", "把垫底的钱备上。"),
    ("furnish", "法语 fournir", "更早是法兰克日耳曼语「供给」。布置就是把东西供给这间屋子。"),
    ("furniture", "法语 fournir「供给」", "更早是日耳曼语。家具是供给屋子的那些东西。"),
    ("future", "拉丁语 futurus「将要是的」", "esse「是」的将来分词。将来。"),
    ("gain", "古法语 gaaignier", "日耳曼语 waidanjan「打猎、觅食」。收益原是觅来的。"),
    ("garage", "法语 garer「使停住」", "更早是日耳曼语 waron「留神、看守」。车库是把车看守起来的地方。"),
    ("gas", "希腊语 khaos「空隙」", "十七世纪范海尔蒙特造了这个科学用词，用来指他觉得像混沌一样的气。"),
    ("general", "拉丁语 generalis", "genus 是种类。总的，就是关乎整个种类的。"),
    ("generous", "拉丁语 generosus", "genus 是出身。大方原是出身好的人该有的气量。"),
    ("gentle", "古法语 gentil", "拉丁语 gentilis「同族的」。后来才是温和。"),
    ("gentleman", "gentle 加上 man", "gentle 来自拉丁语 gentilis。man 是日耳曼词。绅士原是同族里有身份的人。"),
    ("genuine", "拉丁语 genuinus「天生的、地道的」", "真的，就是生来如此，不是后来冒充。"),
    ("gift", "古诺斯语 gift", "日耳曼词，和 give 同族。礼物是给出的东西。"),
    ("gift voucher", "gift 加上 voucher", "gift 是日耳曼词。voucher 来自拉丁语 vocare「呼叫」，是一张可以被兑付时叫出来的凭单。"),
    ("global", "拉丁语 globus「球」", "全球就是这整个球体。"),
    ("goal", "来源没有把握，不写入", ""),
    ("govern", "拉丁语 gubernare", "希腊语 kybernan「掌舵」。治理就是掌舵。"),
    ("government", "拉丁语 gubernare「掌舵」", "掌舵的那套机构。"),
    ("grammar", "希腊语 grammatike", "gramma 是字母。语法是字母和句子的技术。"),
    ("gram(me)", "希腊语 gramma「写下的一小笔、一个小重量」", "克。"),
    ("grant", "古法语 graanter", "拉丁语 credere「相信」。准予就是相信并给出。"),
    ("graphics", "希腊语 graphein「画、写」", "图形。"),
    ("group", "意大利语 gruppo", "日耳曼语里「圆的一簇」。一组就是聚成的一簇，经意大利语、法语进来。"),
    ("guarantee", "日耳曼语里表示担保的词", "经法语进来。和 warranty 是一对。guarantee 更常是一句口头或书面的担保。"),
    ("guard", "古法语 garder", "日耳曼语 ward「看守」。守卫是看守的人。"),
    ("guide", "古法语 guider", "日耳曼语 witan「让人知道路」。向导是把路指出来的人。"),
    ("habit", "拉丁语 habitus", "habere 是持有。习惯是你持有的样子，也指教士的服装。"),
    ("hallo/hello", "英语的招呼", "和 hail 同族，hail 是日耳曼词。它不是拉丁语的 salve。"),
    ("history", "希腊语 historia「打听、探究」", "经拉丁语。历史原是把事情问清楚。"),
    ("honest", "拉丁语 honestus", "honor 是荣誉。诚实是配得上荣誉的。"),
    ("horrible", "拉丁语 horribilis", "horrere 是因恐惧而竖起。可怕的。"),
    ("hospitality", "拉丁语 hospitalitas", "hospes 是客人也是主人。待客。"),
    ("host", "拉丁语 hospes「客人、主人」", "主人。电脑里的主机也是款待别人的那一台。"),
    ("hour", "希腊语 hora", "经拉丁语、法语。小时。它不是日耳曼的 time。"),
    ("hourly fee", "hour 加上 fee", "hour 来自希腊语 hora。fee 是日耳曼词，古英语 feoh，原和牲畜、财产有关。按小时收的费。"),
    ("hourly rate", "hour 加上 rate", "hour 来自希腊语 hora。rate 来自拉丁语 rata「算定的一份」。小时费率。"),
    ("human", "拉丁语 humanus", "人的。和 homo「人」同族。"),
    ("idea", "希腊语 idea「看见的样子、理型」", "主意原是一个看得见的形状。"),
    ("identity", "拉丁语 identitas", "idem 是同一个。身份就是还是同一个人。"),
    ("image", "拉丁语 imago", "imitari 是模仿。图像是仿出来的样子。"),
    ("imagination", "拉丁语 imaginari", "在心里造出图像。"),
    ("imagine", "拉丁语 imaginari", "在心里看见。"),
    ("immediate", "拉丁语 immediatus", "medius 是中间。立刻就是中间没有间隔。"),
    ("immigration", "拉丁语 migrare「迁移」", "in- 是进来。移入。"),
    ("importance", "拉丁语 importare", "把分量带进来。重要就是有分量。"),
    ("important", "拉丁语 importare「带进、有关系」", "有分量的。"),
    ("impossible", "拉丁语 impossibilis", "posse 是能够。不可能就是不能。"),
    ("impressive", "拉丁语 imprimere「压印」", "压进心里的。"),
    ("inch", "拉丁语 uncia「十二分之一」", "古英语就借入了。英寸和盎司是同一个「十二分之一」。"),
    ("inconvenience", "拉丁语 convenire「来到一起、合适」的否定", "不方便就是合不到一起。"),
    ("inconvenient", "拉丁语 convenire", "合不上的。"),
    ("incorrect", "拉丁语 corrigere「扶正」的否定", "没有扶正的。"),
    ("independent", "拉丁语 dependere「挂在下面」的否定", "不挂靠别人。"),
    ("index", "拉丁语 index「食指、指示」", "索引就是用来指的。"),
    ("indication", "拉丁语 indicare", "index 是食指。指示。"),
    ("individual", "拉丁语 individuus", "in- 否定，dividere 是分开。个人就是不能再拆开的一个。"),
    ("industrial", "拉丁语 industria「勤勉」", "industry 的形容词。"),
    ("inflation", "拉丁语 inflare「吹胀」", "flare 是吹。通货膨胀就是把物价吹大。"),
    ("influence", "拉丁语 influere「流进去」", "fluere 是流。影响原是星象流入人事，后来才是一般的影响。"),
    ("inform", "拉丁语 informare「赋予形状」", "通知就是把一个形状放进人的心里。"),
    ("information technology", "information 加上 technology", "information 来自拉丁语 informare。technology 来自希腊语 tekhne「技艺」和 logos「学问」。"),
    ("inhabitant", "拉丁语 inhabitare", "habitare 是居住。居民是住在这里的人。"),
    ("injure", "拉丁语 iniuria", "in- 否定，ius 是权利。伤害就是做出不公。"),
    ("injury", "拉丁语 iniuria「不公、伤害」", "ius 是权利。"),
    ("ink", "希腊语 enkauston", "拉丁语 encaustum，原是烧进去的紫墨。墨水。"),
    ("innovation", "拉丁语 innovare", "novus 是新的。创新就是做新。"),
    ("innovative", "拉丁语 innovare", "会做新的。"),
    ("install", "中世纪拉丁语 installare", "in- 加上 stall。stall 是日耳曼词「位置」。安装就是放到它的位置上。"),
    ("installation", "中世纪拉丁语 installare", "放到位置上的那套设备。"),
    ("instalment", "同一条 install", "分期付款是把一笔钱一次次放到该放的位置上。"),
    ("instructions", "拉丁语 instruere「搭建、装备」", "说明书是把步骤装备给你。"),
    ("instructor", "拉丁语 instruere", "把本领装备给你的人。"),
    ("insurance policy", "insurance 加上 policy", "insurance 来自拉丁语 securus「不必操心」。这里的 policy 来自意大利语 polizza，希腊语 apodeixis「证明」，是保单，不是政治方针那个 policy。"),
    ("insure", "古法语 enseurer", "拉丁语 securus。保险就是让损失来了也不必从零操心。"),
    ("intend", "拉丁语 intendere", "tendere 是伸。打算就是把心意伸向那边。"),
    ("interest rate", "interest 加上 rate", "interest 来自拉丁语 interesse「处在其中、有关系」。rate 来自拉丁语 rata。利率是这笔关系算定的价。"),
    ("invoice", "法语 envoi「寄出」", "拉丁语 inviare「上路」。发票原是随货寄出的单，不是 voice「声音」。"),
    ("involve", "拉丁语 involvere「卷进去」", "volvere 是滚。卷入。"),
    ("item", "拉丁语 item「同样地」", "清单上一项一项往下加时写的词，后来就成了「一项」。"),
    ("job", "来源未定，不单列", ""),
    ("join", "古法语 joindre", "拉丁语 iungere「连接」。"),
    ("journal", "拉丁语 diurnalis", "dies 是一天。日记账按天记。这个词若已有更细的说明，以那一条为准。"),
    ("journey", "古法语 journee", "拉丁语 diurnum「属于一天的」。旅程原是一天的路。"),
    ("judge", "古法语 juge", "拉丁语 iudex，ius「法」加上 dicere「说」。法官是说法的人。"),
    ("jump", "来源未定，不单列", ""),
    ("just", "拉丁语 iustus", "ius 是法、权利。公正就是合乎法。"),
    ("keen", "古英语 cene「勇敢、锐利」", "日耳曼词。热切是从锐利来的。"),
    ("keyboard", "key 加上 board", "key 是日耳曼词。board 也是。键盘是一板的键。"),
    ("kilo/kilogram/kilogramme", "希腊语 khilioi「一千」加上 gramma「一小笔重量」", "千克。"),
    ("kilometre", "希腊语 khilioi「一千」加上 metron「量」", "千米。"),
    ("kitchen", "拉丁语 coquina", "coquere 是煮。古英语借入了这个词。厨房不是日耳曼本族词。"),
    ("knowledge", "古英语 cnawan「知道」", "日耳曼词。knowledge 是知道的那个状态。"),
    ("label", "古法语 label「带子、封条」", "一般认为来自日耳曼语。标签是贴上去的一条。"),
    ("laboratory", "拉丁语 laborare「劳动」", "实验室是干活、做试验的房间。lab 是它的缩短。"),
    ("labour", "古法语 labour", "拉丁语 labor「辛劳」。"),
    ("lake", "古法语 lac", "拉丁语 lacus。湖。"),
    ("lamp", "希腊语 lampas", "lampein 是发光。灯。"),
    ("language", "古法语 langage", "拉丁语 lingua「舌头」。语言。"),
    ("laptop", "lap 加上 top", "lap 是日耳曼词「膝」。top 也是。笔记本电脑是放在膝上的那一台。"),
    ("large", "古法语 large", "拉丁语 largus「充裕的」。大。"),
    ("laser", "英语缩写", "Light Amplification by Stimulated Emission of Radiation。这是二十世纪造的缩写，不是古词。"),
    ("launch", "北方法语 lancher", "拉丁语 lanceare「挥矛」。发射、上市，都是把东西投出去。"),
    ("laundry", "古法语 lavanderie", "拉丁语 lavare「洗」。洗衣房。"),
    ("lavatory", "拉丁语 lavatorium", "lavare 是洗。盥洗室。"),
    ("lawyer", "law 加上指人的后缀", "law 来自古诺斯语，不是拉丁语 lex。lawyer 是从事法律的人。legal 才走 lex。"),
    ("layout", "lay 加上 out", "两个都是日耳曼词。布局就是铺开来的样子。"),
    ("leaflet", "leaf 加上小词后缀", "leaf 是日耳曼词。传单像一小片叶子。"),
    ("lecture", "拉丁语 lectura", "legere 是读。讲座原是照着读。"),
    ("legal", "拉丁语 legalis", "lex 是法。它不是日耳曼的 law。"),
    ("leisure", "古法语 leisir", "拉丁语 licere「被允许」。闲暇原是被允许停下。"),
    ("lesson", "古法语 lecon", "拉丁语 lectio，legere「读」。一课原是读的一段。"),
    ("letter", "古法语 lettre", "拉丁语 littera「字母」。信是写满字母的。"),
    ("level", "古法语 livel", "拉丁语 libella，libra 是天平。水平就是和天平一样平。"),
    ("liberal", "拉丁语 liberalis", "liber 是自由的。开明、慷慨，原是自由人的做派。"),
    ("library", "拉丁语 librarium", "liber 是书。图书馆是放书的地方。"),
    ("licence", "拉丁语 licentia", "licere 是被允许。执照就是一份允许。license 是同一词的另一拼法。"),
    ("line", "拉丁语 linea「麻线」", "linum 是亚麻。线条、队伍、行业里的 line 都从这根线来。它不是日耳曼词。"),
    ("liquid", "拉丁语 liquidus「流动的」", "液体。"),
    ("list", "来源有两说，不单列成定论", ""),
    ("litre", "法语 litre", "希腊语 litra，一个重量或容量，经拉丁语。"),
    ("local", "拉丁语 localis", "locus 是地方。本地的。"),
    ("logo", "希腊语 logos「词」", "标志原是一个认得出的词或印。"),
    ("loyal", "古法语 loial", "拉丁语 legalis，lex 是法。忠诚原是合乎义务。"),
    ("loyalty", "古法语 loial，拉丁语 legalis", "守着这份义务。"),
    ("luxury", "拉丁语 luxuria", "luxus 是过量。奢侈是过了分。"),
    ("machine", "拉丁语 machina", "希腊语 mekhane 或 doric 的 makhana「装置」。机器。"),
    ("machinery", "拉丁语 machina，希腊语 mekhane", "一套机器。"),
    ("magazine", "阿拉伯语 makhzan「仓库」", "经意大利语、法语。杂志原是杂货库，后来是收了各种文章的本子。"),
    ("mail", "古法语 male「旅行袋」", "邮件原是袋里的那一包信。"),
    ("mail order", "mail 加上 order", "mail 来自古法语的袋子。order 来自拉丁语 ordo「行列」。邮购是按单子把货从邮袋里送来。"),
    ("main", "古法语 maine", "拉丁语 magnus「大」。主要的。它看起来像英语小词，其实不是日耳曼词。"),
    ("male", "拉丁语 masculus", "mas「男性」的小词。"),
    ("map", "拉丁语 mappa「餐巾、布」", "地图原是画在一块布上的。"),
    ("market", "拉丁语 mercatus", "merx 是货物。经古北法语。市场是做货物买卖的地方。"),
    ("married", "古法语 marier", "拉丁语 maritare，maritus 是丈夫。"),
    ("mass", "有两支", "作「一堆、质量」，来自拉丁语 massa，希腊语 maza「大麦饼、一团」。作「弥撒」，来自拉丁语 missa「遣散」，是礼拜结束时说的话。"),
    ("master", "拉丁语 magister「更大的人、老师」", "magis 是更。主人、大师都是更大的那一个。它不是日耳曼的 lord。"),
    ("material", "拉丁语 materialis", "materia 是木材、物质。材料。"),
    ("maths", "希腊语 mathematike 的缩短", "manthanein 是学习。数学是学习的学问。"),
    ("mathematics", "希腊语 mathematike", "manthanein 是学习。"),
    ("matter", "古法语 matere", "拉丁语 materia「木材、物质」。事情和物质是同一条。"),
    ("mature", "拉丁语 maturus「成熟的」", "像果子熟了。"),
    ("measure", "古法语 mesure", "拉丁语 mensura，metiri「测量」。"),
    ("mechanic", "希腊语 mekhane「装置」", "修理机器的人。"),
    ("member", "拉丁语 membrum「肢体」", "成员原是一个身体上的一肢。"),
    ("membership", "拉丁语 membrum", "作为一肢属于这个团体。"),
    ("memory", "拉丁语 memoria", "memor 是记住。"),
    ("mention", "拉丁语 mentio", "mens 是心智。提及就是把它从心里叫出来。"),
    ("menu", "法语 menu「细的、详细的」", "拉丁语 minutus「变小的」。菜单是细目。"),
    ("merge", "拉丁语 mergere「沉入」", "合并就是一家没入另一家。"),
    ("message", "古法语 message", "拉丁语 mittere「送」。消息是被送出的。"),
    ("metal", "拉丁语 metallum", "希腊语 metallon「矿、金属」。"),
    ("method", "希腊语 methodos", "meta 加上 hodos「路」。方法是顺着走的一条路。"),
    ("metre", "希腊语 metron「尺度」", "米。"),
    ("microphone", "希腊语 mikros「小」加上 phone「声音」", "把小声音变大的器具。"),
    ("military", "拉丁语 militaris", "miles 是士兵。"),
    ("million", "意大利语 millione", "拉丁语 mille「一千」的大词。很大的千。"),
    ("mineral", "中世纪拉丁语 minerale", "和 mine「矿」一路，矿这个词来自古法语，更早多半是凯尔特语。矿物是从矿里来的。"),
    ("mobile", "拉丁语 mobilis", "movere 是移动。可移动的。"),
    ("model", "意大利语 modello", "拉丁语 modulus，modus「尺度」。模型是一个小尺度。"),
    ("modern", "拉丁语 modernus", "modo 是「刚刚」。现代的原是此刻的。"),
    ("moment", "拉丁语 momentum", "movere 是移动。片刻原是使天平移动的那一点分量。"),
    ("motivate", "拉丁语 movere「移动」", "动机 motive 是使人动的那个。激励就是让人动起来。"),
    ("motivation", "拉丁语 movere", "使人动起来的原因。"),
    ("motor", "拉丁语 motor「使之移动的」", "movere 是移动。发动机。"),
    ("motorbike", "motor 加上 bike", "motor 来自拉丁语 movere。bike 是 bicycle 的缩短，拉丁语 bi- 加上希腊语 kyklos「轮」。"),
    ("motorcycle", "motor 加上 cycle", "motor 来自拉丁语 movere。cycle 来自希腊语 kyklos「圆、轮」。"),
    ("motorway", "motor 加上 way", "motor 来自拉丁语。way 是日耳曼词。高速公路是给机动车的路。"),
    ("mountain", "古法语 montaigne", "拉丁语 mons「山」。"),
    ("move", "古法语 movoir", "拉丁语 movere。移动。"),
    ("movie", "moving picture 的缩短", "move 来自拉丁语 movere。电影是会动的画面。"),
    ("multiply", "拉丁语 multiplicare", "multus「多」加上 plicare「折叠」。乘法就是叠很多次。"),
    ("musical", "希腊语 mousike", "Mousa 是缪斯。音乐属于缪斯。"),
    ("musician", "希腊语 mousike", "做音乐的人。"),
    ("mystery", "希腊语 mysterion", "myein 是闭上眼睛、入会。奥秘原是不对外说的仪式。"),
    ("nation", "拉丁语 natio", "nasci 是出生。民族是同一出处的人。"),
    ("national", "拉丁语 natio", "属于这个民族或国家的。"),
    ("nationwide", "nation 加上 wide", "nation 来自拉丁语 natio。wide 是日耳曼词。全国范围就是这个国家那么宽。"),
    ("natural", "拉丁语 naturalis", "natura 来自 nasci「出生」。"),
    ("necessary", "拉丁语 necessarius", "necesse 是躲不开。必要的就是避不了的。"),
    ("negative", "拉丁语 negativus", "negare 是否认。否定的。"),
    ("nephew", "古法语 neveu", "拉丁语 nepos。外甥、侄子。"),
    ("nerve", "拉丁语 nervus「筋」", "神经后来才用这个词。"),
    ("nervous", "拉丁语 nervosus", "筋绷着的，后来是紧张的。"),
    ("nice", "古法语 nice「无知的、傻的」", "拉丁语 nescius「不知道的」。意思后来从傻变成好。这是意思变了，不是两个词。"),
    ("noise", "古法语 noise", "拉丁语 nausea，希腊语 nausia「晕船」。吵闹和恶心在词源上是同一阵不适。"),
    ("normal", "拉丁语 normalis", "norma 是木匠的矩尺。正常就是符合尺子。"),
    ("note", "拉丁语 nota「记号」", "笔记就是做上记号。"),
    ("notepad", "note 加上 pad", "note 来自拉丁语 nota。pad 是一沓纸，来源晚近。记事本是用来做记号的一沓。"),
    ("notepaper", "note 加上 paper", "note 来自拉丁语 nota。paper 来自希腊语 papyros。信纸。"),
    ("notice", "拉丁语 notitia", "nota 是记号。注意到，或一张告示。"),
    ("novel", "意大利语 novella，拉丁语 novellus", "novus 是新的。小说原是一个新故事，形容词 novel 是新奇的。"),
    ("number", "古法语 nombre", "拉丁语 numerus。数目。"),
    ("nurse", "古法语 norrice", "拉丁语 nutrire「喂养」。护士原是喂养的人。"),
    ("object", "拉丁语 obiectum", "obicere 是「扔到对面」。宾语和物体都是被扔到你面前的东西。"),
    ("objective", "拉丁语 obiectum", "摆在面前的目标。"),
    ("obtain", "拉丁语 obtinere", "tenere 是握住。得到就是握住。"),
    ("office", "拉丁语 officium", "opus「工作」加上 facere「做」。办公室是做事的职责所在。"),
    ("officer", "拉丁语 officium「职责」", "承担一份职责的人。"),
    ("oil", "古法语 oile", "拉丁语 oleum，希腊语 elaion「橄榄油」。"),
    ("online/on-line", "on 加上 line", "on 是日耳曼词。line 来自拉丁语 linea「线」。在线上。"),
    ("operate", "拉丁语 operari", "opus 是工作。操作就是做这件工作。"),
    ("operation", "拉丁语 operatio", "opus 是工作。手术和经营都是一场工作。"),
    ("opinion", "拉丁语 opinio", "心里认定的看法。"),
    ("option", "拉丁语 optio", "optare 是选择。选项。"),
    ("ordinary", "拉丁语 ordinarius", "ordo 是行列。普通就是在常列里。"),
    ("organisation", "中世纪拉丁语 organizare", "希腊语 organon「工具」。组织就是把工具排好。"),
    ("organise", "中世纪拉丁语 organizare", "希腊语 organon。把人和事排成一套工具。"),
    ("original", "拉丁语 originalis", "oriri 是升起。原来的就是从源头升起来的。"),
    ("originality", "拉丁语 origo", "oriri 是升起。独创是从自己的源头来。"),
    ("ought", "古英语 agan「拥有」的过去式", "日耳曼词。应当，原是欠着、负有。"),
    ("ounce", "古法语 unce", "拉丁语 uncia「十二分之一」。盎司。"),
    ("owe", "古英语 agan「拥有、欠」", "日耳曼词。欠就是还负着。"),
    ("pack", "中古荷兰语 pak", "日耳曼词。一包。"),
    ("package", "pack 加上法语后缀 -age", "pack 是日耳曼词。包装是后来造的名词。"),
    ("packet", "pack 的小词", "pack 是日耳曼词。一小包。"),
    ("page", "拉丁语 pagina", "原是一排书写，和 pangere「固定」有关。一页。"),
    ("pain", "古法语 peine", "拉丁语 poena「惩罚」，希腊语 poine。痛苦和惩罚是同一个词源。"),
    ("paint", "古法语 peint", "拉丁语 pingere「画」。"),
    ("pair", "古法语 paire", "拉丁语 paria，par「相等」。一对就是配得上的两个。"),
    ("paper", "古法语 papier", "拉丁语 papyrus，希腊语 papyros。纸从纸草来。"),
    ("paperclip", "paper 加上 clip", "paper 来自希腊语 papyros。clip 是日耳曼词「夹」。回形针夹住纸。"),
    ("paperwork", "paper 加上 work", "paper 来自希腊语、拉丁语。work 是日耳曼词。文书工作就是纸上的活。"),
    ("parcel", "古法语 parcelle", "拉丁语 particula，pars「一份」。包裹是分出来的一小份。"),
    ("parent", "拉丁语 parens", "parere 是生育。父母是生育的人。"),
    ("park", "古法语 parc", "日耳曼语 *parruk「围场」。公园和停车都是把一块地围起来。"),
    ("parking", "古法语 parc，日耳曼语围场", "把车放进围场。"),
    ("parliament", "古法语 parlement", "parler 是说话，拉丁语 parabola，希腊语 parabole「对照着说」。议会原是说话的场合。"),
    ("part-time/part time", "part 加上 time", "part 来自拉丁语 pars「一份」。time 是日耳曼词。兼职是只占一份时间。"),
    ("passenger", "古法语 passager", "拉丁语 passus「一步」。乘客是从这里经过的人。"),
    ("past", "来自 pass", "拉丁语 passus「一步」。过去就是已经走过去的。"),
    ("patient", "拉丁语 patiens", "pati 是忍受。病人是忍受的人，耐心也是忍受。"),
    ("pattern", "古法语 patron", "拉丁语 patronus「保护人、样板」。图案和模式都是拿来照着的样。它不是 father 的日耳曼词。"),
    ("pause", "拉丁语 pausa", "希腊语 pausis。停顿。"),
    ("peace", "古法语 pais", "拉丁语 pax。和平。"),
    ("peak", "来源可能与 pike 有关，不写成定论", ""),
    ("pen", "拉丁语 penna「羽毛」", "笔原是羽毛。"),
    ("pencil", "古法语 pincel", "拉丁语 penicillus「小刷」，和 penis「尾」有关。铅笔原是一支小毛笔。"),
    ("per", "拉丁语 per「通过、每」", "每、经由。"),
    ("per annum", "拉丁语", "per「每」，annus「年」。每年。"),
    ("percent", "拉丁语 per centum", "每一百。"),
    ("percentage", "拉丁语 per centum", "按每一百算出的那一份。"),
    ("perform", "盎格鲁法语 parfournir", "fournir 是供给、做成，更早是日耳曼语。表演和履行都是把事情做满。"),
    ("perhaps", "per 加上 hap", "per 是拉丁语「通过」。hap 是古诺斯语「运气」。也许就是靠运气也许能成。"),
    ("period", "希腊语 periodos", "peri「周围」加上 hodos「路」。周期是走完一圈，句号也是一圈走完。"),
    ("permanent", "拉丁语 permanere", "manere 是留下。永久就是留下不走。"),
    ("person", "拉丁语 persona", "原是面具，后来是面具后面的角色、人。"),
    ("personal", "拉丁语 personalis", "persona 是人、角色。个人的。"),
    ("personal assistant", "personal 加上 assistant", "personal 来自拉丁语 persona。assistant 来自拉丁语 assistere「站在旁边」。私人助理站在你旁边。"),
    ("personal computer", "personal 加上 computer", "personal 来自拉丁语 persona。computer 来自拉丁语 computare「计算」。个人电脑。"),
    ("personality", "拉丁语 persona", "一个人面具背后的那套性情。"),
    ("persuade", "拉丁语 persuadere", "suadere 是劝。说服就是劝透。"),
    ("petrol", "petroleum 的缩短", "拉丁语 petra「石头」来自希腊语，oleum 是油。石油是石头里的油。"),
    ("petrol station", "petrol 加上 station", "petrol 是石油。station 来自拉丁语 stare「站」。加油站是车子站住加油的地方。"),
    ("pharmaceutical", "希腊语 pharmakon「药」", "制药的。"),
    ("pharmacy", "希腊语 pharmakon「药」", "药房。"),
    ("phase", "希腊语 phasis「显现」", "阶段是它显现出来的一个面貌。"),
    ("photocopier", "希腊语 phos「光」加上 copy", "copy 来自拉丁语 copia。复印机用光做出另一份。"),
    ("photocopy", "希腊语 phos「光」加上拉丁语 copia「副本」", "用光复制。"),
    ("photograph", "希腊语 phos「光」加上 graphein「写」", "用光写下来。"),
    ("photography", "希腊语 phos 和 graphein", "用光书写的技术。"),
    ("picture", "拉丁语 pictura", "pingere 是画。图画。"),
    ("piece", "古法语 piece", "更早多半是凯尔特语，不是拉丁语 pars。一块。"),
    ("pilot", "意大利语 pilota", "希腊语 pedon「舵柄」。领航员原是掌舵的人。"),
    ("pin", "晚期拉丁语 pinna「尖、羽」", "古英语借入。别针。"),
    ("pipe", "拉丁语 pipare「啾啾地叫」", "管子像发声的哨。古英语借入。"),
    ("pity", "古法语 pite", "拉丁语 pietas「尽责、慈」。怜悯从这里来。pious 是同一族。"),
    ("place", "古法语 place", "拉丁语 platea，希腊语 plateia「宽街」。地方。"),
    ("plain", "古法语 plain", "拉丁语 planus「平的」。明白和平坦是同一个平。"),
    ("plan", "法语 plan", "拉丁语 planus「平的」。平面图，后来是计划。"),
    ("plane", "拉丁语 planus「平的」", "平面、刨子、飞机的翼面，都是平的那一块。"),
    ("planning", "法语 plan，拉丁语 planus", "把事情摊成一张平面图。"),
    ("plant", "拉丁语 planta", "幼苗，也指脚底。工厂的 plant 是装上去的一套设备，同一拉丁词后来的用法。古英语已借入幼苗这一义。"),
    ("plastic", "希腊语 plastikos", "plassein 是塑造。塑料是可以塑的。"),
    ("platform", "法语 plateforme", "plat「平的」来自希腊语 platys，forme 来自拉丁语 forma。平台是一块平的形。"),
    ("pleasant", "古法语 plaisant", "拉丁语 placere「使高兴」。"),
    ("please", "古法语 plaisir", "拉丁语 placere「使高兴」。请人时说 please，原是「如果你高兴」。"),
    ("pleasure", "古法语 plaisir", "拉丁语 placere。高兴。"),
    ("plenty", "古法语 plente", "拉丁语 plenitas，plenus「满」。充足。"),
    ("plug", "中古荷兰语 plugge", "日耳曼词。塞子。"),
    ("plus", "拉丁语 plus「更多」", "加。"),
    ("pocket", "盎格鲁诺曼语 poket", "日耳曼语 poke「袋子」的小词。口袋是小袋。"),
    ("point", "古法语 point", "拉丁语 punctum，pungere「刺」。点是刺出来的。"),
    ("police", "法语 police", "拉丁语 politia，希腊语 polis「城」。警察制度原是治城的办法。"),
    ("polite", "拉丁语 politus「打磨过的」", "polire 是打磨。有礼貌就是磨光了棱角。"),
    ("politician", "希腊语 polis「城」", "从事城邦事务的人。"),
    ("pollution", "拉丁语 polluere「弄脏」", "污染。"),
    ("poor", "古法语 povre", "拉丁语 pauper。贫穷的。"),
    ("port", "拉丁语有两个近邻", "portus 是港，porta 是门。港口和口岸都从这里来。"),
    ("positive", "拉丁语 positivus", "ponere 是放下。肯定的，就是已经放下、可以算数的。"),
    ("possibility", "拉丁语 possibilis", "posse 是能够。可能。"),
    ("possible", "拉丁语 possibilis", "能够发生的。"),
    ("post", "拉丁语 posita「被放下的」", "驿站是放下马和信的地方。邮件、岗位都从这座驿站来。拉丁语 post「在后」是另一个词。"),
    ("post office", "post 加上 office", "post 来自拉丁语「被放下的驿站」。office 来自拉丁语 officium「职责」。邮局。"),
    ("postage", "post 加上 -age", "post 是驿站。邮资是使用这座驿站的费用。"),
    ("postcard", "post 加上 card", "post 是驿站。card 来自希腊语、拉丁语的纸草。明信片是经邮驿送的卡片。"),
    ("postcode", "post 加上 code", "post 是驿站。code 来自拉丁语 codex「书、法典」。邮政编码是邮局的代码。"),
    ("poster", "post「张贴」", "来自拉丁语 posita。海报是贴出来的。"),
    ("postman", "post 加上 man", "post 是拉丁语的驿站。man 是日耳曼词。邮递员走驿站的人。"),
    ("potential", "拉丁语 potentialis", "posse 是能够。潜在就是还没使出来的能力。"),
    ("pound", "拉丁语 pondo「按重量」", "古英语 pund 借入。英镑和磅都是这个重量。"),
    ("power", "古法语 povoir", "拉丁语 posse「能够」。权力就是能够。"),
    ("practice", "拉丁语 practica", "希腊语 praktikos，prassein 是做。实践。"),
    ("practise", "拉丁语 practicare", "希腊语 prassein「做」。练习就是反复做。"),
    ("praise", "古法语 preisier", "拉丁语 pretium「价钱」。称赞原是给一个高价。"),
    ("precious", "拉丁语 pretiosus", "pretium 是价钱。珍贵就是价高。"),
    ("predict", "拉丁语 praedicere", "dicere 是说。预言就是预先说。"),
    ("prediction", "拉丁语 praedicere", "预先说出的话。"),
    ("prefer", "拉丁语 praeferre", "ferre 是携带。更喜欢就是把它带到前面。"),
    ("preference", "拉丁语 praeferre", "被带到前面的选择。"),
    ("preliminary", "拉丁语 prae「在前」加上 limen「门槛」", "预备就是还在门槛前。"),
    ("premises", "拉丁语 praemissum「前面说过的」", "契约里先写明的房屋，后来就指房产本身。"),
    ("preparation", "拉丁语 praeparare", "parare 是准备。预先准备好的那些。"),
    ("prepare", "拉丁语 praeparare", "预先安排。"),
    ("present", "拉丁语 praesens", "praeesse 是在前面。在场。作礼物时，来自 praesentare「放到面前」。"),
    ("presentation", "拉丁语 praesentare「放到面前」", "演示就是放到众人面前。"),
    ("press", "拉丁语 pressare", "premere 是压。压、新闻界，都是这个压。"),
    ("previous", "拉丁语 praevius", "via 是路。先前的就是路上更前面的。"),
    ("price", "古法语 pris", "拉丁语 pretium「价钱」。"),
    ("price list", "price 加上 list", "price 来自拉丁语 pretium。价目单。"),
    ("primary", "拉丁语 primarius", "primus 是第一。最初的。"),
    ("prime minister", "prime 加上 minister", "prime 来自拉丁语 primus「第一」。minister 是拉丁语「服务者」。首相是第一大臣。"),
    ("printer", "print 加上指人的后缀", "print 来自拉丁语 premere「压」。打印机或印刷工把字压出来。"),
    ("printout", "print 加上 out", "print 来自拉丁语 premere。out 是日耳曼词。打印件是压出来的那一页。"),
    ("priority", "拉丁语 prior「更前面的」", "优先就是排在前面。"),
    ("prison", "古法语 prison", "拉丁语 prensio，prehendere「抓住」。监狱是把人抓住的地方。"),
    ("private", "拉丁语 privatus", "privare 是分到私人一边。私下的。"),
    ("prize", "古法语 pris", "拉丁语 pretium「价钱」。奖赏是一个价。price 是同一个词分出来的拼法。"),
    ("probable", "拉丁语 probabilis", "probare 是检验。很可能，就是经得起估计的。"),
    ("problem", "希腊语 problema", "proballein 是扔到前面。问题就是扔到你面前的一道。"),
    ("procedure", "法语 procédure", "拉丁语 procedere「向前走」。程序就是往前走的步骤。"),
    ("process", "拉丁语 processus", "procedere 是向前走。过程。"),
    ("produce", "拉丁语 producere", "ducere 是带领。生产就是引出来。"),
    ("product", "拉丁语 productum", "被引出来的产物。"),
    ("production", "拉丁语 productio", "把产物引出来。"),
    ("productive", "拉丁语 producere", "能引出产物的。"),
    ("productivity", "拉丁语 producere", "引出产物的能力。"),
    ("profession", "拉丁语 professio", "profiteri 是当众声明。专业原是你公开声明从事的事。"),
    ("professional", "拉丁语 professio", "以公开声明的那一门为业的。"),
    ("professor", "拉丁语 professor", "profiteri 是公开讲明。教授是公开讲这一门的人。"),
    ("profit", "古法语 profit", "拉丁语 profectus，proficere「向前做成」。利润是做成之后多出来的。"),
    ("profitability", "拉丁语 proficere「做成、有进展」", "能不能做出利润。"),
    ("profitable", "拉丁语 proficere", "能做出盈余的。"),
    ("promise", "拉丁语 promissum", "promittere 是向前送出。诺言是预先送出的话。"),
    ("promotion", "拉丁语 promovere「向前移动」", "晋升和促销都是往前推。"),
    ("promotional", "拉丁语 promovere", "用来往前推的。"),
    ("prompt", "拉丁语 promptus", "promere 是拿到前面。及时，就是已经拿到手边。"),
    ("proof", "古法语 prueve", "拉丁语 probare「检验」。证据。"),
    ("proper", "古法语 propre", "拉丁语 proprius「自己的」。恰当就是属于它自己的那个样子。"),
    ("property", "拉丁语 proprietas", "proprius 是自己的。财产。"),
    ("proportion", "拉丁语 proportio", "pro 加上 portio「一份」。比例就是各份之间的关系。"),
    ("protect", "拉丁语 protegere", "tegere 是覆盖。保护就是遮住。"),
    ("protection", "拉丁语 protegere", "遮住。"),
    ("proud", "古法语 prod", "晚期拉丁语 prodesse「有益」。骄傲原和有本事、有好处有关，古英语借入了这个法语词。"),
    ("public", "拉丁语 publicus", "populus 是人民。公共的。"),
    ("public holiday", "public 加上 holiday", "public 来自拉丁语 populus。holiday 是 holy 加 day，两个日耳曼词。公共假日是大家都停的圣日，后来不限于圣日。"),
    ("public limited company", "public、limited、company", "public 来自拉丁语 populus。limited 来自拉丁语 limes「界」。company 来自拉丁语 companio「一起吃饭的人」。股份公开、责任有限的公司。"),
    ("public opinion", "public 加上 opinion", "两者都是拉丁语。公众的看法。"),
    ("public relations", "public 加上 relation", "public 来自 populus。relation 来自 referre「带回」。公共关系是和公众之间来回的那些联系。"),
    ("publicise", "拉丁语 publicus", "使它变成公众的。"),
    ("publicity", "拉丁语 publicus", "公众看得见的程度。"),
    ("publish", "拉丁语 publicare", "使它成为公众的。出版。"),
    ("punctual", "拉丁语 punctualis", "punctum 是点。准时就是卡在点上。"),
    ("punish", "古法语 punir", "拉丁语 punire，poena 是惩罚。"),
    ("pupil", "拉丁语 pupillus「受监护的孩子」", "学生是被照看的孩子。瞳孔 pupilla 是「小玩偶」，因为眼里能看见小人影，是同一个拉丁家族。"),
    ("pure", "拉丁语 purus「干净的」", "纯。"),
    ("qualification", "拉丁语 qualis「什么样」加上 facere", "资格就是证明你是哪一种、做得到。"),
    ("qualify", "拉丁语 qualis", "使它达到某一种标准。"),
    ("quality", "拉丁语 qualitas", "qualis 是「什么样」。质量就是它是什么样。"),
    ("quality control", "quality 加上 control", "quality 来自拉丁语 qualis。control 来自拉丁语 contrarotulus「对照的卷册」。质量控制就是拿质量去对册子。"),
    ("quantity", "拉丁语 quantitas", "quantus 是「多少」。数量。"),
    ("quarrel", "古法语 querele", "拉丁语 querela「抱怨」。争吵。"),
    ("query", "拉丁语 quaerere「问」", "问一句。"),
    ("questionnaire", "法语，拉丁语 quaerere「问」", "问卷就是一串问。"),
    ("queue", "法语 queue「尾巴」", "拉丁语 cauda。排队就是一条尾巴。"),
    ("quiet", "拉丁语 quietus", "quies 是休息。安静。"),
    ("quite", "拉丁语 quietus「自由、清楚」", "经中古英语。完全、相当，原是「清清楚楚地」。"),
    ("radio", "拉丁语 radius「射线、轮辐」", "无线电取的是射线这一义。"),
    ("range", "古法语 rang", "日耳曼语 *hringaz「环、列」。范围是排成的一列。"),
    ("rank", "古法语 ranc", "和 range 一样，来自日耳曼语「列、环」。等级是排出来的位置。"),
    ("rapid", "拉丁语 rapidus", "rapere 是抢走。快得像被抢走。"),
    ("rare", "拉丁语 rarus「稀疏的」", "稀少。"),
    ("rate", "中世纪拉丁语 rata", "pro rata 是按算定的份额。reri 是计算。比率。"),
    ("real", "拉丁语 realis", "res 是事物。真实的就是像一件实在的东西。"),
    ("realise", "法语 réaliser", "拉丁语 res「事物」。实现就是使它成为一件实在的事。"),
    ("reason", "古法语 raison", "拉丁语 ratio，reri 是计算、思考。理由。"),
    ("receiver", "拉丁语 recipere「接住」", "capere 是拿。接收的人，或听筒。"),
    ("recent", "拉丁语 recens「新鲜的」", "近来的。"),
    ("reception", "拉丁语 receptio", "recipere 是接住。接待、接收。"),
    ("receptionist", "拉丁语 recipere「接住」", "在入口把人接住的人。"),
    ("recognise", "拉丁语 recognoscere", "cognoscere 是知道。认出就是再次知道。"),
    ("recommend", "中世纪拉丁语 recommendare", "commendare 是托付。推荐就是把它托到别人面前。"),
    ("recommendation", "拉丁语 recommendare", "托到别人面前的那句话。"),
    ("record", "拉丁语 recordari「记在心里」", "cor 是心。记录就是放回心里，后来才是写下。"),
    ("recorder", "拉丁语 recordari", "用来记录的器具。"),
    ("recover", "拉丁语 recuperare「取回」", "恢复就是再拿到。"),
    ("recovery", "拉丁语 recuperare", "取回、恢复。"),
    ("recruit", "法语 recruter", "拉丁语 recrescere「重新长出」。招募是让人手再长出来。"),
    ("reduction", "拉丁语 reducere", "ducere 是带领。减少就是往回带。"),
    ("redundant", "拉丁语 redundare「溢回来」", "unda 是波浪。多余就是漫出来的。"),
    ("ref", "reference 的缩短", "拉丁语 referre「带回去对照」。"),
    ("refer", "拉丁语 referre", "ferre 是携带。把问题带回去请人看。"),
    ("reference", "拉丁语 referre「带回去」", "用来对照的材料。"),
    ("refrigerator", "拉丁语 frigus「冷」", "造冷的柜子。fridge 是缩短。"),
    ("refund", "拉丁语 refundere", "fundere 是倾倒。退款就是把钱倒回去。"),
    ("refuse", "古法语 refuser", "拉丁语 recusare，和 causa 有关。拒绝。"),
    ("regard", "法语 regarder", "garder 来自日耳曼语 ward「看」。regard 是再看、重视。"),
    ("region", "拉丁语 regio", "regere 是引导、划界。地区是划出来的一片。"),
    ("regional", "拉丁语 regio", "属于这一地区的。"),
    ("register", "中世纪拉丁语 regesta", "regerere 是记回去。登记册。"),
    ("registration", "中世纪拉丁语 regesta", "写进登记册。"),
    ("regret", "古法语 regreter", "和日耳曼词 greet 同族，re- 是拉丁前缀。遗憾是对着这件事再招呼一次。它不是拉丁语的 dolere。"),
    ("regular", "拉丁语 regularis", "regula 是尺。有规则就是按尺。"),
    ("reject", "拉丁语 reicere", "jacere 是扔。拒绝就是扔回去。"),
    ("rejection", "拉丁语 reicere", "扔回去。"),
    ("relation", "拉丁语 relatio", "referre 是带回。关系就是彼此带回的联系。"),
    ("relax", "拉丁语 relaxare", "laxus 是松的。放松就是再松开。"),
    ("relevant", "拉丁语 relevare「举起」", "levis 是轻。相关的，原是能把论点托起来的。"),
    ("reliability", "rely 加上 -able", "rely 来自拉丁语 religare「绑住」。可靠就是绑得住。"),
    ("reliable", "拉丁语 religare「绑住」", "可以依靠的。"),
    ("relief", "古法语 relief", "拉丁语 relevare「再举起」。缓解就是把重的托起来。"),
    ("rely", "拉丁语 religare「绑住」", "依靠就是把自己绑在上面。"),
    ("remain", "拉丁语 remanere", "manere 是留下。留下。"),
    ("remember", "拉丁语 rememorari", "memor 是记住。再记起。"),
    ("remove", "拉丁语 removere", "movere 是移动。移走。"),
    ("renew", "re- 加上 new", "re- 是拉丁语「再」。new 是日耳曼词。更新就是再变新。"),
    ("repair", "拉丁语 reparare", "parare 是准备。修理就是重新备好。"),
    ("repeat", "拉丁语 repetere", "petere 是寻求。重复就是再来一次。"),
    ("replace", "re- 加上 place", "place 来自希腊语 plateia、拉丁语 platea。替换就是重新放到那个位置。"),
    ("represent", "拉丁语 repraesentare", "praesens 是在场。代表就是使它再次在场。"),
    ("representative", "拉丁语 repraesentare", "使别人再次在场的人。"),
    ("reputation", "拉丁语 reputatio", "reputare 是再想一遍。名声是别人反复想到你的方式。"),
    ("research", "古法语 recercher", "cercher 来自拉丁语 circare「转着找」。研究就是再仔细找一遍。"),
    ("reservation", "拉丁语 reservare", "servare 是守住。预订就是替你守住。"),
    ("reserve", "拉丁语 reservare「留着」", "储备、预订。"),
    ("resident", "拉丁语 residere", "sedere 是坐。居民是坐下来的人。"),
    ("residential", "拉丁语 residere", "用来住的。"),
    ("resign", "拉丁语 resignare", "signum 是记号。辞职原是解开封印、把职交回。"),
    ("resignation", "拉丁语 resignare", "把记号交回去。"),
    ("resources", "拉丁语 resurgere「再升起」", "资源是可以再调动起来的来源。"),
    ("response", "拉丁语 respondere", "spondere 是承诺。回应就是应上去。"),
    ("responsibility", "拉丁语 respondere「回应」", "责任就是你必须应的那一份。"),
    ("restaurant", "法语 restaurer", "拉丁语 restaurare「修复」。餐馆原是让人恢复体力的地方。"),
    ("result", "拉丁语 resultare「跳回来」", "salire 是跳。结果是反弹回来的那个。"),
    ("retail", "古法语 retailler「再切开」", "tail 是切。零售是切成小份卖。"),
    ("retail outlet", "retail 加上 outlet", "retail 来自古法语「切成小份」。outlet 是 out 加 let，日耳曼词，出口。零售店是把小份放出去的口。"),
    ("retail price", "retail 加上 price", "retail 是切成小份。price 来自拉丁语 pretium。零售价。"),
    ("retire", "法语 retirer", "tirer 是拉。退休就是抽身回去。tirer 再早不完全确定，这里记到法语。"),
    ("return", "古法语 retourner", "拉丁语 re- 加上 tornare「车削、转动」，希腊语 tornos 是车床。返回就是转回来。"),
    ("reward", "盎格鲁诺曼语 rewarder", "日耳曼语 ward「看、看守」。报酬是看在做得好而给的。它不是拉丁语的 prize。"),
    ("risk", "意大利语 risco，法语 risque", "再早各家不一致，有人说到海上的礁石，没有定论。这里只记到意大利语，不往下写死。"),
    ("river", "古法语 riviere", "拉丁语 riparia，ripa 是河岸。河流原是两岸之间。"),
    ("roll", "古法语 rolle", "拉丁语 rotulus「小轮、卷」。名册和滚动都从卷轴来。"),
    ("round", "古法语 rond", "拉丁语 rotundus「圆的」，rota 是轮。圆的。"),
    ("roundabout", "round 加上 about", "round 来自拉丁语 rotundus。about 是日耳曼词。环岛是绕着走的路口。"),
    ("routine", "法语 routine", "route 来自拉丁语 rupta via「打开的路」。例行就是天天走的那条路。"),
    ("royal", "古法语 roial", "拉丁语 regalis，rex 是王。王室的。"),
    ("rubber", "来自 rub「擦」", "rub 是日耳曼词，来源不算更早。橡胶是用来擦的，这个英语名从用途来，不是拉丁语。"),
    ("rubbish", "可能来自 rubble 一类", "来源没有把握，不写成定论。"),
    ("rule", "古法语 riule", "拉丁语 regula「尺」。规则就是尺子。"),
    ("safe", "古法语 sauf", "拉丁语 salvus「完好的」。安全。"),
    ("safety", "拉丁语 salvus「完好的」", "安全。safe 的名词。"),
    ("satisfaction", "拉丁语 satisfacere", "satis 是足够，facere 是做。满意就是做得足够。"),
    ("satisfactory", "拉丁语 satisfacere", "做得足够的。"),
    ("satisfied", "拉丁语 satisfacere", "已经觉得足够。"),
    ("scene", "拉丁语 scaena", "希腊语 skene「棚、舞台」。一场。"),
    ("schedule", "拉丁语 schedula「小纸条」", "希腊语 skhede。时间表原是一条纸。"),
    ("school", "拉丁语 schola", "希腊语 skhole「闲暇、讲学」。古英语借入。学校不是日耳曼本族词。"),
    ("science", "拉丁语 scientia", "scire 是知道。科学是知道的系统。"),
    ("scissors", "古法语 cisoires", "拉丁语 caedere「切」。剪刀。"),
    ("screen", "古北法语 escren", "日耳曼语里「遮挡」的词，经法语。屏幕是一块挡板。"),
    ("search", "古法语 cerchier", "拉丁语 circare「转着走、四处找」。"),
    ("season", "古法语 seson", "拉丁语 satio「播种」，serere 是种。季节原是播种的时节。"),
    ("second", "拉丁语 secundus「跟着的」", "sequi 是跟随。第二，以及秒这个再分出来的单位。"),
    ("second-hand/second hand", "second 加上 hand", "second 来自拉丁语 secundus「跟着的」。hand 是日耳曼词。二手就是经过第二只手。"),
    ("secondary", "拉丁语 secundarius", "第二位的。"),
    ("secret", "拉丁语 secretus", "secernere 是分开。秘密就是被分到一边、不给人看的。"),
    ("secretarial", "拉丁语 secretarius", "原是掌管秘密文件的人。秘书。"),
    ("section", "拉丁语 sectio", "secare 是切。一节就是切下来的一段。"),
    ("secure", "拉丁语 securus", "se-「离开」加上 cura「操心」。安全就是不必操心。"),
    ("select", "拉丁语 seligere", "legere 是采集。挑选就是拣出来。"),
    ("selection", "拉丁语 seligere", "拣出来的那些。"),
    ("senior", "拉丁语 senior", "senex 是年老的。年长的、级别更高的。"),
    ("sensible", "拉丁语 sensibilis", "sentire 是感觉。明智就是感觉得到分寸。"),
    ("sentence", "拉丁语 sententia", "sentire 是判断。一个句子是一句完整的判断。"),
    ("separate", "拉丁语 separare", "se- 加上 parare。分开到各自一边。"),
    ("series", "拉丁语 series", "serere 是串起来。一系列。"),
    ("serious", "拉丁语 serius「沉重的、认真的」", "严肃。"),
    ("service", "拉丁语 servitium", "servus 是仆人。服务。"),
    ("set", "古英语 settan", "日耳曼词，使坐下、安放。"),
    ("several", "拉丁语 separalis", "separate 是分开。几个就是分开的若干个。"),
    ("sex", "拉丁语 sexus", "性别。"),
    ("shall", "古英语 sculan", "日耳曼词。应当、将要。"),
    ("share", "古英语 scearu「切开的一份」", "日耳曼词。股份就是切出来的一份。"),
    ("shelf", "古英语 scylfe", "日耳曼词。架子。"),
    ("shift", "古英语 sciftan「安排、分开」", "日耳曼词。轮班就是把时间分开安排。"),
    ("ship", "古英语 scip", "日耳曼词。船。"),
    ("shipping", "ship 加上 -ing", "ship 是日耳曼词。装运。"),
    ("shock", "法语 choc", "多半是拟声。惊吓就是这一撞。它不是拉丁语。"),
    ("shop", "古英语 sceoppa「棚」", "日耳曼词。商店原是一个棚子。"),
    ("short", "古英语 sceort", "日耳曼词。短。"),
    ("shortage", "short 加上法语名词后缀 -age", "short 是日耳曼词。短缺是短了的那一截，后缀是后来从法语来的。"),
    ("should", "shall 的过去式", "古英语 sculan。日耳曼词。"),
    ("sign", "拉丁语 signum「记号」", "标志、签名、迹象。"),
    ("signal", "拉丁语 signalis", "signum 是记号。信号。"),
    ("signature", "拉丁语 signare", "signum 是记号。签名就是留下自己的记号。"),
    ("significant", "拉丁语 significare", "signum 加上 facere。有意义就是这个记号做成了分量。"),
    ("silence", "拉丁语 silentium", "silere 是不出声。"),
    ("silent", "拉丁语 silens", "不出声的。"),
    ("silk", "拉丁语 sericum", "Seres 是罗马人对产丝之地的称呼。古英语借入。丝绸不是日耳曼本族词。"),
    ("similar", "拉丁语 similis「相像」", "相似。"),
    ("simple", "拉丁语 simplus 或 simplex", "一折，不是复杂的多层。简单。"),
    ("sincerely", "拉丁语 sincerus「干净、不掺」", "真诚地。"),
    ("single", "拉丁语 singulus「一个一个的」", "单一。"),
    ("sir", "sire 的弱化", "sire 来自拉丁语 senior「更年长的」。先生。"),
    ("site", "拉丁语 situs「位置」", "地点。"),
    ("situate", "拉丁语 situs", "使它位于。"),
    ("situation", "拉丁语 situs「位置」", "处境就是它所在的位置。"),
    ("size", "古法语 sise", "拉丁语 assidere「坐下来评定」。尺寸是评定出来的。"),
    ("social", "拉丁语 socialis", "socius 是同伴。社会的。"),
    ("society", "拉丁语 societas", "同伴结成的群体。"),
    ("software", "soft 加上 ware", "两个都是日耳曼词。软件是软的那一套货。hard 对 hardware，也是日耳曼词。"),
    ("soldier", "古法语 soldier", "拉丁语 solidus，一种用来发饷的金币。士兵原是拿这份钱的人。"),
    ("sole", "拉丁语 solus「单独」", "唯一的。鞋底 sole 是拉丁语 solea，另一词。商务里的 sole agent 用的是「单独」。"),
    ("solid", "拉丁语 solidus「结实的」", "固体、稳固。"),
    ("sort", "拉丁语 sors「签、命运」", "经古法语。种类原是抽到的那一签。"),
    ("source", "古法语 sourse", "拉丁语 surgere「升起来」。来源就是东西从那里冒出来。"),
    ("space", "拉丁语 spatium「延伸、空地」", "空间。"),
    ("spare", "古英语 spær", "日耳曼词。 spare 是省下、多余出来的。"),
    ("special", "拉丁语 specialis", "species 是种类。特别的就是这一种。"),
    ("specialise", "拉丁语 specialis", "收到这一种上。"),
    ("specialist", "拉丁语 specialis", "专这一门的人。"),
    ("speciality", "拉丁语 specialitas", "专长的那一种。"),
    ("speech", "古英语 spræc", "日耳曼词，和 speak 同族。"),
    ("speed", "古英语 sped「成功、迅速」", "日耳曼词。"),
    ("spirit", "拉丁语 spiritus", "spirare 是呼吸。精神原是气息。"),
    ("sport(s)", "disport 的缩短", "古法语 desporter，拉丁语 portare「带走」。运动原是把人从工作里带走。"),
    ("square", "古法语 esquare", "拉丁语 ex 加上 quadra，quattuor 是四。正方形。"),
    ("staff", "古英语 stæf「棍」", "日耳曼词。手杖，后来是班子，因为一班人像一支杖。"),
    ("standard", "古法语 estandart", "核心是日耳曼词 stand。军旗立在那里，后来才是拿来对照的标准。"),
    ("state", "拉丁语 status", "stare 是站。状态、国家，都是站成的样子。"),
    ("station", "拉丁语 statio", "stare 是站。车站是站住的地方。"),
    ("stationery", "拉丁语 stationarius", "station 是固定的摊。文具商原是有固定铺位的人，后来专指纸笔。"),
    ("statistics", "德语 Statistik", "拉丁语 status「状态」。统计学原是关于国家状况的数字。"),
    ("steady", "古英语 stede「地方」", "日耳曼词。稳就是停在地方上。"),
    ("stick", "古英语 sticca「棍」", "日耳曼词。"),
    ("stop", "古英语 stoppian", "一般认为来自通俗拉丁语 *stuppare「用麻絮堵住」，拉丁语 stuppa 是麻絮。它进英语很早，但是借词，不是和 stand 一样的本族词。"),
    ("store", "古法语 estorer", "拉丁语 instaurare「重新备起」。商店和储存都是把货备起来。"),
    ("storeroom", "store 加上 room", "store 来自拉丁语 instaurare。room 是日耳曼词。储藏室。"),
    ("storey", "和 story 的拼写撞在一起", "楼层这一义来源没有完全定论，可能和拉丁语 historia 的一义或古法语 estoree 有关。不把它写成已经定案的日耳曼词。"),
    ("story", "拉丁语 historia", "经盎格鲁法语 estorie。故事原是一段探究过的叙述。楼层 storey 是另一个词。"),
    ("straight", "古英语 streht", "stretch 的古过去分词。日耳曼词。直。"),
    ("strange", "古法语 estrange", "拉丁语 extraneus「外面的」。陌生就是从外面来的。"),
    ("stranger", "拉丁语 extraneus「外面的」", "外人。"),
    ("street", "拉丁语 strata「铺好的路」", "古英语 stræt 借入。街道不是和 road 一样的本族词。road 才是日耳曼词。"),
    ("stress", "古法语 estresse 或拉丁语 strictus", "stringere 是拉紧。压力就是被拉紧。"),
    ("strict", "拉丁语 strictus", "stringere 是拉紧。严格就是拉紧。"),
    ("structure", "拉丁语 structura", "struere 是搭建。结构。"),
    ("student", "拉丁语 studere「投入地学」", "学生。"),
    ("studies", "拉丁语 studium", "投入的学问。"),
    ("study", "拉丁语 studium「热心、学习」", "studere 是投入。学习。"),
    ("stupid", "拉丁语 stupidus", "stupere 是发呆。笨拙原是愣住。"),
    ("style", "拉丁语 stilus「尖笔」", "文体原是笔写出来的样子。"),
    ("subject", "拉丁语 subjectus", "sub- 加上 jacere「扔到下面」。科目和臣民都是被放在下面的。"),
    ("succeed", "拉丁语 succedere", "sub- 加上 cedere「走」。成功原是跟着走上去，也指继承。"),
    ("success", "拉丁语 successus", "走上去的结果。"),
    ("sudden", "古法语 sodain", "拉丁语 subitaneus，subire「悄悄走到下面」。突然。"),
    ("suggest", "拉丁语 suggerere", "sub- 加上 gerere「从下面递上来」。建议就是递上来。"),
    ("suggestion", "拉丁语 suggerere", "递上来的那个主意。"),
    ("suit", "古法语 suite", "拉丁语 sequi「跟随」。一套衣服是相随的几件，诉讼是追随的案件。"),
    ("suitable", "拉丁语 sequi「跟随」", "跟得上需要的。"),
    ("suitcase", "suit 加上 case", "suit 来自拉丁语 sequi。case 来自拉丁语 capsa「盒子」。手提箱是装衣着的盒子。"),
    ("sum", "拉丁语 summa「最高的一笔」", "summus 是最高。总额是加到顶的数。"),
    ("summary", "拉丁语 summa", "把最高的要点收拢。"),
    ("supermarket", "拉丁语 super「在上」加上 market", "market 来自拉丁语 mercatus。超市是更大的市场。"),
    ("supervise", "拉丁语 supervidere", "super 加上 videre「从上面看」。监督。"),
    ("supervision", "拉丁语 supervidere", "从上面看着。"),
    ("supply", "拉丁语 supplere「填满」", "sub- 加上 plere。供应就是把缺的填上。"),
    ("suppose", "拉丁语 supponere", "sub- 加上 ponere「放在下面」。假设就是先放到下面垫着。"),
    ("sure", "古法语 sur", "拉丁语 securus「不必操心」。确定就是可以放心。"),
    ("surface", "法语 surface", "拉丁语 superficies，super「在上」加上 facies「脸」。表面。"),
    ("surprise", "古法语 surprise", "拉丁语 super 加上 prehendere「从上面抓住」。吃惊就是冷不防被抓住。"),
    ("survey", "古法语 surveier", "拉丁语 supervidere「从上面看」。调查就是看一遍。"),
    ("switch", "可能来自低地德语", "日耳曼语里的一根软枝，后来是甩动、转换。它不是拉丁语。再早的细节不多，这里只记日耳曼这一层。"),
    ("system", "希腊语 systema", "syn「一起」加上 histanai「使站立」。系统就是站成一套。"),
    ("table", "古法语 table", "拉丁语 tabula「板」。桌子和表格都是一块板。"),
    ("target", "古法语 targette「小盾」", "日耳曼语 targa。靶子原是盾。"),
    ("task", "古法语 tasque 一类", "拉丁语 taxa，taxare「估价、派定」。任务是派给你的那一份活。"),
    ("taste", "古法语 taster", "拉丁语 taxare「触摸、估价」。味道原是尝一尝、摸一摸。"),
    ("tax", "拉丁语 taxare「估价、触碰」", "税是评定之后要交的。"),
    ("taxation", "拉丁语 taxare", "征税。"),
    ("taxpayer", "tax 加上 payer", "tax 来自拉丁语 taxare。pay 来自拉丁语 pacare「使满意」，不是日耳曼词。纳税人。"),
    ("tea", "闽南话 te", "经马来语、荷兰语进入英语。另一路汉语 cha 给了 chai。茶不是欧洲词。"),
    ("technical", "希腊语 tekhnikos", "tekhne 是技艺。技术的。"),
    ("technician", "希腊语 tekhne「技艺」", "掌握这门技艺的人。"),
    ("technological", "希腊语 tekhne 加上 logos", "关于技艺之学的。"),
    ("technology", "希腊语 tekhnologia", "tekhne 是技艺，logos 是学问。"),
    ("telephone", "希腊语 tele「远」加上 phone「声音」", "电话。"),
    ("television", "希腊语 tele「远」加上拉丁语 visio", "videre 是看见。电视是看见远处。"),
    ("temperature", "拉丁语 temperatura", "temperare 是调配。温度原是冷热调成的状态。"),
    ("temporary", "拉丁语 temporarius", "tempus 是时间。临时就是只占一段时间。"),
    ("term", "拉丁语 terminus「界石、尽头」", "学期、术语、条款，都是被定了边界的一段。"),
    ("terminal", "拉丁语 terminalis", "terminus 是尽头。终点站，或终端。"),
    ("terrible", "拉丁语 terribilis", "terrere 是惊吓。可怕的。"),
    ("test", "拉丁语 testum「陶罐」", "试金是把金属放进罐里炼。考试和测试从这里来。"),
    ("text", "拉丁语 textus「织出来的」", "texere 是织。正文是织成的一段话。"),
    ("textile", "拉丁语 textilis", "texere 是织。纺织品。"),
    ("theatre", "希腊语 theatron", "theasthai 是观看。剧场是观看的地方。"),
    ("theory", "希腊语 theoria「观看、沉思」", "理论原是仔细看见。"),
    ("thermometer", "希腊语 therme「热」加上 metron「量」", "温度计。"),
    ("ticket", "法语 étiquette 的缩短", "étiquette 来自日耳曼语「把条子贴上」。票是贴出或写出的条子。礼节的 etiquette 是同一个「贴出来的规矩」。"),
    ("tidy", "tide", "古英语 tid「时节」。东西收拾到合适的时候，就是整齐。日耳曼词。"),
    ("title", "拉丁语 titulus「题名、荣誉」", "标题。"),
    ("toilet", "法语 toilette", "toile「布」的小词，拉丁语 tela。梳妆原是一块小布，后来是盥洗。"),
    ("ton(ne)", "古英语 tunne「大桶」", "日耳曼词。吨后来从桶的装载变成重量。法语 tonne 是同一条。"),
    ("topic", "希腊语 topos「地方」", "ta topika 是关于场所的论点。题目就是谈论所在的那个点。"),
    ("total", "拉丁语 totus「整个」", "总计就是整个。"),
    ("touch", "古法语 touchier", "通俗拉丁语 toccare，是拟声的敲一下。"),
    ("tour", "古法语 tor", "拉丁语 tornus，希腊语 tornos「车床、圆规」。旅行原是转一圈。"),
    ("tourist", "古法语 tor，希腊语 tornos", "转一圈的人。"),
    ("toward(s)", "古英语 toweard", "to 加上 -ward「朝向」。日耳曼词。"),
    ("tower", "古法语 tour", "拉丁语 turris。塔。"),
    ("trade", "中古低地德语 trade「路径」", "买卖是沿着常走的那条路。它是日耳曼词，不是拉丁语。"),
    ("trade union", "trade 加上 union", "trade 是低地德语「路径、行业」。union 来自拉丁语 unus「一」。工会是一个行业合成的一体。"),
    ("tradition", "拉丁语 traditio", "tradere 是交过去。传统就是交下来的。"),
    ("traditional", "拉丁语 tradere「交过去」", "照交下来的样子。"),
    ("traffic", "意大利语 traffico，法语 trafic", "往来、贸易。再早各家不一致，这里只记到意大利语。"),
    ("traffic jam", "traffic 加上 jam", "traffic 来自意大利语。jam 是塞紧，来源晚近、可能是拟声。交通堵塞。"),
    ("traffic light(s)", "traffic 加上 light", "traffic 来自意大利语。light 是日耳曼词。红绿灯。"),
    ("train", "古法语 trainer", "拉丁语 trahere「拉」。火车是被拉的一串，训练是把人往前拉。"),
    ("trainee", "train 加上 -ee", "train 来自拉丁语 trahere「拉」。受训的人是被拉着走的人。"),
    ("translate", "拉丁语 translatus", "transferre 是 trans-「越过」加上 ferre「携带」。翻译就是把意思带过另一种语言。"),
    ("translation", "拉丁语 transferre", "带过去的那个文本。"),
    ("transport", "拉丁语 transportare", "trans- 加上 portare「运过」。"),
    ("travel", "travail 的一支", "古法语 travailler，和拉丁语 trepalium「三根桩的刑具」有关。旅行原是一番辛苦。"),
    ("travel agent", "travel 加上 agent", "travel 来自法语的辛苦路程。agent 来自拉丁语 agere「去做」。旅行代理替你把路程做成。"),
    ("treat", "古法语 traitier", "拉丁语 tractare，trahere「拉着处理」。对待、请客、治疗都是处理。"),
    ("trial", "盎格鲁法语 trial", "try 来自古法语 trier「拣选」。审判就是拣清楚。trier 再早没有定论。"),
    ("triangle", "拉丁语 triangulus", "tres「三」加上 angulus「角」。"),
    ("trip", "中古荷兰语 trippen「小跳」一类", "日耳曼词。出行。它不是拉丁语。"),
    ("trouble", "古法语 trubler", "拉丁语 turbulare，turba 是混乱。麻烦就是搅浑。"),
    ("truck", "可能和希腊语 trokhos「轮子」有关", "这条没有定死，所以不写成已经核实的词源。"),
    ("try", "古法语 trier「拣选」", "再早没有把握。试用、尝试，是去拣一拣。"),
    ("tube", "拉丁语 tubus「管子」", "管。"),
    ("turn", "拉丁语 tornare", "希腊语 tornos 是车床。转动原是在车床上旋。"),
    ("TV", "television 的缩写", "希腊语 tele「远」加上拉丁语 visio「看见」。"),
    ("type", "希腊语 typos「击打留下的印」", "类型、铅字，都是一个模子。"),
    ("typewriter", "type 加上 writer", "type 来自希腊语 typos。writer 是日耳曼词 write。打字机把模子打到纸上。"),
    ("typical", "希腊语 typikos", "typos 是模子。典型就是像这个模子。"),
    ("typist", "希腊语 typos", "用模子打字的人。"),
    ("umbrella", "意大利语 ombrella", "拉丁语 umbra「影子」。伞是一小块影子。"),
    ("uniform", "拉丁语 uniformis", "unus「一」加上 forma「形状」。制服就是同一种样子。"),
    ("union", "拉丁语 unio", "unus 是一。联合就是合成一个。"),
    ("unit", "拉丁语 unus「一」", "一个单位。"),
    ("universe", "拉丁语 universum", "unus 加上 vertere「转成一个」。宇宙就是转成的整体。"),
    ("university", "拉丁语 universitas", "unus 加上 vertere。原是一个整体的行会，后来是大学。"),
    ("update", "up 加上 date", "up 是日耳曼词。date 来自拉丁语 data「给出的日期」。更新就是把日期往上挪。"),
    ("upgrade", "up 加上 grade", "up 是日耳曼词。grade 来自拉丁语 gradus「一步」。升级就是往上迈一档。"),
    ("urgent", "拉丁语 urgere「推、催」", "紧急就是被推着。"),
    ("use", "古法语 user", "拉丁语 uti。使用。"),
    ("used to", "use 的过去习惯", "use 来自拉丁语 uti。used to 是「过去惯于」。"),
    ("usual", "拉丁语 usualis", "usus 是使用。通常就是惯常使用的。"),
    ("vacancy", "拉丁语 vacare「空着」", "空位。"),
    ("vacation", "拉丁语 vacatio", "vacare 是空出来。假期就是空出来的时间。"),
    ("valid", "拉丁语 validus", "valere 是有力量。有效就是还站得住。"),
    ("valuable", "拉丁语 valere「值钱」", "有价值的。"),
    ("value", "拉丁语 valere", "值多少。"),
    ("van", "caravan 的缩短", "caravan 来自波斯语 karwan「一队旅人」。厢式货车是从商队的车来的。"),
    ("variety", "拉丁语 varietas", "varius 是多样的。"),
    ("various", "拉丁语 varius", "各种各样的。"),
    ("vary", "拉丁语 variare", "使它变化。"),
    ("vehicle", "拉丁语 vehiculum", "vehere 是运载。车辆。"),
    ("venue", "法语 venir 的一个形式", "拉丁语 venire「来」。场地就是人来的地方。"),
    ("verb", "拉丁语 verbum「词」", "动词在语法里占了「词」这个名字。"),
    ("very", "古法语 verai", "拉丁语 verus「真的」。very 原是「真正地」，后来才只是程度。"),
    ("video", "拉丁语 videre「看见」", "我看。录像。"),
    ("view", "古法语 veue", "拉丁语 videre「看见」。景象。"),
    ("village", "古法语 village", "拉丁语 villa「乡间宅子」。村子是宅子周围的聚落。"),
    ("virus", "拉丁语 virus「毒液、黏液」", "病毒借用了这个「毒」。"),
    ("vocabulary", "拉丁语 vocabulum「一个称呼」", "vox 是声音。词汇是你叫得出来的那些词。"),
    ("voice", "古法语 vois", "拉丁语 vox。声音。"),
    ("volume", "拉丁语 volumen「卷起来的书」", "volvere 是滚。体积和音量是后来从「一卷」扩出去的。"),
    ("vote", "拉丁语 votum「誓愿」", "vovere 是许愿。投票原是说出你的誓愿。"),
    ("voyage", "古法语 voiage", "拉丁语 viaticum，via 是路。航行是上路。"),
    ("wage", "古北法语 wage", "日耳曼语 wad「抵押、保证」。工资原是保证会给的那一笔。"),
    ("wait", "古北法语 waitier", "日耳曼语 waht「守夜」。等待就是守着。它经法语进来，不是拉丁语。"),
    ("wall", "拉丁语 vallum「栅栏、墙」", "古英语 weall 借入。墙不是和 house 一样的本族词。"),
    ("war", "古北法语 werre", "法兰克语 werra，日耳曼词。战争经法语进来。"),
    ("waste", "古北法语 waster", "拉丁语 vastare「使荒废」，vastus 是空阔的。浪费、废弃。"),
    ("way", "古英语 weg", "日耳曼词。路。"),
    ("web", "古英语 webb「织物」", "日耳曼词。网是后来的比喻。"),
    ("week", "古英语 wice 或 wicu", "日耳曼词。星期。"),
    ("welcome", "古英语 wilcuma", "wil「意愿」加上 cuma「来的人」。受欢迎的来人。日耳曼词。"),
    ("welfare", "well 加上 fare", "两个都是日耳曼词。过得好。"),
    ("while", "古英语 hwil「一段时间」", "日耳曼词。"),
    ("whole", "古英语 hal「完整、健康」", "日耳曼词。和 holy 是近亲。"),
    ("wine", "拉丁语 vinum", "古英语 win 借入。葡萄酒不是日耳曼本族词。"),
    ("witness", "古英语 witnes", "witan 是知道。证人是知道的人。日耳曼词。"),
    ("zone", "希腊语 zone「带子」", "地带就是束上去的一条。"),
]


FULL = {
    "mean": "mean 作「意思是、打算」来自古英语 mænan，作「共有的、小气的」来自古英语 gemæne，都是日耳曼词。作「平均数」是另一条，来自法语、拉丁语 medianus「中间的」。",
    "case": "case 作「情况、事例」来自拉丁语 casus「落下、发生的事」，动词 cadere。作「箱子」来自拉丁语 capsa「盒子」。两个都是拉丁语，不是同一个词。",
    "match": "match 作「相配、比赛」是日耳曼词，古英语 gemæcca「配偶、相配的人」。作「火柴」是另一条，古法语 mèche，希腊语 myxa「灯芯」。",
    "mine": "mine 作「我的」是日耳曼词。作「矿」来自古法语 mine，更早多半是凯尔特语。两条不是一个词。",
    "sound": "sound 作「声音」来自拉丁语 sonus。作「完好的」是日耳曼词，古英语 gesund。作「测深、海峡」来自古法语 sonder。三种不是一个词。",
    "policy": "policy 作「方针」来自希腊语 politeia「城邦的做法」，经拉丁语、法语。作保险「保单」是另一条，意大利语 polizza，更早和希腊语 apodeixis「证明」有关。",
    "race": "race 作「速度竞赛」是北欧日耳曼语。作「人种」来自意大利语 razza，再早没有定论，所以人种这一义不再往下猜。",
    "rest": "rest 作「休息」是日耳曼词，古英语 ræst。作「剩余」来自古法语 reste，拉丁语 restare「留下」，stare 是站立。",
    "tip": "tip 作「尖端、轻点、倾倒」是日耳曼词。作「小费」是近代俚语，来源没有定论，这里不把小费说成某一条古语。",
    "check in": "check 来自古法语 eschec，波斯语 shah「王」，象棋里将军。check in 是入住时把名字核到这一格。它不是日耳曼的 tick。",
    "check out": "check 来自波斯语 shah，经法语的象棋用语。check out 是离店时把账核完，或把东西取出核过。",
    "o’clock": "of the clock 连读后的样子。of 是日耳曼词。clock 来自中古荷兰语 clocke「铃」，中世纪拉丁语 clocca。",
    "around": "around 是 a-（在……上，日耳曼）加上 round。round 来自古法语 rond，拉丁语 rotundus「圆的」。",
    "bank": "bank 作「银行」来自意大利语 banca「板凳」，钱商坐在板凳后。作「河岸」是另一条，日耳曼词，古诺斯语 bakki。商务英语里的 bank 是板凳这一条。",
    "bank account": "bank 来自意大利语 banca「板凳」。account 来自拉丁语 computare「计算」。银行账户是在钱商的板凳上算清的账。",
    "bank balance": "bank 来自意大利语 banca。balance 来自拉丁语 bilanx「两个盘子」。银行余额是看两个盘子是否对齐。",
    "bank card": "bank 来自意大利语 banca。card 来自希腊语 khartes、拉丁语 charta。银行卡是银行给出的一张卡片。",
    "bank charge": "bank 来自意大利语 banca。charge 来自拉丁语 carrus「车」，经「装载」变成「收取」。银行收费。",
    "bank clerk": "bank 来自意大利语 banca。clerk 来自希腊语 kleros，经拉丁语 clericus。银行职员。",
    "bank loan": "bank 来自意大利语 banca。loan 是日耳曼词，和 lend 同族。银行贷款。",
    "bank manager": "bank 来自意大利语 banca。manager 来自意大利语 maneggiare，拉丁语 manus「手」。银行经理是用手管这家银行的人。",
    "bank statement": "bank 来自意大利语 banca。statement 来自拉丁语 stare「站定」。银行对账单把账站定写清。",
    "bank transfer": "bank 来自意大利语 banca。transfer 来自拉丁语 transferre「带过去」。转账就是把钱从这家带到那家。",
    "banking": "bank 来自意大利语 banca「板凳」，加上英语 -ing。银行业就是坐在这张板凳后的行当。",
    "banknote": "bank 来自意大利语 banca。note 来自拉丁语 nota「记号」。钞票是银行发出的一张有记号的纸。",
    "bankruptcy": "意大利语 banca rotta「断了的板凳」。钱商的板凳断了，就是破产。rotta 来自拉丁语 rumpere「打破」。",
    "blank cheque": "blank 来自法语 blanc，日耳曼语「白」。cheque 和 check 同词，来自波斯语 shah，经象棋。空白支票是还没写上金额的那张。",
    "current account": "current 来自拉丁语 currere「跑」。account 来自 computare「计算」。往来账户是还在流动的那本账。",
    "AOB": "any other business 的缩写。any、other、business 都是日耳曼词。会议末尾问还有没有别的事。",
    "ASAP": "as soon as possible 的缩写。as 和 soon 是日耳曼词。possible 来自拉丁语 possibilis，posse「能够」。",
    "B.Sc.": "Bachelor of Science 的缩写。bachelor 经法语，和中世纪拉丁语 baccalarius 有关。science 来自拉丁语 scientia，scire「知道」。",
    "c/o": "care of 的缩写。care 和 of 都是日耳曼词。由某人转交。",
    "cc": "carbon copy 的缩写。carbon 来自拉丁语 carbo「炭」。copy 来自拉丁语 copia。抄送原是复写纸的那一份。",
    "CD": "compact disc 的缩写。compact 来自拉丁语 compingere「钉到一起」。disc 来自希腊语 diskos。",
    "CD-ROM": "compact disc read-only memory 的缩写。compact 和 disc 见 CD。read 是日耳曼词。memory 来自拉丁语 memoria。只读的光盘。",
    "CEO": "chief executive officer 的缩写。chief 来自拉丁语 caput「头」。executive 来自拉丁语 exsequi「执行」。officer 来自拉丁语 officium。",
    "cm": "centimetre 的缩写。拉丁语 centum「百」加上希腊语 metron「量」。",
    "Co": "company 的缩写。company 来自拉丁语 companio「一起吃面包的人」，panis 是面包。",
    "DTP": "desktop publishing 的缩写。desk 来自希腊语 diskos。top 是日耳曼词。publish 来自拉丁语 publicare。",
    "DVD": "常作 digital versatile disc，也有人说 digital video disc。digital 来自拉丁语 digitus「手指」。video 来自 videre「看见」。disc 来自希腊语 diskos。versatile 来自 vertere「转」。",
    "ID": "identification 的缩写。拉丁语 idem「同一个」加上 facere「做」。身份就是证明还是同一个人。",
    "kg": "kilogram 的缩写。希腊语 khilioi「一千」加上 gramma。",
    "km": "kilometre 的缩写。希腊语 khilioi 加上 metron。",
    "lab": "laboratory 的缩短。拉丁语 laborare「劳动」。",
    "lb": "拉丁语 libra「磅、天平」的缩写。重量单位。",
    "MA": "在这份商务词表里通常是 Master of Arts。master 来自拉丁语 magister。art 来自拉丁语 ars。",
    "MBA": "Master of Business Administration。master 来自拉丁语 magister。business 是日耳曼词。administration 来自拉丁语 administrare。",
    "MD": "商务英语里常是 managing director。manage 来自意大利语 maneggiare、拉丁语 manus「手」。director 来自拉丁语 dirigere。也有人用它表示医学博士 Medicinae Doctor，那是另一条拉丁缩写。",
    "misc": "miscellaneous 的缩短。拉丁语 miscellaneus，miscere「混合」。杂项。",
    "mph": "miles per hour。mile 来自拉丁语 milia「一千步」。per 是拉丁语。hour 来自希腊语 hora。",
    "Mr": "mister，来自 master。拉丁语 magister「更大的人、老师」。",
    "Mrs": "mistress 的缩写。mistress 来自 master 的阴性，拉丁语 magister。",
    "Ms": "二十世纪造的称呼，取 Mrs 和 Miss 的写法，用来不标明婚否。本身不是一个拉丁词的缩写。",
    "NB": "拉丁语 nota bene。nota 是记号，bene 是好。请注意。",
    "NE": "north east 的缩写。north 和 east 都是日耳曼词。",
    "NW": "north west 的缩写。都是日耳曼词。",
    "OHP": "overhead projector。over 和 head 是日耳曼词。projector 来自拉丁语 proicere「向前扔」。",
    "OHT": "overhead transparency。transparency 来自拉丁语 transparere「透过显现」。",
    "p./pp.": "page 和 pages。拉丁语 pagina。",
    "PA": "商务里常是 personal assistant。personal 来自拉丁语 persona。assistant 来自拉丁语 assistere「站在旁边」。",
    "pc": "在这份词表里多指 personal computer。personal 来自拉丁语 persona，computer 来自 computare。",
    "plc": "public limited company。public 来自拉丁语 populus，limited 来自 limes「界」，company 来自 companio「一起吃饭的人」。",
    "pm": "post meridiem。拉丁语 post「在后」，meridies 是正午。下午。",
    "PR": "public relations。public 来自拉丁语 populus。relation 来自 referre「带回」。",
    "PS": "拉丁语 post scriptum。post「在后」，scriptum「写下来的」。附言。",
    "PTO": "please turn over。please 来自拉丁语 placere。turn 来自拉丁语 tornare。over 是日耳曼词。请翻面。",
    "R & D": "research and development。research 来自古法语，和拉丁语 circare「转着找」有关。development 来自法语 développer「打开」。",
    "Rd": "road 的缩写。road 是日耳曼词。",
    "re": "商务信里的 re 是拉丁语 res「事情」的夺格，in re 就是「关于此事」。它不是 day 的前缀。",
    "RSVP": "法语 répondez s'il vous plaît。请回复。répondre 来自拉丁语 respondere。",
    "SAE": "stamped addressed envelope。stamp 的早期来源不算稳。address 来自拉丁语 directus 这一路。envelope 是法语。",
    "St": "有两个常见缩写，这里不合成一个来源。作街是 street，拉丁语 strata。作圣是 saint，拉丁语 sanctus。看到缩写要看它旁边是路名还是人名。",
    "tel": "telephone 的缩短。希腊语 tele「远」加上 phone「声音」。",
    "yd": "yard 的缩写。yard 是日耳曼词，一根杆或一块围地。",
    "yr": "year 的缩写。year 是日耳曼词。",
    "OK/O.K./okay": "来源有不止一种著名说法，包括误拼 all correct，也包括人名旧金德胡克。没有一条已经定案，所以这里不猜测。",
    "foot/feet": "foot 是日耳曼词，古英语 fot。feet 是它的元音交替复数，不是拉丁语 pes。",
    "spot": "spot 是中古英语里的日耳曼词，可能来自中古荷兰语，不是拉丁语。再早的细节不多。",
    "switch": "switch 大概来自低地德语里的一根软枝，后来才是切换。日耳曼语，不是拉丁语。",
    "smile": "smile 是中古英语，可能来自低地德语或北欧日耳曼语，不是拉丁语。",
    "plug": "plug 来自中古荷兰语 plugge，日耳曼词。塞子。",
    "arrive": "arrive 来自古法语 ariver，拉丁语 ad ripam「到岸边」。ripa 是河岸。到达原来是船靠了岸。",
    "arrival": "arrival 和 arrive 同族，来自古法语，拉丁语 ad ripam「到岸边」。到了的那一刻。",
    "long-term/long term": "long 是日耳曼词。term 来自拉丁语 terminus「界、尽头」。长期就是把一段放到比较远的那条边界上。",
    "short-term/short term": "short 是日耳曼词。term 来自拉丁语 terminus「界、尽头」。短期就是离这条边界比较近的一段。",
}


def _family_notes():
    notes = {}
    for source, roles in FAMILIES.items():
        for word, role in roles.items():
            notes[word.lower()] = f"{word} 来自{source}。这里它是{role}。"
    return notes


def _one_off_notes():
    notes = {}
    for word, source, note in ONE_OFFS:
        if not note:
            continue
        notes[word.lower()] = f"{word} 来自{source}。{note}"
    return notes


MORE_ETYM = {}
MORE_ETYM.update(_family_notes())
MORE_ETYM.update(_one_off_notes())
for key, text in FULL.items():
    MORE_ETYM[key.lower()] = text

# Bare Germanic label is only for words that are not Latin, Greek or French loans.
# Uncertain words stay out of this list so they remain「不猜测」.
_NOT_BARE_GERMANIC = {
    "main", "line", "please", "stay", "stop", "round", "sound", "case", "bank",
    "hour", "school", "wine", "wall", "pound", "kitchen", "silk", "street", "cup",
    "tall", "track", "term", "goal", "job", "jump", "list", "peak", "rubbish",
    "truck", "storey",
}
MORE_GERMANIC = [
    word.strip() for word in GERMANIC_WORDS
    if word.strip() and word.strip().lower() not in _NOT_BARE_GERMANIC
]

EXTRA_KIND = {}
for raw in PHRASES:
    phrase = raw.strip()
    if not phrase or phrase.startswith("#"):
        continue
    EXTRA_KIND[phrase.lower()] = ("germanic", _phrase(phrase))

for key, text in list(FULL.items()):
    # Phrases that only say they are Germanic compounds stay in EXTRA_KIND.
    if "是英语里用日耳曼本族词组成的说法" in text:
        EXTRA_KIND[key.lower()] = ("germanic", text)
        MORE_ETYM.pop(key.lower(), None)

# These notes refuse to settle a source. Leave the headword open.
for key, text in list(MORE_ETYM.items()):
    if any(mark in text for mark in ("这里不猜测", "不写成已经核实", "没有完全定论", "不写成定论")):
        MORE_ETYM.pop(key, None)

from etym_open import OPEN_ETYM, OPEN_KIND  # noqa: E402

for key, text in OPEN_ETYM.items():
    MORE_ETYM.setdefault(key.lower(), text)
for key, kind in OPEN_KIND.items():
    EXTRA_KIND.setdefault(key.lower(), kind)

def _with_apostrophes(key: str) -> set[str]:
    straight = key.replace("’", "'").replace("‘", "'")
    return {key, straight, straight.replace("'", "’")}

for key, text in list(MORE_ETYM.items()):
    for alias in _with_apostrophes(key):
        MORE_ETYM.setdefault(alias, text)
for key, kind in list(EXTRA_KIND.items()):
    for alias in _with_apostrophes(key):
        EXTRA_KIND.setdefault(alias, kind)
