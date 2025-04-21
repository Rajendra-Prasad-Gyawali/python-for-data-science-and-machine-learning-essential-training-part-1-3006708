import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

animals = ['cat', 'cow', 'goat', 'dog']
heights = [30,60,40,35]
weights = [5,400,80,60]

fig, ax = plt.subplots()

x = np.arange(len(heights))
width = 0.40

ax.bar(x-0.2, heights, width, color='red')
ax.bar(x+0.2, weights, width, color='orange')

ax.legend(['height', 'weight'])
ax.set_xticks(x)
ax.set_xticklabels(animals)

st.pyplot(fig)

explode = [0.2, 0.1, 0.1, 0.1]
plot_pie, ax = plt.subplots()
ax.pie(heights,explode=explode, labels=animals, autopct='%1.1f%%', shadow=True)
ax.axis('equal')

st.pyplot(plot_pie)
