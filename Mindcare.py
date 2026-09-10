# Mindcare : Mental Wellness Hub - Version 2.0
# Features: wellness resources, mood tracking, wellness activity search

activities = [
    "Meditation",
    "Breathing Exercise",
    "Yoga",
    "Stress Management"
]


def access_resource(resource_id, member_id):
    print("Wellness resource", resource_id, "accessed by member", member_id)


def complete_resource(resource_id):
    print("Wellness resource", resource_id, "completed")


def track_mood(member_id, mood):
    print("Member", member_id, "recorded mood:", mood)


def search_activity(activity):
    if activity in activities:
        print(activity, "is available")
    else:
        print(activity, "not found")


# Example usage
access_resource("MEDITATION_101", "M001")
complete_resource("MEDITATION_101")
track_mood("M001", "Happy")
search_activity("Meditation")
