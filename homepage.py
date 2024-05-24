import streamlit as st
from map import map

# Add a sidebar
st.sidebar.title("Navigation")
st.sidebar.write("Use the sidebar to navigate")

# Add a selectbox in the sidebar
option = st.sidebar.selectbox(
    'Select a page:',
    ('Home', 'Map')
)

# Display content based on the selected page
if option == 'Home':
    # Home Page Content
    st.title("Welcome to My Streamlit Homepage")
    st.header("About This App")
    st.write("""
    This is a simple homepage created using Streamlit. 
    Streamlit is an open-source app framework for Machine Learning and Data Science projects.
    It helps you create beautiful web apps with minimal effort.
    """)
    st.image("https://rapidweblaunch.com/wp-content/uploads/2021/08/web-design-meme-18.jpg", caption='Sample Image')
elif option == 'Map':
    st.title("Mapa do crl")
    st.header("do crl mesmo")
    map()
else:
    st.write("RIP")
