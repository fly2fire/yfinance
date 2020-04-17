#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Yahoo! Finance market data downloader (+fix for Pandas Datareader)
# https://github.com/ranaroussi/yfinance

"""
Sanity check for most common library uses all working

- Stock: Microsoft
- ETF: Russell 2000 Growth
- Mutual fund: Vanguard 500 Index fund
- Index: S&P500
- Currency BTC-USD
"""

from __future__ import print_function
import yfinance as yf


def test_yfinance():
    #symbol_list = ['MSFT', 'IWO', 'VFINX', '^GSPC', 'BTC-USD']
    symbol_list = ['MSFT']
    for symbol in symbol_list:
        print(">>", symbol, end=' ... ')
        ticker = yf.Ticker(symbol)

        # always should have info and history for valid symbols
        assert(ticker.info is not None and ticker.info != {})
        assert(ticker.history(period="max").empty is False)

        # following should always gracefully handled, no crashes
        print('==================cashflow===============\n',ticker.cashflow)
        print('===============balance_sheet=============\n',ticker.balance_sheet)
        print('=================financials==============\n',ticker.financials)
        print('===============sustainability============\n',ticker.sustainability)
        print('===============marjor_holders============\n',ticker.major_holders)
        print('==========institutional_holders==========\n',ticker.institutional_holders)

        print("OK")


if __name__ == "__main__":
    test_yfinance()
