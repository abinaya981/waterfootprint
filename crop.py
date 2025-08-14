import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
df = pd.read_csv("agricultural_water_footprint.csv")

# Clean column names
df.columns = [col.strip().lower().replace(" ", "_").replace("(", "").replace(")", "") for col in df.columns]

# Print available columns (debugging help)
print("Columns in dataset:", df.columns.tolist())
print(df.head(10))

# Function to show water footprint
def show_water_footprint(crop_name):
    crop_name = crop_name.lower().strip()

    # Find the row where crop name matches
    result = df[df['crop'].str.lower() == crop_name]

    if result.empty:
        print(f"\n❌ No data found for crop: {crop_name}")
        return

    try:
        green = float(result['green_water_use_m³/kg'].values[0])
        blue = float(result['blue_water_use_m³/kg'].values[0])
        grey = float(result['water_pollution_grey_water_m³/kg'].values[0])
    except KeyError as e:
        print(f"\n⚠️ Missing expected column: {e}")
        print("Available columns:", df.columns.tolist())
        return

    # Display values
    print(f"\n✅ Water Footprint for '{crop_name.title()}':")
    print(f"  🌱 Green WF: {green} m³/kg")
    print(f"  💧 Blue WF : {blue} m³/kg")
    print(f"  🧪 Grey WF : {grey} m³/kg")

    # Plot
    sns.barplot(x=["Green", "Blue", "Grey"], y=[green, blue, grey])
    plt.title(f"Water Footprint for {crop_name.title()} (per kg)")
    plt.ylabel("Water Footprint (m³ per kg)")
    plt.show()

# Ask for crop name
crop_input = input("Enter a crop name from dataset (e.g., bananas, grapes, apples): ")
show_water_footprint(crop_input)
