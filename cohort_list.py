
def cohort_list(trainer="Harry", index=4, name="Chris"):
    team = ["Ollie", "Bob", "Steve", "Dave", "Chris"]

    team.append(trainer)

    return f"{team}\n{team[index]}\n{team.count(name)}"

print(cohort_list(name="Jeff"))
