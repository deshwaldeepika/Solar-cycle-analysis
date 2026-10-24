# Historical Solar Cycle Analysis

This project uses Python to ingest, clean, and visualize over 250 years of solar activity data provided by the SILSO World Data Center. By executing time-series smoothing, it highlights the distinct 11-year solar cycles from 1749 to the present day.

## Features
* Processes raw, multi-column scientific text files using `pandas`.
* Applies a 13-month centered rolling average to isolate long-term solar cycles from transient space weather noise.
* Generates publication-ready data plots using `matplotlib`.

## Data Visualisation Output
![Solar Cycles](solar_cycle_plot.png)

**Key Insight:** The visualization clearly highlights the distinct ~11-year cyclical nature of solar activity. By applying a 13-month centered rolling average, we smooth out the transient daily space weather noise to reveal the underlying peaks and troughs of historical solar cycles.

## How to Run Externally
1. Clone this repository.
2. Ensure dependencies are installed: `pip install pandas matplotlib`
3. Execute the script: `python analyze_solar_cycle.py`

## Data Acknowledgments
The dataset (`monssn.txt`) used in this analysis is provided courtesy of the **World Data Center for the Sunspot Index and Long-term Solar Observations (WDC-SILSO)**, hosted at the Royal Observatory of Belgium, Brussels.

* **Dataset:** International Sunspot Number V2.0 (Monthly Mean Numbers)
* **License:** CC BY-NC 4.0 (Creative Commons Attribution-NonCommercial)
* **Official Source:** [WDC-SILSO Data Center](https://www.sidc.be/SILSO/datafiles "SILSO sunspot data download")
* **Citation:** *Source: WDC-SILSO, Royal Observatory of Belgium, Brussels, DOI: 10.24414/qnza-ac80*

