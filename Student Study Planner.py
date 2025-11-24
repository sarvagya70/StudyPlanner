def get_subjects():
    subjects = []
    count = int(input("How many subjects? "))
    for i in range(count):
        name = input(f"Enter subject {i+1} name: ")
        hours = float(input(f"Estimated hours needed for {name}: "))
        subjects.append({"name": name, "needed": hours})
    return subjects

def get_available_hours():
    return float(input("How many hours can you study today? "))

def create_plan(subjects, available):
    plan = []
    remaining = available
    for s in subjects:
        if remaining <= 0:
            break
        allocated = min(s["needed"], remaining)
        plan.append({"name": s["name"], "allocated": allocated})
        remaining -= allocated
    return plan, remaining

def show_plan(plan, leftover):
    print("\nToday's Study Plan:")
    for item in plan:
        print(f"- {item['name']}: {item['allocated']} hour(s)")
    if leftover > 0:
        print(f"\nFree time left: {leftover} hour(s)")
    else:
        print("\nNo free time left.")

def main():
    subjects = get_subjects()
    available = get_available_hours()
    plan, leftover = create_plan(subjects, available)
    show_plan(plan, leftover)

if __name__ == "__main__":
    main()
