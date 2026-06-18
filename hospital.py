import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

#Title
st.set_page_config(page_title="Smart Hospital Patient Navigator Arman",
                  page_icon="🏥", layout="wide")

# Load Model and Style
with open("style.html", "r", encoding="utf-8") as f:
    style = f.read()


st.markdown(style, unsafe_allow_html = True)

@st.cache_resource
def load_model():
    with open('hospital_model.pkl', 'rb') as f:
        return pickle.load(f)

bundle        = load_model()
model         = bundle['model']
scaler        = bundle['scaler']
features      = bundle['features']
cols_to_scale = bundle['cols_to_scale']
dept_map_inv  = bundle['dept_map_inv']
gender_map    = bundle['gender_map']
temp_map      = bundle['temp_map']
hr_map        = bundle['hr_map']
dur_map       = bundle['dur_map']
cc_map        = bundle['cc_map']

DEPT_INFO = {
    'Respiratory Medicine': {
        'icon':'🫁','color':'#0284c7','bg':'#e0f2fe','border':'#7dd3fc',
        'desc':'Specialises in conditions affecting the lungs and airways.',
        'next':['Visit Level 2, Wing B','Estimated wait: 15–25 min','Please wear a mask']
    },
    'Cardiology': {
        'icon':'❤️','color':'#dc2626','bg':'#fee2e2','border':'#fca5a5',
        'desc':'Specialises in heart and cardiovascular conditions.',
        'next':['Visit Level 3, Wing A','Estimated wait: 20–30 min','Bring any previous ECG reports']
    },
    'Gastroenterology': {
        'icon':'🫃','color':'#d97706','bg':'#fef3c7','border':'#fcd34d',
        'desc':'Specialises in digestive system and abdominal conditions.',
        'next':['Visit Level 1, Wing C','Estimated wait: 10–20 min','Avoid eating before consultation']
    },
    'Neurology': {
        'icon':'🧠','color':'#7c3aed','bg':'#ede9fe','border':'#c4b5fd',
        'desc':'Specialises in brain, spine, and nervous system conditions.',
        'next':['Visit Level 4, Wing A','Estimated wait: 25–35 min','Bring list of current medications']
    },
    'General Medicine': {
        'icon':'🩺','color':'#059669','bg':'#d1fae5','border':'#6ee7b7',
        'desc':'Handles general health concerns and non-specialist conditions.',
        'next':['Visit Level 1, Wing A','Estimated wait: 10–15 min','Registration desk is open 24/7']
    },
    'Dermatology': {
        'icon':'🔬','color':'#b45309','bg':'#fef9c3','border':'#fde68a',
        'desc':'Specialises in skin, hair, and nail conditions.',
        'next':['Visit Level 2, Wing D','Estimated wait: 15–20 min','Bring photos of affected area if possible']
    },
}
with open('header.html', 'r', encoding='utf-8')as f:
    header_html = f.read()

    st.markdown(header_html, unsafe_allow_html=True)

with st.form("triage_form"):
    #Make the Form
    with open('symptoms.html','r', encoding='utf-8') as f:
        symptoms = f.read()

    st.markdown(symptoms, unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)
    with c1:
        fever = st.checkbox('Fever')
        cough = st.checkbox('Cough')
    with c2:
        headache = st.checkbox('headach')
        shortness_breath = st.checkbox('Shortness of Breath')
    with c3:
        chest_pain = st.checkbox('Cheast Pain')
        stomach_pain = st.checkbox('Stomach Pain')
    with c4:
        nausea_vomiting = st.checkbox('Nausea / Vomitting')
        dizziness = st.checkbox('Dizziness')

    c5, _, _, _ = st.columns(4)

    with c5:
        skin_rash = st.checkbox('Skin Rash')
    
    st.markdown("<br>", unsafe_allow_html = True)

    with open("duration_complaint.html", "r", encoding="utf-8") as f:
        duration_complaint = f.read()
    st.markdown(duration_complaint, unsafe_allow_html = True)

    col_cc, col_dur = st.columns(2)
    with col_cc:
        chief_complaint = st.selectbox("Chief Complaint", options=list(cc_map.keys()))
    with col_dur:
        duration = st.selectbox("Duration", options=list(cc_map.keys()), index=1)
    
    st.markdown("<br>", unsafe_allow_html = True)
    with open("severity.html", "r", encoding="utf-8") as f:
        severity = f.read()
    st.markdown(severity, unsafe_allow_html=True)

    col_temp, col_hc = st.columns(2)
    with col_temp:
        temprature_level = st.selectbox("Tempratur", options=list(temp_map.keys()),index=1)
    with col_hc:
        heart_rate_level = st.selectbox("Heart Rate", options=list(hr_map.keys()),index=1)
    
    st.markdown("<br>", unsafe_allow_html = True)

    with open("history.html", "r", encoding = "utf-8") as f:
        history = f.read()
    st.markdown(history, unsafe_allow_html=True)

    ch1, ch2, ch3, _ = st.columns(4)
    with ch1:
        hypertension = st.checkbox("High Blood Pressure")
    with ch2:
        heart_disease = st.checkbox("Heart Disease")
    with ch3:
        asthma = st.checkbox("Atshma")

    st.markdown("<br>", unsafe_allow_html= True)

    with open("patient.html", "r", encoding="utf-8") as f:
        patient_age = f.read()

    st.markdown(patient_age, unsafe_allow_html=True)

    col_age, col_gen = st.columns(2)
    with col_age:
        age = st.number_input("Age", min_value=1, max_value=120, value=35)
    with col_gen:
        gender = st.selectbox("Gender", options=['Female', 'Male'])

    st.markdown("<br>", unsafe_allow_html = True)
    submitted = st.form_submit_button("Recomend")




