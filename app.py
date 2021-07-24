import streamlit as st

import pickle
import numpy as np
model=pickle.load(open('Pickle_RF_Pump.pkl','rb'))


def predict_machine_status(sensor_41,sensor_42,sensor_43,sensor_44,sensor_45,sensor_46,sensor_47,sensor_48,sensor_49,sensor_51):
    input=np.array([[sensor_41,sensor_42,sensor_43,sensor_44,sensor_45,sensor_46,sensor_47,sensor_48,sensor_49,sensor_51]]).astype(np.float64)
    pred=model.predict(input)
    return int(pred)

def main():
    
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Machine Status Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    
    sensor_41=st.slider('Enter Sensor 41 Value',0.0,40.0)
    sensor_42=st.slider('Enter Sensor 42 Value',0.0,40.0)
    sensor_43=st.slider('Enter Sensor 43 Value',0.0,40.0)
    sensor_44=st.slider('Enter Sensor 44 Value',0.0,40.0)
    sensor_45=st.slider('Enter Sensor 45 Value',0.0,40.0)
    sensor_46=st.slider('Enter Sensor 46 Value',0.0,40.0)
    sensor_47=st.slider('Enter Sensor 47 Value',0.0,40.0)
    sensor_48=st.slider('Enter Sensor 48 Value',0.0,40.0)
    sensor_49=st.slider('Enter Sensor 49 Value',0.0,40.0)
    sensor_50=st.slider('Enter Sensor 50 Value',0.0,40.0)
    sensor_51=st.slider('Enter Sensor 51 Value',0.0,40.0)
    
   
    

    if st.button("Predict"):
        output=predict_machine_status(sensor_41,sensor_42,sensor_43,sensor_44,sensor_45,sensor_46,sensor_47,sensor_48,sensor_49,sensor_51)
        st.title('The condition of machine is {}'.format(output))

    

if __name__=='__main__':
    main()