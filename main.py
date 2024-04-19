import streamlit as st
import pickle
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the pre-trained model
with open('C:\\Users\\SunTec\\Desktop\\New folder\\sentiment_analysis_project\\Sentiment-Analysis-using-streamlit\\sentiment_model.pickle', 'rb') as f:
    model = pickle.load(f)

# Load the tokenizer for the model
tokenizer = AutoTokenizer.from_pretrained("FacebookAI/roberta-base")

# List of emotion labels with corresponding emojis
emotion_emojis = {
    'admiration': '😊',
    'amusement': '😄',
    'anger': '😠',
    'annoyance': '😒',
    'approval': '👍',
    'caring': '❤️',
    'confusion': '😕',
    'curiosity': '🤔',
    'desire': '😍',
    'disappointment': '😞',
    'disapproval': '👎',
    'disgust': '🤢',
    'embarrassment': '😳',
    'excitement': '😆',
    'fear': '😨',
    'gratitude': '🙏',
    'grief': '😢',
    'joy': '😂',
    'love': '😍',
    'nervousness': '😬',
    'optimism': '😊',
    'pride': '😊',
    'realization': '😲',
    'relief': '😌',
    'remorse': '😔',
    'sadness': '😔',
    'surprise': '😮',
    'neutral': '😐'
}

# Function to perform sentiment analysis
def predict_sentiment(text):
    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    
    # Perform sentiment analysis
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class = torch.argmax(outputs.logits).item()
    
    # Get the predicted emotion label
    predicted_emotion = list(emotion_emojis.keys())[predicted_class]
    
    return predicted_emotion

# Streamlit web application
def main():
    # Set title and description
    st.title('Sentiment Analysis App')
    st.write('<span style="font-size:12px;">By Shubham Sharma.</span>', unsafe_allow_html=True)
    st.markdown("[Click Here For Source code ](https://github.com/shubham88c-pr)")
    st.markdown("[Click Here For My LinkedIn Profile ](https://www.linkedin.com/in/shubham-sharma-5bb453221)")
    st.write('Enter some text to analyze its sentiment.')

    # User input for text
    text = st.text_area('Input Text', '')

    # Perform sentiment analysis when user clicks the button
    if st.button('Analyze Sentiment'):
        if text.strip() == '':
            st.warning('Please enter some text.')
        else:
            # Perform sentiment analysis
            sentiment_emotion = predict_sentiment(text)
            emoji = emotion_emojis.get(sentiment_emotion, '❓')  # Default emoji if not found
            st.write(f'Predicted Emotion: {sentiment_emotion} {emoji}')

# Run the app
if __name__ == '__main__':
    main()
