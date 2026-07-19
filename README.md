# 📱 Google Play Store Data Analysis

A complete Exploratory Data Analysis (EDA) project on the Google Play Store dataset using Python.

This project focuses on cleaning messy real-world data, performing exploratory analysis, visualizing trends, and extracting business insights that can help developers understand the Android app ecosystem.

---

# Dataset

The dataset contains information about thousands of Android applications available on the Google Play Store.

Each record includes features such as:

- App Name
- Category
- Rating
- Reviews
- Size
- Installs
- Type (Free/Paid)
- Price
- Content Rating
- Genres
- Android Version
- Last Updated

---

# Project Structure

```
GooglePlayStore-Analysis/
│
├── data/
│   └── googleplaystore.csv
│
├── notebook/
│   ├── Data Analysis Project.ipynb
│   └── .ipynb_checkpoints/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Technologies Used

- Python
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Seaborn

---

# Project Workflow

## 1. Data Cleaning

The raw dataset contained numerous inconsistencies which were handled before analysis.

Cleaning steps included:

- Removing duplicate applications
- Handling missing values
- Correcting invalid ratings
- Converting string values into numerical formats
- Converting dates into datetime format
- Fixing incorrect category values
- Cleaning install counts
- Cleaning price values
- Converting app sizes into MB
- Setting appropriate data types for every column

---

## 2. Exploratory Data Analysis

The following analyses were performed:

- Distribution of app categories
- Highest-rated categories
- Categories with maximum installs
- Rating distribution
- Reviews vs Rating
- Rating vs Installs
- Free vs Paid apps
- Paid vs Free ratings
- Price vs Installs
- App size distribution
- Content rating analysis
- Correlation analysis
- Outlier detection

---

## Visualizations

The project includes:

- Bar Charts
- Histograms
- Scatter Plots
- Pie Charts
- Heatmaps
- Box Plots

---

# Key Insights

Some major findings from the analysis include:

- The **Family** category contains the highest number of applications.
- **Game** apps receive the highest number of installs.
- Most applications have ratings between **3.5 and 4.5**.
- Applications with more reviews generally receive more installs.
- More than **90%** of Play Store apps are free.
- Paid apps show a slightly higher median rating than free apps.
- Most applications are smaller than **40 MB**.
- The majority of applications are suitable for **Everyone**.
- Reviews and installs exhibit a strong positive correlation.

---

# Business Recommendations

Based on the analysis:

- Prioritize developing free applications with premium features or in-app purchases.
- Focus on app quality to improve ratings and user engagement.
- Keep application size small for better accessibility.
- Encourage user reviews to improve visibility and downloads.
- Target popular categories while identifying less competitive niches.

---

# Skills Demonstrated

- Data Cleaning
- Data Wrangling
- Exploratory Data Analysis
- Data Visualization
- Statistical Interpretation
- Business Insight Generation
- Feature Engineering
- Pandas
- Matplotlib
- Seaborn

---

# How to Run

Clone the repository

```bash
git clone <repository-url>
```

Install dependencies

```bash
pip install -r requirements.txt
```

Start Jupyter Notebook

```bash
jupyter notebook
```

Open

```
notebook/Data Analysis Project.ipynb
```

---

# Author

**Kavya**

B.Tech Computer Science (Data Science)
