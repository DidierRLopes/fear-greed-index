"""Scrape CNN HTML helper"""
__docformat__ = "numpy"

import random
import requests
from bs4 import BeautifulSoup
import io
from PIL import Image
from matplotlib import pyplot as plt


def _get_user_agent() -> str:
    """Get a random User-Agent strings from a list of some recent real browsers

    Parameters
    ----------
    None

    Returns
    -------
    str
        random User-Agent strings
    """
    user_agent_strings = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:86.1) Gecko/20100101 Firefox/86.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:86.1) Gecko/20100101 Firefox/86.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:82.1) Gecko/20100101 Firefox/82.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:86.0) Gecko/20100101 Firefox/86.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:86.0) Gecko/20100101 Firefox/86.0",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:83.0) Gecko/20100101 Firefox/83.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:84.0) Gecko/20100101 Firefox/84.0",
    ]

    return random.choice(user_agent_strings)


def _get_html(url: str):
    """Wraps HTTP requests.get for testibility.
    Fake the user agent by changing the User-Agent header of the request
    and bypass such User-Agent based blocking scripts used by websites.

    Parameters
    ----------
    url : str
        HTML page URL

    Returns
    -------
    str
        HTML page
    """
    return requests.get(url, headers={"User-Agent": _get_user_agent()}).text


def _get_fear_greed_index():
    """Scrapes CNN Fear and Greed Index HTML page

    Parameters
    ----------
    None

    Returns
    -------
    BeautifulSoup
        CNN Fear And Greed Index HTML page
    """
    return BeautifulSoup(
        _get_html("https://money.cnn.com/data/fear-and-greed/"),
        "lxml",
    )


def _get_chart(chart_type: str) -> Image:
    """Scrapes Chart image from CNN Fear and Greed Index HTML

    Parameters
    ----------
    chart_type : str
        Chart_type to scrape

    Returns
    -------
    Image
        Chart Image
    """
    r = requests.get(
        f"http://markets.money.cnn.com/Marketsdata/Api/Chart/FearGreedHistoricalImage?chartType={chart_type}"
    )
    r.raise_for_status()
    r.raw.decode_content = True
    dataBytesIO = io.BytesIO(r.content)
    return Image.open(dataBytesIO)
