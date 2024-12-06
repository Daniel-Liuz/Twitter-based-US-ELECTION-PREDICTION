import pandas as pd
import re

# 读取数据
df = pd.read_csv('pre_data.csv')

# 保留需要的列
df = df[['rawContent', 'replyCount', 'retweetCount', 'likeCount', 'quoteCount']]


# 清理文本数据
def clean_text(text):
    # 如果文本是缺失值或非字符串类型，则返回空字符串
    if not isinstance(text, str):
        return ''
    # 去除URL
    text = re.sub(r'http\S+|www\S+', '', text)
    # 允许标点符号和中文字符
    text = re.sub(r'[^\w\s.,!?;:]', '', text)  # 保留字母、数字、空格、常见标点符号
    # 如果文本为空，返回空字符串
    return text.strip()
df['cleaned_content'] = df['rawContent'].apply(lambda x: clean_text(x))
# 删除包含缺失值的行
df.dropna(inplace=True)

# 输出处理后的数据（可选）
df.to_csv('cleaned_data.csv', index=False)

# 你可以查看数据结构
print(df.head())

# 检查清理后的数据数量
print(f"Number of rows after cleaning: {len(df)}")
