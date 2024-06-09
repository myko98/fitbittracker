document.getElementById("sleepForm").addEventListener("submit",async (e) =>  {
    e.preventDefault()
    const startDate = document.getElementById("startDate").value
    const endDate = document.getElementById("endDate").value

    console.log(startDate)

    try {
        const response = await fetch(`/sleep_data/?start_date=${startDate}&end_date=${endDate}`)
        if (!response.ok) {
            throw new Error("error")
        }
        console.log(response)
        const data = await response.json()
        console.log(data)
        document.getElementById('sleep-data').textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        document.getElementById('sleep-data').textContent = `Error: ${error.message}`;
    }
})