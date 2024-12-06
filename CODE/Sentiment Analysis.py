import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# 读取数据
df = pd.read_excel('keywords_extracted.xlsx')

# 初始化 VADER 情感分析器
sia = SentimentIntensityAnalyzer()

# 定义情感分类函数
def get_sentiment(text):
    # 确保文本是字符串
    if not isinstance(text, str):
        text = str(text)  # 将非字符串类型转换为字符串
    score = sia.polarity_scores(text)
    if score['compound'] >= 0.05:
        return 'positive'
    elif score['compound'] <= -0.05:
        return 'negative'
    else:
        return 'neutral'

# 应用情感分析
df['sentiment'] = df['cleaned_content'].apply(get_sentiment)

# 保存结果到新的 Excel 文件
df.to_excel('keywords_with_sentiment.xlsx', index=False)
