import streamlit as st
## libraries
import pandas as pd
import numpy as np

# visualization
import altair as alt

st.set_page_config(page_title='Streamlit - Dashboard 🤯',
                    page_icon="🚀",
                    layout='wide'
)

st.title("Analysys of the marketing campaign")

def load_data():
    df = pd.read_csv('bank_marketing.csv')


    #split the names of the columns and the rows
    names = df.columns.str.split(';').tolist()
    df = df.iloc[:, 0].str.split(';', expand=True)
    df.columns = names

    #from multi-index to simple index
    df.columns = df.columns.get_level_values(0)

    #replacing the " " from the columns names.
    df.columns = df.columns.str.replace('(["])', '')

    #removing " " from the rows
    df['job'] = df.job.str.replace('"', '')
    df['marital'] = df.marital.str.replace('"', '')
    df['education'] = df.education.str.replace('"', '')
    df['default'] = df.default.str.replace('"', '')
    df['housing'] = df.housing.str.replace('"', '')
    df['loan'] = df.loan.str.replace('"', '')
    df['contact'] = df.contact.str.replace('"', '')
    df['month'] = df.month.str.replace('"', '')
    df['day_of_week'] = df.day_of_week.str.replace('"', '')
    df['duration'] = df.duration.str.replace('"', '')
    df['campaign'] = df.campaign.str.replace('"', '')
    df['pdays'] = df.pdays.str.replace('"', '')
    df['previous'] = df.previous.str.replace('"', '')
    df['poutcome'] = df.poutcome.str.replace('"', '')
    df['y'] = df.y.str.replace('"', '')

    # changing data type
    df["age"] = df["age"].astype(int)
    df["duration"] = df["duration"].astype(int)
    df["campaign"] = df["campaign"].astype(int)
    df["pdays"] = df["pdays"].astype(int)
    df["previous"] = df["previous"].astype(int)
    df["emp.var.rate"] = df["emp.var.rate"].astype(float)
    df["cons.price.idx"] = df["cons.price.idx"].astype(float)
    df["cons.conf.idx"] = df["cons.conf.idx"].astype(float)
    df["euribor3m"] = df["euribor3m"].astype(float)
    df["nr.employed"] = df["nr.employed"].astype(float)

    # renaming the similar indexes to avoid feature problems 
    df.loc[ df['education'] == 'unknown', 'education'] = 'no info'
    df.loc[ df['job'] == 'unknown', 'job'] = 'no answer'
    df.loc[ df['housing'] == 'unknown', 'housing'] = 'no registers'

    # convert the y column to int. 0 means no and 1 means yes.
    df['y'] = df['y'].map({'yes': 1, 'no': 0})
    # rename the column.
    df.rename(columns = {'y':'result'}, inplace = True)

    # df succesfull campaigns
    df_success_camp = df[df['result'] == 1] 

    return df

df = load_data()

@st.cache(suppress_st_warning=True)
def get_fvalue(val):
    feature_dict = {"No":1,"Yes":2}
    for key,value in feature_dict.items():
        if val == key:
            return value

def get_value(val,my_dict):
    for key,value in my_dict.items():
        if val == key:
            return value

app_mode = st.sidebar.selectbox('Select Page',['EDA','UML', 'SML']) #two pages

if app_mode=='EDA':
    st.title('Describing the client :')  
    st.image('client.jpg')
    df
    st.text("Visualization of chosen categories")
    source = df_success_camp
    alt.Chart(source).mark_boxplot(extent='min-max').encode(
    x='education:O',
    y='age:Q'
    )
    st.box_plot
