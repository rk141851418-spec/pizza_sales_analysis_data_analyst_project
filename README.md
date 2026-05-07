# 🍕 Pizza Sales Data Analytics Project

## 📌 Overview
Understanding customer ordering behavior and sales trends is essential for improving revenue and business decisions in the restaurant industry.

This project analyzes a pizza restaurant’s transactional sales data using **Python, SQL, and Jupyter Notebook** to generate actionable business insights.

The dataset includes:
- Order date & time
- Pizza types and sizes
- Quantities and prices

Since the data is stored across multiple tables, it requires **data cleaning, transformation, and joining** before analysis.

---

## 🎯 Objective
Transform raw datasets into a **clean, analysis-ready dataset** and perform SQL-based business analysis and visualization to identify sales trends and performance insights.

## ❓ Problem Statement

The restaurant wants to use historical sales data to improve revenue, optimize menu performance, and support better business decisions.

This project answers the following key business questions:

### 📊 Sales Overview
- What are the total orders, total pizzas sold, and total revenue?
- How do sales change over time?

### ⏰ Time Analysis
- What are the peak ordering hours?
- Which days and months generate the highest sales?
- When should staffing be increased?

### 🍕 Product Performance
- Which pizzas are the best and worst sellers?
- Which pizza sizes generate the most revenue?
- Which pizza categories perform best?

### 💰 Revenue Insights
- Which pizzas contribute the most to revenue?
- What is the revenue contribution by category and size?

### 📈 Business Impact
Use insights to:
- Improve staffing and inventory planning  
- Optimize the menu  
- Increase overall revenue

- ## 📂 Project Structure

pizza_sales_project/
│
├── pizza_sales_data/          # Raw CSV dataset files
├── logs/                      # ETL and summary log files
├── scripts/                   # Python ETL & data processing scripts
├── notebooks/                 # Jupyter notebooks for analysis
│
├── dashboard.pbix             # Power BI dashboard
├── pizza sales analysis using sql.pdf   # SQL analysis report
├── report.pdf                 # Final business insights report

## ⚙️ Automated ETL Pipeline
The project includes a reusable ETL pipeline built using Python and SQLite to automate data ingestion, transformation, and analytical dataset creation.
### Pipeline Workflow
Raw CSV Files
   ↓
Python Ingestion Scripts
   ↓
SQLite Database Tables
   ↓
SQL Joins & Transformations
   ↓
Clean Analytical Dataset
### Key Features
- Automated ingestion of multiple CSV files into SQLite
- Reusable Python functions for data loading
- SQL joins and transformation pipeline
- Logging system for execution tracking
- Automated table refresh using replace logic
- Feature engineering for month, weekday, and hourly analysis


## 📈 Strategic Revenue & Operational Insights

### 💰 Profitability vs Popularity
- The **Classic Deluxe** is the highest-volume pizza, but **Thai Chicken Pizza** generates the highest revenue.
- Premium pizzas are strong revenue drivers even with lower order volume.

### 📦 Order & Size Behavior
- Customers typically purchase **1 pizza per size/type**.
- However, the most common order contains **2 pizzas in total**, indicating combo-style purchasing.
- This suggests strong potential for **bundle offers and upselling larger sizes**.
  
### 🍕 Category Performance
- The **Classic category** leads in both total orders and total revenue.
- It provides a stable revenue base while niche categories contribute smaller shares.

### ⏰ Peak Demand Window
- **12:00 PM (Lunch hour)** is the biggest revenue driver.
- Lunch outperforms dinner, indicating strong weekday office demand.

### 📉 Underutilized Capacity
- **72.8% of revenue comes from weekdays**.
- Sales drop significantly between **2 PM – 4 PM**, showing unused kitchen capacity.

### 📋 Menu Optimization Opportunity
- Some pizzas fail to reach **1,000 orders and $15K revenue**.
- These items increase inventory and menu complexity without strong ROI.

- ## 📊 Dashboard

An interactive Power BI dashboard was created to visualize key business metrics:

- KPI cards for Revenue, Orders and Pizzas Sold  
- Sales trends by Hour, Day and Month  
- Top Selling Pizzas  
- Revenue by Category and Size  

The dashboard helps stakeholders quickly understand performance and make data-driven decisions.<img width="1288" height="725" alt="Screenshot 2025-12-19 071904" src="https://github.com/user-attachments/assets/7ee80c9a-1360-48b1-95b4-13ddb33fcced" />

## ▶️ How to Read & Run This Project

Follow these steps to understand and reproduce the complete workflow.

### 1️⃣ Clone the Repository
git clone <[your-repo-link](https://github.com/rk141851418-spec/pizza_sales_analysis_data_analyst_project)>  
cd pizza_sales_project

### 2️⃣ Load Data & Create Database Tables
Run the ETL script to ingest CSV files into SQLite:
python scripts/ingest_data.py

This will create:
- SQLite database
- Pizza sales tables
- Log files

### 3️⃣ Open and Run Notebooks
Start Jupyter Notebook:
jupyter notebook

Open notebooks in this order:
1. Data Exploration  
2. SQL Analysis  
3. Visualization  

### 4️⃣ Open Power BI Dashboard
Open **dashboard.pbix** in Power BI Desktop to explore the final interactive dashboard.

## 🚀 Future Work

- Automate the ETL pipeline to run on a schedule (Airflow / Cron).
- Migrate the database from SQLite to a cloud database (PostgreSQL / BigQuery).
- Publish the Power BI dashboard to Power BI Service for online access.
- Implement machine learning to forecast pizza demand.
- Perform customer segmentation and recommendation analysis.

## 👤 Author

**Rakesh Kumar**  
Data Analyst  

## 📬 Contact
- Email: rk141851418@gmail.com
