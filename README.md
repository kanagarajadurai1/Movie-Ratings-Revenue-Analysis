# Movie-Ratings-Revenue-Analysis

This project aims to uncover what makes a movie successful by analyzing patterns in:
Audience ratings
Movie budgets
Box office revenue
Genres, directors, and cast performance
The goal is to help production houses, distributors, and marketers make data-driven decisions in the entertainment industry.

Dataset Used:
The dataset is based on The Movie Database (TMDb) 5000 Movie Dataset and includes:
Budget, Revenue, Runtime
Genres, Directors, Cast
Average Ratings, Popularity
Language, Production Company, Release Date

Key Questions Explored:
Do high-budget movies always make more revenue?
Which genres perform best in terms of ratings and earnings?
Who are the top-grossing directors and actors?
What’s the correlation between popularity and revenue?
How do release dates (months/years) impact success?

Tools & Technologies Used:
Python: Core analysis
Pandas, NumPy: Data preprocessing & wrangling
Matplotlib, Seaborn: Static visualizations
Plotly (optional): Interactive graphs
Jupyter Notebook: Analysis environment

Project Workflow:
✅ 1. Data Preprocessing:
Converted release dates to datetime format
Cleaned currency columns (removed 0 or null entries in budget, revenue)
Parsed genres and cast fields from nested JSON to lists
Created new features like ROI = (Revenue - Budget) / Budget

✅ 2. Exploratory Data Analysis (EDA):
Histograms of budgets, revenue, ratings
Box plots for revenue by genre
Correlation matrix between budget, popularity, ratings, and revenue
Time-series revenue trends over years

✅ 3. Visualizations Created:
📈 Budget vs Revenue Scatter Plot
🍿 Most Popular Genres Bar Chart
⭐ Top 10 Directors by Average Revenue
🎭 WordCloud of Most Cast Actors
📅 Revenue by Release Month Heatmap

Key Insights:
High budget ≠ high revenue: Some low-budget films had very high ROI (e.g., horror, drama).
Genres like Action, Adventure, Sci-Fi earn more but require higher investments.
Family and Animation genres consistently get high ratings.
Directors like Christopher Nolan and James Cameron are top performers by revenue.
Movies released in November–December often outperform others due to holidays.

Recommendations:
Maximize ROI by investing in moderately budgeted films with historically successful genres like Thriller or Horror.
Schedule major releases during holiday seasons for better box office performance.
Use popularity trends and cast pairing data to predict a movie’s success.
Consider combining strong storyline genres (Drama) with visually engaging genres (Sci-Fi) for wide appeal.

