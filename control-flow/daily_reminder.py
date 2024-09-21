task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
            print(
                f"High Alert: '{task}' is a high priority task and must be completed immdeiately as it is time-bound!"
            )
        elif time_bound == "no":
            print(
                f"High Alert: '{task}' is a high priority task and must be completed as soon as you can!"
            )
    case "medium":
        if time_bound == "yes":
            print(
                f"Medium Alert: '{task}' is a medium priority task but must be completed immdeiately as it is time-bound!"
            )
        elif time_bound == "no":
            print(
                f"Medium Alert: '{task}' is a medium priority task, please try to do it as soon as you can!"
            )
    case "low":
        if time_bound == "yes":
            print(
                f"Low Alert: '{task}' is a low priority task but must be completed immdeiately as it is time-bound!"
            )
        elif time_bound == "no":
            print(
                f"Low Alert: '{task}' is a low priority task, please try to do it as soon as you can!"
            )
