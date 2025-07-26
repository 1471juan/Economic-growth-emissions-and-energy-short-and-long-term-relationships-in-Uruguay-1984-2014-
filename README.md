# Economic-growth-emissions-and-energy-short-and-long-term-relationships-in-Uruguay-1984-2014-
Test for the environmental Kuznets curve hypotesis, and cointegration analysis between real GDP per capita, GHG emissions per capita, Fossil fuel energy consumption and Agriculture, forestry, and fishing, value added in Uruguay between 1984 and 2014. 

## Introduction
The objective of this analysis is to test for cointegration and build an error correction model. I'll be using the real GDP per capita, GHG emissions per capita, fossil fuel consumption and a variable that represents the agriculture and livestock sector due to their theoretical relevance and potential for cointegration. the period choosen was between 1984 and 2014.
This period was selected because of the production matrix change of Uruguay after the dictatorship of the 70s and 80s debt crisis of 'la tablita', there was a clear structural turn from commodities production to services. Also, this period reflects, except for the 2002 crisis, a pretty stable economy, especially after the 90s with the price stabilization plan. There is too, an interest before the complete change of the energy production system to alternative renewable sources, namely biomass, wind power, and mini-hydro. In 2014, Uruguay had the most wind power capacity per capita in the world. In 2018, wind farms generated 40% of the total energy produced by the entire system in Uruguay.

First I tested all four variables with an augmented dickey fuller unit root test, in order to check if they are stationary, then I'll run a Johansen cointegration test(I won't be using the Engle-Granger test because I am doing a multivariate analysis.) and use an error correction model(VECM) to analyze the dynamic short and long term relationship between the variables, making use of the impulse response functions to see the behaviour in face of external shocks of the other variables.
Finally, I'll test the environmental Kuznets curve hypothesis for Uruguay by using the error correction model with the real GDP per capita as a quadratic and the GHG emissions per capita, and then find the turning point value after which economic growth implicates lower pollution levels.

I had trouble finding relevant variables, environmental information is not generally publicly available for developing countries like Uruguay. However, all of this time series were recopilated from the worldbank webpage as csv files. I took the series for Uruguay and created a separated file with google sheets, and then imported it into python with the pandas library. Then use the 'YEAR' column as an index to create a dataframe for the analysis, the result is 30 observations from the period 1984 to 2014.

The Total GHG emissions and Total GDP were modified so they are in per capita terms, this was done by dividing them with the corresponding total Uruguay population for each year.

## Variables
All of the following series contained data from different countries with different periods, for this analysis, as described earlier, we focus on Uruguay between 1984 and 2014.

<u>GDP (constant 2015 US$) - Uruguay</u>
Uruguay’s GDP, reported in constant 2015 US dollars, reflects the real value of all goods and services produced within its borders over time. This inflation-adjusted figure allows for accurate comparisons across years by neutralizing the effects of price changes. The indicator can be estimated through various approaches, expenditure, income, or production and serves as a foundational measure of the country’s economic activity.

<u>Fossil fuel energy consumption (% of total)</u>
Fossil fuel energy consumption data from 1960 to 2015, showing how dependent a country is on energy derived from coal, oil, and natural gas. This metric, expressed as a percentage of total energy use, originates from the International Energy Agency (IEA), a trusted authority in global energy statistics.

<u>Agriculture, forestry, and fishing, value added (% of GDP)</u>
The share of agriculture, forestry, and fishing in GDP measures the economic contribution of natural resource based activities. It includes crop cultivation, animal husbandry, timber harvesting, and fishing. By calculating value added, net output after subtracting intermediate consumption, this indicator reveals the structural composition of the economy and can signal shifts from rural-based to more industrial or service-oriented development.

<u>Total greenhouse gas emissions excluding LULUCF (Mt CO2e)</u>
Total greenhouse gas emissions(GHG), excluding those from land-use change and forestry (LULUCF), track the annual emissions of major gases like carbon dioxide, methane, and nitrous oxide, alongside industrial compounds. These are standardized to CO2 equivalent figures using IPCC conversion factors, allowing comparability. By turning the variable into per capita, it reflects the average environmental impact of individuals in a country, highlighting patterns in energy, waste, industrial, and agricultural emissions over time and being comparable to real GDP per capita.
## Augmented dickey fuller and Johansen cointegration tests
In order to test for stationarity, I used the adfuller function from the statmodels library. By using an iterative process, we can test, and if the series is not stationary, we differenciate the series and try again, until we reject the null hypotesis of stationarity. I made use of visual tools to check for a constant mean in the series.
After repeating this process with all the variables, they were all integrated of order 1, meaning they have to be differenciated once in order to get stationarity. Only then I moved forward and tested for cointegration.

The ADF test has shown that the data mets the criteria to be tested for cointegration, they all have the same integration order.

