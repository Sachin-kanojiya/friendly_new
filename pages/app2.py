import streamlit as st
from logic import harvest_html   #  connect logic

st.title("Entire Html Code ")
st.subheader("This Is Where You  Can  Find  Entire Html Code ")

url = st.text_input("Enter url of website")

st.write("Download file")

#  LOGIC CONNECTION 
if st.button("Click to download"):

    if not url.strip():
        st.error("Please enter a valid URL")
    else:
        try:
            html_data = harvest_html(url)   #  call logic

            # create text file
            with open("harvested_data.text", "w", encoding="utf-8") as f:
                f.write(html_data)

            st.success("File ready")

            # download
            st.download_button(
                label="Download harvested file",
                data=html_data,
                file_name="harvested_data.text",
                mime="text/plain"
            )

        except Exception as e:
            st.error("Error fetching website")


if st.button("Back to Home"):
    st.switch_page("app.py")
