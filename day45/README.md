# **Day 45 - ContractGuard Pro (Hybrid Edge-Cloud AI)**

**Phase 3 -** Agent Framework Foundations

## **📝 The Challenge**

**Goal -** Build a production-grade, multimodal Streamlit application that solves a critical business problem (Contract Analysis) while addressing the primary hurdle of Enterprise AI - **Data Privacy**.

Here, built an advanced AI app that processes PDFs, DOCX files and images to identify unfair legal clauses. To solve the privacy issue, engineered a **Hybrid Edge-Cloud Architecture**.

## **🛠️ Tech Stack**

* **Frontend -** Streamlit.  
* **Cloud AI (Reasoning) -** LangChain + gemini for deep legal analysis and natural language generation.  
* **Edge AI (Privacy Shield) -** LangChain + Ollama. Uses the ultra-lightweight gemma3:270m model to scrub PII (Personally Identifiable Information) locally on the user's machine *before* data ever hits the cloud.  
* **Local Vision -** Uses moondream via Ollama for local OCR on contract images.  
* **Utilities -** pypdf, python-docx, FPDF (for generating downloadable PDF reports).

## **📂 Solution Overview**

1. **The Privacy Shield -** When enabled, the app intercepts uploaded documents. It uses a small, local open-source model running via Ollama to scrub names and addresses. If the scrub is successful (passing safety guardrails), only the *anonymized* clauses are sent to the Gemini API.  
2. **Contextual Role Prompting -** The SystemMessage dynamically updates based on the user's selected Role and Jurisdiction (e.g., A freelancer in the UK vs a Business Owner in the US).  
3. **Audit-to-Draft Workflow -** The app performs a two-step reasoning process. First, it identifies risks. Second, the user selects a Strategy (Collaborative vs. Firm), and a second LLM call automatically drafts a negotiation email based on the audit results.  
4. **PDF Generation -** Implemented a custom FPDF parser to convert the AI's markdown response into a clean, downloadable PDF report.

## **🏃‍♂️ How to Run**

1. Install dependencies:  
   pip install -r requirements.txt

2. **(Optional but recommended) Start Ollama for the Privacy Shield:**  
   * Download Ollama from [ollama.com](https://ollama.com)  
   * Run ollama pull gemma3:270m and ollama pull moondream in your terminal.  
3. Run the app:  
   streamlit run day45_contract_guard.py

## **🧠 Key Learnings & Reflections**

* **Hybrid Architecture is the Future -** Cloud models (like Gemini) are brilliant at complex reasoning, but companies hesitate to upload raw contracts to them. Edge models (like Gemma 270m) are terrible at complex reasoning, but great at simple text replacement. Combining them yields a secure, highly capable system.  
* **Guardrailing Small Models -** The local scrubber sometimes hallucinated and deleted entire clauses. Had to implement a programmatic guardrail - if len(scrubbed) \< (0.7 \* len(text)), reject the scrub and fallback. We can not blindly trust small local models.  
* **Markdown to PDF -** Converting LLM-generated markdown into a structured PDF using FPDF requires a surprisingly complex parsing loop to handle dynamic table widths and cell heights.

---
[Back to Main Repo](../README.md)
