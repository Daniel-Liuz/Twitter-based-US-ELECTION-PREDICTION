import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取 Excel 文件
df = pd.read_excel('keywords_extracted.xlsx')  # 根据实际路径调整

# 假设你的 DataFrame 中有一列 'keywords'，它存储了提取的关键词
# 如果 'keywords' 是字符串类型，每行是关键词的列表，你可能需要先将它们合并成一个长字符串
all_keywords = ' '.join(df['keywords'].apply(lambda x: ' '.join(x) if isinstance(x, list) else str(x)))

# 创建词云对象
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_keywords)

# 显示词云
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
