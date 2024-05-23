import streamlit as st

led_blue = False
led_red = False
led_green = False

def toggle_led(state):
    return not state

st.title("Control de Luces LED")

if st.button('Toggle LED Azul (A)'):
    led_blue = toggle_led(led_blue)
if st.button('Toggle LED Roja (B)'):
    led_red = toggle_led(led_red)
if st.button('Toggle LED Verde (C)'):
    led_green = toggle_led(led_green)

st.write(f"Luz LED Azul: {'Encendida' (led_blue) else 'Apagada'}")
st.write(f"Luz LED Roja: {'Encendida' if led_red else 'Apagada'}")
st.write(f"Luz LED Verde: {'Encendida' if led_green else 'Apagada'}")

if led_blue:
    st.markdown("<p style='color:blue;'>LED Azul Encendida</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='color:gray;'>LED Azul Apagada</p>", unsafe_allow_html=True)

if led_red:
    st.markdown("<p style='color:red;'>LED Roja Encendida</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='color:gray;'>LED Roja Apagada</p>", unsafe_allow_html=True)

if led_green:
    st.markdown("<p style='color:green;'>LED Verde Encendida</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='color:gray;'>LED Verde Apagada</p>", unsafe_allow_html=True)
