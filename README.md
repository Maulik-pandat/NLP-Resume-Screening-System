# NLP Resume Screening System

## Overview

The NLP Resume Screening System is a Python-based project that automates the initial resume screening process. Instead of manually reviewing hundreds of resumes, the system analyzes resumes against a predefined job description and ranks candidates based on relevance.

The project uses Natural Language Processing (NLP) techniques such as text preprocessing, TF-IDF vectorization, cosine similarity, and skill matching to identify the most suitable candidates for a given role.

---

## Features

* Extracts text from PDF resumes
* Performs text preprocessing and cleaning
* Uses TF-IDF vectorization for text representation
* Calculates similarity between resumes and job description using cosine similarity
* Matches required skills with resume content
* Generates a final score based on similarity and skill matching
* Ranks candidates from most relevant to least relevant
* Exports results to a CSV file

---

## Technologies Used

* Python
* PDFPlumber
* Pandas
* Scikit-Learn
* TF-IDF Vectorization
* Cosine Similarity
* Natural Language Processing (NLP)

---

## Project Workflow

Resume PDF
↓
Text Extraction
↓
Text Preprocessing
↓
TF-IDF Vectorization
↓
Cosine Similarity Calculation
↓
Skill Matching
↓
Final Score Calculation
↓
Candidate Ranking
↓
CSV Report Generation

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/NLP-Resume-Screening-System.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Usage

1. Place resumes inside the `resume_Screening` folder.
2. Update the job description and required skills in the script if needed.
3. Run:

```bash
python resume_screening.py
```

4. The results will be saved as:

```text
resume_screening_results.csv
```

---

## Output

The generated CSV file contains:

* Resume Name
* TF-IDF Similarity (%)
* Skill Match (%)
* Final Score
* Matched Skills
* Missing Skills

Candidates are ranked according to their Final Score.

---

## Future Improvements

* Streamlit Web Interface
* Dynamic Job Description Input
* Automatic Skill Extraction
* BERT/Sentence Transformer Based Matching
* Support for Multiple Job Roles

---

## Author

Maulik Bhardwaj

