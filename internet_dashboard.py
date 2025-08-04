import pandas as pd
import plotly_express as px
import streamlit as st

st.set_page_config(layout='wide')

df = pd.read_csv('share-of-individuals-using-the-internet.csv')
df = df[(df['Year'] >= 2000) & (df['Year'] <= 2016)]
print(df.columns)
print(df.info())

st.header('Internet Usage Dashboard')

years = df['Year'].unique()
years.sort()
countries = df['Country'].unique()

selected_year = st.selectbox(label = 'Year',
                             index = 0,
                             options = years)

df_plot = df[df['Year'] == selected_year]

col1, col2 = st.columns([3,1])

plot = px.choropleth(data_frame= df_plot,
                     locations = 'Country',
                     locationmode='country names',
                     color = 'Individuals using the Internet (% of population)',
                     color_continuous_scale=px.colors.qualitative.Vivid,
                     title = 'Visual showing internet usage percentage across countries')

histogram_1 = px.histogram(data_frame=df_plot,
                           x = 'Individuals using the Internet (% of population)',
                           title='Distribution of Internet Usage for year {}'.format(selected_year))

col1.plotly_chart(plot)
col2.plotly_chart(histogram_1)

st.sidebar.subheader('Country level detail')

form = st.sidebar.form('form')
select_country = form.selectbox(label = 'Select Country',
               options = countries,
               index =  0)
submit = form.form_submit_button('Submit')

if submit:
    st.subheader('Country level analytics for {}'.format(select_country))
    df_by_year_and_country = df[df['Country'] == select_country]
    line_plot = px.line(data_frame= df_by_year_and_country,
                   x= 'Year',
                   y = 'Individuals using the Internet (% of population)',
                   title = 'Internet Usage over time in {}'.format(select_country))
    st.plotly_chart(line_plot)