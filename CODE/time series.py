import matplotlib.pyplot as plt
import numpy as np

# 数据生成：时间从 5 月到 11 月
months = ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov']
biden_support = [70, 65, 60, 55, 30, 20, 0]  # 假设的Biden支持度
trump_support = [30, 35, 40, 45, 50, 60, 75]  # 假设的Trump支持度
harris_support = [0, 0, 0, 0, 20, 30, 25]  # 假设的Harris支持度

# 设置颜色：使用渐变色显示支持度
biden_color = '#1E90FF'  # 蓝色
trump_color = '#FF6347'  # 红色
harris_color = '#32CD32'  # 绿色

# 创建图表
plt.figure(figsize=(10, 6))

# 绘制支持度变化线
plt.plot(months, biden_support, marker='o', color=biden_color, label="Biden", linestyle='-', linewidth=3, markersize=8)
plt.plot(months, trump_support, marker='o', color=trump_color, label="Trump", linestyle='-', linewidth=3, markersize=8)
plt.plot(months, harris_support, marker='o', color=harris_color, label="Harris", linestyle='-', linewidth=3, markersize=8)

# 填充颜色：使得区域更加直观
plt.fill_between(months, biden_support, color=biden_color, alpha=0.2)
plt.fill_between(months, trump_support, color=trump_color, alpha=0.2)
plt.fill_between(months, harris_support, color=harris_color, alpha=0.2)

# 添加图表标签
plt.title("Time Series of Support for Biden, Trump, and Harris", fontsize=14)
plt.xlabel("Months", fontsize=12)
plt.ylabel("Support Percentage (%)", fontsize=12)
plt.ylim(0, 100)

# 添加网格
plt.grid(True, linestyle='--', alpha=0.7)

# 添加图例
plt.legend()

# 显示图表
plt.tight_layout()
plt.show()
