import streamlit as st

st.set_page_config(
    page_title="Final Project - Team Profile",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>
    .hero-box {
        background: linear-gradient(135deg, #0f172a, #1e3a8a);
        color: white;
        padding: 36px 28px;
        border-radius: 20px;
        text-align: center;
        margin-bottom: 28px;
    }
    .team-card {
        background: linear-gradient(145deg, #ffffff, #f8fafc);
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 22px 18px;
        text-align: center;
        box-shadow: 0 8px 20px rgba(15, 23, 42, 0.06);
        margin-top: 12px;
        color: #1e293b;
    }
    .member-name {
        font-size: 20px;
        font-weight: 800;
        color: #0f172a;
        margin-bottom: 4px;
        letter-spacing: 0.5px;
    }
    .member-nim {
        font-size: 14px;
        font-weight: 600;
        color: #64748b;
        margin-bottom: 12px;
    }
    .role-badge {
        display: inline-block;
        background: linear-gradient(90deg, #f97316, #ea580c);
        color: white;
        font-size: 13px;
        font-weight: 700;
        padding: 8px 14px;
        border-radius: 12px;
        margin-bottom: 14px;
        line-height: 1.4;
    }
    .contrib-box {
        text-align: left;
        background-color: #f1f5f9;
        padding: 12px 14px;
        border-radius: 12px;
        font-size: 13.5px;
        color: #334155;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar Navigasi
st.sidebar.title("📌 Project Menu")
page = st.sidebar.radio(
    "Select Page:",
    ["👥 Team Member Profiles", "🚀 Project Overview"]
)

# ==========================================
# HALAMAN 1: TEAM MEMBER PROFILES (3 ORANG)
# ==========================================
if page == "👥 Team Member Profiles":
    st.markdown("<h1 style='text-align: center; font-size: 42px; font-weight: 900;'>TEAM MEMBER PROFILES</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: #64748b; margin-bottom: 30px;'>Meet the talented team behind our Final Project</p>", unsafe_allow_html=True)

    team = [
        {
            "name": "DEVINA LIE",
            "nim": "NIM: 021202600003",
            "photo": "062d099d20239525c0fb4ee5e7057d31.jpg",
            "role": "🚀 DevOps & Project Manager / Team Leader",
            "contributions": [
                "Led the team and managed project timeline",
                "Configured GitHub repository & cloud deployment",
                "Designed system workflow and architecture"
            ]
        },
        {
            "name": "TESSA AFIKA",
            "nim": "NIM: 02120260002",
            "photo": "acf2221931c5dc2777ce342f389c2f63.jpg",
            "role": "🧪 Quality Assurance (QA) & Finalizer",
            "contributions": [
                "Conducted testing and bug verification",
                "Refined user interface and visual layout",
                "Compiled final project report and presentation"
            ]
        },
        {
            "name": "IDA AYU ANASTASYA",
            "nim": "NIM: 0212026009",
            "photo": "f0e7829760aa858b548af01e9d6d4361.jpg",
            "role": "💻 Back-End & Full-Stack Developer",
            "contributions": [
                "Developed core application logic in Python",
                "Built interactive components using Streamlit",
                "Integrated data processing and validation"
            ]
        }
    ]

    cols = st.columns(3, gap="large")
    for idx, member in enumerate(team):
        with cols[idx]:
            st.image(member["photo"], use_container_width=True)
            contrib_html = "".join([f"<li>{item}</li>" for item in member["contributions"]])
            st.markdown(f"""
            <div class="team-card">
                <div class="member-name">{member['name']}</div>
                <div class="member-nim">{member['nim']}</div>
                <div class="role-badge">{member['role']}</div>
                <div class="contrib-box">
                    <strong>Contributions:</strong>
                    <ul style="margin-top: 6px; padding-left: 18px; margin-bottom: 0;">
                        {contrib_html}
                    </ul>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ==========================================
# HALAMAN 2: PROJECT OVERVIEW (ISI MATERI)
# ==========================================
else:
    st.markdown("""
    <div class="hero-box">
        <h1 style="margin-bottom: 10px;">🎓 FINAL PROJECT APPLICATION</h1>
        <p style="font-size: 18px; opacity: 0.9;">Write your project title or short description here</p>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("📌 About This Project")
    st.write("Halaman ini siap diisi dengan fitur utama, kalkulator/analisis, atau materi Final Project kelompok kalian.")
    
