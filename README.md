# 英语词源

给 BEC 用的离线词库。每个词尽量说明它从拉丁语、希腊语、日耳曼语或其他语言里的哪一条路来，并把能放在一起记的词收成词根和传说。

## 词库里有什么

- 初级词头参考剑桥英语公开发布的 Business Preliminary 词表。原表的例句没有收录。
- 中级和高级按 BEC Vantage、Higher 的常见主题另作整理。剑桥没有公布一份和初级同等的中高级官方全表。
- 简明中文来自 [ECDICT](https://github.com/skywind3000/ECDICT)（MIT）。一批商务多义词做了改写。
- 词源、50 个词根、34 则传说和 6 课短文是这个仓库自己写的。没有把握的词标成「不猜测」，不用拼写硬编来源。

打开应用后可以查词、按词根看共性、读传说，也可以读「拉丁语、希腊语和英语」那一组短文。

## 怎么用

网页在 `docs/`。用浏览器打开 `docs/index.html` 即可离线查阅。

安卓安装包：`release/yingyuxuexi.apk`。安装前允许来自未知来源的应用。这是调试签名的安装包，可以装到手机上，不是应用商店的上架包。

苹果手机：用 Safari 打开仓库的网页（GitHub Pages 路径是 `/yingyuxuexi/`），点分享，再点「添加到主屏幕」。页面带离线缓存。签名的 App Store 安装包需要 Mac 和苹果开发者账号，这个仓库无法在 Windows 上生成。

## 重新生成词库

`scripts/build_lexicon.py` 需要本机的剑桥词表 PDF 和 ECDICT 的 `ecdict.csv`，路径写在脚本顶部。生成结果是 `docs/data.js`。课文和词源原文在 `content/curriculum.py`。

## 重新打包安卓

需要 JDK 17 和 Android SDK（compileSdk 34）。在 `android/` 目录执行：

```
gradle wrapper
gradlew assembleDebug
```

打包前把 `docs/` 复制到 `android/app/src/main/assets/www/`。
