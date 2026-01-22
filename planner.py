def create_task(action):
    # MVP stub – replace later with Jira/Notion/etc.
    print("📌 TASK CREATED")
    print(f"Title   : {action.text}")
    print(f"Owner   : {action.owner}")
    print(f"Deadline: {action.deadline}")
