import streamlit as st


st.title("Indicateurs des performances")
st.write(
    "Présentation de l’identification des acteurs les plus présents et les périodes associées, l’évolution de la durée moyenne des films au fil des années, la comparaison entre les acteurs présents au cinéma et dans les séries, l’âge moyen des acteurs, ainsi que les films les mieux notés et les caractéristiques qu’ils partagent."
)
st.markdown(
    '<iframe class="iframe_powerbi"  title="projet2_powerbi" width="600" height="636" src="https://app.powerbi.com/view?r=eyJrIjoiYTg1NmQyNGYtYTlkYS00ZmI2LWI2MmQtZDYwZTNlZjk1YzJjIiwidCI6ImRjZjlkYjM3LTc0MGUtNDZkZS04NTFiLWQ1YTE1MGNlYmVhNSJ9&pageName=a0b29f7e9243c02194c0" frameborder="0" allowFullScreen="true"></iframe>',
    unsafe_allow_html=True,
)
