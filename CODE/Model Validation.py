import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import confusion_matrix, roc_curve, auc, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# 1. 读取数据
df = pd.read_excel('keywords_with_sentiment.xlsx')


# 创建候选人分类列
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

# 2. 数据处理
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(df['keywords'])
y = df['candidate'].apply(lambda x: 1 if x == 'Trump' else (2 if x == 'Harris' else (3 if x == 'Biden' else 0)))

# 数据划分
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 3. 模型训练
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. 支持率计算
probabilities = model.predict_proba(X_test)
prob_trump = probabilities[:, 1]
prob_harris = probabilities[:, 2]

# 调整 Biden 的权重
prob_biden = probabilities[:, 3]
prob_harris_adjusted = prob_harris + 0 * prob_biden

trump_support = np.mean(prob_trump > prob_harris_adjusted) * 100
harris_support = np.mean(prob_harris_adjusted > prob_trump) * 100

print(f"Trump Support: {trump_support:.2f}%")
print(f"Harris Support: {harris_support:.2f}%")


# 5. 可视化

# (1) 条形图
def plot_bar_chart(trump_support, harris_support):
    candidates = ['Trump', 'Harris']
    support_percentages = [trump_support, harris_support]

    plt.figure(figsize=(8, 6))
    plt.bar(candidates, support_percentages, color=['blue', 'green'])
    plt.xlabel('Candidates')
    plt.ylabel('Support Percentage (%)')
    plt.title('Support Prediction for Trump vs. Harris')
    plt.ylim(0, 100)

    for i, v in enumerate(support_percentages):
        plt.text(i, v + 3, f'{v:.2f}%', ha='center', va='bottom', fontsize=12)
    plt.show()


plot_bar_chart(trump_support, harris_support)


# (2) 饼图
def plot_pie_chart(trump_support, harris_support):
    labels = ['Trump', 'Harris']
    sizes = [trump_support, harris_support]
    colors = ['#4C84FF', '#63B478']
    explode = (0.1, 0)

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140,
            wedgeprops={'edgecolor': 'black'})
    plt.title('Support Prediction for Trump vs. Harris')
    plt.show()


plot_pie_chart(trump_support, harris_support)


# (3) 混淆矩阵
def plot_confusion_matrix(y_test, predictions):
    cm = confusion_matrix(y_test, predictions)
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Other', 'Trump', 'Harris', 'Biden'],
                yticklabels=['Other', 'Trump', 'Harris', 'Biden'])
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('Confusion Matrix')
    plt.show()


plot_confusion_matrix(y_test, model.predict(X_test))


# (4) ROC 曲线
def plot_roc_curve(y_test, prob_trump, prob_harris_adjusted):
    fpr_trump, tpr_trump, _ = roc_curve(y_test == 1, prob_trump)
    fpr_harris, tpr_harris, _ = roc_curve(y_test == 2, prob_harris_adjusted)

    roc_auc_trump = auc(fpr_trump, tpr_trump)
    roc_auc_harris = auc(fpr_harris, tpr_harris)

    plt.figure(figsize=(8, 6))
    plt.plot(fpr_trump, tpr_trump, color='blue', lw=2, label=f'Trump ROC curve (area = {roc_auc_trump:.2f})')
    plt.plot(fpr_harris, tpr_harris, color='green', lw=2, label=f'Harris ROC curve (area = {roc_auc_harris:.2f})')

    plt.plot([0, 1], [0, 1], color='gray', linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='lower right')
    plt.show()


plot_roc_curve(y_test, prob_trump, prob_harris_adjusted)
