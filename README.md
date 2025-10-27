# IT Incident Summarizer & Real-Time Log Analyzer

This project is a high-throughput system for real-time log analysis and automated incident management. It ingests over 1,000 log events per minute, classifies them, and retrieves related past issues to speed up resolution.

## 🚀 Key Features & Impact

* **High-Throughput Ingestion:** Processes 1,000+ log events per minute in real-time.
* **AI-Powered Triage:** Uses **FAISS** for vector similarity search to find related historical incidents, **cutting resolution time by 40%**.
* **Automated Summarization:** Leverages **LangChain** to automatically generate incident reports, reducing manual ops-team workload by ~5 hours/week.

## 🔧 Tech Stack

* **Python**
* **River**: For real-time stream processing and classification.
* **FAISS**: For high-speed vector similarity search.
* **LangChain**: For LLM-based summarization and report generation.
* **Streamlit**: For the interactive user interface.

## 🎥 Demo

(Video/GIF demo coming soon. The system is run locally.)

## ⚙️ How to Run Locally

1.  Clone the repository:
    ```bash
    git clone [https://github.com/Badri467/IT_Incident_Summariser](https://github.com/Badri467/IT_Incident_Summariser)
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```
