# Your solutions to questions in part 2 on the exam will go in this file.
# Modify the code below per the provided specifications. Do NOT change the 
# names of functions/methods/classes nor their signatures.


def schedule_slots(d: dict[str, set[str]]) -> dict[str, set[str]]:
    result = {}

    # Sort the dates based on the number of available persons in descending order
    sorted_dates = sorted(d.keys(), key=lambda x: (-len(d[x]), x))

    assigned_persons = set()

    for date in sorted_dates:
        available_persons = d[date] - assigned_persons

        if available_persons:
            result[date] = available_persons
            assigned_persons.update(available_persons)

    return result
