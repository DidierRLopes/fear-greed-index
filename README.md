# Unofficial CNN Fear and Greed Index

## About the project

This module has been created with the intention of adding this data to the economy menu of [GamestonkTerminal](https://github.com/GamestonkTerminal/GamestonkTerminal).

## Usage

By doing:
```python
from fear_greed_index.CNNFearAndGreedIndex import CNNFearAndGreedIndex

cnn_fg = CNNFearAndGreedIndex()

# plot Fear and Greed charts
fig = plt.figure(figsize=(20, 7))
cnn_fg.plot_all_charts(fig)
plt.show()

# print Fear and Greed complete report
print(cnn_fg.get_complete_report())
```

You can expect something like:

![Fear-and-Greed-Charts](https://user-images.githubusercontent.com/25267873/122658705-5e126580-d168-11eb-8d55-61fe7d6a89fd.png)

```
Fear & Greed Now: 30 (Fear)
   Previous Close: 41 (Fear)
   1 Week Ago: 54 (Neutral)
   1 Month Ago: 35 (Fear)
   1 Year Ago: 51 (Neutral)

Junk Bond Demand: Greed                                                                             [Updated Jun 17 at 8:00pm]
   Investors in low quality junk bonds are accepting 2.03 percentage points in additional yield over safer investment grade corporate bonds. This spread is down from recent levels and indicates that investors are pursuing higher risk strategies.
   (Last changed Jun 8 from an Extreme Greed rating)

Market Volatility: Neutral                                                                          [Updated Jun 18 at 4:14pm]
   The CBOE Volatility Index (VIX) is at 20.70. This is a neutral reading and indicates that market risks appear low.
   (Last changed May 12 from an Extreme Fear rating)

Put and Call Options: Fear                                                                          [Updated Jun 18 at 5:55pm]
   During the last five trading days, volume in put options has lagged volume in call options by 55.47% as investors make bullish bets in their portfolios. However, this is still among the highest levels of put buying seen during the last two years, indicating fear on the part of investors.
   (Last changed Jun 17 from a Greed rating)

Market Momentum: Fear                                                                               [Updated Jun 18 at 5:09pm]
   The S&P 500 is 4.44% above its 125-day average. During the last two years, the S&P 500 has typically been further above this average than it is now, indicating that investors are committing capital to the market at a slower rate than they had been previously.
   (Last changed Jun 17 from a Neutral rating)

Stock Price Strength: Extreme Fear                                                                  [Updated Jun 18 at 4:01pm]
   The number of stocks hitting 52-week highs exceeds the number hitting lows but is at the lower end of its range, indicating extreme fear.
   (Last changed May 20 from a Fear rating)

Stock Price Breadth: Extreme Fear                                                                   [Updated Jun 18 at 4:07pm]
   The McClellan Volume Summation Index measures advancing and declining volume on the NYSE. During the last month, approximately 10.43% more of each day's volume has traded in declining issues than in advancing issues, pushing this indicator towards the lower end of its range for the last two years.
   (Last changed Jun 17 from a Fear rating)

Safe Heaven Demand: Extreme Fear                                                                    [Updated Jun 17 at 8:00pm]
   Stocks and bonds have provided similar returns during the last 20 trading days. However, this has been among the weakest periods for stocks relative to bonds in the past two years and indicates investors are fleeing risky stocks for the safety of bonds.
   (Last changed Apr 30 from a Fear rating)
```

