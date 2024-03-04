#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import re

def clean_publication_name(text):
    # If the text starts with 'www.', return the text as it is
    if text.startswith('www.'):
        return text
    
    # Remove the contents within parentheses
    text = re.sub(r"\(.*?\)", "", text)
    
    text = re.sub(r"\..*$", "", text)
    text = re.sub(r"[^\w\s-]", "", text).lower()
    text = re.sub(r"\s", "", text)
    
    # Return None if the cleaned text is empty
    return text if text else None

# Title and description for your app
st.title("Publication Cleaner Tool")
st.write("This tool cleans publication names within Excel files.")

# File upload for 'CS Chorus List.xlsx'
uploaded_file1 = st.file_uploader("Upload 'CS Chorus List.xlsx':", type="xlsx")

# File upload for 'GCH List.xlsx'
uploaded_file2 = st.file_uploader("Upload 'GCH List.xlsx':", type="xlsx")

if uploaded_file1 is not None and uploaded_file2 is not None:
    # Read the data from uploaded files using pandas.read_excel
    data1 = pd.read_excel(uploaded_file1)
    data2 = pd.read_excel(uploaded_file2)

    # Clean the data
    publications1 = data1['Publications'].tolist()
    cleaned_publications1 = [clean_publication_name(pub) for pub in publications1]
    cleaned_data1 = pd.DataFrame({'Cleaned Publication Name': cleaned_publications1})

    publications2 = data2['Publication'].tolist()
    cleaned_publications2 = [clean_publication_name(pub) for pub in publications2]
    cleaned_data2 = pd.DataFrame({'Cleaned Publication Name': cleaned_publications2})

    # Download cleaned data as CSV files (alternative to Excel)
    st.download_button(
        label="Download Cleaned 'CS Chorus List.xlsx' (as CSV)",
        data=cleaned_data1.to_csv(index=False),
        file_name="Cleaned CS Chorus List.csv",
        mime="text/csv"
    )

    st.download_button(
        label="Download Cleaned 'GCH List.xlsx' (as CSV)",
        data=cleaned_data2.to_csv(index=False),
        file_name="Cleaned GCH List.csv",
        mime="text/csv"
    )

else:
    st.info("Please upload both files.")

