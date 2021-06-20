"""Fear and Greed Indicator Class"""
__docformat__ = "numpy"


class FearAndGreedIndicator:
    """Fear and Greed Indicator"""

    def __init__(self, type_indicator: str):
        """Constructor

        Parameters
        ----------
        type_indicator : str
            Between the 7 Indicators: Junk Bond Demand, Market Volatility, Market Volatility,
            Put and Call Options, Market Momentum, Stock Price Strength, Stock Price Breadth,
            Safe Heaven Demand"
        """
        self.type_indicator = type_indicator
        self.sentiment = "N/A"
        self.summary = "N/A"
        self.last_sentiment = "N/A"
        self.last_changed = "N/A"
        self.update_on = "N/A"
        self.chart = None

    def _set_sentiment(self, sentiment):
        """Set indicator sentiment"""
        self.sentiment = sentiment

    def _set_summary(self, summary):
        """Set indicator summary"""
        self.summary = summary

    def _set_last_sentiment(self, last_sentiment):
        """Set indicator last_sentiment"""
        self.last_sentiment = last_sentiment

    def _set_last_changed(self, last_changed):
        """Set indicator last_changed"""
        self.last_changed = last_changed

    def _set_update_on(self, update_on):
        """Set indicator update_on"""
        self.update_on = update_on

    def _set_chart(self, chart):
        """Set indicator chart"""
        self.chart = chart

    def get_sentiment(self):
        """Get indicator sentiment"""
        return self.sentiment

    def get_summary(self):
        """Get indicator summary"""
        return self.summary

    def get_last_sentiment(self):
        """Get indicator last sentiment"""
        return self.last_sentiment

    def get_last_changed(self):
        """Get indicator last changed"""
        return self.last_changed

    def get_update_on(self):
        """Get indicator update on"""
        return self.update_on

    def get_type_indicator(self):
        """Get indicator type"""
        return self.type_indicator

    def get_chart(self):
        """Get indicator chart"""
        return self.chart

    def get_report(self):
        report = f"{self.type_indicator}: {self.sentiment}\t\t[{self.update_on}]\n"
        report += f"   {self.summary}\n"
        report += f"   {self.last_changed}\n"
        return report
