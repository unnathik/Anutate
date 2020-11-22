import streamlit as st
from gensim.summarization import summarize

import spacy
import nltk

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

def sumy_summarizer(docx):
    parser = PlaintextParser.from_string(docx, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, 3)
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

def main():
    st.title("Anutate")
    st.subheader("Your on-the-go annotation assistant!")
    message = st.text_area("Enter your text: could be a textbook or notes snippet that you'd like to extract the most value from!", "")
    summary_options = st.selectbox("What would you like?", ("A short, crisp annotation", "A longer but detailed annotation"))
   

    if st.button("Generate"):
        if summary_options == 'A short, crisp annotation':
            st.text('Generating your short and crisp annotation...')
            summary_result = summarize(message)
        elif summary_options == 'A longer but detailed annotation':
            st.text('Generating your longer but detailed annotation...')
            summary_result = sumy_summarizer(message)
        
        else:
            st.warning("Using default summarizer")
            st.text("Using gensim...")
            summary_result = summarize(message)

        st.success(summary_result)
    
    st.sidebar.subheader("About the App")
    st.sidebar.info("Anutate is an intelligent web app to assist you in note-taking. It helps you generate annotations for longer pieces of text, to extract the most meaning. I hope this is useful!")
    st.sidebar.info("Note: the web app will work most effectively if you input text with more than 10 lines.")

    st.sidebar.subheader("Contact: unnathiutpal6@gmail.com")

if __name__ == "__main__":
    main()