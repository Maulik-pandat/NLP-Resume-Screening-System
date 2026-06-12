# NLP Resume Screening System

## Overview

The NLP Resume Screening System is a Python-based project designed to automate the initial resume screening process. Organizations often receive a large number of resumes for a single job opening, making manual screening time-consuming and inefficient.

This project helps identify the most relevant candidates by comparing resumes with a predefined job description using Natural Language Processing (NLP) techniques. It calculates similarity scores, performs skill matching, and ranks candidates based on their overall suitability for the role.

---

## Features

* Extracts text from PDF resumes
* Cleans and preprocesses resume text
* Uses TF-IDF Vectorization for text representation
* Calculates resume-job description similarity using Cosine Similarity
* Performs skill matching based on required job skills
* Generates a Final Score using similarity and skill match percentages
* Ranks candidates from highest to lowest score
* Exports results into a CSV file for easy review

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

1. Read PDF resumes
2. Extract resume text
3. Preprocess text data
4. Compare resumes with the job description using TF-IDF
5. Calculate cosine similarity score
6. Match required skills
7. Generate final candidate score
8. Rank candidates
9. Export results to CSV

---

## Dataset

This project was tested using a resume dataset containing resumes from multiple professional domains.

The original dataset contained a large number of resume files. To keep this repository lightweight and easy to download, the complete dataset has not been uploaded.

Users can place their own PDF resumes inside the `resume_Screening` folder and run the project without any modifications.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/NLP-Resume-Screening-System.git
```

Move into the project directory:

```bash
cd NLP-Resume-Screening-System
```

Install required dependencies:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```text
NLP-Resume-Screening-System/
│
├── resume_Screening/
│   └── sample resumes
│
├── resume_screening.py
├── requirements.txt
├── README.md
└── resume_screening_results.csv
```

---

## Usage

1. Place PDF resumes inside the `resume_Screening` folder.
2. Update the Job Description and Skills in the script if required.
3. Run the project:

```bash
python resume_screening.py
```

4. After execution, a CSV file will be generated containing candidate rankings and scores.

---

## Output

The generated CSV report contains:

* Resume Name
* TF-IDF Similarity (%)
* Skill Match (%)
* Final Score
* Matched Skills
* Missing Skills

Candidates are ranked according to their Final Score.

---

## Example Use Case

Suppose a company is hiring for a Data Scientist role.

Instead of manually reviewing hundreds of resumes, the HR team can run this system to:

* Compare resumes with the job description
* Identify matching skills
* Rank candidates automatically
* Shortlist the most relevant applicants

This significantly reduces manual screening effort and speeds up the recruitment process.

---

## Future Improvements

* Streamlit Web Application
* Dynamic Job Description Input
* Automatic Skill Extraction
* Resume Classification
* BERT/Sentence Transformer Based Matching
* Multi-Role Resume Screening

---

## Author

**Maulik Bhardwaj**


