from dotenv import load_dotenv
import os
import httpx
import pandas as pd

load_dotenv()


# implicit grant flow -> we cannot access user data
accessToken = os.getenv("implicitToken")

header = {'Authorization': 'Bearer {}'.format(accessToken)}

# testing basic profile
# r = httpx.get("https://api.fitbit.com/1/user/-/profile.json", headers=header).json()
# print(r)

# trying sleep endpoint
response = httpx.get("https://api.fitbit.com/1.2/user/-/sleep/date/2024-03-05/2024-03-10.json", headers=header).json()
print(response)

sleep_records = response["sleep"]

sleep_list = []

for sleep in sleep_records:
    sleep_list.append({
        "Date of Sleep": sleep["dateOfSleep"],
        "End Time": sleep["endTime"],
        "Is Main Sleep": sleep["isMainSleep"],
        "Minutes Asleep": sleep["minutesAsleep"],
        "Minutes Awake": sleep["minutesAwake"],
        "Time in Bed": sleep["timeInBed"],
        "Start Time": sleep["startTime"]
    })

# Create a DataFrame from the list
df = pd.DataFrame(sleep_list)

# Save to Excel
df.to_excel("sleep_data.xlsx", index=False)

print("Excel file created successfully.")