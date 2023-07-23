from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import plotly.express as px

# Page setting
st.set_page_config(layout="wide", page_title="Trends")

logo="logo.png"
head1, head2 = st.columns(2)
head1.image(logo)
st.markdown("<h1 style='text-align: center; color: #1697B7;'>Trends Across Academia and Industry</h1>", unsafe_allow_html=True)

# -- Read in the data
df_submission=pd.read_csv("/data/dashboard_submission_yearly.csv")
df_arxiv_category = pd.read_csv("/data/dashboard_arxiv_normalized_category_freq.csv")
df_patent_category = pd.read_csv("/data/dashboard_patent_normalized_category_freq.csv")
df_arxiv_term = pd.read_csv("/data/dashboard_arxiv_normalized_term_frequency.csv")
df_patent_term = pd.read_csv("/data/dashboard_patent_normalized_term_freq.csv")

fig = px.line(df_submission, x="year", y=["arxiv","patent"], color_discrete_map={
                 "arxiv": "#F3AD78",
                 "patent": "#30C3CD"})
fig.update_layout(title="Yearly sumbission for arXiv and patents")
st.plotly_chart(fig, use_container_width=True)


arxiv_col, patent_col = st.columns([3, 3])
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
    fig = px.bar(df_patent_category , x="year", y=patent_choice)
    fig.update_layout(title="Patent Category frequency")
    # -- Input the Plotly chart to the Streamlit interface
    st.plotly_chart(fig, use_container_width=False)


arxiv_term_col, patent_term_col = st.columns([3, 3])
with arxiv_term_col:
    arxiv_term_choice = st.selectbox(
        "Choose arXiv Term for frequency over years",
        ("artificial intelligence", "internet of things", "virtual reality", "quantum computing", "robotics", "cloud computing", "autonomous vehicles", "blockchain","covid-19", "physics","superconductivity"),
    )
    fig = px.bar(df_arxiv_term , x="year", y=arxiv_term_choice)
    fig.update_layout(title="arXiv Term frequency")
    # -- Input the Plotly chart to the Streamlit interface
    st.plotly_chart(fig, use_container_width=False)

with patent_term_col:
    patent_term_choice = st.selectbox(
        "Choose Patent term for frequency over years",
        ("artificial intelligence", "internet of things", "virtual reality", "quantum computing", "robotics", "cloud computing", "autonomous vehicles", "blockchain","covid-19", "physics","superconductivity"),
    )
    fig = px.bar(df_patent_term , x="year", y=patent_term_choice)
    fig.update_layout(title="Patent Term frequency")
    # -- Input the Plotly chart to the Streamlit interface
    st.plotly_chart(fig, use_container_width=False)




    

