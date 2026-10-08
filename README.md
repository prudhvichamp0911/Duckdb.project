# DuckDB Data Analysis Project

## 📌 Project Overview

This project demonstrates the use of **DuckDB**, a high-performance analytical SQL database designed for fast data analysis and OLAP workloads.

The project focuses on using SQL queries to explore, transform, analyze, and extract meaningful insights from datasets. DuckDB provides an efficient way to perform analytical queries directly on local data files without requiring a separate database server.

## 🛠️ Technologies Used

- **DuckDB**
- **SQL**
- **Python** *(if applicable)*
- **CSV / Excel / Parquet datasets**
- **Git & GitHub**

## 📂 Project Objectives

- Understand DuckDB fundamentals
- Create and manage DuckDB databases
- Import and analyze datasets
- Perform SQL-based data analysis
- Filter, sort, and aggregate data
- Use `GROUP BY`, `JOIN`, `ORDER BY`, and other SQL operations
- Perform analytical queries efficiently
- Work with local CSV and Parquet files
- Generate useful insights from structured data

## 🔍 Key SQL Concepts

The project covers commonly used SQL operations such as:

```sql
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
JOIN
COUNT()
SUM()
AVG()
MIN()
MAX()
```

## 🗄️ DuckDB Example

DuckDB can query CSV files directly:

```sql
SELECT *
FROM 'data.csv';
```

Example analytical query:

```sql
SELECT
    category,
    COUNT(*) AS total_records,
    AVG(price) AS average_price
FROM 'data.csv'
GROUP BY category
ORDER BY total_records DESC;
```

## 📊 Data Analysis Workflow

```text
Dataset
   ↓
Load Data
   ↓
DuckDB
   ↓
SQL Queries
   ↓
Data Cleaning & Transformation
   ↓
Data Analysis
   ↓
Insights
```

## 🚀 Getting Started

### 1. Install DuckDB

Download and install DuckDB from the official DuckDB website.

### 2. Open DuckDB

Start the DuckDB command-line interface:

```bash
duckdb
```

Or create/open a database:

```bash
duckdb project.duckdb
```

### 3. Load Data

For a CSV file:

```sql
CREATE TABLE data AS
SELECT *
FROM 'data.csv';
```

For a Parquet file:

```sql
CREATE TABLE data AS
SELECT *
FROM 'data.parquet';
```

### 4. Query the Data

```sql
SELECT *
FROM data
LIMIT 10;
```

## 📁 Project Structure

```text
Duckdb.project/
│
├── data/
│   └── dataset.csv
│
├── queries/
│   └── analysis.sql
│
├── duckdb/
│   └── project.duckdb
│
├── README.md
└── .gitignore
```

> Update the folder names above to match the actual files in your repository.

## 📈 Project Outcomes

Through this project, I gained practical experience in:

- Analytical SQL
- NoSQL vs analytical database concepts
- Data exploration
- Data aggregation
- Data transformation
- Query optimization
- Working with CSV and Parquet data
- DuckDB database management

## 🎯 Skills Demonstrated

**SQL | DuckDB | Data Analysis | Data Cleaning | Data Transformation | Data Querying | Database Management | Git & GitHub**

## 👨‍💻 Author

**Prudhvi Sai Vootukuri**

GitHub: [Prudhvi Sai Vootukuri](https://github.com/prudhvichamp0911)

## ⭐ Acknowledgment

This project was created as part of my learning and practical exploration of **DuckDB and SQL-based data analytics**.
