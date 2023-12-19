import streamlit as st

def main():
    st.title("Rain prediction app")

    minTemp_slider = st.slider("Min temperature", min_value=-10, max_value=50, step=1)
    maxTemp_slider = st.slider("Max temperature", min_value=-10, max_value=50, step=1)
    rainfall_slider = st.slider("Rainfall", min_value=0, max_value=400, step=1)
    evaporation_slider = st.slider("Evaporation", min_value=0, max_value=150, step=1)
    sunshine_slider = st.slider("Sunshine", min_value=0, max_value=15, step=1)
    windGustSpeed_slider = st.slider("Wind gust speed", min_value=0, max_value=140, step=1)
    windSpeed9am_slider = st.slider("Wind speed at 9am", min_value=0, max_value=140, step=1)
    windSpeed3pm_slider = st.slider("Wind speed at 3am", min_value=0, max_value=140, step=1)
    humidity9am_slider = st.slider("Humidity at 9am", min_value=0, max_value=100, step=1)
    humidity3pm_slider = st.slider("Humidity at 3pm", min_value=0, max_value=100, step=1)
    pressure9am_slider = st.slider("Pressure at 9am", min_value=970, max_value=1050, step=1)
    pressure3pm_slider = st.slider("Pressure at 3pm", min_value=970, max_value=1050, step=1)
    cloud9am_slider = st.slider("Cloudiness at 9am", min_value=0, max_value=10, step=1)
    cloud3pm_slider = st.slider("Cloudiness at 3pm", min_value=0, max_value=10, step=1)
    temp9am_slider = st.slider("Temperature at 9am", min_value=-10, max_value=50, step=1)
    temp3pm_slider = st.slider("Temperature at 3pm", min_value=-10, max_value=50, step=1)




if __name__ == "__main__":
    main()