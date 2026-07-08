import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("netflix_titles_cleaned.csv")

print("=" * 50)
print("Dataset Shape")
print("=" * 50)
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nSummary Statistics")
print(df.describe(include="all"))

# ----------------------------
# Movies vs TV Shows
# ----------------------------
plt.figure(figsize=(6,4))
df["type"].value_counts().plot(kind="bar")
plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ----------------------------
# Top 10 Countries
# ----------------------------
plt.figure(figsize=(10,5))
df["country"].value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# Top 10 Ratings
# ----------------------------
plt.figure(figsize=(8,5))
df["rating"].value_counts().head(10).plot(kind="bar")
plt.title("Content Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# ----------------------------
# Content Released by Year
# ----------------------------
plt.figure(figsize=(12,5))
df["release_year"].value_counts().sort_index().plot()
plt.title("Netflix Content by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.tight_layout()
plt.show()

# ----------------------------
# Top Directors
# ----------------------------
top_directors = df[df["director"] != "Unknown"]["director"].value_counts().head(10)

plt.figure(figsize=(10,5))
top_directors.plot(kind="bar")
plt.title("Top 10 Directors")
plt.xlabel("Director")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ----------------------------
# Top Genres
# ----------------------------
genres = (
    df["listed_in"]
    .str.split(", ")
    .explode()
)

plt.figure(figsize=(10,6))
genres.value_counts().head(10).plot(kind="bar")
plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("images/top_countries.png", dpi=300, bbox_inches="tight")
plt.savefig("images/ratings.png", dpi=300, bbox_inches="tight")
plt.savefig("images/release_year.png", dpi=300, bbox_inches="tight")
plt.savefig("images/top_directors.png", dpi=300, bbox_inches="tight")
plt.savefig("images/top_genres.png", dpi=300, bbox_inches="tight")

print("\nEDA Completed Successfully!")