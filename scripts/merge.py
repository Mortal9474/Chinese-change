import json
import os

def merge_hanzi_data():
    if not os.path.exists('dictionary.txt'):
        print("❌ 找不到 dictionary.txt")
        return
    if not os.path.exists('STCharacters.txt'):
        print("❌ 找不到 STCharacters.txt")
        return

    # 1. 读取 MakeMeAHanzi
    print("📖 正在读取 dictionary.txt ...")
    hanzi_dict = {}
    with open('dictionary.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                data = json.loads(line)
            except:
                continue
            char = data.get('character')
            if char:
                hanzi_dict[char] = {
                    'definition': data.get('definition', ''),
                    'pinyin': data.get('pinyin', []),
                }
    print(f"   读取到 {len(hanzi_dict)} 个汉字")

    # 2. 读取 STCharacters
    print("🔄 正在读取 STCharacters.txt ...")
    simp_to_trad = {}
    with open('STCharacters.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split('\t')
            if len(parts) >= 2:
                simp = parts[0]
                trad_part = parts[1].split('#')[0].strip()
                trad_variants = trad_part.split()
                simp_to_trad[simp] = trad_variants
    print(f"   读取到 {len(simp_to_trad)} 组简繁映射")

    # 3. 合并（不丢字）
    print("🔗 正在合并数据 ...")
    merged = {}
    processed = set()

    for simp, variants in simp_to_trad.items():
        for trad in variants:
            if trad in processed:
                continue
            trad_info = hanzi_dict.get(trad)
            simp_info = hanzi_dict.get(simp)

            meaning = ''
            pinyin = []
            if trad_info:
                meaning = trad_info.get('definition', '')
                pinyin = trad_info.get('pinyin', [])
            elif simp_info:
                meaning = simp_info.get('definition', '')
                pinyin = simp_info.get('pinyin', [])

            # 不丢字：即使没字义也收录
            merged[trad] = {
                'simplified': simp,
                'meaning': meaning,
                'pinyin': pinyin,
            }
            processed.add(trad)

    with open('merged_hanzi.json', 'w', encoding='utf-8') as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)

    print(f"✅ 合并完成！共生成 {len(merged)} 个繁体字条目")

if __name__ == '__main__':
    merge_hanzi_data()