import streamlit as st

st.set_page_config(page_title="Masilo Makola - CV", layout="centered")

# ---------------- STYLE ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #E3F2FD, #BBDEFB);
    font-family: "Segoe UI", sans-serif;
}

h1, h2, h3 {
    color: #0D47A1;
}

[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #2196F3, #64B5F6);
    color: white;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
    margin-bottom: 20px;
}

.small-text {
    color: #333333;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- PROFILE DATA ----------------
name = "Masilo Makola"
location = "Midrand, Gauteng"
phone = "078 745 6224"
email = "masilo3850@gmail.com"
github = "https://github.com/Masilo1Makola"

profile_summary = """
Motivated final year BCom Statistics and Data Science student at the University of Pretoria
with strong analytical, technical, and problem-solving skills. Hands-on experience in
Python, SAS, R, SQL, Power BI, and basic machine learning workflows. Experienced in data
collection, cleaning, dashboard creation, and trend analysis. Passionate about data-driven
decision-making and eager to grow in process mining, data engineering, and advanced analytics.
"""

education = [
    "BCom Statistics (Triple Major: Statistics, Data Science, Informatics) – University of Pretoria (Expected: Dec 2026)",
    "Extended Programme (Data Science & Statistics) – University of Pretoria (Completed: 2022)",
    "Matric – Ponelopele Oracle Secondary School (Completed: 2020)"
]

experience = {
    "Excelerate Internship – Data Analyst Associate (Sep 2025 – Nov 2025)": [
        "Cleaned, prepared, and validated datasets for reporting",
        "Built interactive dashboards for insight generation",
        "Conducted trend and anomaly identification",
        "Presented insights to cross-functional teams"
    ],
    "KJM Attorneys – Messenger (Jun 2021 – Present)": [
        "Provided admin support using Excel, Word, and PowerPoint",
        "Worked with diverse teams ensuring smooth communication",
        "Delivered and collected legal documents"
    ]
}

technical_skills = {
    "Programming": ["Python", "R", "SAS", "SQL", "C#", "HTML", "CSS", "JavaScript"],
    "Tools": ["Power BI", "RStudio", "SQL Server", "PostgreSQL", "Visual Studio", "SAS Studio"],
    "Concepts": ["Data Structures", "Data Management", "Statistical Modelling", "Data Visualization"]
}

strengths = [
    "Strong analytical and critical-thinking ability",
    "Detail-oriented and highly organized",
    "Effective communicator and team collaborator",
    "Fast learner with strong adaptability",
    "Passionate about solving problems using data"
]

hobbies = [
    "Learning new programming languages",
    "Running and fitness",
    "Gaming and strategy development"
]

projects = {
    "Divorce Data Analysis – South Africa": {
        "description": [
            "Analysed South African divorce data using Python and pandas",
            "Performed data cleaning and handled unspecified values using probabilistic imputation",
            "Created visualisations to identify trends by year, province, and grounds for divorce",
            "Produced a written analytical report summarising key findings"
        ],
        "link": "https://github.com/Masilo1Makola"
    }
}

# ---------------- SIDEBAR ----------------
menu = st.sidebar.radio(
    "Navigation",
    ["Profile", "Education", "Experience", "Projects", "Skills", "Strengths", "Hobbies"]
)

# ---------------- PAGE CONTENT ----------------
if menu == "Profile":
    st.markdown(f"""
    <div class='card'>
        <h1>{name}</h1>
        <p class='small-text'>
        📍 {location}<br>
        📞 {phone}<br>
        📧 {email}
        </p>
        <h3>Profile Summary</h3>
        <p>{profile_summary}</p>
    </div>
    """, unsafe_allow_html=True)

    # GitHub link rendered properly
    st.markdown(f"🐙 **GitHub:** [{github}]({github})")

elif menu == "Education":
    st.markdown("<div class='card'><h2>Education</h2></div>", unsafe_allow_html=True)
    for edu in education:
        st.markdown(f"<div class='card'>• {edu}</div>", unsafe_allow_html=True)

elif menu == "Experience":
    st.markdown("<div class='card'><h2>Experience</h2></div>", unsafe_allow_html=True)
    for role, duties in experience.items():
        st.markdown(f"<div class='card'><h3>{role}</h3>", unsafe_allow_html=True)
        for duty in duties:
            st.markdown(f"- {duty}")
        st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Projects":
    st.markdown("<div class='card'><h2>Projects</h2></div>", unsafe_allow_html=True)
    for project, details in projects.items():
        st.markdown(f"<div class='card'><h3>{project}</h3>", unsafe_allow_html=True)
        for point in details["description"]:
            st.markdown(f"- {point}")
        st.markdown(f"🔗 **GitHub:** [{details['link']}]({details['link']})")
        st.markdown("</div>", unsafe_allow_html=True)

elif menu == "Skills":
    st.markdown("<div class='card'><h2>Technical Skills</h2></div>", unsafe_allow_html=True)
    for category, skills in technical_skills.items():
        st.markdown(f"<div class='card'><h3>{category}</h3>{', '.join(skills)}</div>", unsafe_allow_html=True)

elif menu == "Strengths":
    st.markdown("<div class='card'><h2>Strengths</h2></div>", unsafe_allow_html=True)
    for s in strengths:
        st.markdown(f"<div class='card'>✔ {s}</div>", unsafe_allow_html=True)

elif menu == "Hobbies":
    st.markdown("<div class='card'><h2>Hobbies</h2></div>", unsafe_allow_html=True)
    for h in hobbies:
        st.markdown(f"<div class='card'>🎯 {h}</div>", unsafe_allow_html=True)
