# Mindcare : Mental Wellness Hub - Version 1.1
# Features: wellness resources and mood tracking

def access_resource(resource_id, member_id):
    print("Wellness resource", resource_id, "accessed by member", member_id)


def complete_resource(resource_id):
    print("Wellness resource", resource_id, "completed")


def track_mood(member_id, mood):
    print("Member", member_id, "recorded mood:", mood)


# Example usage
access_resource("MEDITATION_101", "M001")
complete_resource("MEDITATION_101")
track_mood("M001", "Happy")
