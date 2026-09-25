import csv
import json
import re

CSV_FILE = 'dict_revised.csv'
HANZI_FILE = 'merged_hanzi.json'

def clean(text):
    """清理释义"""
    if not text:
        return ''
    text = str(text)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# 1. 读 CSV
print('📖 读取 CSV ...')
moe = {}
with open(CSV_FILE, 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        word = row.get('字詞名', '').strip()
        if len(word) == 1:
            definition = clean(row.get('釋義', ''))
            if definition:
                if word in moe:
                    moe[word] += ' ／ ' + definition
                else:
                    moe[word] = definition

print(f'✅ 从教育部辞典提取到 {len(moe)} 个单字释义')

# 2. 加载字库
with open(HANZI_FILE, 'r', encoding='utf-8') as f:
    hanzi_data = json.load(f)

# 3. 更新释义（全部保留，没找到显示“无”）
updated = 0
no_meaning = 0
for char in hanzi_data:
    if char in moe:
        meaning = moe[char]
        if len(meaning) > 500:
            meaning = meaning[:500] + '…'
        hanzi_data[char]['meaning'] = meaning
        updated += 1
    else:
        hanzi_data[char]['meaning'] = '无'
        no_meaning += 1

# 4. 写回
with open(HANZI_FILE, 'w', encoding='utf-8') as f:
    json.dump(hanzi_data, f, ensure_ascii=False, indent=2)

print(f'✅ 已更新 {updated} 个字有释义')
print(f'⚠️ {no_meaning} 个字无释义（显示为“无”）')
print(f'📊 合计 {len(hanzi_data)} 个字')