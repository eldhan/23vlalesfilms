import streamlit as st


st.title("Indicateurs des tendances")
st.markdown(
    "<p class='centered-paragraph'>KPI sur les tendances du cinéma.</p>",
    unsafe_allow_html=True,
)
st.markdown(
    '<iframe class="iframe_powerbi" title="projet2_powerbi" width="600" height="636" src="https://app.powerbi.com/view?r=eyJrIjoiMTA0YzgxYWUtZWQ4My00ZTFhLWJjZTMtMGZkZGIzNjc4ODkzIiwidCI6ImRjZjlkYjM3LTc0MGUtNDZkZS04NTFiLWQ1YTE1MGNlYmVhNSJ9" frameborder="0" allowFullScreen="true"></iframe>',
    unsafe_allow_html=True,
)
