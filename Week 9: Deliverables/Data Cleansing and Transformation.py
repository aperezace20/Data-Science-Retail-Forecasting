{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "51b5b547",
   "metadata": {},
   "source": [
    "# <span style=\"color:red\">Beverages</span> <span style=\"color:blue\">Business in Australia</span>\n",
    "\n",
    "<img src=\"https://raw.githubusercontent.com/aperezace20/Data-Science-Retail-Forecasting/main/Week%209%3A%20Deliverables/flag-australia-truck-inscription-supply-chain-concept-cargo-transportation-logistics-254500107.jpg\" alt=\"Alt text\" width=\"400\"/>\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0eab72ee",
   "metadata": {},
   "source": [
    "<b> Problem Statement: </b>The large company who is into beverages business in Australia. They sell their products through various super-markets and also engage into heavy promotions throughout the year. Their demand is also influenced by various factors like holiday, seasonality. They needed forecast of each of products at item level every week in weekly buckets.\n",
    "\n",
    "<b> Challenges: </b>The time series data showed a range of patterns, some with trends, some seasonal, and some with neither. At the time, they were using their own software, written in-house, but it often produced forecasts that did not seem sensible. Company wanted to explore power of AI/ML based forecasting to replace their in house local solution"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f210c359",
   "metadata": {},
   "source": [
    "<h2 style=\"background-color:white; color:red; text-align:center;\"><b>Analyzing the Beverage Business in Australia</b></h2>\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "346d49d0",
   "metadata": {},
   "source": [
    "### <font color = #800000> 1.1: </font> <font color = #800000> Importing Python Modules</font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "203f9fd2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import plotly.graph_objs as go\n",
    "from plotly.offline import iplot\n",
    "import requests\n",
    "import io "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8a3963a1",
   "metadata": {},
   "source": [
    "### <font color = #800000> 1.2: </font> <font color = #800000> Importing a Database from GitHub</font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "596b8b97",
   "metadata": {},
   "outputs": [],
   "source": [
    "url1 = \"https://raw.githubusercontent.com/aperezace20/Data-Science-Retail-Forecasting/main/forecasting.csv\"\n",
    "download = requests.get(url1).content\n",
    "forecasting = pd.read_csv(io.StringIO(download.decode('utf-8')))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e349380",
   "metadata": {},
   "source": [
    "### <font color = #800000> 1.3: </font> <font color = #800000> Data Cleaning Best Practices</font>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dfaf6cde",
   "metadata": {},
   "source": [
    "####  <font color = maroon> 1.3.1: Type of Data</font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "42023405",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Product                       object\n",
       "date                  datetime64[ns]\n",
       "Sales                          int64\n",
       "Price Discount (%)            object\n",
       "In-Store Promo                 int64\n",
       "Catalogue Promo                int64\n",
       "Store End Promo                int64\n",
       "Google_Mobility              float64\n",
       "Covid_Flag                     int64\n",
       "V_DAY                          int64\n",
       "EASTER                         int64\n",
       "CHRISTMAS                      int64\n",
       "month                          int64\n",
       "dtype: object"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forecasting.dtypes"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b0160bd9",
   "metadata": {},
   "source": [
    "####  <font color = maroon> 1.3.2: Head & Tail </font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "b28b24c7",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>date</th>\n",
       "      <th>Sales</th>\n",
       "      <th>Price Discount (%)</th>\n",
       "      <th>In-Store Promo</th>\n",
       "      <th>Catalogue Promo</th>\n",
       "      <th>Store End Promo</th>\n",
       "      <th>Google_Mobility</th>\n",
       "      <th>Covid_Flag</th>\n",
       "      <th>V_DAY</th>\n",
       "      <th>EASTER</th>\n",
       "      <th>CHRISTMAS</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>SKU1</td>\n",
       "      <td>2/5/2017</td>\n",
       "      <td>27750</td>\n",
       "      <td>0%</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>SKU1</td>\n",
       "      <td>2/12/2017</td>\n",
       "      <td>29023</td>\n",
       "      <td>0%</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>SKU1</td>\n",
       "      <td>2/19/2017</td>\n",
       "      <td>45630</td>\n",
       "      <td>17%</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>SKU1</td>\n",
       "      <td>2/26/2017</td>\n",
       "      <td>26789</td>\n",
       "      <td>0%</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>SKU1</td>\n",
       "      <td>3/5/2017</td>\n",
       "      <td>41999</td>\n",
       "      <td>17%</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Product       date  Sales Price Discount (%)  In-Store Promo  \\\n",
       "0    SKU1   2/5/2017  27750                 0%               0   \n",
       "1    SKU1  2/12/2017  29023                 0%               1   \n",
       "2    SKU1  2/19/2017  45630                17%               0   \n",
       "3    SKU1  2/26/2017  26789                 0%               1   \n",
       "4    SKU1   3/5/2017  41999                17%               0   \n",
       "\n",
       "   Catalogue Promo  Store End Promo  Google_Mobility  Covid_Flag  V_DAY  \\\n",
       "0                0                0              0.0           0      0   \n",
       "1                0                1              0.0           0      1   \n",
       "2                0                0              0.0           0      0   \n",
       "3                0                1              0.0           0      0   \n",
       "4                0                0              0.0           0      0   \n",
       "\n",
       "   EASTER  CHRISTMAS  \n",
       "0       0          0  \n",
       "1       0          0  \n",
       "2       0          0  \n",
       "3       0          0  \n",
       "4       0          0  "
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forecasting.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b6c576b3",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>date</th>\n",
       "      <th>Sales</th>\n",
       "      <th>Price Discount (%)</th>\n",
       "      <th>In-Store Promo</th>\n",
       "      <th>Catalogue Promo</th>\n",
       "      <th>Store End Promo</th>\n",
       "      <th>Google_Mobility</th>\n",
       "      <th>Covid_Flag</th>\n",
       "      <th>V_DAY</th>\n",
       "      <th>EASTER</th>\n",
       "      <th>CHRISTMAS</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1213</th>\n",
       "      <td>SKU6</td>\n",
       "      <td>10/18/2020</td>\n",
       "      <td>96619</td>\n",
       "      <td>54%</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>-7.56</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1214</th>\n",
       "      <td>SKU6</td>\n",
       "      <td>10/25/2020</td>\n",
       "      <td>115798</td>\n",
       "      <td>52%</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>-8.39</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1215</th>\n",
       "      <td>SKU6</td>\n",
       "      <td>11/1/2020</td>\n",
       "      <td>152186</td>\n",
       "      <td>54%</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>-7.43</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1216</th>\n",
       "      <td>SKU6</td>\n",
       "      <td>11/8/2020</td>\n",
       "      <td>26445</td>\n",
       "      <td>44%</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>-5.95</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1217</th>\n",
       "      <td>SKU6</td>\n",
       "      <td>11/15/2020</td>\n",
       "      <td>26414</td>\n",
       "      <td>44%</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>-7.20</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Product        date   Sales Price Discount (%)  In-Store Promo  \\\n",
       "1213    SKU6  10/18/2020   96619                54%               0   \n",
       "1214    SKU6  10/25/2020  115798                52%               0   \n",
       "1215    SKU6   11/1/2020  152186                54%               1   \n",
       "1216    SKU6   11/8/2020   26445                44%               1   \n",
       "1217    SKU6  11/15/2020   26414                44%               0   \n",
       "\n",
       "      Catalogue Promo  Store End Promo  Google_Mobility  Covid_Flag  V_DAY  \\\n",
       "1213                1                0            -7.56           1      0   \n",
       "1214                1                0            -8.39           1      0   \n",
       "1215                0                1            -7.43           1      0   \n",
       "1216                0                1            -5.95           1      0   \n",
       "1217                0                0            -7.20           1      0   \n",
       "\n",
       "      EASTER  CHRISTMAS  \n",
       "1213       0          0  \n",
       "1214       0          0  \n",
       "1215       0          0  \n",
       "1216       0          0  \n",
       "1217       0          0  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forecasting.tail()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1eaf1136",
   "metadata": {},
   "source": [
    "#### <font color = maroon> 1.3.3: Shape of Data</font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a68f4c2b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1218, 12)"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forecasting.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b05f49eb",
   "metadata": {},
   "source": [
    "#### <font color = maroon> 1.3.4: Missing Values</font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3fd406aa",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Product               0\n",
       "date                  0\n",
       "Sales                 0\n",
       "Price Discount (%)    0\n",
       "In-Store Promo        0\n",
       "Catalogue Promo       0\n",
       "Store End Promo       0\n",
       "Google_Mobility       0\n",
       "Covid_Flag            0\n",
       "V_DAY                 0\n",
       "EASTER                0\n",
       "CHRISTMAS             0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forecasting.isnull().sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dedce617",
   "metadata": {},
   "source": [
    "#### <font color = maroon> 1.3.5: Data Size</font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "57fb0a62",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "14616"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forecasting.size"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d9bf25cb",
   "metadata": {},
   "source": [
    "#### <font color = maroon> 1.3.6: Split by Month & Adding Column Month</font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "99b9e238",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "     Product       date   Sales Price Discount (%)  In-Store Promo  \\\n",
      "0       SKU1 2017-02-05   27750                 0%               0   \n",
      "1       SKU1 2017-02-12   29023                 0%               1   \n",
      "2       SKU1 2017-02-19   45630                17%               0   \n",
      "3       SKU1 2017-02-26   26789                 0%               1   \n",
      "4       SKU1 2017-03-05   41999                17%               0   \n",
      "...      ...        ...     ...                ...             ...   \n",
      "1213    SKU6 2020-10-18   96619                54%               0   \n",
      "1214    SKU6 2020-10-25  115798                52%               0   \n",
      "1215    SKU6 2020-11-01  152186                54%               1   \n",
      "1216    SKU6 2020-11-08   26445                44%               1   \n",
      "1217    SKU6 2020-11-15   26414                44%               0   \n",
      "\n",
      "      Catalogue Promo  Store End Promo  Google_Mobility  Covid_Flag  V_DAY  \\\n",
      "0                   0                0             0.00           0      0   \n",
      "1                   0                1             0.00           0      1   \n",
      "2                   0                0             0.00           0      0   \n",
      "3                   0                1             0.00           0      0   \n",
      "4                   0                0             0.00           0      0   \n",
      "...               ...              ...              ...         ...    ...   \n",
      "1213                1                0            -7.56           1      0   \n",
      "1214                1                0            -8.39           1      0   \n",
      "1215                0                1            -7.43           1      0   \n",
      "1216                0                1            -5.95           1      0   \n",
      "1217                0                0            -7.20           1      0   \n",
      "\n",
      "      EASTER  CHRISTMAS  month  \n",
      "0          0          0      2  \n",
      "1          0          0      2  \n",
      "2          0          0      2  \n",
      "3          0          0      2  \n",
      "4          0          0      3  \n",
      "...      ...        ...    ...  \n",
      "1213       0          0     10  \n",
      "1214       0          0     10  \n",
      "1215       0          0     11  \n",
      "1216       0          0     11  \n",
      "1217       0          0     11  \n",
      "\n",
      "[1218 rows x 13 columns]\n"
     ]
    }
   ],
   "source": [
    "forecasting['date'] = pd.to_datetime(forecasting['date'])\n",
    "\n",
    "def get_month(dt):\n",
    "    return dt.month\n",
    "\n",
    "forecasting['month'] = forecasting['date'].apply(get_month)\n",
    "\n",
    "print(forecasting)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8d2da33d",
   "metadata": {},
   "source": [
    "#### <font color = maroon> 1.3.7: Checking the head</font>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "810efb39",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Product</th>\n",
       "      <th>date</th>\n",
       "      <th>Sales</th>\n",
       "      <th>Price Discount (%)</th>\n",
       "      <th>In-Store Promo</th>\n",
       "      <th>Catalogue Promo</th>\n",
       "      <th>Store End Promo</th>\n",
       "      <th>Google_Mobility</th>\n",
       "      <th>Covid_Flag</th>\n",
       "      <th>V_DAY</th>\n",
       "      <th>EASTER</th>\n",
       "      <th>CHRISTMAS</th>\n",
       "      <th>month</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>SKU1</td>\n",
       "      <td>2017-02-05</td>\n",
       "      <td>27750</td>\n",
       "      <td>0%</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>SKU1</td>\n",
       "      <td>2017-02-12</td>\n",
       "      <td>29023</td>\n",
       "      <td>0%</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>SKU1</td>\n",
       "      <td>2017-02-19</td>\n",
       "      <td>45630</td>\n",
       "      <td>17%</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>SKU1</td>\n",
       "      <td>2017-02-26</td>\n",
       "      <td>26789</td>\n",
       "      <td>0%</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>SKU1</td>\n",
       "      <td>2017-03-05</td>\n",
       "      <td>41999</td>\n",
       "      <td>17%</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Product       date  Sales Price Discount (%)  In-Store Promo  \\\n",
       "0    SKU1 2017-02-05  27750                 0%               0   \n",
       "1    SKU1 2017-02-12  29023                 0%               1   \n",
       "2    SKU1 2017-02-19  45630                17%               0   \n",
       "3    SKU1 2017-02-26  26789                 0%               1   \n",
       "4    SKU1 2017-03-05  41999                17%               0   \n",
       "\n",
       "   Catalogue Promo  Store End Promo  Google_Mobility  Covid_Flag  V_DAY  \\\n",
       "0                0                0              0.0           0      0   \n",
       "1                0                1              0.0           0      1   \n",
       "2                0                0              0.0           0      0   \n",
       "3                0                1              0.0           0      0   \n",
       "4                0                0              0.0           0      0   \n",
       "\n",
       "   EASTER  CHRISTMAS  month  \n",
       "0       0          0      2  \n",
       "1       0          0      2  \n",
       "2       0          0      2  \n",
       "3       0          0      2  \n",
       "4       0          0      3  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forecasting.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "934350a4",
   "metadata": {},
   "source": [
    "#### <font color = maroon> 1.3.8: Groupby Months & Sales "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "1b1c0b8b",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "month\n",
       "1     1593297\n",
       "2     2519111\n",
       "3     2896089\n",
       "4     2703389\n",
       "5     2935247\n",
       "6     3741038\n",
       "7     3155868\n",
       "8     3368431\n",
       "9     3904996\n",
       "10    3948299\n",
       "11    3293141\n",
       "12    2840013\n",
       "Name: Sales, dtype: int64"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "forecasting.groupby('month')['Sales'].sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72dc961d",
   "metadata": {},
   "source": [
    "#### <font color = maroon> 1.3.9: Bar Graph Months & Sales "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7465e2d",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
