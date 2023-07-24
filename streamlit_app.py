from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import plotly.express as px

# Page setting
st.set_page_config(layout="wide", page_title="Trends")

with open('style.css') as f:
  st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


#word cloud image
patent_cloud="patent_word_cloud.png"
arxiv_cloud="arxiv_word_cloud.png"

color_arxiv='red'
color_patent='blue'
# -- Read in the data
df_submission=pd.read_csv("dashboard_submission_yearly.csv")
df_arxiv_category = pd.read_csv("dashboard_arxiv_normalized_category_freq.csv")
df_patent_category = pd.read_csv("dashboard_patent_normalized_category_freq.csv")
df_arxiv_term = pd.read_csv("dashboard_arxiv_normalized_term_frequency.csv")
df_patent_term = pd.read_csv("dashboard_patent_normalized_term_freq.csv")

st.markdown("<h1 style='text-align: center; color: '#F3F3F3';'>Trending topics across Academia and Industry</h1>", unsafe_allow_html=True)
st.markdown("<br><br>", unsafe_allow_html=True)

yearly_submission, arxiv_col, patent_col= st.columns([1,1,1])
with yearly_submission:
    fig = px.line(df_submission, x="year", y=["arxiv","patent"], labels={'Year', 'Number of sumbission'})
    fig.update_layout(title=dict(text="Yearly sumbission for arXiv and patents", font=dict(size=20)))
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    st.plotly_chart(fig, use_container_width=True)

with arxiv_col:
    arxiv_choice = st.selectbox(
        "Choose Category for frequency over years",
        ("Computer Science", "Economics", "Electrical Engineering and Systems Science", "Mathematics", "Physics", "Quantitative Biology", "Quantitative Finance", "Statistics"),
    )
    fig = px.bar(df_arxiv_category , x="year", y=arxiv_choice)
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    fig.update_layout(title=dict(text="ArXiv Category Frequency", font=dict(size=20)))
    # -- Input the Plotly chart to the Streamlit interface
    st.plotly_chart(fig, use_container_width=False)

with patent_col:
    patent_choice = st.selectbox(
        "Choose Category for frequency over years",
        ("Chemistry; Metallurgy", "Electricity", "Fixed Construction", "General Technology", "Human Necessities", "Mechanical Engineering; Lighting; Heating; Weapons; Blasting", "Performing Operation; Transporting", "Physics","Textiles; Paper"),
    )
    fig = px.bar(df_patent_category , x="year", y=patent_choice, color_discrete_map={patent_choice : color_patent})
    fig.update_layout(title=dict(text="Patents Category Frequency", font=dict(size=20)))
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    # -- Input the Plotly chart to the Streamlit interface
    st.plotly_chart(fig, use_container_width=False)




term_col,center_col,word_col = st.columns([1,1,1])
    

with term_col:
    choice =st.selectbox(
        "Choose a Term for frequency over years",
        ("artificial intelligence", "internet of things", "virtual reality", "quantum computing", "robotics", "cloud computing", "autonomous vehicles", "blockchain","covid-19", "physics","superconductivity"),
    )
    fig = px.line(df_arxiv_term, x="year", y=choice) 
    fig.add_scatter(x=df_patent_term['year'], y=df_patent_term[choice], mode='lines', name="Patents")
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)

    fig.update_layout(title=dict(text="Dataset Category frequency", font=dict(size=20)))
    # -- Input the Plotly chart to the Streamlit interface
    st.plotly_chart(fig, use_container_width=False)


    
with center_col:
    st.markdown("<h3 style='text-align: center; color: '#F3F3F3';'>ArXiv dataset word cloud </h3>", unsafe_allow_html=True)
    st.image(arxiv_cloud)
    

    

with word_col:
    st.markdown("<h3 style='text-align: center; color: '#F3F3F3';'>Patents dataset word cloud </h3>", unsafe_allow_html=True)
    st.image(patent_cloud)





    

