# import streamlit as st 
# import pickle
# import streamlit.components.v1 as components

# with open('personality.pkl', 'rb') as f:
#     model = pickle.load(f)
    
# st.title("مدل تشخیص شخصیت")
# st.text("لطفا اطلاعات خود را وارد کنید")
# Time_spent_Alone = st.number_input("میزان زمان تنهایی",min_value=0, max_value=11)
# Social_event_attendance=st.number_input("میزان زمان شرکت در رویداد اجتماعی",min_value=0, max_value=10)
# Going_outside=st.number_input("میزان زمان بیرون رفتن",min_value=0, max_value=7)
# Friends_circle_size=st.number_input("تعداد دوستان",min_value=0, max_value=15)
# Post_frequency=st.number_input("تعداد پست در روز",min_value=0, max_value=10)
# Drained_after_socializing=st.number_input("خسته شدن بعد از معاشرت",min_value=0, max_value=10)

# dict_stage={
#     "دارم":1,
#     "ندارم":0
# }
# Stage_fear=st.radio("ترس از صحنه", dict_stage.keys())
# Stage_fear_number = dict_stage[Stage_fear]

# dict_personality={
#     "0":"برونگرا",
#     "1":"درونگرا"
# }

# if st.button ("پیش بینی"):
#     data=[[Time_spent_Alone, Stage_fear_number, Social_event_attendance,
#        Going_outside, Drained_after_socializing, Friends_circle_size,
#        Post_frequency]]
    
#     y_pred=str(model.predict(data)[0])
#     st.write("شخصیت شما :",dict_personality[y_pred])

# st.text("توسط:رزیتا بویر")

import streamlit as st
import streamlit as st
import pickle
import streamlit.components.v1 as components

with open('personality.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="مدل تشخیص شخصیت", page_icon="🧠", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #A0D8F1, #FFFFFF);
    color: #FF1493;
}
.card {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.25);
    margin-bottom: 20px;
    color: #FF1493;
}
.title {
    color: #FF1493;
    text-align: center;
    font-size: 2.5em;
    font-weight: bold;
}
.footer {
    color: #FF1493;
    text-align: center;
}
label, .st-bx, .stRadio > div > label, .stNumberInput > label {
    color: #FF1493 !important;
}
.stRadio > div > label {
    color: #FF1493 !important;
}
.stButton > button {
    background-color: #FF1493;
    color: white;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

snow_html = """
<div style="position: fixed; top:0; left:0; width:100%; height:100%; z-index:-1; overflow:hidden;">
  <canvas id="snow" style="width:100%; height:100%;"></canvas>
  <script>
    const canvas = document.getElementById('snow');
    const ctx = canvas.getContext('2d');
    function resizeCanvas() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
    window.addEventListener('resize', resizeCanvas);
    resizeCanvas();
    const flakes = [];
    for(let i=0;i<300;i++){
        flakes.push({x:Math.random()*canvas.width, y:Math.random()*canvas.height, r:Math.random()*3+1, d:Math.random()*1});
    }
    function draw(){
        ctx.clearRect(0,0,canvas.width,canvas.height);
        ctx.fillStyle="#FFB6C1";
        ctx.beginPath();
        for(let i=0;i<flakes.length;i++){
            let f = flakes[i];
            ctx.moveTo(f.x,f.y);
            ctx.arc(f.x,f.y,f.r,0,Math.PI*2,true);
        }
        ctx.fill();
        move();
    }
    function move(){
        for(let i=0;i<flakes.length;i++){
            let f=flakes[i];
            f.y += Math.pow(f.d,2) + 1;
            if(f.y > canvas.height){ f.y = 0; f.x = Math.random()*canvas.width; }
        }
    }
    setInterval(draw,30);
  </script>
</div>
"""
components.html(snow_html, height=0)

st.markdown("<h1 class='title'>🧠 مدل تشخیص شخصیت</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>لطفا اطلاعات خود را وارد کنید</p>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        Time_spent_Alone = st.number_input("⏳ میزان زمان تنهایی", min_value=0, max_value=11)
        Social_event_attendance = st.number_input("🎉 میزان زمان شرکت در رویداد اجتماعی", min_value=0, max_value=10)
        Going_outside = st.number_input("🚶‍♀️ میزان زمان بیرون رفتن", min_value=0, max_value=7)
    with col2:
        Friends_circle_size = st.number_input("👥 تعداد دوستان", min_value=0, max_value=15)
        Post_frequency = st.number_input("📱 تعداد پست در روز", min_value=0, max_value=10)
        Drained_after_socializing = st.number_input("😴 خسته شدن بعد از معاشرت", min_value=0, max_value=10)
    dict_stage = {"دارم":1, "ندارم":0}
    Stage_fear = st.radio("😨 ترس از صحنه", list(dict_stage.keys()), horizontal=True)
    Stage_fear_number = dict_stage[Stage_fear]
    st.markdown("</div>", unsafe_allow_html=True)

dict_personality = {"0":"برونگرا", "1":"درونگرا"}

with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    if st.button("💡 پیش بینی"):
        data=[[Time_spent_Alone, Stage_fear_number, Social_event_attendance,
               Going_outside, Drained_after_socializing, Friends_circle_size,
               Post_frequency]]
        y_pred=str(model.predict(data)[0])
        st.markdown(f"<h2 style='text-align:center; color:#FF1493;'>✨ شخصیت شما: {dict_personality[y_pred]}</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p class='footer'>توسط: رزیتا بویر</p>", unsafe_allow_html=True)






