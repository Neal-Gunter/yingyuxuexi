(function () {
  const data = window.YY;
  if (!data) {
    document.getElementById("view").textContent = "词库没有载入。";
    return;
  }
  const words = data.words;
  const roots = data.roots;
  const legends = data.legends;
  const lessons = data.lessons;
  const scenes = data.scenes || [];
  const byWord = new Map(words.map((item) => [item.w.toLowerCase(), item]));
  const byRoot = new Map(roots.map((item) => [item.id, item]));
  const byLegend = new Map(legends.map((item) => [item.id, item]));
  const byLesson = new Map(lessons.map((item) => [item.id, item]));
  const byScene = new Map(scenes.map((item) => [item.id, item]));
  const rootCount = new Map();
  words.forEach((item) => {
    (item.rs || []).forEach((id) => rootCount.set(id, (rootCount.get(id) || 0) + 1));
  });

  const view = document.getElementById("view");
  const q = document.getElementById("q");
  const state = { level: "all", lang: "all", shown: 60 };
  const STORE = "yy-srs-v1";
  const DAY = 86400000;
  const MINUTE = 60000;
  let voice = null;
  let session = null;
  let lastHash = "";

  const levelName = { P: "初级", V: "中级", H: "高级" };
  const kindName = { traced: "已核对", root: "词根", germanic: "日耳曼", open: "不猜测" };

  function esc(value) {
    return String(value ?? "").replace(/[&<>"']/g, (ch) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    }[ch]));
  }

  function wordHref(word) {
    return "#/w/" + encodeURIComponent(word);
  }

  function speakButton(text, label) {
    return '<button class="speak" type="button" data-speak="' + esc(text) + '">' + (label || "朗读") + "</button>";
  }

  function pickVoice() {
    if (!window.speechSynthesis) return;
    const list = speechSynthesis.getVoices();
    voice = list.find((item) => /en-GB/i.test(item.lang))
      || list.find((item) => /^en/i.test(item.lang))
      || null;
  }

  function speak(text) {
    if (!window.speechSynthesis) {
      view.insertAdjacentHTML("afterbegin", '<p class="empty">这台设备没有可用的英文语音。</p>');
      return;
    }
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = "en-GB";
    utterance.rate = 0.92;
    if (voice) utterance.voice = voice;
    speechSynthesis.cancel();
    speechSynthesis.resume();
    speechSynthesis.speak(utterance);
    return utterance;
  }

  function speakLines(lines) {
    if (!window.speechSynthesis || !lines.length) return;
    speechSynthesis.cancel();
    let index = 0;
    const next = () => {
      if (index >= lines.length) return;
      const utterance = new SpeechSynthesisUtterance(lines[index].en);
      utterance.lang = "en-GB";
      utterance.rate = 0.92;
      if (voice) utterance.voice = voice;
      const timer = setTimeout(step, Math.max(2500, lines[index].en.length * 80));
      utterance.onend = () => { clearTimeout(timer); step(); };
      speechSynthesis.speak(utterance);
    };
    const step = () => { index += 1; next(); };
    next();
  }

  if (window.speechSynthesis) {
    pickVoice();
    speechSynthesis.onvoiceschanged = pickVoice;
    speechSynthesis.getVoices();
  }

  function loadStore() {
    try {
      return JSON.parse(localStorage.getItem(STORE)) || { cards: {} };
    } catch (error) {
      return { cards: {} };
    }
  }

  function saveStore(store) {
    localStorage.setItem(STORE, JSON.stringify(store));
  }

  function cardOf(store, word) {
    return store.cards[word.toLowerCase()];
  }

  function gradeCard(card, grade) {
    const now = Date.now();
    card.ease = card.ease || 2.5;
    if (grade === 0) {
      card.reps = 0;
      card.interval = 0;
      card.lapses = (card.lapses || 0) + 1;
      card.ease = Math.max(1.3, card.ease - 0.2);
      card.due = now + 10 * MINUTE;
      card.wrong = true;
    } else if (grade === 1) {
      card.ease = Math.max(1.3, card.ease - 0.15);
      card.interval = 0;
      card.due = now + 10 * MINUTE;
    } else {
      card.wrong = false;
      card.reps = (card.reps || 0) + 1;
      if (card.reps === 1) card.interval = grade === 3 ? 4 : 1;
      else if (card.reps === 2) card.interval = grade === 3 ? 7 : 3;
      else card.interval = Math.max(1, Math.round(card.interval * card.ease * (grade === 3 ? 1.3 : 1)));
      if (grade === 3) card.ease = Math.min(3, card.ease + 0.15);
      card.due = now + card.interval * DAY;
    }
    return card;
  }

  function markWrong(word) {
    const store = loadStore();
    const key = word.toLowerCase();
    const card = store.cards[key] || { ease: 2.5, interval: 0, reps: 0, lapses: 0, due: 0, wrong: false };
    gradeCard(card, 0);
    store.cards[key] = card;
    saveStore(store);
  }

  function progressCounts() {
    const store = loadStore();
    const now = Date.now();
    const counts = { fresh: 0, learning: 0, known: 0, wrong: 0, due: 0 };
    words.forEach((item) => {
      const card = cardOf(store, item.w);
      if (!card) {
        counts.fresh += 1;
        return;
      }
      if (card.wrong) counts.wrong += 1;
      if (card.due && card.due <= now && (card.reps || card.lapses)) counts.due += 1;
      if ((card.interval || 0) >= 7 && !card.wrong) counts.known += 1;
      else counts.learning += 1;
    });
    return counts;
  }

  function orderedStudyWords() {
    const levelRank = { P: 0, V: 1, H: 2 };
    const kindRank = { traced: 0, root: 1, germanic: 2, open: 3 };
    return words.slice().sort((a, b) =>
      (levelRank[a.lv] - levelRank[b.lv])
      || ((kindRank[a.ek] || 9) - (kindRank[b.ek] || 9))
      || a.w.localeCompare(b.w)
    );
  }

  function freshWords(limit) {
    const store = loadStore();
    return orderedStudyWords().filter((item) => !cardOf(store, item.w)).slice(0, limit);
  }

  function dueWords() {
    const store = loadStore();
    const now = Date.now();
    return words.filter((item) => {
      const card = cardOf(store, item.w);
      return card && card.due && card.due <= now && (card.reps || card.lapses);
    });
  }

  function wrongWords() {
    const store = loadStore();
    return words.filter((item) => {
      const card = cardOf(store, item.w);
      return card && card.wrong;
    });
  }

  function hash(text) {
    let score = 0;
    for (let i = 0; i < text.length; i += 1) score = (score * 33 + text.charCodeAt(i)) % 1000003;
    return score;
  }

  function sampleOthers(item, count) {
    const same = words.filter((word) => word.w !== item.w && word.lv === item.lv);
    const source = same.length >= count ? same : words.filter((word) => word.w !== item.w);
    const picks = [];
    let step = 0;
    while (picks.length < count && step < 40) {
      const candidate = source[(hash(item.w) + step * 17) % source.length];
      if (candidate && !picks.some((pick) => pick.w === candidate.w)) picks.push(candidate);
      step += 1;
    }
    return picks;
  }

  function shuffle(list) {
    return list.slice().sort((a, b) => hash(a.w + b.w) % 2 === 0 ? 1 : -1);
  }

  function ensureSession(mode) {
    if (session && session.mode === mode) return;
    let queue = [];
    if (mode === "review") queue = dueWords();
    else if (mode === "wrong") queue = wrongWords();
    else if (mode === "new") queue = freshWords(15);
    else if (mode === "picture") queue = words.filter((item) => item.pic);
    else queue = freshWords(12);
    if (!queue.length) queue = orderedStudyWords().slice(0, 12);
    session = { mode: mode, queue: queue, index: 0, revealed: false, picked: null };
  }

  function setTab(name) {
    document.querySelectorAll(".tabs a").forEach((link) => {
      link.classList.toggle("on", link.dataset.tab === name);
    });
  }

  function countRow(href, title, note, num) {
    return '<a class="card count-row" href="' + href + '"><span><b>' + esc(title) +
      '</b><small>' + esc(note) + '</small></span><span class="num">' + num + "</span></a>";
  }

  function studyHome() {
    setTab("study");
    const counts = progressCounts();
    const total = data.meta.counts;
    view.innerHTML =
      '<section class="hero"><p class="kicker">记忆</p><h1>今天学一点</h1>' +
      '<p class="counts">词库 ' + total.words + " · 已掌握 " + counts.known + " · 错题 " + counts.wrong + "</p>" +
      '<div class="stat-grid">' +
      '<a class="stat" href="#/go/new"><b>' + counts.fresh + '</b>未学</a>' +
      '<a class="stat" href="#/go/review"><b>' + counts.due + '</b>待复习</a>' +
      '<a class="stat" href="#/go/wrong"><b>' + counts.wrong + '</b>错题</a>' +
      '<a class="stat" href="#/sort"><b>' + counts.known + '</b>已掌握</a>' +
      "</div></section>" +
      '<div class="list">' +
      countRow("#/go/new", "学习新词", "一次 15 个，先初级、先有词源的", counts.fresh) +
      countRow("#/go/review", "复习到期", "按记得住的程度拉长间隔", counts.due) +
      countRow("#/go/listen", "听音选义", "先听读音，再选中文", 12) +
      countRow("#/go/choice", "看义选词", "给中文，选出英文", 12) +
      countRow("#/go/cloze", "例句填空", "把句子里的词补上", 12) +
      countRow("#/go/picture", "看图选词", "一组配了图的核心词", words.filter((item) => item.pic).length) +
      countRow("#/go/wrong", "错题再练", "答错和不认识的词会留在这里", counts.wrong) +
      "</div>";
  }

  function applyGrade(item, grade) {
    const store = loadStore();
    const key = item.w.toLowerCase();
    const card = store.cards[key] || { ease: 2.5, interval: 0, reps: 0, lapses: 0, due: 0, wrong: false };
    store.cards[key] = gradeCard(card, grade);
    saveStore(store);
    session.index += 1;
    session.revealed = false;
    session.picked = null;
    renderGo(session.mode);
  }

  function renderExamples(item) {
    return (item.xs || []).map((row) =>
      '<div class="line"><div><p class="who">' + esc(row.k) + "</p><p>" + esc(row.en) +
      "</p><p class=\"muted\">" + esc(row.zh) + "</p></div>" + speakButton(row.en, "读") + "</div>"
    ).join("");
  }

  function renderGo(mode) {
    setTab("study");
    ensureSession(mode);
    const item = session.queue[session.index];
    if (!item) {
      const counts = progressCounts();
      view.innerHTML =
        '<a class="back" href="#/">返回学习</a>' +
        '<article class="detail"><p class="kicker">完成</p><h1>这一组做完了</h1>' +
        "<p>未学 " + counts.fresh + " · 待复习 " + counts.due + " · 错题 " + counts.wrong + " · 已掌握 " + counts.known + "</p>" +
        '<a class="primary" href="#/">回学习首页</a></article>';
      return;
    }
    const place = (session.index + 1) + " / " + session.queue.length;
    if (mode === "listen" || mode === "choice" || mode === "cloze" || mode === "picture") {
      renderQuiz(mode, item, place);
      return;
    }
    view.innerHTML =
      '<a class="back" href="#/">返回学习</a>' +
      '<article class="detail"><p class="kicker">' + esc(place) + " · " + esc(levelName[item.lv] || "") + "</p>" +
      '<div class="head-row"><h1>' + esc(item.w) + "</h1>" + speakButton(item.w, "读单词") + "</div>" +
      '<p class="meta phonetic">' + esc(item.ph ? "/" + item.ph + "/" : "") + "</p>" +
      (session.revealed
        ? "<p>" + esc(item.zh) + "</p>" + renderExamples(item) +
          '<div class="etym ' + esc(item.ek) + '"><p>' + esc(item.et) + "</p></div>" +
          '<div class="grades">' +
          '<button class="grade" type="button" data-grade="0">不认识</button>' +
          '<button class="grade" type="button" data-grade="1">模糊</button>' +
          '<button class="grade" type="button" data-grade="2">认识</button>' +
          '<button class="grade" type="button" data-grade="3">简单</button></div>'
        : '<button class="primary" type="button" id="show">看释义和例句</button>') +
      "</article>";
    const show = document.getElementById("show");
    if (show) show.onclick = () => { session.revealed = true; renderGo(mode); };
    view.querySelectorAll("[data-grade]").forEach((button) => {
      button.onclick = () => applyGrade(item, Number(button.dataset.grade));
    });
  }

  function renderQuiz(mode, item, place) {
    if (!session.choices || session.choiceFor !== item.w) {
      const others = sampleOthers(item, 3);
      session.choices = shuffle([item].concat(others));
      session.choiceFor = item.w;
      session.picked = null;
    }
    let prompt = "";
    if (mode === "listen") {
      prompt = "<p>听读音，选出中文。</p>" + speakButton(item.w, "再听一次");
      if (!session.picked) speak(item.w);
    } else if (mode === "picture") {
      prompt = '<img class="pic" alt="" src="./' + esc(item.pic) + '"><p>这张图是哪个词？</p>';
    } else if (mode === "choice") {
      prompt = "<p>" + esc(item.zh) + "</p><p class=\"muted\">选出对应的英文。</p>";
    } else {
      const sentence = ((item.xs || [])[0] || {}).en || item.w;
      const cloze = sentence.replace(new RegExp(item.w.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "i"), "____");
      prompt = "<p>" + esc(cloze) + "</p>" + speakButton(sentence, "读句子");
    }
    const options = session.choices.map((choice) => {
      let mark = "";
      if (session.picked) {
        if (choice.w === item.w) mark = " ok";
        else if (choice.w === session.picked) mark = " bad";
      }
      const label = mode === "listen" ? choice.zh : choice.w;
      return '<button class="choice' + mark + '" type="button" data-pick="' + esc(choice.w) + '">' + esc(label) + "</button>";
    }).join("");
    view.innerHTML =
      '<a class="back" href="#/">返回学习</a><article class="detail"><p class="kicker">' + esc(place) +
      "</p>" + prompt + options +
      (session.picked ? '<button class="primary" type="button" id="next">下一题</button>' : "") +
      "</article>";
    view.querySelectorAll("[data-pick]").forEach((button) => {
      button.onclick = () => {
        if (session.picked) return;
        session.picked = button.dataset.pick;
        if (session.picked !== item.w) markWrong(item.w);
        renderGo(mode);
      };
    });
    const next = document.getElementById("next");
    if (next) next.onclick = () => {
      session.index += 1;
      session.picked = null;
      session.choices = null;
      renderGo(mode);
    };
  }

  function sceneList() {
    setTab("scenes");
    view.innerHTML =
      '<section class="hero"><p class="kicker">情景</p><h1>把词放进对话</h1>' +
      "<p>日常和搞笑两种口气。点进去可以整段朗读，也可以一句一句听。</p></section>" +
      '<div class="list">' + scenes.map((scene) =>
        countRow("#/scene/" + scene.id, scene.title, scene.tone + " · " + scene.blurb, scene.words.length + " 词")
      ).join("") + "</div>";
  }

  function sceneDetail(id) {
    setTab("scenes");
    const scene = byScene.get(id);
    if (!scene) return;
    view.innerHTML =
      '<a class="back" href="#/scenes">全部场景</a>' +
      '<article class="detail"><p class="kicker">' + esc(scene.tone) + " · " + scene.words.length + " 个词</p>" +
      "<h1>" + esc(scene.title) + "</h1><p>" + esc(scene.blurb) + "</p>" +
      '<button class="primary" type="button" id="play-all">朗读整段</button>' +
      scene.lines.map((line) =>
        '<div class="line"><div><p class="who">' + esc(line.who) + "</p><p>" + esc(line.en) +
        '</p><p class="muted">' + esc(line.zh) + "</p></div>" + speakButton(line.en, "读") + "</div>"
      ).join("") +
      '<div class="row">' + scene.words.map((word) => {
        const item = byWord.get(word.toLowerCase());
        return item ? '<a class="chip" href="' + wordHref(item.w) + '">' + esc(item.w) + "</a>" : "";
      }).join("") + "</div></article>";
    document.getElementById("play-all").onclick = () => speakLines(scene.lines);
  }

  function sortHome() {
    setTab("sort");
    const total = data.meta.counts;
    const prog = progressCounts();
    const kinds = ["traced", "root", "germanic", "open"].map((kind) =>
      countRow("#/words", kindName[kind], "在词库里按词源状态浏览", total[kind] || 0)
    ).join("");
    view.innerHTML =
      '<section class="hero"><p class="kicker">分类</p><h1>每一类都有数量</h1>' +
      "<p>级别、掌握程度、词源、场景、词根和传说分开计数。</p></section>" +
      "<h2>掌握</h2><div class=\"list\">" +
      countRow("#/go/new", "未学", "还没有记忆记录", prog.fresh) +
      countRow("#/go/review", "待复习", "到了该再见面的时间", prog.due) +
      countRow("#/go/wrong", "错题", "不认识或选错的词", prog.wrong) +
      countRow("#/sort", "已掌握", "间隔已经到 7 天或更长", prog.known) +
      "</div><h2>级别</h2><div class=\"list\">" +
      countRow("#/words", "全部", "三个级别一起", total.words) +
      countRow("#/words", "初级 Preliminary", "公开词表里的词头", total.P) +
      countRow("#/words", "中级 Vantage", "按中级主题补充", total.V) +
      countRow("#/words", "高级 Higher", "按高级主题补充", total.H) +
      "</div><h2>词源</h2><div class=\"list\">" + kinds +
      "</div><h2>场景</h2><div class=\"list\">" +
      scenes.map((scene) => countRow("#/scene/" + scene.id, scene.title, scene.tone, scene.words.length)).join("") +
      "</div><h2>别的入口</h2><div class=\"list\">" +
      countRow("#/roots", "词根", "拉丁语和希腊语的共性", roots.length) +
      countRow("#/legends", "历史与传说", "神、钱币和具体的物", legends.length) +
      countRow("#/lessons", "短文", "拉丁语、希腊语和英语的关系", lessons.length) +
      countRow("#/about", "这本词库怎么来的", "来源和没有写进词库的东西", 1) +
      "</div>";
  }

  function filteredWords() {
    const query = q.value.trim().toLowerCase();
    return words.filter((item) => {
      if (state.level !== "all" && item.lv !== state.level) return false;
      if (!query) return true;
      return item.w.toLowerCase().includes(query) || (item.zh || "").toLowerCase().includes(query);
    });
  }

  function home() {
    setTab("words");
    const traced = words.filter((item) => item.ek === "traced");
    const start = new Date(new Date().getFullYear(), 0, 0);
    const day = Math.floor((Date.now() - start) / DAY);
    const pick = traced[day % traced.length];
    const counts = data.meta.counts;
    const list = filteredWords();
    const slice = list.slice(0, state.shown);
    const levelCount = { all: counts.words, P: counts.P, V: counts.V, H: counts.H };
    view.innerHTML =
      '<section class="hero">' +
      '<p class="kicker">今日一词</p>' +
      '<div class="head-row"><h1><a href="' + wordHref(pick.w) + '">' + esc(pick.w) + "</a></h1>" +
      speakButton(pick.w, "读") + "</div>" +
      "<p>" + esc(pick.zh) + "</p>" +
      '<p class="counts">这一页 ' + list.length + " / 词库 " + counts.words + "</p></section>" +
      '<div class="filters">' +
      ["all", "P", "V", "H"].map((lv) => {
        const label = (lv === "all" ? "全部" : levelName[lv]) + " " + levelCount[lv];
        return '<button type="button" data-level="' + lv + '" class="' + (state.level === lv ? "on" : "") + '">' + label + "</button>";
      }).join("") +
      "</div>" +
      '<div class="list">' + (slice.map(renderWordLink).join("") || '<p class="empty">没有找到这个词。</p>') + "</div>" +
      (list.length > slice.length ? '<button class="more" type="button" id="more">再显示 60 个</button>' : "");
    view.querySelectorAll("[data-level]").forEach((button) => {
      button.onclick = () => {
        state.level = button.dataset.level;
        state.shown = 60;
        home();
      };
    });
    const more = document.getElementById("more");
    if (more) more.onclick = () => { state.shown += 60; home(); };
  }

  function renderWordLink(item) {
    return '<a class="word" href="' + wordHref(item.w) + '"><b>' + esc(item.w) +
      "</b><small>" + esc(item.zh) + "</small></a>";
  }

  function detail(word) {
    setTab("words");
    const item = byWord.get(decodeURIComponent(word).toLowerCase());
    if (!item) {
      view.innerHTML = '<p class="empty">词库里没有这个条目。</p>';
      return;
    }
    const rootLinks = (item.rs || []).map((id) => {
      const root = byRoot.get(id);
      return root ? '<a class="chip lang-' + esc(root.lang) + '" href="#/root/' + id + '">' + esc(root.title) + "</a>" : "";
    }).join("");
    const legend = item.lg ? byLegend.get(item.lg) : null;
    const related = [];
    (item.rs || []).forEach((id) => {
      const root = byRoot.get(id);
      if (!root) return;
      root.members.forEach((member) => {
        if (member.toLowerCase() !== item.w.toLowerCase() && related.length < 8) related.push(member);
      });
    });
    view.innerHTML =
      '<a class="back" href="#/words">返回词库</a>' +
      '<article class="detail">' +
      '<p class="kicker">' + esc(levelName[item.lv] || "") + " · " + esc(kindName[item.ek] || "") + "</p>" +
      '<div class="head-row"><h1>' + esc(item.w) + "</h1>" + speakButton(item.w, "读单词") + "</div>" +
      '<p class="meta"><span class="phonetic">' + esc(item.ph ? "/" + item.ph + "/" : "") + "</span> " + esc(item.pos) + "</p>" +
      "<p>" + esc(item.zh) + "</p>" +
      '<div class="etym ' + esc(item.ek) + '"><p class="label">词源</p><p>' + esc(item.et) + "</p></div>" +
      "<h2>例句</h2>" + renderExamples(item) +
      '<button class="primary" type="button" id="wrong-btn">记入错题</button>' +
      (rootLinks ? '<div class="row">' + rootLinks + "</div>" : "") +
      (legend ? '<p><a class="chip" href="#/legend/' + legend.id + '">传说 · ' + esc(legend.title) + "</a></p>" : "") +
      (related.length ? '<p class="muted">同族可以接着看：' + related.map((member) => '<a href="' + wordHref(member) + '">' + esc(member) + "</a>").join("、") + "</p>" : "") +
      "</article>";
    document.getElementById("wrong-btn").onclick = () => {
      markWrong(item.w);
      document.getElementById("wrong-btn").textContent = "已记入错题";
    };
  }

  function rootList() {
    setTab("sort");
    const list = roots.filter((root) => state.lang === "all" || root.lang === state.lang);
    view.innerHTML =
      '<a class="back" href="#/sort">返回分类</a>' +
      '<section class="hero"><p class="kicker">共性 · ' + roots.length + ' 族</p><h1>词根</h1>' +
      "<p>同一族词共用一个拉丁语或希腊语动作。数字是这一族在词库里的词数。</p></section>" +
      '<div class="filters">' +
      [["all", "全部 " + roots.length], ["拉丁", "拉丁"], ["希腊", "希腊"]].map(([id, label]) => {
        const num = id === "all" ? roots.length : roots.filter((root) => root.lang === id).length;
        const text = id === "all" ? label : label + " " + num;
        return '<button type="button" data-lang="' + id + '" class="' + (state.lang === id ? "on" : "") + '">' + text + "</button>";
      }).join("") +
      "</div>" +
      '<div class="list">' + list.map((root) =>
        countRow("#/root/" + root.id, root.title, root.lang, rootCount.get(root.id) || root.members.length)
      ).join("") + "</div>";
    view.querySelectorAll("[data-lang]").forEach((button) => {
      button.onclick = () => { state.lang = button.dataset.lang; rootList(); };
    });
  }

  function rootDetail(id) {
    setTab("sort");
    const root = byRoot.get(id);
    if (!root) return;
    const members = root.members.map((member) => byWord.get(member.toLowerCase())).filter(Boolean);
    view.innerHTML =
      '<a class="back" href="#/roots">全部词根</a>' +
      '<article class="detail"><p class="kicker lang-' + esc(root.lang) + '">' + esc(root.lang) + " · " + members.length + " 词</p>" +
      "<h1>" + esc(root.title) + "</h1>" +
      "<p>" + esc(root.meaning) + "</p>" +
      '<div class="etym root"><p class="label">共性</p><p>' + esc(root.pattern) + "</p></div>" +
      '<div class="list">' + members.map(renderWordLink).join("") + "</div></article>";
  }

  function legendList() {
    setTab("sort");
    view.innerHTML =
      '<a class="back" href="#/sort">返回分类</a>' +
      '<section class="hero"><p class="kicker">故事 · ' + legends.length + ' 则</p><h1>历史与传说</h1>' +
      "<p>这些词还带着神、城、钱币或一件具体的物。</p></section>" +
      '<div class="list">' + legends.map((legend) =>
        countRow("#/legend/" + legend.id, legend.title, legend.kind + " · " + legend.lang, legend.words.length)
      ).join("") + "</div>";
  }

  function legendDetail(id) {
    setTab("sort");
    const legend = byLegend.get(id);
    if (!legend) return;
    view.innerHTML =
      '<a class="back" href="#/legends">全部传说</a>' +
      '<article class="lesson"><p class="kicker">' + esc(legend.kind) + " · " + legend.words.length + " 词</p>" +
      "<h1>" + esc(legend.title) + "</h1>" +
      legend.story.map((paragraph) => "<p>" + esc(paragraph) + "</p>").join("") +
      '<div class="list">' + legend.words.map((link) => {
        const item = byWord.get(link.w.toLowerCase());
        return item ? renderWordLink(item) : "";
      }).join("") + "</div></article>";
  }

  function lessonList() {
    setTab("sort");
    view.innerHTML =
      '<a class="back" href="#/sort">返回分类</a>' +
      '<section class="hero"><p class="kicker">课文 · ' + lessons.length + ' 课</p><h1>拉丁语、希腊语和英语</h1></section>' +
      '<div class="list">' + lessons.map((lesson, index) =>
        countRow("#/lesson/" + lesson.id, lesson.title, lesson.kicker, index + 1)
      ).join("") + "</div>";
  }

  function lessonDetail(id) {
    setTab("sort");
    const lesson = byLesson.get(id);
    if (!lesson) return;
    const body = lesson.blocks.map((block) => {
      if (block.type === "p") return "<p>" + esc(block.text) + "</p>";
      const head = "<tr>" + block.headers.map((cell) => "<th>" + esc(cell) + "</th>").join("") + "</tr>";
      const rows = block.rows.map((row) => "<tr>" + row.map((cell) => "<td>" + esc(cell) + "</td>").join("") + "</tr>").join("");
      return "<table>" + head + rows + "</table>";
    }).join("");
    view.innerHTML =
      '<a class="back" href="#/lessons">全部课文</a>' +
      '<article class="lesson"><p class="kicker">' + esc(lesson.kicker) + "</p><h1>" + esc(lesson.title) + "</h1>" +
      body + "</article>";
  }

  function about() {
    setTab("sort");
    const counts = data.meta.counts;
    view.innerHTML =
      '<a class="back" href="#/sort">返回分类</a>' +
      '<article class="lesson"><p class="kicker">来源</p><h1>这本词库怎么来的</h1>' +
      "<p>初级词头参考剑桥英语公开发布的 Business Preliminary 词表。中级 " + counts.V +
      " 个、高级 " + counts.H + " 个按考试主题补充。释义来自 MIT 许可的 ECDICT，商务多义词另作了改写。</p>" +
      "<p>每个词有办公、日常、搞笑三类例句，用来把词放进句子。八个情景对话是写成的短剧，可以整段朗读。词源仍然只在有把握时写明来源。</p>" +
      "<p>记忆用本地间隔重复：不认识会进入错题，认识以后间隔从 1 天拉长。进度只存在这台设备的浏览器里。</p>" +
      "<p>朗读使用设备自己的英文语音。安卓安装包在仓库的 release 目录。苹果手机把网页添加到主屏幕即可使用；签名的 App Store 包需要 Mac。</p></article>";
  }

  function route() {
    const hash = decodeURIComponent(location.hash || "#/");
    if (hash !== lastHash && hash.indexOf("#/go/") === 0) session = null;
    lastHash = hash;
    const parts = hash.replace(/^#\/?/, "").split("/").filter(Boolean);
    const head = parts[0] || "";
    if (!head) return studyHome();
    if (head === "go" && parts[1]) return renderGo(parts[1]);
    if (head === "scenes") return sceneList();
    if (head === "scene" && parts[1]) return sceneDetail(parts[1]);
    if (head === "sort") return sortHome();
    if (head === "words") return home();
    if (head === "w" && parts[1]) return detail(parts.slice(1).join("/"));
    if (head === "roots") return rootList();
    if (head === "root" && parts[1]) return rootDetail(parts[1]);
    if (head === "legends") return legendList();
    if (head === "legend" && parts[1]) return legendDetail(parts[1]);
    if (head === "lessons") return lessonList();
    if (head === "lesson" && parts[1]) return lessonDetail(parts[1]);
    if (head === "about") return about();
    studyHome();
  }

  view.addEventListener("click", (event) => {
    const button = event.target.closest("[data-speak]");
    if (!button) return;
    event.preventDefault();
    speak(button.getAttribute("data-speak") || "");
  });

  q.addEventListener("input", () => {
    state.shown = 60;
    if (location.hash !== "#/words") location.hash = "#/words";
    else home();
  });
  window.addEventListener("hashchange", route);
  route();

  if ("serviceWorker" in navigator && location.protocol.startsWith("http")) {
    navigator.serviceWorker.register("./sw.js").catch(() => {});
  }
})();
