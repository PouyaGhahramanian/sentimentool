# SentimenTool

SentimenTool is a simple sentiment analysis web application built using Streamlit and Hugging Face Transformers. It allows users to download a pre-trained model and analyze sentiment on user-inputted texts.

## How It Works

1. **Select the Model**: Currently supports TinyBERT for sentiment analysis.
2. **Select the Dataset**: Currently supports the IMDB dataset for sentiment analysis.
3. **Download Model**: Downloads the pre-trained TinyBERT model from an S3 bucket. 
4. **Enter Text**: Input any text for sentiment prediction.
5. **Get Prediction**: The tool returns a sentiment label (positive/negative) and a confidence score.

<img width="1086" alt="sentimentool" src="https://github.com/user-attachments/assets/a801f11e-cd3e-48f1-969d-24f3a2a01ea6">
