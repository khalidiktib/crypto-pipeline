# Crypto Data Pipeline & Dashboard

This project is an end-to-end data engineering pipeline that collects real-time cryptocurrency data from the CoinGecko API, processes and stores it in a database, and presents insights through an interactive Streamlit dashboard. It showcases the full lifecycle of data, from ingestion to visualization, using automated and modular components.

## Pipeline Architecture

API → Extract → Raw Storage → Transform → Database → Dashboard

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language for the pipeline |
| requests | Fetch data from the CoinGecko API |
| JSON | Store raw data files |
| pandas | Data cleaning and transformation |
| SQLite | Store structured data |
| SQL | Define schema and query data |
| Streamlit | Build interactive dashboard |
| glob | Handle file selection (latest data) |
| datetime | Generate timestamps for data collection |

---

## How to Install and Run

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd crypto-pipeline
```

### 2. Create and activate virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the pipeline
```bash
python pipeline.py
```

### 5. Launch the dashboard
```bash
streamlit run dashboard.py
```
---

## What I Learned

- How to build an end-to-end data pipeline (Extract → Transform → Load → Dashboard)
- How to work with REST APIs and handle real-world issues like network errors and bad responses
- How to clean and structure data using pandas for analysis and storage
- How to design a database schema and store time-series data using SQLite
- How to organize a project into modular scripts (extract, transform, load, pipeline)
- How to turn data into insights using an interactive Streamlit dashboard

---


# What is built
- Data pipeline  
- Database  
- Automation  
- Dashboard  
- Documentation  

---

