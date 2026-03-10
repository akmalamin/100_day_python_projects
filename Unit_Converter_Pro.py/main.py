# ===== CORRECTED CONVERSION FUNCTIONS (TOP LEVEL - ACCESSIBLE) =====
def celsius_to_fahrenheit(temp):
	return (temp * 9 / 5) + 32


def fahrenheit_to_celsius(temp):
	return (temp - 32) * 5 / 9


def celsius_to_kelvin(temp):
	return temp + 273.15


def kelvin_to_celsius(temp):
	return temp - 273.15


def fahrenheit_to_kelvin(temp):
	return (temp - 32) * 5 / 9 + 273.15  # FIXED FORMULA


def kelvin_to_fahrenheit(temp):
	return (temp - 273.15) * 9 / 5 + 32


def cm_to_meters(leng):
	return leng / 100


def millimeters_to_meters(leng):
	return leng / 1000


def meters_to_cm(leng):
	return leng * 100


def meters_to_mm(leng):
	return leng * 1000


def inches_to_cm(leng):
	return leng * 2.54


def foot_to_meters(leng):
	return leng * 0.3048  # FIXED: 0.3048 (not 0.3084)


def meters_to_km(leng):
	return leng / 1000


def g_to_kg(weight):
	return weight / 1000  # FIXED: /1000 (not /100)


def kg_to_g(weight):
	return weight * 1000


def mg_to_g(weight):
	return weight / 1000


def g_to_mg(weight):
	return weight * 1000


def kg_to_ton(weight):  # REMOVED typo 'kg_to_tong'
	return weight / 1000  # Metric ton


def ml_to_l(volume):
	return volume / 1000


def l_to_ml(volume):
	return volume * 1000


def liters_to_cubic_meters(volume):  # RENAMED for clarity
	return volume / 1000


# ===== HELPER: VALIDATED NUMBER INPUT =====
def get_number(prompt):
	while True:
		try:
			return float(input(prompt))
		except ValueError:
			print("❌ Please enter a valid number.")


# ===== CORRECTED MENU FUNCTIONS (WITH USER INTERACTION) =====
def temperature_menu(history):
	while True:
		print("\n" + "=" * 50)
		print("🌡️  TEMPERATURE CONVERSIONS")
		print("=" * 50)
		print("1. Celsius to Fahrenheit")
		print("2. Fahrenheit to Celsius")
		print("3. Celsius to Kelvin")
		print("4. Kelvin to Celsius")
		print("5. Fahrenheit to Kelvin")
		print("6. Kelvin to Fahrenheit")
		print("7. Back to Main Menu")
		print("=" * 50)
		
		choice = input("Select conversion (1-7): ").strip()
		
		if choice == "7":
			break
		
		if choice not in ["1", "2", "3", "4", "5", "6"]:
			print("❌ Invalid choice. Please select 1-7.")
			continue
		
		value = get_number("Enter value: ")
		
		if choice == "1":
			result = celsius_to_fahrenheit(value)
			entry = f"{value}°C = {result:.2f}°F"
		elif choice == "2":
			result = fahrenheit_to_celsius(value)
			entry = f"{value}°F = {result:.2f}°C"
		elif choice == "3":
			result = celsius_to_kelvin(value)
			entry = f"{value}°C = {result:.2f}K"
		elif choice == "4":
			result = kelvin_to_celsius(value)
			entry = f"{value}K = {result:.2f}°C"
		elif choice == "5":
			result = fahrenheit_to_kelvin(value)
			entry = f"{value}°F = {result:.2f}K"
		elif choice == "6":
			result = kelvin_to_fahrenheit(value)
			entry = f"{value}K = {result:.2f}°F"
		
		print(f"\n✅ {entry}")
		history.append(entry)
		input("\nPress Enter to continue...")


def length_menu(history):
	while True:
		print("\n" + "=" * 50)
		print("📏 LENGTH CONVERSIONS")
		print("=" * 50)
		print("1. cm to meters")
		print("2. mm to meters")
		print("3. meters to cm")
		print("4. meters to mm")
		print("5. inches to cm")
		print("6. feet to meters")
		print("7. meters to km")
		print("8. Back to Main Menu")
		print("=" * 50)
		
		choice = input("Select conversion (1-8): ").strip()
		
		if choice == "8":
			break
		
		if choice not in [str(i) for i in range(1, 9)]:
			print("❌ Invalid choice. Please select 1-8.")
			continue
		
		value = get_number("Enter value: ")
		
		if choice == "1":
			result = cm_to_meters(value)
			entry = f"{value} cm = {result:.4f} m"
		elif choice == "2":
			result = millimeters_to_meters(value)
			entry = f"{value} mm = {result:.6f} m"
		elif choice == "3":
			result = meters_to_cm(value)
			entry = f"{value} m = {result:.2f} cm"
		elif choice == "4":
			result = meters_to_mm(value)
			entry = f"{value} m = {result:.2f} mm"
		elif choice == "5":
			result = inches_to_cm(value)
			entry = f"{value}\" = {result:.2f} cm"
		elif choice == "6":
			result = foot_to_meters(value)  # USING CORRECTED FORMULA
			entry = f"{value} ft = {result:.4f} m"
		elif choice == "7":
			result = meters_to_km(value)
			entry = f"{value} m = {result:.6f} km"
		
		print(f"\n✅ {entry}")
		history.append(entry)
		input("\nPress Enter to continue...")


