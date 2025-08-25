import streamlit as st
import numpy as np
import pandas as pd

st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">""", unsafe_allow_html=True)
st.markdown("""
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>""", unsafe_allow_html=True)

st.markdown("""
<nav class="navbar navbar-expand-lg navbar-light bg-light" style="background-color: blue;margin-top: -70px;">
  <div class="container-fluid" >
    <a class="navbar-brand" href="https://streamlit.io/">Streamlit</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="https://streamlit.io/gallery">Gallery</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://streamlit.io/components">Components</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://streamlit.io/cloud">Cloud</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="https://streamlit.io/community" tabindex="-1">Community</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
""", unsafe_allow_html=True)


# SIDEBAR
about = st.Page(page="pages/usabout.py",
                title="About page",
                icon="🅰️",
                # default=True,
                )
mtrail = st.Page(page="pages/mtrial.py",
                title="Trail page",
                icon="📈",
              )

contact = st.Page(page="pages/contact.py",
                title="Contact page",
                icon="Ⓜ️"
                )

message = st.Page(page="pages/message.py",
                title="Message page",
                icon="🏦"
                )

pg = st.navigation({"One":[about, mtrail],"Two":[message,contact]})

pg.run()




# TOP NAV BAR

# pages = {
#      "Your account": [
#          st.Page("pages\contact.py", title="Create your account"),
#          st.Page("pages\\usabout.py", title="Manage your account"),
#      ],
#      "Resources": [
#          st.Page("pages\message.py", title="Learn about us"),
#          st.Page("pages\mtrial.py", title="Try it out"),
#      ],
#  }

# pg = st.navigation(pages, position="top")
# pg.run()