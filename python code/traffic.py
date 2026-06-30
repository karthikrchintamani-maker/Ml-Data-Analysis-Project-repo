import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv(r"C:\Users\Karthik R\Downloads\archive (2)\Indian_Traffic_Violations.csv")
print(data.describe())
df = data[['Violation_ID',
           'Violation_Type',
           'Fine_Amount',
           'Location',
           'Date',
           'Time',
           'Vehicle_Type',
           'Driver_Age',
           'Driver_Gender',
           'Penalty_Points']]
df.columns = ['vid', 'vtype', 'fine', 'loc', 'dt', 'tm', 'veh', 'age', 'gender', 'points']
print(df.head())
count = df.groupby(['loc', 'vtype']).size().reset_index(name='count')
print(count)
plt.figure(figsize=(14,6))
sns.barplot(
    x='loc',
    y='count',
    hue='vtype',
    data=count,
    palette='Set2'
)
plt.title("Traffic Violations by Location")
plt.xlabel("Location")
plt.ylabel("Number of Violations")
plt.xticks(rotation=45)
plt.show()