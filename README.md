Low-Cost Solar Simulator
Technologies: Python, NASA POWER API, Pandas, Matplotlib

Project Overview

This project presents a **cost-effective solar simulator** designed to replicate real-world **solar irradiance** and **ambient temperature** 
conditions for laboratory testing of solar panels. Unlike expensive commercial simulators, this solution integrates live data from the **NASA POWER API** 
and uses a Python-based backend to offer accurate and dynamic simulation capabilities.

The tool is highly customizable, user-friendly, and serves as an accessible alternative for educational institutions and researchers.

---
Features

Live Data Fetching from NASA's POWER API based on user-input location and date.
Hourly Resolution of Solar Intensity (W/m²) and Temperature (°C).
Cleaned and Formatted Output using Pandas.
Dynamic Visualizationusing Matplotlib for better insight and analysis.
Automatic Excel Export using OpenPyXL for record-keeping and future use.
Interactive CLI for easy user input and flexibility.
Robust Error Handlingfor invalid inputs and API failures.

---

🛠️ Tech Stack

| Category            | Tools / Libraries                |
|---------------------|----------------------------------|
| Programming Language| Python 3.11                      |
| API Integration     | NASA POWER REST API              |
| Data Processing     | Pandas, JSON                     |
| Visualization       | Matplotlib                       |
| File Export         | OpenPyXL (Excel `.xlsx`)         |
| CLI Interaction     | Python `input()` function        |

---

How It Works

  User Input
   - Latitude and longitude (e.g., 23.2, 77.4)
   - Date (e.g., 25-06-2025)
  
  Data Fetching
  Connects to the NASA POWER API
  Retrieves hourly values for:
    Solar Irradiance (ALLSKY_SFC_SW_DWN)
    Temperature (T2M)
  
  Stored in a structured DataFrame
  Output Generation
  
  Saved to Excel (solar_intensity_and_temperature.xlsx)
  Visualized using line plots

📑 Requirements
    pip install requests, pandas, matplotlib, openpyxl
