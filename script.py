import httpx
import pandas as pd

# implicit grant flow -> we cannot access user data
accessToken = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1BIVzUiLCJzdWIiOiJCV1NORzMiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd3BybyB3bnV0IHdzbGUgd3dlaSB3c29jIHdhY3Qgd3NldCB3bG9jIiwiZXhwIjoxNzQ5NDIyMDMwLCJpYXQiOjE3MTc4ODYwMzB9.zKw_L4DnGjh8KTxFW9EHEkd0nVBjLuYyAwjwaxWxfVM"

# using oauth 2 token, expires every 8 hours tho
oauthToken = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM1BIVzUiLCJzdWIiOiJCV1NORzMiLCJpc3MiOiJGaXRiaXQiLCJ0eXAiOiJhY2Nlc3NfdG9rZW4iLCJzY29wZXMiOiJ3aHIgd3BybyB3bnV0IHdzbGUgd2VjZyB3c29jIHdhY3Qgd294eSB3dGVtIHd3ZWkgd2NmIHdzZXQgd2xvYyB3cmVzIiwiZXhwIjoxNzE3NzUwODU4LCJpYXQiOjE3MTc3MjIwNTh9.gjmGdllWPcshzH6-J-_4AxN2Summ2wL9nwxcUN117rk"


header = {'Authorization': 'Bearer {}'.format(accessToken)}
clientId = "23PHW5"

# print(header)

r = httpx.get("https://api.fitbit.com/1/user/-/profile.json", headers=header).json()
print(r)

# trying sleep endpoint
response = httpx.get("https://api.fitbit.com/1.2/user/-/sleep/date/2024-03-05/2024-03-20.json", headers=header).json()
print(response)

# sleep_records = response["sleep"]
# # print(sleep["duration"])

# sleep_list = []

# for sleep in sleep_records:
#     sleep_list.append({
#         "Date of Sleep": sleep["dateOfSleep"],
#         "Duration (ms)": sleep["duration"],
#         "Efficiency (%)": sleep["efficiency"],
#         "End Time": sleep["endTime"],
#         "Is Main Sleep": sleep["isMainSleep"],
#         "Minutes Asleep": sleep["minutesAsleep"],
#         "Minutes Awake": sleep["minutesAwake"],
#         "Time in Bed": sleep["timeInBed"],
#         "Start Time": sleep["startTime"]
#     })

# # Create a DataFrame from the list
# df = pd.DataFrame(sleep_list)

# # Save to Excel
# df.to_excel("sleep_data.xlsx", index=False)

# print("Excel file created successfully.")