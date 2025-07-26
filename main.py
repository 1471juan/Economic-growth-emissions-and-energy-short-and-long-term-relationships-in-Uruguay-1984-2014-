import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller, coint
from statsmodels.tsa.vector_ar.vecm import coint_johansen, VECM

#########################
#LOAD DATA FROM CSV FILES
data_fossilConsumption = pd.read_csv('data/FossilConsumption.csv', parse_dates=['YEAR'])
data_population = pd.read_csv('data/TotalPopulation.csv', parse_dates=['YEAR'])
data_agr_va= pd.read_csv('data/Agriculture_forestry_fishing_value_added.csv', parse_dates=['YEAR'])
data_realgdp = pd.read_csv('data/real_gdp_uruguay.csv', parse_dates=['YEAR'])
data_totalghg = pd.read_csv('data/Total_GHG_emissions.csv', parse_dates=['YEAR'])

###########
#DATAFRAMES
for dataframe in [data_fossilConsumption, data_agr_va, data_realgdp, data_totalghg, data_population]:
    dataframe.set_index('YEAR', inplace=True)
dataframe = pd.DataFrame(index=data_fossilConsumption.index)
dataframe['totalghg'] = np.log(data_totalghg['VALUE'] / data_population['VALUE'])
dataframe['fossil'] = np.log(data_fossilConsumption['VALUE'])
dataframe['agr_va'] = np.log(data_agr_va['VALUE'])
dataframe['realgdp'] = np.log(data_realgdp['VALUE'] / data_population['VALUE'])

dataframe['realgdp_squared'] = dataframe['realgdp'] ** 2

dataframe.dropna(inplace=True)

dataframe_kec = pd.DataFrame({
    'totalghg': dataframe['totalghg'],
    'realgdp': dataframe['realgdp'],
    'realgdp_squared': dataframe['realgdp_squared']
}).dropna()

#VECM is automatically run at first difference(use variables at level)
def model_VECM(df):
    #I used 'lo' because I see some series have a trend.
    vecm = VECM(df, k_ar_diff=1, coint_rank=1, deterministic='lo')
    vecm_fit = vecm.fit()
    print(vecm_fit.summary())
    irf = vecm_fit.irf(10)
    irf.plot(orth=True, signif=0.1)
    plt.show()

#Use variables on their level(not on differences)
def Johansen_cointegration(df): 
    #JOHANSEN COINTEGRATION TEST
    model = coint_johansen(df, det_order=0, k_ar_diff=1)
    print(model)
    print("Statistic value:", model.lr1)
    #print("Critical values :", model.cvt)
    print("Critical values (95%):", model.cvt[:, 1])

#DICKEY FULLER
def adf(serie,a):
    result = adfuller(serie, regression=a)
    tag = ['statistic', 'p-value', 'lags', 'obs']
    for value, q in zip(result[:4], tag):
        print(f'{q:20}: {value:.4f}')
    print('\n critical vlaue:')
    for x, value in result[4].items():
        print(f' Level {x:>4} : {value:.4f}')
    #AIC
    print(f'\nAIC: {result[5]:.4f}')

def E_G_cointegration(serie1,serie2):
    #Engle-Granger
    result = coint(serie1, serie2, trend='c')
    stat, p, c = result
    print(f'trace statistic: {stat:.4f}')
    print(f'p-value: {p:.4f}')
    print('critical values:')
    print(c)

    
def plot_k_curve():
    sns.set_theme(style='whitegrid')
    plt.figure(figsize=(10, 6))

    sns.regplot(
        x='realgdp', y='totalghg', data=dataframe_kec,
        order=2,
        ci=None,
        scatter_kws={'s': 20,'color': "#4A7200", 'alpha': 0.9},
        line_kws={'color': "#5fa834", 'linewidth': 3}
    )

    turning_point=10.019

    plt.axvline(turning_point, color='red', linestyle='--', label='Turning Point')
    plt.title('Environmental Kuznets Curve (EKC) in Uruguay (1984-2014)')
    plt.xlabel('Log of Real GDP per Capita')
    plt.ylabel('GHG Emissions per Capita')
    plt.legend()
    plt.tight_layout()
    plt.show()

#Dickey fuller test
#adf(dataframe['agr_va'].diff().dropna(),'c')
#adf(dataframe['realgdp_squared'].diff().dropna(),'c')

#realgdp: trend
#fossil: constant
#totalghg: trend
#agr_va: trend

#plt.plot(dataframe['agr_va'])
#plt.show()

##########################
#Johansen_cointegration(dataframe_kec)
#model_VAR()
#model_VECM(dataframe_kec)
#plot_k_curve()