def weight_menu(history):
	while True:
		print("\n" + "=" * 50)
		print("⚖️  WEIGHT CONVERSIONS")
		print("=" * 50)
		print("1. grams to kg")
		print("2. kg to grams")
		print("3. mg to grams")
		print("4. grams to mg")
		print("5. kg to metric tons")
		print("6. Back to Main Menu")
		print("=" * 50)
		
		choice = input("Select conversion (1-6): ").strip()
		
		if choice == "6":
			break
		
		if choice not in [str(i) for i in range(1, 7)]:
			print("❌ Invalid choice. Please select 1-6.")
			continue
		
		value = get_number("Enter value: ")
		
		if choice == "1":
			result = g_to_kg(value)  # USING CORRECTED FORMULA
			entry = f"{value} g = {result:.6f} kg"
		elif choice == "2":
			result = kg_to_g(value)
			entry = f"{value} kg = {result:.2f} g"
		elif choice == "3":
			result = mg_to_g(value)
			entry = f"{value} mg = {result:.6f} g"
		elif choice == "4":
			result = g_to_mg(value)
			entry = f"{value} g = {result:.2f} mg"
		elif choice == "5":
			result = kg_to_ton(value)  # USING CORRECTED FUNCTION
			entry = f"{value} kg = {result:.6f} tons"
		
		print(f"\n✅ {entry}")
		history.append(entry)
		input("\nPress Enter to continue...")


def volume_menu(history):
	while True:
		print("\n" + "=" * 50)
		print("🫗 VOLUME CONVERSIONS")
		print("=" * 50)
		print("1. mL to Liters")
		print("2. Liters to mL")
		print("3. Liters to Cubic Meters")
		print("4. Back to Main Menu")
		print("=" * 50)
		
		choice = input("Select conversion (1-4): ").strip()
		
		if choice == "4":
			break
		
		if choice not in ["1", "2", "3"]:
			print("❌ Invalid choice. Please select 1-4.")
			continue
		
		value = get_number("Enter value: ")
		
		if choice == "1":
			result = ml_to_l(value)
			entry = f"{value} mL = {result:.6f} L"
		elif choice == "2":
			result = l_to_ml(value)
			entry = f"{value} L = {result:.2f} mL"
		elif choice == "3":
			result = liters_to_cubic_meters(value)  # USING RENAMED FUNCTION
			entry = f"{value} L = {result:.6f} m³"
		
		print(f"\n✅ {entry}")
		history.append(entry)
		input("\nPress Enter to continue...")


# ===== MAIN FUNCTION (FIXED LOOP & NAVIGATION) =====
def main():
	history = []
	
	while True:
		print("\n" + "=" * 60)
		print("🌡️📏⚖️🫗 UNIT CONVERTER PRO 🫗⚖️📏🌡️")
		print("=" * 60)
		print("1. 🌡️  Temperature")
		print("2. 📏 Length")
		print("3. ⚖️  Weight")
		print("4. 🫗 Volume")
		print("5. 📜 View History")
		print("6. 👋 Exit")
		print("=" * 60)
		
		choice = input("\nSelect an option (1-6): ").strip()
		
		if choice == "1":
			temperature_menu(history)
		elif choice == "2":
			length_menu(history)
		elif choice == "3":
			weight_menu(history)
		elif choice == "4":
			volume_menu(history)
		elif choice == "5":
			print("\n" + "=" * 50)
			print("📜 CONVERSION HISTORY")
			print("=" * 50)
			if not history:
				print("📭 No conversions recorded yet.")
			else:
				for i, entry in enumerate(history, 1):
					print(f"{i}. {entry}")
				print(f"\nTotal conversions: {len(history)}")
			print("=" * 50)
			input("\nPress Enter to return to main menu...")
		elif choice == "6":
			print("\n" + "=" * 50)
			print("👋 Thank you for using UNIT CONVERTER PRO!")
			print("✅ All conversions are scientifically accurate.")
			print("=" * 50 + "\n")
			break
		else:
			print("\n❌ Invalid choice! Please select 1-6.")


if __name__ == "__main__":
	main()