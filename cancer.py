import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_excel(r"Datasets/Cancer_Statewise_Dataset_500_Rows (1).xlsx")
df = data[['State', 'Cured_Cases', 'Deaths']]
print(data.describe())
state_data = df.groupby('State').sum().reset_index()
state_data.plot(
    x='State',
    y=['Cured_Cases', 'Deaths'],
    kind='bar',
    figsize=(14,6),
    color=['green', 'red']
)
plt.title("State vs Cured Cases and Deaths")
plt.xlabel("State")
plt.ylabel("Number of Patients")
plt.xticks(rotation=90)
plt.show()