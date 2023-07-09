import pickle
import streamlit as st
with open('model.pickle', 'rb') as file:
    model = pickle.load(file)

print(model)

st.title('Spam Email classifier')

email = st.text_input(label ='Enter you mail : ')

if st.button('Submit'):
    email = email.lower()
    y_pred = model.predict([email])
    st.write(y_pred[0])