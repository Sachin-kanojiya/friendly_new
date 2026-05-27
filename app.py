import streamlit as st




st.markdown(
    """
    <style>
    /* Sidebar background color */
    section[data-testid="stSidebar"] {
        background-color: #f2f6ff;
    }

    </style>
    """,
    unsafe_allow_html=True
)



st.title("Web Harvesting")

# here using a bit of animation for makin home page interactive
# st.subheader("Welcome TO Screen Scripting ")
st.markdown(
    """
    <style>
    .rainbow-text {
        background: linear-gradient(
            270deg,
            red, orange, yellow, green, blue, indigo, violet
        );
        background-size: 400% 400%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: rainbow 6s ease infinite;
        font-weight: bold;
        font-size: 24px;
    }

    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>

    <div class="rainbow-text">
        Welcome TO Screen Scripting 
    </div>
    """,
    unsafe_allow_html=True
)





st.write(
    "This is the main page. "
    "Use the sidebar buttons to navigate to other pages."
)

st.image("images/bgimage.png", use_container_width=True)# if need to resize can be done by ====> width=30px 




