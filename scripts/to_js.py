import json

with open('merged_hanzi.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('hanzi-data.js', 'w', encoding='utf-8') as f:
    f.write('// 自动生成，请勿手动编辑\n')
    f.write('window.HANZI_DATA = ')
    json.dump(data, f, ensure_ascii=False, separators=(',', ':'))  # 压缩
    f.write(';\n')

print(f'✅ 已生成 hanzi-data.js，共 {len(data)} 个条目')