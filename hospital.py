import streamlit as st
import pandas as pd
import numpy as np
import pickle
import os

#Title


# Load Model and Style



bundle        =
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


with st.form("triage_form"):
    #Make the Form
    pass

if submitted:
    patient = pd.DataFrame([{
        'age' : age,
        'gender' : gender_map.get(gender, 0),
        'fever' : int(fever),
        'cough' : int(cough),
        'headache' : int(headache),
        'chest_pain' : int(chest_pain),
        'stomach_pain' : int(stomach_pain),
        'shortness_breath' : int(shortness_beath),
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
        pass
        # 1. Build the loop string in Python (too complex for pure HTML)

        
        # 2. Load the HTML shell

            
        # 3. Inject the variables and display



    # ==========================================
    # RIGHT COLUMN: THE CONFIDENCE BARS
    # ==========================================
    with prob_col:
        # 1. Build the loop string in Python
        sorted_depts = sorted(dept_map_inv.items(), key=lambda x: proba[x[0]], reverse=True)
        bars_html = ""
        for idx, dname in sorted_depts:
            #add The Department
            pct    = proba[idx] * 100
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


        # 3. Inject the loop and display
        
   


    



