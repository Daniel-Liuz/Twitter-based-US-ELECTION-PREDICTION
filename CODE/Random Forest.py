import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

# 读取数据
df = pd.read_excel('keywords_with_sentiment.xlsx')

# 创建一个新的列用于候选人分类
def get_candidate(sentiment, keywords):
    if 'Trump' in keywords and sentiment == 'positive':
        return 'Trump'
    elif 'Harris' in keywords and sentiment == 'positive':
        return 'Harris'
    elif 'Biden' in keywords and sentiment == 'positive':
        return 'Biden'
    else:
        return 'Other'  # 用于非支持性评论

df['candidate'] = df.apply(lambda row: get_candidate(row['sentiment'], row['keywords']), axis=1)

# 将 'keywords' 和 'candidate' 转化为特征
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['keywords'])  # 使用 keywords 列进行特征提取

# 使用 candidate 列作为标签，分别为 Trump、Harris 或 Biden
y = df['candidate'].apply(lambda x: 1 if x == 'Trump' else (2 if x == 'Harris' else 0))  # Trump:1, Harris:2, Other:0

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练 Random Forest 模型
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 预测并评估模型
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
