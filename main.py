project_name = "Supply Chain Demand Forecasting"

print("Welcome to my first AI project!")
print(f"Project: {project_name}")
print("Developer: Computer Science Graduate")
print("Technology: Python and Machine Learning")
# Indian Restaurant Food Demand Tracker

dishes = {
    "Shahi Paneer": [12, 15, 14, 18, 22],
    "Dal Makhani": [10, 12, 11, 15, 19],
    "Chana Masala": [8, 9, 10, 12, 15],
    "Jeera Rice": [14, 16, 15, 19, 24]
}

print("\nINDIAN RESTAURANT DEMAND REPORT")
print("--------------------------------")

for dish, quantities in dishes.items():
    average = sum(quantities) / len(quantities)
    print(f"{dish}: {average:.1f} kg per day")

print("--------------------------------")
print("Report completed successfully!")
print("\nINDIAN RESTAURANT FOOD TRACKER")
print("--------------------------------")

dish = input("Enter dish name: ")

prepared = float(input("Quantity prepared (kg): "))
leftover = float(input("Quantity leftover (kg): "))

if prepared < 0 or leftover < 0 or leftover > prepared:
    print("\nInvalid quantities. Please try again.")
else:
    used = prepared - leftover
    waste_percentage = (leftover / prepared * 100) if prepared > 0 else 0

    print("\nRESTAURANT DAILY REPORT")
    print("--------------------------------")
    print(f"Dish: {dish}")
    print(f"Prepared: {prepared:.1f} kg")
    print(f"Leftover: {leftover:.1f} kg")
    print(f"Used: {used:.1f} kg")
    print(f"Leftover percentage: {waste_percentage:.1f}%")
    print("--------------------------------")

