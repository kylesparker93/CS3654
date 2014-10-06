import pandas as pd
import Quandl
# 5

bitStampUSD = pd.DataFrame(Quandl.get("BCHARTS/BITSTAMPUSD", trim_start="2011-09-13", trim_end="2014-09-30", authtoken="8asAGRt2jn6feJDk3uLw"))
bitFinexUSD = pd.DataFrame(Quandl.get("BCHARTS/BITFINEXUSD", trim_start="2013-03-31", trim_end="2014-09-30", authtoken="8asAGRt2jn6feJDk3uLw"))
lakeUSD = pd.DataFrame(Quandl.get("BCHARTS/LAKEUSD", trim_start="2014-03-01", trim_end="2014-09-30", authtoken="8asAGRt2jn6feJDk3uLw"))


# 6
bitStampUSD.head()
# Columns are: Date, Open, High, Low, Close, Volume (BTC), Volume (Currency), Weighted Price
# Data is updated daily

bitFinexUSD.head()
# Columns are: Date, Open, High, Low, Close, Volume (BTC), Volume (Currency), Weighted Price
# Data is updated daily

lakeUSD.head()
# Columns are: Date, Open, High, Low, Close, Volume (BTC), Volume (Currency), Weighted Price
# Data is updated daily


# 7
ind1 = bitStampUSD.index
ind2 = bitFinexUSD.index
ind3 = lakeUSD.index


# 8
ind1
# 1116 elements
ind2
# 551 elements
ind3
# 216 elements

# 9
ind1.values
ind2.values
ind3.values
# all three are arrays of 'datetime64[ns]' objects

# 10
bitStampUSD.columns
bitFinexUSD.columns
lakeUSD.columns
# there are 7 columns in all three data frames

# 11
bitStampUSD = bitStampUSD.drop('Volume (BTC)', 1)
bitFinexUSD = bitFinexUSD.drop('Volume (BTC)', 1)
lakeUSD = lakeUSD.drop('Volume (BTC)', 1)