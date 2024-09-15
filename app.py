import os
import boto3
import streamlit as st
import torch
from transformers import pipeline

bucket_name = 'mlops-garage'
s3_prefix = 'models'
local_path = 'tinybert-sentiment-analysis'
s3 = boto3.client('s3')

def download_directory(bucket_name, local_path, s3_prefix):
    os.makedirs(local_path, exist_ok = True)
    paginator = s3.get_paginator('list_objects_v2')
    for page in paginator.paginate(Bucket = bucket_name, Prefix = s3_prefix):
        if 'Contents' in page.keys():
            for item in page['Contents']:
                s3_key = item['Key']
                rel_path = os.path.relpath(s3_key, s3_prefix)
                local_file = os.path.join(local_path, rel_path)
                print(f'Downloading file {s3_key} from bucket {bucket_name}')
                s3.download_file(Bucket = bucket_name, Key = s3_key, Filename = local_file)
        else:
            print(f'Bucket {bucket_name} is empty!')

st.title('SentimenTool')
st.header('Sentiment Analyzer Tool')

selectino_model = st.selectbox('Model', ['TinyBERT'])
selection_dataset = st.selectbox('Data', ['IMDB'])
btn_dwonload = st.button('Download model')
if btn_dwonload:
    with st.spinner('Downloading, please wait...'):
        download_directory(bucket_name = bucket_name, local_path = local_path, s3_prefix = s3_prefix)

tweet_text = st.text_area('Tweet')
btn_predict = st.button('Predict')

device = torch.device('mps') if torch.backends.mps.is_available() else torch.device('cpu')
model = pipeline('text-classification', model = 'tinybert-sentiment-analysis', device = device)

if btn_predict:
    with st.spinner('Predicting, please wait...'):
        pred = model(tweet_text)
        st.write(pred)









