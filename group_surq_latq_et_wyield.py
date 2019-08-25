import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# read the data
data_flow = pd.read_excel('.\observed_simulated.xlsx')

# copy the data from the read excel into the new dataframe
# flow_dataframe = data_flow[['Date', 'SURQ', 'LATQ', 'GWQ', 'ET', 'WATER YIELD']].loc[data_flow['Date'] != np.nan]
flow_dataframe = data_flow[['Date', 'Observed', 'Simulated']].loc[data_flow['Date'] != np.nan]
last_row_index = int(flow_dataframe.index[-1])
new_index = [index for index in range(0,last_row_index)]
flow_dataframe.reindex(new_index)

# convert all text date fields to pandas datetime fields use the date as the index
flow_dataframe['Date']=pd.to_datetime(flow_dataframe['Date'],format='%m/%d/%y')
flow_dataframe.index = flow_dataframe['Date']
grouped = flow_dataframe.groupby(by=[ flow_dataframe.index.year, flow_dataframe.index.month])

# for name, group in grouped:
#     print name
#     print group

# print the grouped data with the mean value for the observed and simulated
grouped_data = grouped['Observed', 'Simulated'].agg(np.mean)

# print grouped_data

# header array
header=['Observed', 'Simulated']

# export to excel with the header array defined
grouped_data.to_excel('.\export_Observed_Simulated.xlsx', index=False, header=header)

# plot line graphs with the observed and simulated columns
# grouped_data.plot.line()
# plt.xlabel("Month and Year")
# plt.ylabel("Flow rate")
# plt.title("From 1995 to 2000")
# plt.show()