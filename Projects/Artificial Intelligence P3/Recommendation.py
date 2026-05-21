import math
import sys
from collections import Counter

# ==========================================
# SIMULATED DATASET (Emulating raw_skills.csv)
# ==========================================
JOB_ROLES_DATASET = {
    "Data Scientist": ["python", "sql", "machine learning", "data analysis", "statistics", "r"],
    "DevOps Engineer": ["aws", "docker", "kubernetes", "ci/cd", "linux", "automation", "git"],
    "Backend Developer": ["java", "python", "sql", "apis", "git", "data structures", "django"],
    "Frontend Developer": ["javascript", "react", "html", "css", "git", "web design", "typescript"],
    "Cloud Architect": ["aws", "cloud computing", "azure", "automation", "linux", "security"]
}

TRENDING_FALLBACKS = ["Data Scientist", "Backend Developer", "DevOps Engineer"]

# ==========================================
# DATA FILTERING & SYNONYM DICTIONARY
# ==========================================
VOCABULARY_MAPPING = {
    "frontend": "web design",
    "ui design": "web design",
    "ml": "machine learning",
    "deep learning": "machine learning",
    "databases": "sql",
    "cloud": "cloud computing",
    "web development": "html",
    "version control": "git",
    "pipelines": "ci/cd"
}

# ==========================================
# CORE MATHEMATICAL HELPER FUNCTIONS
# ==========================================
def calculate_idf(dataset):
    total_docs = len(dataset)
    unique_skills = set(skill for skills in dataset.values() for skill in skills)
    
    idf_scores = {}
    for skill in unique_skills:
        containing_docs = sum(1 for skills in dataset.values() if skill in skills)
        idf_scores[skill] = math.log(total_docs / containing_docs) if containing_docs > 0 else 0.0
    return idf_scores

def compute_tfidf_vector(skills_list, idf_scores):
    total_terms = len(skills_list)
    if total_terms == 0:
        return {}
    
    term_counts = Counter(skills_list)
    tf_scores = {term: count / total_terms for term, count in term_counts.items()}
    
    tfidf_vector = {}
    for term, tf in tf_scores.items():
        if term in idf_scores:
            tfidf_vector[term] = tf * idf_scores[term]
            
    return tfidf_vector

def calculate_cosine_similarity(vector_a, vector_b):
    dot_product = 0.0
    for term in vector_a:
        if term in vector_b:
            dot_product += vector_a[term] * vector_b[term]
            
    magnitude_a = math.sqrt(sum(val ** 2 for val in vector_a.values()))
    magnitude_b = math.sqrt(sum(val ** 2 for val in vector_b.values()))
    
    if magnitude_a == 0.0 or magnitude_b == 0.0:
        return 0.0
        
    return dot_product / (magnitude_a * magnitude_b)

# ==========================================
# THE 4-STEP RECOMMENDATION PIPELINE
# ==========================================
def get_career_recommendations(user_skills, dataset, top_n=3):
    idf_scores = calculate_idf(dataset)
    
    # ----------------------------------------------------
    # STEP 1: INGESTION & COLD START CHECK (With Translation)
    # ----------------------------------------------------
    processed_user_skills = []
    for skill in user_skills:
        clean_skill = skill.lower().strip()
        
        if clean_skill:
            if clean_skill in VOCABULARY_MAPPING:
                standardized_skill = VOCABULARY_MAPPING[clean_skill]
                print(f"-> Bot Logic: Translating '{clean_skill}' to system keyword '{standardized_skill}'")
                processed_user_skills.append(standardized_skill)
            else:
                processed_user_skills.append(clean_skill)
                
    if not processed_user_skills:
        print("\n[Cold Start] No valid features parsed. Activating Trending Fallbacks...") # [cite: 266]
        return [(role, 1.0) for role in TRENDING_FALLBACKS[:top_n]]
        
    user_vector = compute_tfidf_vector(processed_user_skills, idf_scores)
    
    # ----------------------------------------------------
    # STEP 2: SCORING
    # ----------------------------------------------------
    role_scores = {}
    for role_name, role_skills in dataset.items():
        role_vector = compute_tfidf_vector(role_skills, idf_scores)
        score = calculate_cosine_similarity(user_vector, role_vector)
        role_scores[role_name] = score
        
    # ----------------------------------------------------
    # STEP 3: SORTING
    # ----------------------------------------------------
    sorted_recommendations = sorted(role_scores.items(), key=lambda x: x[1], reverse=True)
    
    # ----------------------------------------------------
    # STEP 4: FILTERING
    # ----------------------------------------------------
    return sorted_recommendations[:top_n]

# ==========================================
# INTERACTIVE CHATBOT RECO ENGINE INTERFACE
# ==========================================
def matchmaker_chatbot():
    print("--- DecodeLabs Matchmaker Chatbot Engine ---")
    print("Type your technical skills when prompted. Type 'exit' to stop the loop.")
    print("-" * 55)

    while True:
        try:
            print("\nBot: Let's calculate your optimal stack. You must provide 3 skills to initialize profile density.") # [cite: 204]
            
            user_inputs = []
            for i in range(1, 4):
                raw_input = input(f"Enter Skill {i}: ")
                
                if raw_input.lower().strip() in ['exit', 'quit', 'bye']:
                    print("Bot: Goodbye! Closing the digital loop.")
                    return
                    
                user_inputs.append(raw_input)
            
            recommendations = get_career_recommendations(user_inputs, JOB_ROLES_DATASET, top_n=3)
            
            print("\nBot: Based on angular alignment vectors, here are your top paths:") # [cite: 306]
            for rank, (role, score) in enumerate(recommendations, 1):
                print(f"  {rank}. {role} (Match Quality: {score * 100:.1f}%)")
            
            # ----------------------------------------------------
            # LOOP BREAK CONTROL (Fixes the immediate loop reset)
            # ----------------------------------------------------
            print("\n" + "-" * 40)
            next_action = input("Bot: Would you like to evaluate another tech stack? (yes/no): ").lower().strip()
            if next_action not in ['yes', 'y']:
                print("Bot: Goodbye! Closing the digital loop.")
                break
                
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Disconnecting heartbeat loop gracefully.")
            break

if __name__ == "__main__":
    matchmaker_chatbot()