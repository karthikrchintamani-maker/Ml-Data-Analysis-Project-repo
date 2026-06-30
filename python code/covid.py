import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv(r'C:\Users\Karthik R\Downloads\archive\covid_19_india.csv')
df = data[['Sno', 'Date', 'Time', 'State/UnionTerritory',
           'ConfirmedIndianNational', 'ConfirmedForeignNational',
           'Cured', 'Deaths', 'Confirmed']]
df.columns = ['sn', 'dt', 'tm', 'state', 'cin', 'cfn', 'cur', 'dth', 'conf']
print(data.describe())
today = df[df['dt'] == '2020-03-14']
print("Data for 2020-03-14:")
print(today)
maxdt = today.sort_values(by='dth', ascending=False)
print("\nSorted by Deaths:")
print(maxdt)
tsd = maxdt.head(10)
print("\nTop 10 States:")
print(tsd)
plt.figure(figsize=(10,5))
sns.barplot(x='state', y='dth', data=tsd)
plt.show()