from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os
import httpx

load_dotenv()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    with open("static/index.html","r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.get("/sleep_data/")
async def get_sleep_data(start_date: str, end_date: str):
    accessToken = os.getenv("implicitToken")
    if not accessToken:
        raise HTTPException(status_code=401, detail="access token not found")

    header = {'Authorization': 'Bearer {}'.format(accessToken)}

     # Fetch sleep data from Fitbit API
    url = f"https://api.fitbit.com/1.2/user/-/sleep/date/{start_date}/{end_date}.json"
    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=header)
    
    if response.status_code != 200:
        raise HTTPException(status_code=401,detail="error fetching data")

    data = response.json()

    if "sleep" not in data:
        raise HTTPException(status_code=404, detail="no sleep data found")
    
    sleep_records = data["sleep"]

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
    
    return JSONResponse(content=sleep_list)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)




