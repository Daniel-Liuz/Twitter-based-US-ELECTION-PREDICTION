import pandas as pd
import spacy

# 读取数据
df = pd.read_excel('cleaned_content.xlsx')

# 处理缺失值
df['cleaned_content'] = df['cleaned_content'].fillna('')  # 填充缺失值为空字符串

# 确保所有内容都是字符串
df['cleaned_content'] = df['cleaned_content'].astype(str)

# 加载spaCy模型
nlp = spacy.load('en_core_web_sm')

# 提取关键词（例如：人物、组织等）
def extract_keywords(text):
    doc = nlp(text)
    keywords = [ent.text for ent in doc.ents if ent.label_ in ['PERSON', 'ORG']]
    return keywords

# 提取关键词
df['keywords'] = df['cleaned_content'].apply(extract_keywords)

# 保存提取后的数据
df.to_excel('keywords_extracted.xlsx', index=False)

# 查看数据结构
print(df.head())
