import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.io import mmwrite, mmread
import pickle

df_review = pd.read_csv('../games_with_review_and_genre.csv')
df_review.info()

Tfidf = TfidfVectorizer(sublinear_tf=True)
Tfidf_matrix = Tfidf.fit_transform(df_review['reviews'])
print(Tfidf_matrix.shape)

with open('../models/tfidf.pickle', 'wb') as f:
    pickle.dump(Tfidf, f)

mmwrite('../models/Tfidf_review.mtx', Tfidf_matrix)
