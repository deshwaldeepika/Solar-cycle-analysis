import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the SILSO sunspot data file
# The data uses spaces as separators and has no column headers natively
columns = ['Year', 'Month', 'Fractional_Year', 'Sunspot_Number', 'Std_Dev', 'Observations', 'Def_Ind']
data = pd.read_csv('monssn.txt', sep=r'\s+', names=columns)

# 2. Combine Year and Month into a clean timeline column
data['Date'] = pd.to_datetime(data['Year'].astype(str) + '-' + data['Month'].astype(str) + '-01')

# 3. Calculate a 13-month rolling average to smooth out the noise
data['Smoothed_Sunspots'] = data['Sunspot_Number'].rolling(window=13, center=True).mean()

# 4. Generate the scientific visualization plot
plt.figure(figsize=(12, 6))
plt.plot(data['Date'], data['Sunspot_Number'], label='Monthly Mean Sunspot Number', color='orange', alpha=0.5)
plt.plot(data['Date'], data['Smoothed_Sunspots'], label='13-Month Smoothed Cycle', color='red', linewidth=2)

# 5. Format the chart
plt.title('Historical Solar Activity Cycles (1749 - Present)', fontsize=14, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Sunspot Count', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(fontsize=10)

# Save the final plot graph as an image file
plt.savefig('solar_cycle_plot.png', dpi=300, bbox_inches='tight')
print("Analysis complete! 'solar_cycle_plot.png' has been successfully generated.")
