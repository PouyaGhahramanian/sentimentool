# SentimenTool

SentimenTool is a simple sentiment analysis web application built using Streamlit and Hugging Face Transformers. It allows users to download a pre-trained model and analyze sentiment on user-inputted texts.

You can access and use the SentimenTool directly online at https://sentimentool.streamlit.app/.

## How It Works

1. **Select the Model**: Currently supports TinyBERT for sentiment analysis.
2. **Select the Dataset**: Currently supports the IMDB dataset for sentiment analysis.
3. **Download Model**: Downloads the pre-trained TinyBERT model from an S3 bucket. 
4. **Enter Text**: Input any text for sentiment prediction.
5. **Get Prediction**: The tool returns a sentiment label (positive/negative) and a confidence score.

![Screenshot 2024-09-24 at 00 07 36](https://github.com/user-attachments/assets/8e0b69ae-c6ca-4595-a5c9-db98cb6786b0)
