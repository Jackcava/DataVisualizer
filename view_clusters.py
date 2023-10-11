import os
import streamlit as st
import pandas as pd
import plotly.express as px

# streamlit run [.py file]

st.set_page_config(page_title="Telomeropathy - Clustering analysis", page_icon=":hospital:",layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'>Telomeropathy - Clustering analysis</h1>", unsafe_allow_html=True)

curr_path = os.getcwd()
files = os.listdir(os.path.join(curr_path))
#df = pd.read_excel("TBD_clustered.xlsx")

extensions = [".xlsx"]
uploaded_file = st.file_uploader("**Upload your ready-to-use dataset here:**", type=extensions)

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, header = 0)
    if st.checkbox('Show dataset',key="uploaded file"):
        st.write(str(df.shape[0]) + " rows x " + str(df.shape[1]) + " columns")
        st.dataframe(df)

    tab_2D, tab_3dD = st.tabs(["Plot 2D", "Dynamic 3D"])

    with tab_2D:

        _, _, col1, col2, _, _ = st.columns([1, 1, 1, 1, 1, 1])
        
        with col1:
            symbol = st.radio(
                "Choose the variable to display:",
                (None, "Mutations", "Classification","GENE","VARIANT","ZYGOSITY","INHERITANCE","L1°p","L10°p"),
                key="2D_1"
            )
        
        with col2:
            annotation = st.radio(
                "Choose the annotation to display:",
                (None, "UPN", "Mutations", "Classification","GENE","VARIANT","ZYGOSITY","INHERITANCE","L1°p","L10°p"),
                key="2D_2"
            )

        fig = px.scatter(df, x="dim0", y="dim1",
                        color="Cluster", symbol=symbol, text=annotation, log_x=True, width=1200, height=800)
        fig.update_traces(marker_size=10, textposition='top center')
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    with tab_3dD:

        _, _, col1, col2, _, _ = st.columns([1, 1, 1, 1, 1, 1])
        
        with col1:
            symbol = st.radio(
                "Choose the variable to display:",
                (None, "Mutations", "Classification","GENE","VARIANT","ZYGOSITY","INHERITANCE","L1°p","L10°p"),
                key="3D_1"
            )
        
        with col2:
            annotation = st.radio(
                "Choose the annotation to display:",
                (None, "UPN", "Mutations", "Classification","GENE","VARIANT","ZYGOSITY","INHERITANCE","L1°p","L10°p"),
                key="3D_2"
            )

        fig = px.scatter_3d(df, x='dim0', y='dim1', z='dim2',
                    color='Cluster', symbol=symbol, text=annotation, log_x=True, width=1200, height=1000)
        #fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        
        fig.update_traces(marker_size=5, textposition='top center', textfont_size=25)

        st.plotly_chart(fig, theme="streamlit", use_container_width=True)