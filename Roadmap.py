from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.set_font("Arial", size=12)

pdf.cell(200, 10, txt="Roadmap: Transition from Deloitte to AI/ML Role at Google", ln=True, align='C')
pdf.ln(10)

content = """
🎯 GOAL: Move from Icertis CLM Integration role at Deloitte to AI/ML role at Google

-----------------------------------------------------------
🧭 STEP 1: Identify Target Roles at Google
-----------------------------------------------------------
- Machine Learning Engineer
- Data Scientist
- AI/ML Software Engineer
- Cloud AI Specialist / AI Consultant (Google Cloud)
👉 Based on your Deloitte + CLM integration background, roles like Cloud AI Engineer / AI Consultant or ML Engineer (Cloud AI) could be perfect entry points.

-----------------------------------------------------------
📚 STEP 2: Build Core Technical Skills
-----------------------------------------------------------
- Programming: Python (NumPy, Pandas, Scikit-learn, Matplotlib)
- Math: Linear Algebra, Probability, Statistics, Calculus
- DSA: Practice on LeetCode/HackerRank
- ML: Regression, Classification, Clustering, Model Evaluation
- Frameworks: TensorFlow, PyTorch
- Courses:
  1. Andrew Ng’s Machine Learning (Coursera)
  2. Deep Learning Specialization (Coursera)
  3. Google ML Crash Course (Free)
  4. Fast.ai Practical Deep Learning

-----------------------------------------------------------
☁️ STEP 3: Leverage Consulting Experience
-----------------------------------------------------------
- Learn Google Cloud (Vertex AI, BigQuery ML, AutoML)
- Understand data engineering: ETL, Airflow, BigQuery
- Certifications:
  * Google Cloud ML Engineer
  * TensorFlow Developer
  * Google Cloud Data Engineer

-----------------------------------------------------------
🧩 STEP 4: Build Real Projects
-----------------------------------------------------------
- Predictive analytics, NLP chatbot, Image classification
- AI CLM document analyzer (tie to Deloitte domain)
- Host projects on GitHub and write blog posts

-----------------------------------------------------------
🧑‍💼 STEP 5: Network & Personal Branding
-----------------------------------------------------------
- Optimize LinkedIn + GitHub
- Engage with Googlers and AI communities
- Attend GDG, TensorFlow meetups, hackathons

-----------------------------------------------------------
🧪 STEP 6: Prepare for Google Interviews
-----------------------------------------------------------
- DSA: LeetCode Medium-level
- System Design & ML Design
- ML Fundamentals (algorithms, evaluation, overfitting)
- Behavioral: Googleyness, collaboration, innovation

-----------------------------------------------------------
🕒 STEP 7: 12–18 Month Plan
-----------------------------------------------------------
0–3 months: Python, Math, DSA refresh
3–6 months: ML Fundamentals + Projects
6–9 months: Deep Learning + GCP ML Engineer prep
9–12 months: Real-world projects + Networking
12–18 months: Mock interviews + Referrals + Apply

-----------------------------------------------------------
⚡ BONUS TIP
-----------------------------------------------------------
First target AI/ML Consultant role in Deloitte or GCP partner teams as a bridge to Google AI.
"""

pdf.multi_cell(0, 10, txt=content)
pdf.output("AI_ML_Roadmap_to_Google.pdf")

print("✅ PDF created: AI_ML_Roadmap_to_Google.pdf")
