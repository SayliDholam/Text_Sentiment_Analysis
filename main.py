from textblob import TextBlob
import pandas as pd
import streamlit as st
import cleantext
import matplotlib.pyplot as plt
from googletrans import Translator

# Initialize the Google Translator
translator = Translator()

# Set up the header for the Streamlit app
st.header('Sentiment Analysis')

# Function to analyze sentiment
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = round(blob.sentiment.polarity, 2)
    subjectivity = round(blob.sentiment.subjectivity, 2)

    # Initialize contributions
    positive_contribution = 0
    negative_contribution = 0
    neutral_contribution = 0
    
    # Calculate contributions
    if polarity > 0:
        positive_contribution = polarity * 100  # Scale of 0 to 1
    elif polarity < 0:
        negative_contribution = abs(polarity) * 100  # Scale of 0 to 1
    else:
        neutral_contribution = 100  # Fully neutral
    
    return polarity, subjectivity, positive_contribution, negative_contribution, neutral_contribution

# English Text Analysis Section
with st.expander('Analyze English Text'):
    english_text = st.text_input('English Text here: ')
    if english_text:
        polarity, subjectivity, positive_contribution, negative_contribution, neutral_contribution = analyze_sentiment(english_text)

        # Display results
        st.write('Polarity: ', polarity)
        st.write('Subjectivity: ', subjectivity)
        st.write(f"Positive Contribution: {round(positive_contribution, 2)}%")
        st.write(f"Negative Contribution: {round(negative_contribution, 2)}%")
        st.write(f"Neutral Contribution: {round(neutral_contribution, 2)}%")

# Hindi Text Analysis Section
with st.expander('Analyze Hindi Text'):
    hindi_text = st.text_input('Hindi Text here: ')
    if hindi_text:
        try:
            # Translate Hindi text to English for analysis
            translated_hindi = translator.translate(hindi_text, dest='en').text
            polarity, subjectivity, positive_contribution, negative_contribution, neutral_contribution = analyze_sentiment(translated_hindi)

            # Display results
            st.write('Polarity: ', polarity)
            st.write('Subjectivity: ', subjectivity)
            st.write(f"Positive Contribution: {round(positive_contribution, 2)}%")
            st.write(f"Negative Contribution: {round(negative_contribution, 2)}%")
            st.write(f"Neutral Contribution: {round(neutral_contribution, 2)}%")
        except Exception as e:
            st.error("Error in translation: " + str(e))

# Marathi Text Analysis Section
with st.expander('Analyze Marathi Text'):
    marathi_text = st.text_input('Marathi Text here: ')
    if marathi_text:
        try:
            # Translate Marathi text to English for analysis
            translated_marathi = translator.translate(marathi_text, dest='en').text
            polarity, subjectivity, positive_contribution, negative_contribution, neutral_contribution = analyze_sentiment(translated_marathi)

            # Display results
            st.write('Polarity: ', polarity)
            st.write('Subjectivity: ', subjectivity)
            st.write(f"Positive Contribution: {round(positive_contribution, 2)}%")
            st.write(f"Negative Contribution: {round(negative_contribution, 2)}%")
            st.write(f"Neutral Contribution: {round(neutral_contribution, 2)}%")
        except Exception as e:
            st.error("Error in translation: " + str(e))

# CSV Analysis Section for English Texts
with st.expander('Analyze CSV for English Texts'):
    upl_eng = st.file_uploader('Upload English text file (xlsx)', type='xlsx')

    if upl_eng:
        df_eng = pd.read_excel(upl_eng)

        # Check if 'tweets' column exists
        if 'tweets' not in df_eng.columns:
            st.error("The file should have a 'tweets' column containing the text.")
        else:
            # Apply sentiment analysis to the text directly (No translation needed)
            df_eng['polarity'], df_eng['subjectivity'], df_eng['positive_contribution'], df_eng['negative_contribution'], df_eng['neutral_contribution'] = zip( 
                *df_eng['tweets'].apply(analyze_sentiment)
            )

            # Add analysis labels based on scores
            def analyze(x, positive_threshold=0.5, negative_threshold=-0.5):
                if x >= positive_threshold:
                    return 'Positive'
                elif x <= negative_threshold:
                    return 'Negative'
                else:
                    return 'Neutral'
            
            df_eng['analysis'] = df_eng['polarity'].apply(analyze)
            st.write(df_eng[['tweets', 'polarity', 'positive_contribution', 'negative_contribution', 'neutral_contribution', 'analysis']].head(10))

            # Visualize sentiment distribution
            sentiment_counts_eng = df_eng['analysis'].value_counts()
            st.bar_chart(sentiment_counts_eng)

            # Display sentiment distribution as a bar chart using Matplotlib
            plt.figure(figsize=(8, 4))
            plt.bar(sentiment_counts_eng.index, sentiment_counts_eng.values, color=['#00FF00', '#FFD700', '#FF0000'])
            plt.title('Sentiment Distribution')
            plt.xlabel('Sentiment')
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            st.pyplot(plt)

            # Function to convert dataframe to CSV
            @st.cache_data
            def convert_df_eng(df_eng):
                return df_eng.to_csv().encode('utf-8')

            csv_eng = convert_df_eng(df_eng)

            st.download_button(
                label="Download English CSV",
                data=csv_eng,
                file_name='sentiment_english.csv',
                mime='text/csv',
            )

# CSV Analysis Section for Hindi and Marathi Texts
with st.expander('Analyze CSV for Hindi/Marathi Texts'):
    upl = st.file_uploader('Upload Hindi/Marathi text file (xlsx)', type='xlsx')

    if upl:
        df = pd.read_excel(upl)

        # Check if 'tweets' column exists
        if 'tweets' not in df.columns:
            st.error("The file should have a 'tweets' column containing the text.")
        else:
            # Translate non-English tweets to English and analyze sentiment
            df['translated_text'] = df['tweets'].apply(lambda x: translator.translate(x, dest='en').text)

            # Apply sentiment analysis to the translated text
            df['polarity'], df['subjectivity'], df['positive_contribution'], df['negative_contribution'], df['neutral_contribution'] = zip(
                *df['translated_text'].apply(analyze_sentiment)
            )

            # Add analysis labels based on scores
            def analyze(x, positive_threshold=0.5, negative_threshold=-0.5):
                if x >= positive_threshold:
                    return 'Positive'
                elif x <= negative_threshold:
                    return 'Negative'
                else:
                    return 'Neutral'
            
            df['analysis'] = df['polarity'].apply(analyze)
            st.write(df[['tweets', 'translated_text', 'polarity', 'positive_contribution', 'negative_contribution', 'neutral_contribution', 'analysis']].head(10))

            # Visualize sentiment distribution
            sentiment_counts = df['analysis'].value_counts()
            st.bar_chart(sentiment_counts)

            # Display sentiment distribution as a bar chart using Matplotlib
            plt.figure(figsize=(8, 4))
            plt.bar(sentiment_counts.index, sentiment_counts.values, color=['#00FF00', '#FFD700', '#FF0000'])
            plt.title('Sentiment Distribution')
            plt.xlabel('Sentiment')
            plt.ylabel('Count')
            plt.xticks(rotation=45)
            st.pyplot(plt)

            # Function to convert dataframe to CSV
            @st.cache_data
            def convert_df(df):
                return df.to_csv().encode('utf-8')

            csv = convert_df(df)

            st.download_button(
                label="Download Hindi/Marathi CSV",
                data=csv,
                file_name='sentiment_hindi_marathi.csv',
                mime='text/csv',
            )
