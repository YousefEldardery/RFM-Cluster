import pandas as pd
import numpy as np
import streamlit as st
import sklearn


df = pd.read_csv("df_Clustered.csv")

def get_recommendations(user , num_of_recom):
    try:
        cluster = df[df["CustomerID"] == int(user)]["Cluster"].unique()[0]
        df_cluster = df[df["Cluster"] == cluster]
        Top_Merchant_index = df_cluster.groupby("MerchantName")["TransactionValue"].sum().nlargest(num_of_recom).index
        for index , mer in enumerate(Top_Merchant_index) :
            st.text(f"The Recommended Merchant number {index} is {mer}")
    except:
        st.text(f"The User number {user} is not exist")

def main():
    st.title("RFM Recommendations")
    user = st.text_input("User ID")
    num_of_recom = st.selectbox("num of recommendations" , list(range(1,10)))
    if st.button("Recommend"):
        get_recommendations(user , num_of_recom)

main()
