"""Fear and Greed Index Class"""
__docformat__ = "numpy"

from matplotlib import pyplot as plt
from fear_greed_index import scrape_cnn
from fear_greed_index.FearAndGreedIndicator import FearAndGreedIndicator


class CNNFearAndGreedIndex:
    """CNN Fear and Greed Index"""

    indicator_chart_type = {
        "Junk Bond Demand": "IGHYPtile",
        "Market Volatility": "VIXPtile",
        "Put and Call Options": "PutCallPtile",
        "Market Momentum": "SPXPtile",
        "Stock Price Strength": "NHNLPtile",
        "Stock Price Breadth": "McOscPtile",
        "Safe Heaven Demand": "StkBdPtile",
    }

    def __init__(self):
        """Constructor"""
        self.junk_bond_demand = FearAndGreedIndicator("Junk Bond Demand")
        self.market_volatility = FearAndGreedIndicator("Market Volatility")
        self.put_and_call_options = FearAndGreedIndicator("Put and Call Options")
        self.market_momentum = FearAndGreedIndicator("Market Momentum")
        self.stock_price_strength = FearAndGreedIndicator("Stock Price Strength")
        self.stock_price_breadth = FearAndGreedIndicator("Stock Price Breadth")
        self.safe_heaven_demand = FearAndGreedIndicator("Safe Heaven Demand")
        self.index_summary = "N/A"
        self.index_chart = None
        self.all_indicators = [
            self.junk_bond_demand,
            self.market_volatility,
            self.put_and_call_options,
            self.market_momentum,
            self.stock_price_strength,
            self.stock_price_breadth,
            self.safe_heaven_demand,
        ]

        self._load_fear_and_greed()

    def _load_fear_and_greed(self):
        """Load Fear and Greed Index by scraping CNN data"""
        text_soup_cnn = scrape_cnn._get_fear_greed_index()

        # Fill in indicators summary, last_sentiment, last_changed, update_on
        indicator_idx = 0
        for text in text_soup_cnn.findAll("div", {"class": "modContent feargreed"}):
            for content in text.contents:
                for txt in content.find_all("div", {"class": "wsod_fLeft smarttext"}):
                    self.all_indicators[indicator_idx]._set_summary(
                        txt.contents[0].text
                    )

                    if len(txt.contents) > 1:
                        self.all_indicators[indicator_idx]._set_last_changed(
                            txt.contents[1].text
                        )
                        self.all_indicators[indicator_idx]._set_last_sentiment(
                            txt.contents[1].span.text
                        )

                        if len(txt.contents) > 2:
                            self.all_indicators[indicator_idx]._set_update_on(
                                txt.contents[2].text
                            )

                    indicator_idx += 1

        # Fill in indicator sentiment
        indicator_idx = 0
        for text in text_soup_cnn.findAll("div", {"class": "modContent feargreed"}):
            for content in text.contents:
                for txt in content.find_all("div", {"class": "wsod_fRight"}):

                    if "wsod_fgIndicatorCht" not in txt["class"]:
                        self.all_indicators[indicator_idx]._set_sentiment(
                            txt.contents[0]
                        )
                        indicator_idx += 1

        # Fill in indicators charts
        for indicator in self.all_indicators:
            indicator._set_chart(
                scrape_cnn._get_chart(
                    self.indicator_chart_type[indicator.get_type_indicator()]
                )
            )

        # Fill in fear and greed index
        index_data = (
            text_soup_cnn.findAll("div", {"class": "modContent feargreed"})[0]
            .contents[0]
            .text
        )
        fg_index = [fg + ")" for fg in index_data.split(")")[:-1]]
        self.index_summary = fg_index[0] + "\n   "
        self.index_summary += "\n   ".join(
            [fg.strip("Fear & Greed ") for fg in fg_index[1:]]
        )

        # Fill in index chart
        self.index_chart = scrape_cnn._get_chart("AvgPtileModel")

    def get_junk_bond_demand(self):
        """Get Junk Bond Demand"""
        return self.junk_bond_demand

    def get_market_volatility(self):
        """Get Market Volatility"""
        return self.market_volatility

    def get_put_and_call_options(self):
        """Get Put and Call Options"""
        return self.put_and_call_options

    def get_market_momentum(self):
        """Get Market Momentum"""
        return self.market_momentum

    def get_stock_price_strength(self):
        """Get Stock Price Strength"""
        return self.stock_price_strength

    def get_stock_price_breadth(self):
        """Get Stock Price Breadth"""
        return self.stock_price_breadth

    def get_safe_heaven_demand(self):
        """Get Safe Heaven Demand"""
        return self.safe_heaven_demand

    def get_indicators_report(self):
        """Get Indicators Report"""
        indicators_report = ""
        for indicator in self.all_indicators:
            indicators_report += indicator.get_report() + "\n"
        return indicators_report

    def get_index(self):
        """Get Index Summary"""
        return self.index_summary

    def get_index_chart(self):
        """Get Index Chart"""
        return self.index_chart

    def get_complete_report(self):
        """Plot Complete report"""
        complete_report = self.get_index() + "\n\n"
        complete_report += self.get_indicators_report()
        return complete_report

    def plot_all_charts(self, fig: plt.figure):
        """Plot all indicators and index charts"""
        for i, indicator in enumerate(self.all_indicators):
            ax = fig.add_subplot(3, 3, i + 1)
            ax.set_axis_off()
            plt.imshow(indicator.chart)

        ax = fig.add_subplot(3, 3, 8)
        ax.set_axis_off()
        plt.imshow(self.index_chart)
        fig.subplots_adjust(wspace=0, hspace=-1)
        plt.tight_layout()
        return fig