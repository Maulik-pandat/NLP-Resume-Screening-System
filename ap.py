import os
import pdfplumber
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# =========================
# Resume Read
# =========================
def extract_text(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + " "
    return text

# =========================
# Preprocessing
# =========================
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# =========================
# TF-IDF Similarity
# =========================
def calculate_similarity(resume_text, job_description):
    documents = [resume_text, job_description]
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)
    score = cosine_similarity(vectors[0], vectors[1])
    return score[0][0] * 100

# =========================
# Skill Matching
# =========================
def skill_matching(resume_text, job_skills):
    matched_skills = []
    missing_skills = []
    for skill in job_skills:
        if skill in resume_text:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)
    return matched_skills, missing_skills

# =========================
# Job Description
# =========================
job_description = """
We are looking for a Data Scientist.
Required Skills:
Python
Machine Learning
NLP
SQL
Deep Learning
Pandas
NumPy
TensorFlow
"""

job_skills = [
    "python",
    "machine learning",
    "nlp",
    "sql",
    "deep learning",
    "pandas",
    "numpy",
    "tensorflow"
]

job_description_clean = preprocess_text(job_description)

# =========================
# Folder with all resumes
# =========================
resume_folder = r"resume_Screening"# <-- yaha apna folder path daal

results = []

for filename in os.listdir(resume_folder):
    if filename.lower().endswith(".pdf"):
        pdf_path = os.path.join(resume_folder, filename)
        try:
            raw_text = extract_text(pdf_path)
            resume_text = preprocess_text(raw_text)

            similarity_percentage = calculate_similarity(resume_text, job_description_clean)
            matched_skills, missing_skills = skill_matching(resume_text, job_skills)
            skill_match_percentage = (len(matched_skills) / len(job_skills)) * 100

            results.append({
    "Resume": filename,
    "TF-IDF Similarity (%)": round(similarity_percentage, 2),
    "Skill Match (%)": round(skill_match_percentage, 2),
    "Final Score": round(
        0.7 * similarity_percentage +
        0.3 * skill_match_percentage,
        2
    ),
    "Matched Skills": ", ".join(matched_skills),
    "Missing Skills": ", ".join(missing_skills)
})

            print(f"Done: {filename}")

        except Exception as e:
            print(f"Error in {filename}: {e}")

# ===================
# Save results to CSV
# =========================
df = pd.DataFrame(results)


df = df.sort_values(by="Final Score", ascending=False)
df.to_csv("resume_screening_results.csv", index=False)

print("\n✅ All resumes processed! Result saved in resume_screening_results.csv")

