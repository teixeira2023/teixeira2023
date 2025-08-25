import streamlit as st
from controller import LightController

def main():
    st.title("Light Controller")
    
    controller = LightController()
    
    st.header("Control the Lights")
    
    for i in range(1, 5):
        intensity = st.slider(f"Light {i} Intensity", 0, 3, 0, 1, format="%d")
        controller.set_intensity(i, intensity)
    
    if st.button("Show Current State"):
        current_state = controller.get_current_state()
        st.write("Current Light Intensities:")
        for light, intensity in current_state.items():
            st.write(f"Light {light}: Intensity {intensity}")

if __name__ == "__main__":
    main()