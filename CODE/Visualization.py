import matplotlib.pyplot as plt

# 第一种情况数据
candidates_case1 = ['Trump', 'Biden']
support_case1 = [24.29, 59.64]

# 第二种情况数据
candidates_case2 = ['Trump', 'Harris']
support_case2 = [59.38, 24.39]

# 饼图
plt.figure(figsize=(12, 6))

# 第一种情况饼图
plt.subplot(1, 2, 1)
plt.pie(support_case1, labels=candidates_case1, autopct='%1.1f%%', startangle=90,
        colors=['#FF4F4F', '#4B8FE6'], explode=(0.1, 0))  # Trump 红色, Biden 蓝色
plt.title('Support Distribution (Case 1)', fontsize=16)

# 第二种情况饼图
plt.subplot(1, 2, 2)
plt.pie(support_case2, labels=candidates_case2, autopct='%1.1f%%', startangle=90,
        colors=['#FF4F4F', '#63B478'], explode=(0.1, 0))  # Trump 红色, Harris 绿色
plt.title('Support Distribution (Case 2)', fontsize=16)

plt.tight_layout()
plt.show()
