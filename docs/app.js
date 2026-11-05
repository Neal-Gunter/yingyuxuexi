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
  const byWord = new Map(words.map((item) => [item.w.toLowerCase(), item]));
  const byRoot = new Map(roots.map((item) => [item.id, item]));
  const byLegend = new Map(legends.map((item) => [item.id, item]));
  const byLesson = new Map(lessons.map((item) => [item.id, item]));
  const rootCount = new Map();
  words.forEach((item) => {
    (item.rs || []).forEach((id) => rootCount.set(id, (rootCount.get(id) || 0) + 1));
  });

  const view = document.getElementById("view");
  const q = document.getElementById("q");
  const state = { level: "all", lang: "all", shown: 60 };

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

  function chipLevel(lv) {
    return '<span class="chip">' + esc(levelName[lv] || lv) + "</span>";
  }

  function renderWordLink(item) {
    return '<a class="word" href="' + wordHref(item.w) + '"><b>' + esc(item.w) +
      "</b><small>" + esc(item.zh) + "</small></a>";
  }

  function setTab(name) {
    document.querySelectorAll(".tabs a").forEach((link) => {
      link.classList.toggle("on", link.dataset.tab === name);
    });
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
    const pick = traced[new Date().getDate() % traced.length];
    const counts = data.meta.counts;
    const list = filteredWords();
    const slice = list.slice(0, state.shown);
    view.innerHTML =
      '<section class="hero">' +
      '<p class="kicker">今日一词</p>' +
      '<h1><a href="' + wordHref(pick.w) + '">' + esc(pick.w) + "</a></h1>" +
      "<p>" + esc(pick.zh) + "</p>" +
      '<p class="counts">词库 ' + counts.words + " · 初级 " + counts.P + " · 中级 " + counts.V +
      " · 高级 " + counts.H + " · 已核对词源 " + counts.traced + "</p>" +
      '<div class="row"><a class="chip" href="#/card">抽一张词源卡</a><a class="chip" href="#/about">这本词库怎么来的</a></div>' +
      "</section>" +
      '<div class="filters">' +
      ["all", "P", "V", "H"].map((lv) => {
        const label = lv === "all" ? "全部" : levelName[lv];
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
      '<a class="back" href="#/">返回词库</a>' +
      '<article class="detail">' +
      '<p class="kicker">' + esc(levelName[item.lv] || "") + " · " + esc(kindName[item.ek] || "") + "</p>" +
      "<h1>" + esc(item.w) + "</h1>" +
      '<p class="meta"><span class="phonetic">' + esc(item.ph ? "/" + item.ph + "/" : "") + "</span> " + esc(item.pos) + "</p>" +
      "<p>" + esc(item.zh) + "</p>" +
      '<div class="etym ' + esc(item.ek) + '"><p class="label">词源</p><p>' + esc(item.et) + "</p></div>" +
      (item.ex ? '<p class="example">' + esc(item.ex) + "</p>" : "") +
      (rootLinks ? '<div class="row">' + rootLinks + "</div>" : "") +
      (legend ? '<p><a class="chip" href="#/legend/' + legend.id + '">传说 · ' + esc(legend.title) + "</a></p>" : "") +
      (related.length ? "<p class=\"muted\">同族可以接着看：" + related.map((member) => '<a href="' + wordHref(member) + '">' + esc(member) + "</a>").join("、") + "</p>" : "") +
      "</article>";
  }

  function rootList() {
    setTab("roots");
    const list = roots.filter((root) => state.lang === "all" || root.lang === state.lang);
    view.innerHTML =
      '<section class="hero"><p class="kicker">共性</p><h1>词根</h1>' +
      "<p>同一族词共用一个拉丁语或希腊语动作。前缀负责方向，词根负责事情本身。</p></section>" +
      '<div class="filters">' +
      [["all", "全部"], ["拉丁", "拉丁"], ["希腊", "希腊"]].map(([id, label]) =>
        '<button type="button" data-lang="' + id + '" class="' + (state.lang === id ? "on" : "") + '">' + label + "</button>"
      ).join("") +
      "</div>" +
      '<div class="list">' + list.map((root) =>
        '<a class="card" href="#/root/' + root.id + '"><b>' + esc(root.title) + "</b><small>" +
        esc(root.lang) + " · " + (rootCount.get(root.id) || root.members.length) + " 个词</small></a>"
      ).join("") + "</div>";
    view.querySelectorAll("[data-lang]").forEach((button) => {
      button.onclick = () => { state.lang = button.dataset.lang; rootList(); };
    });
  }

  function rootDetail(id) {
    setTab("roots");
    const root = byRoot.get(id);
    if (!root) return;
    const members = root.members.map((member) => byWord.get(member.toLowerCase())).filter(Boolean);
    view.innerHTML =
      '<a class="back" href="#/roots">全部词根</a>' +
      '<article class="detail"><p class="kicker lang-' + esc(root.lang) + '">' + esc(root.lang) + "</p>" +
      "<h1>" + esc(root.title) + "</h1>" +
      "<p>" + esc(root.meaning) + "</p>" +
      '<div class="etym root"><p class="label">共性</p><p>' + esc(root.pattern) + "</p></div>" +
      '<div class="list">' + members.map(renderWordLink).join("") + "</div></article>";
  }

  function legendList() {
    setTab("legends");
    view.innerHTML =
      '<section class="hero"><p class="kicker">故事</p><h1>历史与传说</h1>' +
      "<p>这些词还带着神、城、钱币或一件具体的物。故事用来记住来源，不代替词在合同里的意思。</p></section>" +
      '<div class="list">' + legends.map((legend) =>
        '<a class="card" href="#/legend/' + legend.id + '"><b>' + esc(legend.title) + "</b><small>" +
        esc(legend.kind) + " · " + esc(legend.lang) + " · " + legend.words.length + " 个词</small></a>"
      ).join("") + "</div>";
  }

  function legendDetail(id) {
    setTab("legends");
    const legend = byLegend.get(id);
    if (!legend) return;
    view.innerHTML =
      '<a class="back" href="#/legends">全部传说</a>' +
      '<article class="lesson"><p class="kicker">' + esc(legend.kind) + " · " + esc(legend.lang) + "</p>" +
      "<h1>" + esc(legend.title) + "</h1>" +
      legend.story.map((paragraph) => "<p>" + esc(paragraph) + "</p>").join("") +
      '<div class="list">' + legend.words.map((link) => {
        const item = byWord.get(link.w.toLowerCase());
        return item ? renderWordLink(item) : "";
      }).join("") + "</div></article>";
  }

  function lessonList() {
    setTab("lessons");
    view.innerHTML =
      '<section class="hero"><p class="kicker">关系</p><h1>拉丁语、希腊语和英语</h1>' +
      "<p>六课短文。先看三条路，再看双生词、前缀、希腊零件，以及钱和合同上的动作。</p></section>" +
      '<div class="list">' + lessons.map((lesson) =>
        '<a class="card" href="#/lesson/' + lesson.id + '"><b>' + esc(lesson.title) + "</b><small>" + esc(lesson.kicker) + "</small></a>"
      ).join("") + "</div>";
  }

  function lessonDetail(id) {
    setTab("lessons");
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

  function card() {
    setTab("words");
    const pool = words.filter((item) => item.ek === "traced" || item.ek === "root");
    const item = pool[Math.floor(Math.random() * pool.length)];
    view.innerHTML =
      '<a class="back" href="#/">返回</a>' +
      '<article class="detail"><p class="kicker">先猜来源</p><h1>' + esc(item.w) + "</h1>" +
      "<p>" + esc(item.zh) + "</p>" +
      '<button class="primary" type="button" id="reveal">看词源</button></article>';
    document.getElementById("reveal").onclick = () => {
      location.hash = "#/w/" + encodeURIComponent(item.w);
    };
  }

  function about() {
    setTab("words");
    const counts = data.meta.counts;
    view.innerHTML =
      '<a class="back" href="#/">返回</a>' +
      '<article class="lesson"><p class="kicker">来源</p><h1>这本词库怎么来的</h1>' +
      "<p>初级词头参考剑桥英语公开发布的 Business Preliminary 词表，范围大约 " + counts.P +
      " 个。原表里的例句没有搬进来。中级 " + counts.V + " 个、高级 " + counts.H +
      " 个，是按 BEC Vantage 和 Higher 的常见主题另作整理的。剑桥没有公布一份和初级同等的中高级官方全表。</p>" +
      "<p>简明中文释义取自 MIT 许可的 ECDICT，并按商务用法改写了一批多义词。词源、词根、传说和六课短文是为这个词库写的。写了「不猜测」的词，只提供释义，不用拼写硬编来源。</p>" +
      "<p>已核对词源 " + counts.traced + " 条，归入词根的 " + counts.root + " 条，标明日耳曼本族的 " +
      counts.germanic + " 条。传说 " + counts.legendEntries + " 则，词根 " + counts.roots + " 个。</p>" +
      "<p>安卓安装包在仓库的 release 目录。苹果手机可以把这个网页添加到主屏幕，离线使用。签名的 App Store 安装包需要 Mac 和苹果开发者账号，这一步无法在当前的 Windows 环境里完成。</p></article>";
  }

  function route() {
    const hash = decodeURIComponent(location.hash || "#/");
    const parts = hash.replace(/^#\/?/, "").split("/").filter(Boolean);
    const head = parts[0] || "";
    if (!head) return home();
    if (head === "w" && parts[1]) return detail(parts.slice(1).join("/"));
    if (head === "roots") return rootList();
    if (head === "root" && parts[1]) return rootDetail(parts[1]);
    if (head === "legends") return legendList();
    if (head === "legend" && parts[1]) return legendDetail(parts[1]);
    if (head === "lessons") return lessonList();
    if (head === "lesson" && parts[1]) return lessonDetail(parts[1]);
    if (head === "card") return card();
    if (head === "about") return about();
    home();
  }

  q.addEventListener("input", () => {
    state.shown = 60;
    if (!location.hash || location.hash === "#/" || location.hash.startsWith("#/w/")) {
      if (location.hash.startsWith("#/w/")) location.hash = "#/";
      else home();
    } else if (q.value.trim()) {
      location.hash = "#/";
    }
  });
  window.addEventListener("hashchange", route);
  route();

  if ("serviceWorker" in navigator && location.protocol.startsWith("http")) {
    navigator.serviceWorker.register("./sw.js").catch(() => {});
  }
})();
