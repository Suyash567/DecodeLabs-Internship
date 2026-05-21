# DecodeLabs Recommending Chatbot Engine

A lightweight, terminal-based career recommendation engine that uses mathematical vector modeling to align user-provided technical skills with target industry job roles.

## Core Features & Pipeline

* **Synonym Mapping & Standardization:** Features an ingestion layer that translates common tech acronyms and aliases (e.g., "ml", "frontend", "cloud") into uniform system keywords before vector processing.
* **TF-IDF Vectorization:** Computes customized Term Frequency-Inverse Document Frequency (TF-IDF) vectors dynamically across the document dataset to weight the uniqueness of individual skill sets.
* **Cosine Similarity Matching:** Employs an algebraic scoring pipeline to measure the angular alignment between user skill vectors and predefined career profiles.
* **Cold Start Safeguards:** Implements a fallback protocol that recommends high-density trending tech roles if input parsing returns an empty or unrecognized skill profile.
* **Interactive Input Loop:** Prompts users sequentially for 3 distinctive profile skills, rendering matched paths accompanied by calculated percentage-based "Match Quality" metrics.

## Mathematical Architecture

The pipeline processes recommendations using three foundational algorithmic formulas:

* **Inverse Document Frequency (IDF):** Measures term rarity across job roles:
    $$IDF(t) = \ln\left(\frac{\text{Total Roles}}{\text{Roles containing } t}\right)$$
* **Term Frequency-Weighting (TF-IDF):** Determines feature density per profile:
    $$TF\text{-}IDF(t, d) = TF(t, d) \times IDF(t)$$
* **Cosine Similarity Score:** Calculates proximity between user and career vectors:
    $$\text{Similarity}(\vec{A}, \vec{B}) = \frac{\vec{A} \cdot \vec{B}}{\|\vec{A}\| \|\vec{B}\|} = \frac{\sum A_i B_i}{\sqrt{\sum A_i^2} \sqrt{\sum B_i^2}}$$

## Predefined Target Profiles
The engine evaluates affinity scores across five industry standard baselines:
* **Data Scientist:** Python, SQL, Machine Learning, Data Analysis, Statistics, R.
* **DevOps Engineer:** AWS, Docker, Kubernetes, CI/CD, Linux, Automation, Git.
* **Backend Developer:** Java, Python, SQL, APIs, Git, Data Structures, Django.
* **Frontend Developer:** JavaScript, React, HTML, CSS, Git, Web Design, TypeScript.
* **Cloud Architect:** AWS, Cloud Computing, Azure, Automation, Linux, Security.

## Getting Started

### System Requirements
* Python 3.x (Utilizes native standard library components `math`, `sys`, and `collections`).

### Running the Engine
Execute the program from your terminal to begin the interactive matchmaking loop:
```bash
python Recommendation.py
