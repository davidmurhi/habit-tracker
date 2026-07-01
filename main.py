import json


def load_habits():
    try:
        with open("habits.json", "r") as file:
            return json.load(file)
    except:
        return []


def save_habits(habits):
    with open("habits.json", "w") as file:
        json.dump(habits, file)


def view_habits(habits):
    print("Your habits:")
    number = 1
    for items in habits:
        print(f"{number}. {items['name']} (streak: {items['streak']})")
        number += 1


def add_habit(habits, name):
    habits.append({"name": name, "streak": 0})
    return name


def mark_done(habits):
    view_habits(habits)
    try:
        habit_number = int(input("Which habit number is done? ")) - 1
        habits[habit_number]["streak"] += 1
        print(
            f"Nice! {habits[habit_number]['name']} streak is now {habits[habit_number]['streak']}")
    except ValueError:
        print("Please enter a valid number")


def delete_habit(habits):
    view_habits(habits)
    try:
        habit_number = int(
            input("Which habit number do you want to delete? ")) - 1
        habits.pop(habit_number)
        print("Deleted successfully")
    except ValueError:
        print("Please enter a valid number")


if __name__ == "__main__":
    habits = load_habits()
    while True:
        print("\n--- Habit Tracker ---")
        print("1. Add a habit")
        print("2. View habits")
        print("3. Mark habit done")
        print("4. Delete habit")
        print("5. Quit")
        choice = input("Choose an option: ")
        if choice == "1":
            name = input("What habit do you want to track? ")
            print("Added:", add_habit(habits, name))
        elif choice == "2":
            view_habits(habits)
        elif choice == "3":
            mark_done(habits)
        elif choice == "4":
            delete_habit(habits)
        elif choice == "5":
            print("Goodbye!")
            save_habits(habits)
            break
        else:
            print("That's not a valid option, try again")
