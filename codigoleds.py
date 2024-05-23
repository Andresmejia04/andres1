import streamlit as st

# Estados iniciales de las luces LED
if 'led_blue' not in st.session_state:
    st.session_state.led_blue = False
if 'led_red' not in st.session_state:
    st.session_state.led_red = False
if 'led_green' not in st.session_state:
    st.session_state.led_green = False

# Funciones para encender y apagar las luces
def toggle_led(state):
    return not state

st.title("Control de Luces LED")

# Botones para controlar las luces LED
if st.button('Toggle LED Azul (A)'):
    st.session_state.led_blue = toggle_led(st.session_state.led_blue)
if st.button('Toggle LED Roja (B)'):
    st.session_state.led_red = toggle_led(st.session_state.led_red)
if st.button('Toggle LED Verde (C)'):
    st.session_state.led_green = toggle_led(st.session_state.led_green)

# Mostrar el estado actual de las luces
st.write(f"Luz LED Azul: {'Encendida' if st.session_state.led_blue else 'Apagada'}")
st.write(f"Luz LED Roja: {'Encendida' if st.session_state.led_red else 'Apagada'}")
st.write(f"Luz LED Verde: {'Encendida' if st.session_state.led_green else 'Apagada'}")

# Cambiar el color del texto según el estado de las luces
if st.session_state.led_blue:
    st.markdown("<p style='color:blue;'>LED Azul Encendida</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='color:gray;'>LED Azul Apagada</p>", unsafe_allow_html=True)

if st.session_state.led_red:
    st.markdown("<p style='color:red;'>LED Roja Encendida</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='color:gray;'>LED Roja Apagada</p>", unsafe_allow_html=True)

if st.session_state.led_green:
    st.markdown("<p style='color:green;'>LED Verde Encendida</p>", unsafe_allow_html=True)
else:
    st.markdown("<p style='color:gray;'>LED Verde Apagada</p>", unsafe_allow_html=True)

