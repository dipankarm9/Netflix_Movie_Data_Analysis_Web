# 🎬 Netflix Movie Data Analysis Dashboard

This project is a **Streamlit-based interactive dashboard** designed to analyze and visualize Netflix movie data. It provides insights into various aspects of the dataset, such as movie popularity, genre distribution, release year trends, and more. The dashboard is user-friendly and visually appealing, making it easy to explore the data.

---

## 📋 Features

### 1. **Movie Popularity Highlights**

- Displays the **most popular movie** and the **least popular movie** based on the `Popularity` metric.
- Uses Streamlit's `st.success` and `st.error` components to highlight these insights.

### 2. **Genre Analysis**

- Visualizes the **most frequent genres** in the dataset using a bar chart.
- Helps identify the most common genres in Netflix's movie catalog.

### 3. **Vote Average Distribution**

- Categorizes movies into popularity levels (`Not Popular`, `Below Average`, `Average`, `Popular`) based on their `Vote_Average`.
- Displays the distribution of these categories using a bar chart.

### 4. **Release Year Distribution**

- Shows the number of movies released per year using a histogram.
- Helps identify trends in movie releases over time.

### 5. **Clean and Processed Data**

- Handles missing values and cleans columns like `Vote_Count`, `Vote_Average`, and `Release_Date`.
- Explodes multi-genre movies into individual rows for better analysis.

---

## 🛠️ Technologies Used

- **Python**: Core programming language.
- **Streamlit**: For building the interactive web-based dashboard.
- **Pandas**: For data manipulation and cleaning.
- **Matplotlib**: For creating visualizations like histograms.
- **Seaborn**: For creating aesthetically pleasing charts.

---

## 📂 Project Structure

```
Netflix Movie Data Analysis/
│
├── app.py                 # Main Streamlit app
├── data/
│   └── mymoviedb.csv      # Dataset used for analysis
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

---

## 📊 Dataset Overview

The dataset (`mymoviedb.csv`) contains information about Netflix movies, including:

- **Title**: Name of the movie.
- **Genre**: Movie genres (e.g., Drama, Comedy).
- **Popularity**: Popularity score of the movie.
- **Vote_Count**: Number of votes the movie received.
- **Vote_Average**: Average rating of the movie.
- **Release_Date**: Release date of the movie.

---

## 🚀 How to Run the Project

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/dipankarm9/Netflix_Movie_Data_Analysis_Web.git
   cd Netflix_Movie_Data_Analysis_Web
   ```

2. **Install Dependencies**:
   Ensure you have Python installed, then run:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**:

   ```bash
   streamlit run app.py
   ```

4. **Access the Dashboard**:
   Open your browser and navigate to `http://localhost:8501`.

---

## 📈 Visualizations

### 🎭 Most Frequent Genres

A bar chart showing the most common genres in the dataset.

### ⭐ Vote Average Distribution

A bar chart categorizing movies based on their average votes.

### 🎬 Release Year Distribution

A histogram displaying the number of movies released per year.

---

## ❤️ Credits

- **Author**: Dipankar
- **Powered by**: [Streamlit](https://streamlit.io)