For the cointegration test, I used the coint_johansen function from the statsmodels library. The series were tested on level, not with the differences applied.
The trace statistic was greater than the critical value in this first hypothesis with 95% confidence. Specifically, for the null hypothesis that there are zero cointegrating relationships, the trace statistic value is 58.2007 which is greater than the critical value of 47.854, meaning we have enough statistical evidence to reject the null hypothesis of zero cointegrating equations in the model at 95% confidence level. The same can't be said for the rest hypothesis, meaning we can't assure there is more than one cointegrating equation.

The Johansen cointegration test has shown that there is a unique cointegration relationship between the variables, meaning they share a similar long term trend.

## Vector Error Correction Model(VECM)
The trend coefficient is significant at 95% confidence for all variables except for realgdp, which has a trend coefficient statistically significant at 90%

I'll proceed to interpret the short term effects for the fossil variable, its own past persists, a 1% increase of the fossil fuel energy consumption will increase 0.6291% in the next period with a 95% significance. An 1% increase of the real GDP per capita will lead to a positive 1.4076% change in the fossil fuel energy consumption, with a 99% confidence.

For the agr_va variable, a 1% increase of the fossil variable will lead to a reduction of agriculture, forestry, and fishing value added as a percentage of the GDP in -0.8332%. 
An 1% increase of the real GDP per capita will lead to a positive 1.4458% change in the agriculture, forestry, and fishing value added as a percentage of the GDP, with a 95% confidence.

The real GDP per capita has a positive relationship with its own past, specifically with the previous year's value.

The GHG emission per capita have a positive relationship with the real GDP per capita. A 1% change on the real GDP per capita will lead to a positive increase of 0.6242% in the GHG emissions per capita with 99% confidence

When we analyze the error correction coefficient, that is, the long term adjustment, fossil, agr_va and totalghg actively participate in the long term adjustment mechanism, however realgdp coefficient has p-value of 0.178.
All the β coefficients are positive and highly significant, with p-values lower than 0.01. This could indicate a stable long term relationship between fossil, agr_va, realgdpd and totalghg.

#### Interpretation of the results
There is a clear positive relationship with the shocks from real GDP per capita and the fossil fuel energy consumption, however, this relationship is not clear in the reverse order, this means an increase in the usage of fossil fuel as energy, doesn't necessarily increase GDP per capita, but as the economy grows, there is an increasing need for energy consumption, and in this period, agents agents use more of this energy source to satisfy this need. In the long term this relationship is negative, this might be because of the structural change on the energy sources in the production system.

It could indicate an increase of urbanization and usage of vehicles, as the individuals get more income, they can afford to import personal vehicles, and businesses adopt vehicles to increase efficiency, more data would be needed to analyze this hypothesis.

The usage of a trend made sense, as most of the variables had significant trends in the short term.

The agr_var increases as the GHG emissions per capita increase, this might be due of the environmental pollution of livestock and agriculture, plus the destruction of biodiversity and inefficient production techniques. We must remember the production matrix of Uruguay is mostly composed of commodities and it's a big exportator of products such as meat. 

The GHG emissions per capita are impacted positively by real GDP per capita and Fossil fuel energy consumption in the short term. This makes sense and it's the expected relationship. The higher the production, the higher the energy consumption from environmentally harmful sources and the higher the GHG emissions, even though the fossil coefficient wasn't statistically significant.

This model shows a partial transition from the usage of fossil fuel energy consumption and its impact on emissions, as we discussed earlier, this happened due to the adoption of alternative energy sources. The agriculture and livestock sector doesn't seem to have a statistically strong impact over other variables on the short term.

Analyzing the long term, with the following equation(cointegration relations),

totalghgt​ = 0.8236⋅agr_vat​ + 0.2248⋅realgdpt ​+ 0.8660⋅fossilt​ + error

The fossil variable has the highest coefficient with the value 0.8660, this means fossil fuel energy consumption is the lead cause of emissions in the long term and should be regulated. In respect to the agr_va variable, while I couldn't analyze the model with more than one lag, and no statistically significant evidence of its impact over GHG emissions per capita was found on the short term, there is a clear positive effect over the emissions on the long term. 
Interestingly, real GDP per capita has the least impact of the three variables, this might be explained by the lack of an industrial sector in the country. All the coefficients are positive and highly statistically significant.

## Impulse response functions(IRF)
<img width="1920" height="975" alt="VECM_90confidence" src="https://github.com/user-attachments/assets/4d2dd035-7294-4228-b649-5ab0ef4ef69c" />


Let's analyze the most important relationships. An unexpected positive shock on the real GDP per capitia impacts positively on GHG emissions per capita(totalghg), this shock then impacts negatively after the second period, then, the shock remains with its negative impact over time, as it can be seen with the confidence interval bounds, the shock doesn't converge to zero. 
The shock behaves similarly over the fossil fuel energy consumption, but unlike with the other variable, the shock dies over time.

