import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
df = pd.read_csv("agricultural_water_footprint.csv")

# Clean column names
df.columns = [col.strip().lower().replace(" ", "_").replace("(", "").replace(")", "") for col in df.columns]

# Drop rows where water data is missing
df = df.dropna(subset=['green_water_use_m³/kg', 'blue_water_use_m³/kg', 'water_pollution_grey_water_m³/kg'])

# Calculate total water footprint per crop
df['total_water_footprint_m3_per_kg'] = (
    df['green_water_use_m³/kg'] +
    df['blue_water_use_m³/kg'] +
    df['water_pollution_grey_water_m³/kg']
)

# Sort by highest total footprint
df_sorted = df[['crop', 'total_water_footprint_m3_per_kg']].sort_values(by='total_water_footprint_m3_per_kg', ascending=False)

# Plot
plt.figure(figsize=(12, 8))
sns.barplot(data=df_sorted, x='total_water_footprint_m3_per_kg', y='crop')
plt.title("Total Water Footprint (m³ per kg) for Each Crop")
plt.xlabel("Total Water Footprint (m³/kg)")
plt.ylabel("Crop")
plt.tight_layout()
plt.show()
