import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt
import numpy as np

# 读取数据
df = pd.read_excel('keywords_with_sentiment.xlsx')

# 创建一个新的列用于候选人分类，考虑 Harris 加入，Biden 退出且权重为 1/2
def get_candidate(sentiment, keywords):
    if 'Trump' in keywords and sentiment == 'positive':
        return 'Trump'
    elif 'Harris' in keywords and sentiment == 'positive':
        return 'Harris'
    elif 'Biden' in keywords and sentiment == 'positive':
        return 'Biden'
    else:
        return 'Other'

df['candidate'] = df.apply(lambda row: get_candidate(row['sentiment'], row['keywords']), axis=1)

# 将 'keywords' 和 'candidate' 转化为特征
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['keywords'])

# 使用 candidate 列作为标签，分别为 Trump、Harris 或 Biden
y = df['candidate'].apply(lambda x: 1 if x == 'Trump' else (2 if x == 'Harris' else (0 if x == 'Biden' else -1)))

# 在这里我们用 -1 表示其他的类别，并将Biden的支持权重降为1/2
# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练 Random Forest 模型
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 获取 Trump 和 Harris 的预测概率
probabilities = model.predict_proba(X_test)

# 获取每个样本是 Trump (类别 1)、Harris (类别 2) 或 Biden (类别 0) 的概率
prob_trump = probabilities[:, 1]  # Trump 类别的预测概率
prob_harris = probabilities[:, 2]  # Harris 类别的预测概率
prob_biden = probabilities[:, 0]  # Biden 类别的预测概率

# 计算 Trump 和 Harris 获胜的支持比例
# 为了将Biden的支持按1/2的权重计入Harris支持，我们调整prob_harris
prob_harris_adjusted = prob_harris + 0.5 * prob_biden

# 计算 Trump 和 Harris（包括Biden支持）获胜的支持比例
trump_support = np.mean(prob_trump > prob_harris_adjusted) * 100
harris_support = np.mean(prob_harris_adjusted > prob_trump) * 100

print(f"Trump Support: {trump_support:.2f}%")
print(f"Harris Support: {harris_support:.2f}%")