if submitted:
    patient = pd.DataFrame([{
        'age' : age,
        'gender' : gender_map.get(gender, 0),
        'fever' : int(fever),
        'cough' : int(cough),
        'headache' : int(headache),
        'chest_pain' : int(chest_pain),
        'stomach_pain' : int(stomach_pain),
        'shortness_breath' : int(shortness_breath),
        'nausea_vomiting' : int(nausea_vomiting),
        'dizziness' : int(dizziness),
        'skin_rash' : int(skin_rash),
        'temperature_level' : temp_map.get(temprature_level,1),
        'heart_rate_level' : hr_map.get(heart_rate_level, 1),
        'duration' : dur_map.get(duration, 1),
        'asthma' : int(asthma),
        'hypertension' : int(hypertension),
        'heart_disease' : int(heart_disease),
        'chief_complaint' : cc_map.get(chief_complaint, 9)
    }])
    patient_scaled = patient.copy()
    patient_scaled[cols_to_scale] = scaler.tranform(patient.tranform(patient[cols_to_scale]))
    pred = model.predict(patient_scaled[features])[0]
    prob = model.predict_proba(patient_scaled[features])[0]
    dept_name = dept_map_inv[pred]
    confidence = prob[pred] * 100
    info = DEPT_INFO[dept_name]
   # Use the ai Model
    st.markdown("---")
    st.markdown("""
    <div style="font-size:22px;font-weight:700;color:#111827;margin-bottom:4px;">AI Recommendation</div>
    <div style="font-size:14px;color:#6b7280;margin-bottom:1.5rem;">Based on the information you provided</div>
    """, unsafe_allow_html=True)

    res_col, prob_col = st.columns([3,2])

# ==========================================
# LEFT COLUMN: THE RESULT CARD
# ==========================================
    with res_col:
        steps_html = ''.join(
            f'<div style="display:flex;alige-item:center;gap:8px;margin-bottom:6px;"'
            f'<span style="color:{info["color"]};font-size:14px;"></span"'
            f'<span style="font-size:14px;color:#374151;">{step}</span></div>'
            for step in info['next']
        )
        # 1. Build the loop string in Python (too complex for pure HTML)
        with open("result.html","r", encoding="utf-8") as f:
            result_template = f.read()

        st.markdown(result_template.format(
            bg=info['bg'],
            border=info['border'],
            icon=info['icon'],
            color=info['color'],
            deft_name=dept_name,
            desc=info['desc'],
            steps_html = steps_html
        ), unsafe_allow_html=True)
        
        # 2. Load the HTML shell

            
        # 3. Inject the variables and display



    # ==========================================
    # RIGHT COLUMN: THE CONFIDENCE BARS
    # ==========================================
    with prob_col:
        # 1. Build the loop string in Python
        sorted_depts = sorted(dept_map_inv.items(), key=lambda x: prob[x[0]], reverse=True)
        bars_html = ""
        for idx, dname in sorted_depts:
            #add The Department
            pct    = prob[idx] * 100
            dinfo  = DEPT_INFO[dname]
            is_top = dname == dept_name
            bars_html += f"""
<div style="margin-bottom:14px;">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:5px;">
        <span style="font-size:13px;font-weight:{'700' if is_top else '400'};color:{'#111827' if is_top else '#6b7280'};">
            {dinfo['icon']} {dname}
        </span>
        <span style="font-size:13px;font-weight:{'700' if is_top else '400'};color:{dinfo['color'] if is_top else '#9ca3af'};">
            {pct:.1f}%
        </span>
        </div>
            <div style="background:#f3f4f6;border-radius:6px;height:8px;overflow:hidden;">
                <div style="background:{'linear-gradient(90deg,'+dinfo['color']+','+dinfo['border']+')' if is_top else '#e5e7eb'};
                                height:100%;border-radius:6px;width:{pct}%;transition:width 0.5s ease;"></div>
            </div>
</div>"""

        # 2. Load the HTML shell
        with open("confidence_card.html","r", encoding="utf-8") as f:
            confidence_template = f.read()


        # 3. Inject the loop and display
        st.markdown(confidence_template.format(
            bars_html = bars_html
        ), unsafe_allow_html=True)
        
   


    



