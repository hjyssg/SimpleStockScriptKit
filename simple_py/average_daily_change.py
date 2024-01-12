# 计算出一个每年每天的平均走势
import pandas as pd

# 读取CSV文件
df = pd.read_csv('../data/1985年开始的纳斯达克100^NDX.csv')

# 将Date列转换为日期格式
df['Date'] = pd.to_datetime(df['Date'])

# 计算每一天的涨跌百分比（考虑开盘价）
df['Daily_Return'] = (df['Close'] - df['Open']) / df['Open'] * 100

# 创建新的列，表示每个日期对应的月日
df['Month_Day'] = df['Date'].dt.strftime('%m-%d')

# 计算每个月日的平均涨跌百分比
average_daily_return = df.groupby('Month_Day')['Daily_Return'].mean().reset_index()

# 打印结果
print(average_daily_return)

# python -m pip install  matplotlib -i https://pypi.tuna.tsinghua.edu.cn/simple
import matplotlib.pyplot as plt
# 假设1月1号股价是100
initial_price = 100

# 初始化股价序列
stock_prices = [initial_price]

# 根据涨跌百分比计算每天的股价
for i in range(1, len(average_daily_return)):
    price_change = stock_prices[-1] * (1 + average_daily_return['Daily_Return'][i] / 100)
    stock_prices.append(price_change)

# 可视化股票走势
plt.figure(figsize=(10, 6))
plt.plot(average_daily_return['Month_Day'], stock_prices, label='Stock Price')


# 设置x轴刻度
plt.xticks(average_daily_return['Month_Day'][::30])  # 每30天显示一次刻度

# 添加tooltip
# for i, txt in enumerate((average_daily_return['Month_Day'])):
#     plt.annotate(txt, (average_daily_return['Month_Day'].iloc[i], stock_prices[i]))


plt.title('Stock Price Trend for the Year')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.show()