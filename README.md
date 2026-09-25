# Chinese-change
简体字繁体字转换
# 繁体字学习 · 描红练习

一个纯前端的繁体字学习工具，支持简繁对照、字义解释、描红练习。

## 使用方法

直接双击 `index.html` 即可打开使用，无需服务器。

## 功能

- 🔍 搜索繁体字或简体字
- 📖 简繁对照 + 中文释义（来自台湾教育部《国语辞典》）
- ✍️ 楷体描红练习（鼠标或手指）
- 📄 分页浏览字库

## 数据来源

- 简繁映射：[OpenCC](https://github.com/BYVoid/OpenCC)
- 字义解释：[教育部《重編國語辭典修訂本》](https://language.moe.gov.tw/001/Upload/Files/site_content/M0001/respub/dict_reviseddict_download.html)
- 拼音数据：[MakeMeAHanzi](https://github.com/skishore/makemeahanzi)

## 重新生成数据

如果需要重新生成 `hanzi-data.js`：

1. 下载数据源：
   - [dictionary.txt](https://raw.githubusercontent.com/skishore/makemeahanzi/master/dictionary.txt)
   - [STCharacters.txt](https://raw.githubusercontent.com/BYVoid/OpenCC/master/data/dictionary/STCharacters.txt)
   - [教育部辞典](https://language.moe.gov.tw/001/Upload/Files/site_content/M0001/respub/dict_reviseddict_download.html)

2. 按顺序运行脚本：
```bash
python merge.py          # 合并简繁映射
python excel_to_csv.py   # Excel → CSV（教育部数据）
python extract_moe.py    # 提取中文释义
python to_js.py          # 生成 hanzi-data.js
