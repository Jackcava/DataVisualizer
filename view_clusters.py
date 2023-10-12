import os
import streamlit as st
import pandas as pd
import plotly.express as px

# streamlit run [.py file]

st.set_page_config(page_title="Telomeropathy - Clustering analysis", page_icon=":hospital:",layout="wide")
st.markdown("<h1 style='text-align: center; color: black;'>Telomeropathy - Clustering analysis</h1>", unsafe_allow_html=True)

curr_path = os.getcwd()
files = os.listdir(os.path.join(curr_path))

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
        
        first_dim_opts = ['dim0','dim1','dim2','dim3']
        second_dim_opts = ['dim0','dim1','dim2','dim3']
        with col1:
            first_dim = st.selectbox(
            'Choose the first dimension to display:',
            tuple(first_dim_opts),key="first_dim")
            second_dim_opts = [el for el in first_dim_opts if el != first_dim]

            symbol = st.radio(
                "Choose the variable to display:",
                (None, "Mutations", "Classification","GENE","VARIANT","ZYGOSITY","INHERITANCE","L1°p","L10°p"),
                key="2D_1"
            )
        
        with col2:
            second_dim = st.selectbox(
            'Choose the second dimension to display:',
            tuple(second_dim_opts),key="second_dim",)
            first_dim_opts = [el for el in second_dim_opts if el != second_dim]

            annotation = st.radio(
                "Choose the annotation to display:",
                (None, "UPN", "Mutations", "Classification","GENE","VARIANT","ZYGOSITY","INHERITANCE","L1°p","L10°p"),
                key="2D_2"
            )

        fig = px.scatter(df, x=first_dim, y=second_dim,
                        color="Cluster", symbol=symbol, text=annotation, log_x=True, width=1200, height=800)
        fig.update_traces(marker_size=10, textposition='top center')
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    with tab_3dD:

        _, col1, col2, col3, _ = st.columns([1, 1, 1, 1, 1])
        
        with col1:
            symbol = st.radio(
                "Choose the dimensions to plot:",
                ("dim0-dim1-dim2", "dim0-dim1-dim3","dim1-dim2-dim3","dim0-dim2-dim3"),
                key="dims"
            )
            if symbol == "dim0-dim1-dim2":
                first_dim3D="dim0"
                second_dim3D="dim1"
                third_dim3D="dim2"
            elif symbol == "dim0-dim1-dim3":
                first_dim3D="dim0"
                second_dim3D="dim1"
                third_dim3D="dim3"
            elif symbol == "dim1-dim2-dim3":
                first_dim3D="dim1"
                second_dim3D="dim2"
                third_dim3D="dim3"
            elif symbol == "dim0-dim2-dim3":
                first_dim3D="dim0"
                second_dim3D="dim2"
                third_dim3D="dim3"

        with col2:
            symbol = st.radio(
                "Choose the variable to display:",
                (None, "Mutations", "Classification","GENE","VARIANT","ZYGOSITY","INHERITANCE","L1°p","L10°p"),
                key="3D_1"
            )
        
        with col3:
            annotation = st.radio(
                "Choose the annotation to display:",
                (None, "UPN", "Mutations", "Classification","GENE","VARIANT","ZYGOSITY","INHERITANCE","L1°p","L10°p"),
                key="3D_2"
            )

        fig = px.scatter_3d(df, x=first_dim3D, y=second_dim3D, z=third_dim3D,
                    color='Cluster', symbol=symbol, text=annotation, log_x=True, width=1200, height=1000)
        #fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))
        
        fig.update_traces(marker_size=5, textposition='top center', textfont_size=25)

        st.plotly_chart(fig, theme="streamlit", use_container_width=True)