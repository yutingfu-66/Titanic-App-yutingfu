
# import packages
import streamlit as st
import pandas as pd
import matplotlib as plt
import seaborn as sns
sns.set()

# show the titleS
st.title('Titanic-App-yutingfu')

# read csv and show the dataframe
df = pd.read_csv('train.csv')
df

# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
fig,  axes = plt.subplots(1,3,figsize = (15, 5) )
df[df['Pclass'] == 1].boxplot(column = 'Fare', ax=axes[0])
axes[0].set_xlabel('PClass = 1')
axes[0].set_ylabel('Fare')

df[df['Pclass'] == 2].boxplot(column='Fare', ax=axes[1])
axes[1].set_xlabel('PClass = 2')
axes[1].set_ylabel('Fare')

df[df['Pclass'] == 3].boxplot(column='Fare', ax=axes[2])
axes[2].set_xlabel('PClass = 3')
axes[2].set_ylabel('Fare')

plt.tight_layout()
st.pyplot(fig)

