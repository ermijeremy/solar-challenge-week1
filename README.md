# ☀️ Solar Data Discovery Challenge - Week 0

This project is part of the **10 Academy Week 0 Challenge**, aimed at analyzing solar farm data from multiple African countries to identify optimal regions for solar energy investment.

<<<<<<< eda-sierra_leone
The goal is to support MoonLight Energy Solutions in enhancing its operations through **data-driven recommendations** based on environmental measurements and solar irradiance data.

---

## 🧭 Business Objective

MoonLight Energy Solutions seeks to identify **high-potential regions for solar energy deployment** by analyzing solar irradiance, weather, and environmental sensor data from various countries.

This project performs **data profiling**, **cleaning**, and **exploratory data analysis (EDA)** to:

- Detect trends and patterns in solar data
- Quantify the impact of environmental factors
- Compare solar potential across countries

---

## 🛠️ Project Implementation Overview

### ✅ Task 1: Git & Environment Setup
- Initialized GitHub repository: [solar-challenge-week1](https://github.com/ermijeremy/solar-challenge-week1)
- Set up Python virtual environment using `venv`
- Installed required dependencies and exported `requirements.txt`
- Created GitHub Actions workflow for environment verification
- Maintained Git hygiene with `.gitignore` and structured commits
- Created and merged `setup-task` branch into `main`

### ✅ Task 2: Data Profiling & EDA
Performed EDA and data cleaning for the following countries:
- **Togo (Dapaong)**
- **Benin**
- **Sierra Leone**

Key steps included:
- Z-score based outlier removal
- Median imputation for missing values
- Time series plots for GHI, DNI, DHI
- Correlation heatmaps and scatter plots
- Pre/post-cleaning analysis using module data (ModA/B)
- Cleaned datasets saved to: `data/<country>_clean.csv`

### ✅ Task 3: Cross-Country Comparison
- Combined cleaned datasets across all three countries
- Computed summary statistics (mean, median, std) for GHI, DNI, DHI
- Plotted boxplots and bar charts to compare solar potential
- Performed ANOVA statistical testing
- Summarized findings in markdown cell

---

## 🙋‍♂️ My Contributions

- Set up and documented Git repository, virtual environment, and GitHub Actions CI
- Collected and cleaned solar datasets for Togo, Benin, and Sierra Leone
- Performed detailed exploratory data analysis (EDA) using Python (Pandas, Seaborn, Matplotlib)
- Generated comparative visualizations and statistical summaries
- Wrote markdown documentation and interim report
- Managed branches (`setup-task`, `eda-togo`, `eda-benin`, `eda-sierra_leone`, `compare-countries`) and followed best Git practices

---

## 📁 Folder Structure

solar-challenge-week1/
│
├── data/ # Contains raw and cleaned CSVs (ignored by Git)  
├── notebooks/ # Jupyter notebooks for EDA and comparison  
│ ├── togo_eda.ipynb  
│ ├── benin_eda.ipynb  
│ ├── sierra_leone_eda.ipynb  
│ └── compare_countries.ipynb  
├── scripts/ # Placeholder for Python utility scripts  
│  
├── .github/workflows/ # GitHub Actions workflow  
│ └── ci.yml  
├── .gitignore  
├── requirements.txt  
├── README.md  
=======
1. Clone the repo
2. Set up Python virtual environment, create .gitignore, requirements.txt, and CI/CD workflow
3. Install dependencies:
>>>>>>> main
