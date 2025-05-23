import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.datasets import load_iris

iris_data = load_iris()
data = pd.DataFrame(iris_data.data, columns=iris_data.feature_names)

fig = plt.figure()
sns.histplot(data=data, bins=20)
st.pyplot(fig)

fig = plt.figure()
sns.boxplot(data=data)
st.pyplot(fig)

fig = plt.figure()
sns.scatterplot(data=data)
st.pyplot(fig)