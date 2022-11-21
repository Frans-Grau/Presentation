### Required Imports
import streamlit as st
import streamlit_nested_layout 
from streamlit_option_menu import option_menu
from PIL import Image

### App layout
st.set_page_config(page_title=None, page_icon=None, layout="wide", menu_items=None)
st.title('Francisco Grau')
st.markdown('fransgrau0@gmail.com // +34 686 418 704')
st.write(" ")

### Code
selected = option_menu(menu_title=None, options = ["About me", "Experience", "Portfolio"], orientation = "horizontal",)

if selected == "About me":
    col, col1, col2 = st.columns([1,0.1,0.8])
    
    with col:
        st.subheader('Nice to meet you :)') 
        st.markdown('''<div style="text-align: justify;">I am a BBA graduate from ESADE Business School in Barcelona, Spain who after a few 
        working years, decided to enter the exciting world of Data and enrolled a full-time Data Analysis Bootcamp in Lisbon.</div>''', unsafe_allow_html=True)
        st.write('')
        st.markdown('''<div style="text-align: justify;">My last role was as a Consultant (Venture Architect) at Liquid Lab Ventures, 
        a Corporate Venture Builder, where I leveraged lean startups' methodology - Venture Building - to ideate, validate 
        (Fast-Business Prototyping), launch and operate new digital business models for corporate clients. From a given hunting ground 
        to low-fidelity MVPs and later scale-ups. Performed all tasks from opportunity size definition (TAM/SAM/SOM) 
        to digital marketing campaigns design, landing pages, analytics monitoring and Investment Memorandums' drafts. 
        </div>''', unsafe_allow_html=True)
        st.write('')
        st.markdown('''<div style="text-align: justify;">Further, I designed Digital Transformation Strategies for traditional corporations 
        aiming at boosting their presence in the digital scene and take advantage of new technologies to engage directly with customers 
        (D2C channels) and gather qualitative insights for future iterations within their Business Model. 
        Lastly, I co-wrote a book on Corporate Venture Building techniques</div>''', unsafe_allow_html=True)
        st.write('')
        st.markdown('''<div style="text-align: justify;">Prior to that last work expereince, I worked as a Junior Consultan an Operations 
        Consulting firm where weak spots in clients’ operations and handling activities were identified based on benchmarking and 
        data analysis in order to increase effciency. However, my first real work experience was an intership 
        I did in Singapore for SATS a ground handling and food solution provider for airports and airlines.</div>''', unsafe_allow_html=True)
    
    with col1:
        st.subheader('')   

    with col2:
        st.subheader('I wrote a book! ')
        inner_cols = st.columns([0.5,2])
        with inner_cols[0]:
                image = Image.open('portada_libro2.png')
                st.image(image)
        with inner_cols[1]: 
                st.markdown('''<div style="text-align: justify;"> In my time at Liquid Lab Ventures among my usual tasks I led the process 
                of documenting our methodology and writting a book where the Venture Building process is explained and detailed with our 
                own ventures and expepreinces. The book is a guide for all of those willing to launch a new business making the most 
                of the digital world! </div>''', unsafe_allow_html=True)

if selected == "Experience":
    col3, col4 = st.columns(2)

    with col3:
        st.subheader('TT')
        st.markdown('**_Year_**: 1972')
    
    with col4:
        st.subheader('XXX')
        st.markdown('**_XXX')

if selected == "Portfolio":
    col5, colx, col6 = st.columns([0.8,0.1,0.8])

    with col5:
        st.subheader('Movie Recomendation Engine')
        
        inner_cols = st.columns([0.4,2])
        with inner_cols[0]:
                image = Image.open('portada_libro2.png')
                st.image(image)
        with inner_cols[1]: 
                st.markdown('''<div style="text-align: justify;">Movie recommendation engine powered by Machine Learning (KNNeighbors). The engine
                is twofold; if given a movie title it recommends 3 other movies based on genre, duration, year and rating amongst others. Further, 
                it also presents the user with three top picks for the most rated genres and a sneak-peek to the movie's trailer. </div>''', unsafe_allow_html=True)
                st.write('')
                st.markdown('''<div style="text-align: justify;">This project leverages two databases: Imdb and Rotten Tomatoes. In terms of technology, the 
                the engine is built with streamlit and all the EDA and ML with python and its libraries such as Pandas and Scikit-learn.</div>''', unsafe_allow_html=True)
        
        st.subheader('Movie Recomendation Engine')      
        inner_cols = st.columns([0.4,2])
        with inner_cols[0]:
                image = Image.open('portada_libro2.png')
                st.image(image)
        with inner_cols[1]: 
                st.markdown('''<div style="text-align: justify;"> In my time at Liquid Lab Ventures among my usual tasks I led the process 
                of documenting our methodology and writting a book where the Venture Building process is explained and detailed with our 
                own ventures and expepreinces. The book is a guide for all of those willing to launch a new business making the most 
                of the digital world! </div>''', unsafe_allow_html=True)
    with colx:
        st.subheader('')   

    with col6:
        st.subheader('Movie Recomendation Engine')
        
        inner_cols = st.columns([0.4,2])
        with inner_cols[0]:
                image = Image.open('portada_libro2.png')
                st.image(image)
        with inner_cols[1]: 
                st.markdown('''<div style="text-align: justify;"> In my </div>''', unsafe_allow_html=True)