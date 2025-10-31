import streamlit as st 
import pickle

with open('personality.pkl', 'rb') as f:
    model = pickle.load(f)
    
st.title("مدل تشخیص شخصیت")
st.text("لطفا اطلاعات خود را وارد کنید")
Time_spent_Alone = st.number_input("میزان زمان تنهایی",min_value=0, max_value=11)
Social_event_attendance=st.number_input("میزان زمان شرکت در رویداد اجتماعی",min_value=0, max_value=10)
Going_outside=st.number_input("میزان زمان بیرون رفتن",min_value=0, max_value=7)
Friends_circle_size=st.number_input("تعداد دوستان",min_value=0, max_value=15)
Post_frequency=st.number_input("تعداد پست در روز",min_value=0, max_value=10)
Drained_after_socializing=st.number_input("خسته شدن بعد از معاشرت",min_value=0, max_value=10)

dict_stage={
    "دارم":1,
    "ندارم":0
}
Stage_fear=st.radio("ترس از صحنه", dict_stage.keys())
Stage_fear_number = dict_stage[Stage_fear]


dict_personality={
    "0":"برونگرا",
    "1":"درونگرا"
}


if st.button ("پیش بینی"):
    data=[[Time_spent_Alone, Stage_fear_number, Social_event_attendance,
       Going_outside, Drained_after_socializing, Friends_circle_size,
       Post_frequency]]
    
    y_pred=str(model.predict(data)[0])
    st.write("شخصیت شما :",dict_personality[y_pred])


st.text("توسط:رزیتا بویر")