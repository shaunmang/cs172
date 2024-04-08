#Shaun Mangan sam677
from food import FoodItem
import inputroutines
name = input("Enter food item's name: ")

    # get serving size
serving_size = inputroutines.intInRange(0, 500)
    
    # get grams of fat, carbs, and protein per serving
fat = inputroutines.floatInRange(0.00, 50.00)
carbs = inputroutines.floatInRange(0.00, 50.00)
protein = inputroutines.floatInRange(0.00, 50.00)

    # Create FoodItem 
food_item = FoodItem(name, serving_size, fat, carbs, protein)

    # Display food item information
print(f"\nNutritional information per serving of {food_item.getName()}")
print(f"Serving Size: {food_item.getServingSize()} grams / mL")
print(f"Fat: {food_item.getFat():.2f} grams")
print(f"Carbohydrates: {food_item.getCarbs():.2f} grams")
print(f"Protein: {food_item.getProtein():.2f} grams")
print("Number of calories for 1 serving: {:.2f}".format(food_item.calculateCalories(1)))

    # Get and validate number of servings consumed
servings = inputroutines.intInRange(0, 10)

    # Calculate and display total calories
total_calories = food_item.calculateCalories(servings)
print(f"Number of calories for {servings} serving(s): {total_calories:.2f}")

