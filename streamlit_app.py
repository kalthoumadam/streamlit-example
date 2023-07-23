from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import plotly.express as px

# Page setting
st.set_page_config(layout="wide", page_title="Trends")

with open('/Users/kalthoumadam/Documents/GitHub/streamlit-example/style.css') as f:
  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#logo image
logo="/Users/kalthoumadam/Documents/GitHub/streamlit-example/wordcloud.png"
color_arxiv='red'
color_patent='blue'
# -- Read in the data
df_submission=pd.read_csv("/Users/kalthoumadam/Documents/GitHub/streamlit-example/dashboard_submission_yearly.csv")
df_arxiv_category = pd.read_csv("/Users/kalthoumadam/Documents/GitHub/streamlit-example/dashboard_arxiv_normalized_category_freq.csv")
df_patent_category = pd.read_csv("/Users/kalthoumadam/Documents/GitHub/streamlit-example/dashboard_patent_normalized_category_freq.csv")
df_arxiv_term = pd.read_csv("/Users/kalthoumadam/Documents/GitHub/streamlit-example/dashboard_arxiv_normalized_term_frequency.csv")
df_patent_term = pd.read_csv("/Users/kalthoumadam/Documents/GitHub/streamlit-example/dashboard_patent_normalized_term_freq.csv")

st.markdown("<h1 style='text-align: center; color: '#F3F3F3';'>Trending topics across Academia and Industry</h1>", unsafe_allow_html=True)


yearly_submission, arxiv_col, patent_col= st.columns([1,1,1])
with yearly_submission:
    fig = px.line(df_submission, x="year", y=["arxiv","patent"], color_discrete_map={
                 "arxiv": "#F3AD78",
                 "patent": "#30C3CD"}, labels={'Year', 'Number of sumbission'})
    fig.update_layout(title="Yearly sumbission for arXiv and patents")
    st.plotly_chart(fig, use_container_width=True)

with arxiv_col:
    arxiv_choice = st.selectbox(
        "Choose Category for frequency over years",
        ("Computer Science", "Economics", "Electrical Engineering and Systems Science", "Mathematics", "Physics", "Quantitative Biology", "Quantitative Finance", "Statistics"),
    )
    fig = px.bar(df_arxiv_category , x="year", y=arxiv_choice)
    fig.update_layout(title="arXiv Category frequency")
    # -- Input the Plotly chart to the Streamlit interface
    st.plotly_chart(fig, use_container_width=False)

with patent_col:
    patent_choice = st.selectbox(
        "Choose Category for frequency over years",
        ("Chemistry; Metallurgy", "Electricity", "Fixed Construction", "General Technology", "Human Necessities", "Mechanical Engineering; Lighting; Heating; Weapons; Blasting", "Performing Operation; Transporting", "Physics","Textiles; Paper"),
    )
    fig = px.bar(df_patent_category , x="year", y=patent_choice, color_discrete_map={patent_choice : color_patent})
    fig.update_layout(title="Patent Category frequency")
    # -- Input the Plotly chart to the Streamlit interface
    st.plotly_chart(fig, use_container_width=False)




term_col,center_col,word_col = st.columns([1,1.5,1])
    

with term_col:
    choice =st.selectbox(
        "Choose a Term for frequency over years",
        ("artificial intelligence", "internet of things", "virtual reality", "quantum computing", "robotics", "cloud computing", "autonomous vehicles", "blockchain","covid-19", "physics","superconductivity"),
    )
    options=['ArXiv', 'Patents']
    option=st.radio('Choose the dataset to display Term frequency', options)
    if option == 'ArXiv':
        data=df_arxiv_term
        choice_color=color_arxiv
    else:
        data=df_patent_term
        choice_color=color_patent
    
   

with center_col:
    fig = px.bar(data, x="year", y=choice, color_discrete_map={choice : choice_color})
    fig.update_layout(title="Dataset Category frequency")
    # -- Input the Plotly chart to the Streamlit interface
    st.plotly_chart(fig, use_container_width=False)

word_col.image(logo)





    

