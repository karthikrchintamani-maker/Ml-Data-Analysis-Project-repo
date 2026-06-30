import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv(r'C:\Users\Karthik R\Downloads\LPG_Statewise_Migration_Dataset_500_Rows.csv')
df = data[['State', 'LPG_Consumption_MMT', 'People_Migrated']]
df.columns = ['state', 'cons', 'migrated']
print(data.describe())
tsd = df.sort_values(by='cons', ascending=False).head(10)
plot_df = tsd.melt(
    id_vars='state',
    value_vars=['cons', 'migrated'],
    var_name='Category',
    value_name='Value'
)
plt.figure(figsize=(12, 6))
sns.barplot(x='state', y='Value', hue='Category', data=plot_df)
plt.title("LPG Consumption and People Migrated by State")
plt.xlabel("State")
plt.ylabel("Value")
plt.xticks(rotation=45)
plt.show()