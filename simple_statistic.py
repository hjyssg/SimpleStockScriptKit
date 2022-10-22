import pandas as pd

def calculate_change(begin_row, end_row):
    open_value = begin_row["Open"]
    close_value = end_row["Close"]

    return (close_value - open_value) / open_value

df = pd.read_csv('data/1971年开始的纳斯达克^IXIC.csv', parse_dates=["Date"])

print(df.shape)

# float(df[0:1]["Open"])
# df[df['Date'].dt.year == 2001]

output_data = []
for year in range(1971, 2022):
    # df[df[Date] == year + "-11-01"]
    year_df = df[df['Date'].dt.year == year]

    early_days = 40
    first_day = year_df.iloc[0]
    day_early = year_df.iloc[early_days]
    last_day = year_df.iloc[-1]
    # print(year_df.head(10))

    # 选择11月
    sub1 =  year_df[year_df['Date'].dt.month == 11]
    middle_day = sub1.iloc[0]

    year_change = calculate_change(first_day, last_day)
    change_early = calculate_change(first_day, day_early)
    ytd_change = calculate_change(first_day, middle_day)
    rest_change = calculate_change(middle_day, last_day)


    output_data.append({
        "year": year,
        "全年变化百分比":  round(year_change * 100, 2),
        ("年初变化百分比 - " + str(early_days)): round(change_early * 100, 2),
        "前10月变化百分比": round(ytd_change * 100, 2),
        "最后两个月变化百分比": round(rest_change * 100, 2),
        "年初价格": first_day["Open"],
        "年中价格": middle_day["Open"],
        "年尾价格": last_day["Close"]
    })


output_df = pd.DataFrame.from_dict(output_data)
output_df.to_excel("简易统计.xlsx", index=False)