Shocks on the GDP per capita impact negatively on the non industral sector, represented in this model by the Agriculture and livestock variable. This might be caused by the transition to a service economy and urbanization.

Another interesting relationship is the impact on the Agriculture and livestock over fossil consumption, it impacts negatively until the second year, when the shock impact is reversed and then dies.
The rural sector may initially be forced to reduce fossil use due to adoption of renewable energy, efficient machinery, or low-energy practices. Unlike the industrial sector, agriculture is labour rather than energy intensive, which may explain the initial negative behaviour, later, rural businesses' need for fossil fuel energy use could be explained by seasonality, there are long periods in which crop production or animal growth don't make use of this kind of energy.

Lastly, GHG emissions per capita shocks will have an immediate positive impact over fossil fuel energy consumption. This is expected as fossil fuel combustion is a major source of GHGs, and if the initial shock is explained by economic growth, it would make sense that the agents would need to increase energy consumption to satisfy the higher production, implying there is not yet a complete transition to renewable energy sources.

## Environmental Kuznets curve
The environmental Kuznets curve (EKC) is a hypotesis about the relationship between pollution and economic development, the environmental problems get worse as the economy grows, but after a certain turning point, where the average income is high enough, the relationship is reversed. So, "the solution to pollution is economic growth.".
This is a known hypothesis, emissions increase with GDP up to a point, then decrease.

For the following analysis I created a new variable, the square of the logarithm of real GDP per capita, and then run an ADF to be sure it is integrated of order 1, the first difference had a p-value of 0.0123, rejecting the null hypotesis.
Then I run the johansens cointegration test, but only with the GHG emissions per capita, real GDP per capita and it's quadratic form.

From the test, the trace statistic value is 43.29 and the critical value at 95% confidence is 29.79, therefore we can reject the null hypotesis of zero cointegration equations, meaning there is at least one cointegration relationship, but there is not enough statistical evidence of more than one.

The next step is running the VECM and checking the following equation:

log_totalghg = β1log_totalghg + β2log_​realgdp + β3(log_​realgdp)^2 + error

If we get  β2>0 and then β3<0 we found evidence of the environmental Kuznets curve in Uruguay between 1984 and 2014, which is as we discussed earlier, a period in which Uruguay transitioned to a services economy.
With a confidence of 99%, we can say β2 = 2.3206 > 0 and β3 = -0.1158 < 0

We can maximize this function and get the turning point, that is, the point in which higher economic growth implies lower pollution.
In this case:
dlog_totalghg/dlog_realgdp = β2+2β3(log_realgdp) = 0
log_realgdp = -β2 / 2β3
therefore, the turning point is:
turning point = -2.3206 / 2(-0.1158) = 10.019
Because the variable is in logarithms, we apply an exponential expression to get the value.
Therefore the real GDP per capita would be aproximately 22,448.96 USD. 

The results of the VECM model confirm the existence of a long-term nonlinear relationship between real GDP per capita and GHG emissions emissions per capita in Uruguay between 1984 and 2014, verifying the environmental kuznets curve hypothesis. Emissions increase with economic growth until reaching a turning point, estimated at approximately US$22,448.96 (GDP per capita in constant 2015 prices). Beyond this income level, emissions begin to decline, showing shifts in the energy source usage toward renewable alternatives, and environmental policies implemented in the country. This result suggests that during the period, Uruguay may have begun a transition toward more sustainable development beyond a certain income threshold.

<img width="1920" height="975" alt="ekcfigure" src="https://github.com/user-attachments/assets/f8ed10d1-8d5e-493c-812a-5a8821db2501" />

## Sources
- https://es.wikipedia.org/wiki/Energ%C3%ADa_e%C3%B3lica_en_Uruguay
- https://en.wikipedia.org/wiki/Kuznets_curve#Environmental_Kuznets_curve
- Fossil fuel energy consumption (% of total) https://data360.worldbank.org/en/indicator/WB_ESG_EG_USE_COMM_FO_ZS?utm_source=chatgpt.com
- Total population https://data360.worldbank.org/en/indicator/WB_WDI_SP_POP_TOTL
- Agriculture, forestry, and fishing, value added (% of GDP) API_NV.AGR.TOTL.ZS_DS2_en_csv_v2_21645 https://data.worldbank.org/indicator/NV.AGR.TOTL.ZS
- GDP (constant 2015 US$) - Uruguay https://data.worldbank.org/indicator/NY.GDP.MKTP.KD?locations=UY
- Total greenhouse gas emissions excluding LULUCF (Mt CO2e) https://data.worldbank.org/indicator/EN.GHG.ALL.MT.CE.AR5

