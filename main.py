import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read the yearly deaths dataset
yearly_df = pd.read_csv("yearly_deaths_by_clinic.csv")

# Display the yearly dataset
print(yearly_df.head())
print(yearly_df.shape)
print(yearly_df.info())

# Calculate the proportion of deaths
yearly_df["Proportion of Deaths"] = yearly_df["deaths"] / yearly_df["births"]

# Separate the dataset into 2 datasets, one for each clinic
clinic_1 = yearly_df[yearly_df["clinic"] == "clinic 1"]
clinic_2 = yearly_df[yearly_df["clinic"] == "clinic 2"]

# Visualize the Number of deaths every year in clinic 1
plt.bar(clinic_1.year, clinic_1.deaths, width=0.6, color="red")
plt.title("Clinic 1: Number of Deaths per Year")
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.show()

# Visualize the Number of deaths every year in clinic 2
plt.bar(clinic_2.year, clinic_2.deaths, width=0.6, color="green")
plt.title("Clinic 2: Number of Deaths per Year")
plt.xlabel("Year")
plt.ylabel("Number of Deaths")
plt.show()

# Plot the proportion of deaths in clinic 1 and 2
ax = clinic_1.plot(x="year", y="Proportion of Deaths", label="clinic_1", color="red")
clinic_2.plot(x="year", y="Proportion of Deaths", label="clinic_2", ax=ax, ylabel="Proportion of Deaths", color="green")

# Step 2: Read the monthly deaths dataset
monthly_df = pd.read_csv("monthly_deaths.csv")

# Display the first few rows of the monthly dataset
print(monthly_df.head())
print(monthly_df.info())

# Calculate the proportion of deaths per month
monthly_df["Proportion of Deaths"] = monthly_df["deaths"] / monthly_df["births"]

# Change the data type of "date" column from string to datetime
monthly_df['date'] = pd.to_datetime(monthly_df['date'])

# Label the date at which handwashing started to "start_handwashing"
start_handwashing = pd.to_datetime('1847-06-01')

# Split monthly into before and after handwashing_start
before_washing = monthly_df[monthly_df["date"] < start_handwashing]
after_washing = monthly_df[monthly_df["date"] >= start_handwashing]

# Visualize the proportion of deaths before handwashing
plt.plot(before_washing["date"], before_washing["Proportion of Deaths"], color="orange")
plt.title("Before Handwashing")
plt.xlabel("Date")
plt.ylabel("Proportion of Deaths")
plt.show()

# Visualize the proportion of deaths after handwashing
plt.plot(after_washing["date"], after_washing["Proportion of Deaths"], color="green")
plt.title("After Handwashing")
plt.xlabel("Date")
plt.ylabel("Proportion of Deaths")
plt.show()

# Combine both plots in one chart
ax = before_washing.plot(x="date", y="Proportion of Deaths", label="Before Handwashing", color="orange")
after_washing.plot(x="date", y="Proportion of Deaths", label="After Handwashing", ax=ax, ylabel="Proportion deaths", color="green")

# Calculate the average proportion of deaths before and after handwashing
before_proportion = before_washing["Proportion of Deaths"].mean()
after_proportion = after_washing["Proportion of Deaths"].mean()

# Calculate the difference between both proportions
mean_diff = after_proportion - before_proportion

# Display the results
print(f"Average Proportion of Deaths Before Handwashing: {before_proportion:.2%}")
print(f"Average Proportion of Deaths After Handwashing: {after_proportion:.2%}")
print(f"Decrease in Proportion of Deaths: {mean_diff:.2%}")
