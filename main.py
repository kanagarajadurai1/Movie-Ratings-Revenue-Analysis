import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("movie_ratings_revenue_analysis.csv")  # Replace with actual path

# Budget vs Revenue
sns.scatterplot(data=df, x='budget', y='revenue')
plt.title('Budget vs Revenue')
plt.xlabel('Budget ($)')
plt.ylabel('Revenue ($)')
plt.show()

# ROI
df['ROI'] = (df['revenue'] - df['budget']) / df['budget']
top_roi = df.sort_values(by='ROI', ascending=False).head(10)
print(top_roi[['title', 'budget', 'revenue', 'ROI']])

# Popular genres
from ast import literal_eval
df['genres'] = df['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x])
df['main_genre'] = df['genres'].apply(lambda x: x[0] if x else 'Unknown')
sns.countplot(data=df, y='main_genre', order=df['main_genre'].value_counts().index[:10])
plt.title('Most Common Genres')
plt.show()
