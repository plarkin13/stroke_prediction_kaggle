import pandas as pd
import streamlit as st
import pickle 
import matplotlib.pyplot as plt

#add page config
st.set_page_config(
    page_icon='📖',
    initial_sidebar_state='expanded'
)

# add title
st.title('Do you write more like Poe or Austen?')

#add description
st.write('Select which page you want to view')

#add sidebar
page = st.sidebar.selectbox('Page', ('About', 'EDA', 'Make a Prediction'))

#write reusable functions

@st.cache

def load_data():
    df = pd.read_csv('data/austen_poe.csv')
    return df

@st.cache
def load_vectorized_data():
    vectorized_df = pd.read_csv('data/vectorized_text.csv')
    return vectorized_df

if page == 'About':
    st.subheader('About this project')
    st.write("Here's what happened...")
elif page == 'EDA':
    st.subheader('Exploratory Data Analysis')
    st.write("this model was trained on...")

    df = load_data()
    st.table(df.sample(5))

    vec = load_vectorized_data()
    top_10 = (vec.drop(columns = ['original_author']).sum().sort_values(ascending = False).head(10))

    #create visualization
    fig, ax = plt.subplots()
    ax.bar(x = top_10.index, height = top_10.values)

    ax.set_title('Occurence of most common words')
    st.pyplot(fig)

elif page == 'Make a Prediction':
    st.subheader('Which author do you write like?')
    st.write('Enter your text to generate a prediction')

    #load in model
    with open('models/mnb_pipe.pkl', 'rb') as pickle_in:
        pipe = pickle.load(pickle_in)
    
    your_text = st.text_input(label = 'Enter your text here')
    value = 'Quoth the raven, nevermore',
    max_chars = 1000

    predicted_author = pipe.predict([your_text])[0]

    st.subheader('Results:')
    st.write(f'You write most like: {predicted_author}')