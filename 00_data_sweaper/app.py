import pandas as pd
import streamlit as st 
import os
from io import BytesIO

# Page configuration
st.set_page_config(page_title="Data Sweeper", page_icon=":bar_chart:", layout="wide")
st.title("Data Sweeper")
st.write("This app is designed to help you find the best data for your project.")

# File Uploading
uploaded_file = st.file_uploader("Upload a CSV or Excel file", type=["csv", "xlsx"], accept_multiple_files=True)

# Handle file
if uploaded_file:
    for file in uploaded_file:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        elif file.name.endswith(".xlsx"):
            df = pd.read_excel(file)
        else:
            st.error("Unsupported file format. Please upload a CSV or Excel file.")
            continue

        # File name and size
        st.write(f"**File Name**: {file.name}")
        st.write(f"**File Size**: {file.size/1024}")

        st.write("**Data Preview**")
        st.dataframe(df.head())

        # Data Cleaning
        st.subheader("Data Cleaning Options")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)

            with col1:
                if st.button(f"Remove duplicates from {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.success("Duplicates removed successfully!")


            with col2:
                if st.button(f"Fill missing values from {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.success("Missing values filled successfully!")


        # Choose specific coloumns
        st.subheader("Select Columns to Convert")
        selected_columns = st.multiselect("Select columns to convert", df.columns, default=df.columns)
        df = df[selected_columns]

        # Create some visualizations
        st.subheader("Data Visualizations")
        if st.checkbox(f"Show visualizations for {file.name}"):
            st.bar_chart(df.select_dtypes(include=['number']).iloc[:, :2])

        # Convert file to CSV or Excel
        st.subheader("Convert File") 
        conversion_type = st.radio("Select conversion type", ("CSV", "Excel"))   
        if st.button(f"Convert {file.name} to {conversion_type}"):
            buffer = BytesIO()
            if conversion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.split('.')[0] + '.csv'
                mime_type = 'text/csv'

            elif conversion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.split('.')[0] + '.xlsx'
                mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            buffer.seek(0)  


        st.download_button(
            label=f"Download {file.name}",
            data=buffer,
            file_name=file_name,
            mime=mime_type
        )


