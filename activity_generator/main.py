import json
from dataclasses import dataclass

@dataclass
class Activity:
    activity: str
    activity_type: str
    cost: int
    people: int


def load_data() -> list[Activity]:
    activities: list[Activity] = []
    with open('activities.json', 'r') as f:
        for activity in json.load(f):
            activities.append(
                Activity(
                    activity['activity'],
                    activity['type'],
                    activity['cost'],
                    activity['people']
                )
            )

        return activities

def generate_activities(activities: list[Activity]) -> None:
    try:
        people: int = int(input('How many people are you? '))
        cost: int = int(input('How much are you willing to spend per person? '))
        location: str = input('Indoor or outdoor? (press ENTER if no preference) ').lower()
    except ValueError:
        print('Error: Please enter only numerical values.')
        return


    matched_activities: list[Activity] = []
    for activity in activities:
        activity_cost = activity.cost
        activity_people = activity.people
        if location:
            activity_location = activity.activity_type
            if activity_cost <= cost and activity_people <= people and activity_location == location:
                matched_activities.append(activity)

        else:
            if activity_cost <= cost and activity_people <= people:
                matched_activities.append(activity)

    if matched_activities:
        for i, matched in enumerate(matched_activities, start=1):
            print(f'{i}: {matched.activity}: {matched.cost}$ per person [{people}p: {people * matched.cost}$]')
    else:
        print('No activities found...')

def main() -> None:
    activities: list[Activity] = load_data()
    generate_activities(activities)


if __name__ == '__main__':
    main()


