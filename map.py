import streamlit as st
import folium
from streamlit_folium import st_folium
from opencage.geocoder import OpenCageGeocode

# Set the title of the app
st.title("OpenStreetMap with Streamlit")

# Set your OpenCage API key
opencage_api_key = st.secrets["open_cage_api_key"]
geocoder = OpenCageGeocode(opencage_api_key)

# Set a default location (Lisbon, near Alameda)
default_location = "Lisbon, Alameda"

# Function to get coordinates from location name
def get_coordinates(place):
    result = geocoder.geocode(place)
    if result and len(result):
        return [result[0]['geometry']['lat'], result[0]['geometry']['lng']]
    else:
        return None

def map():
    # Input box for the user to enter a location
    user_location = st.text_input("Enter a location:", default_location)

    # Get coordinates for the user-entered location
    coordinates = get_coordinates(user_location)

    # Create a map centered at the user-entered location or default if invalid
    if coordinates:
        m = folium.Map(location=coordinates, zoom_start=13)
        folium.Marker(
            location=coordinates,
            popup=user_location,
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)
    else:
        st.write("Location not found. Using default location.")
        default_coords = get_coordinates(default_location)
        m = folium.Map(location=default_coords, zoom_start=13)
        folium.Marker(
            location=default_coords,
            popup=default_location,
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)

    # Display the map in the Streamlit app
    st_data = st_folium(m, width=725)

    # Optionally, you can add more components or customization
    st.write("This is an example of how to integrate OpenStreetMap with Streamlit using folium.")
