import pandas as pd

# 读取 Excel（30MB 那个）
print('📖 读取 Excel，可能需要 30 秒...')
df = pd.read_excel('dict_revised_2015_20260625.xlsx')

print(f'✅ 读取完成，共 {len(df)} 行')
print(f'   列名：{list(df.columns)[:8]} ...')

# 导出 CSV
df.to_csv('dict_revised.csv', index=False, encoding='utf-8-sig')
print('✅ 已导出 dict_revised.csv')