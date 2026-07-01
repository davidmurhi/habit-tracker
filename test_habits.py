from main import add_habit, load_habits


def test_add_habit_adds_to_list():
    habits = []
    add_habit(habits, "running")
    assert len(habits) == 1
    assert habits[0]["name"] == "running"
    assert habits[0]["streak"] == 0


def test_add_habit_returns_name():
    habits = []
    result = add_habit(habits, "coding")
    assert result == "coding"


def test_load_habits_returns_empty_list_when_no_file():
    import os
    if os.path.exists("habits.json"):
        os.remove("habits.json")
    result = load_habits()
    assert result == []
