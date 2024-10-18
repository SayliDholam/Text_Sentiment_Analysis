from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Set up the header for the Streamlit app
st.header('Sentiment Analysis')

# Text analysis section
with st.expander('Analyze Text'):
    text = st.text_input('Text here: ')
    if text:
        blob = TextBlob(text)
        st.write('Polarity: ', round(blob.sentiment.polarity, 2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity, 2))

    pre = st.text_input('Clean Text: ')
    if pre:
        st.write(cleantext.clean(pre, clean_all=False, extra_spaces=True,
                                 stopwords=True, lowercase=True, numbers=True, punct=True))

# CSV analysis section
with st.expander('Analyze CSV'):
    upl = st.file_uploader('Upload file')

    def score(x):
        blob1 = TextBlob(x)
        return blob1.sentiment.polarity

    def analyze(x, positive_threshold=0.5, negative_threshold=-0.5):
        if x >= positive_threshold:
            return 'Positive'
        elif x <= negative_threshold:
            return 'Negative'
        else:
            return 'Neutral'

    if upl:
        df = pd.read_excel(upl)
        
        # Check if the 'Unnamed: 0' column exists before attempting to delete it
        if 'Unnamed: 0' in df.columns:
            del df['Unnamed: 0']
        
        # Proceed with scoring and analysis
        df['score'] = df['tweets'].apply(score)
        df['analysis'] = df['score'].apply(analyze)
        st.write(df.head(10))

        # Visualize sentiment distribution
        sentiment_counts = df['analysis'].value_counts()
        
        # Create a bar chart for sentiment distribution
        st.subheader('Sentiment Distribution')
        st.bar_chart(sentiment_counts)

        # Display sentiment distribution as a bar chart using Matplotlib
        plt.figure(figsize=(8, 4))
        plt.bar(sentiment_counts.index, sentiment_counts.values, color=['#00FF00', '#FFD700', '#FF0000'])
        plt.title('Sentiment Distribution')
        plt.xlabel('Sentiment')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        st.pyplot(plt)

        # Generate and display word clouds for positive and negative sentiments
        positive_words = ' '.join(df[df['analysis'] == 'Positive']['tweets'])
        negative_words = ' '.join(df[df['analysis'] == 'Negative']['tweets'])

        # Create word clouds
        positive_wc = WordCloud(width=800, height=400, background_color='white').generate(positive_words)
        negative_wc = WordCloud(width=800, height=400, background_color='black', colormap='Reds').generate(negative_words)

        # Display the word clouds
        st.subheader('Word Cloud for Positive Sentiments')
        plt.figure(figsize=(10, 5))
        plt.imshow(positive_wc, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)

        st.subheader('Word Cloud for Negative Sentiments')
        plt.figure(figsize=(10, 5))
        plt.imshow(negative_wc, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt)

        @st.cache
        def convert_df(df):
            # IMPORTANT: Cache the conversion to prevent computation on every rerun
            return df.to_csv().encode('utf-8')

        csv = convert_df(df)

        st.download_button(
            label="Download data as CSV",
            data=csv,
            file_name='sentiment.csv',
            mime='text/csv',
        )

