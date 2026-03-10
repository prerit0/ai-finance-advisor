# 💰 AI Personal Finance Advisor
<img width="1536" height="842" alt="bg" src="https://github.com/user-attachments/assets/41a23f47-5197-4b35-a3fc-0b0ed22db427" />


### Generative AI + PyTorch + Streamlit

An **end-to-end Generative AI application** that analyzes personal financial data and generates **AI-powered financial recommendations**.

Upload your expense dataset and the system will automatically:

* Analyze spending patterns
* Calculate financial metrics
* Visualize spending trends
* Generate **personalized financial advice using a transformer model**

---

## 🌐 Live Demo

**Try the app here**

```
https://prerit0-ai-finance-advisor-appstreamlit-app-54enr5.streamlit.app/
```

Upload a CSV dataset and instantly receive **AI-generated financial insights**.

---

# 🧠 Project Overview

Managing personal finances can be challenging when spending patterns are unclear.

This project builds an **AI-powered financial advisor** that combines:

* Data analytics
* Financial metrics
* Machine learning
* Generative AI

The system transforms **raw financial data into meaningful financial advice**.

---

# ⚙️ How It Works

The system follows a **data-to-insight pipeline**:

```
User Uploads Expense Dataset
            │
            ▼
Data Ingestion (Pandas)
            │
            ▼
Data Preprocessing
            │
            ▼
Financial Metrics Engine
            │
            ▼
Spending Analysis + Insights
            │
            ▼
Transformer Model (PyTorch)
            │
            ▼
AI Financial Recommendations
            │
            ▼
Interactive Streamlit Dashboard
```

---

# 📊 Features

### 📂 Dataset Upload

Upload a CSV containing personal expense data.

Example structure:

| Date       | Category | Amount | Type    |
| ---------- | -------- | ------ | ------- |
| 2025-01-01 | Salary   | 50000  | Income  |
| 2025-01-02 | Food     | 450    | Expense |

---

### 📈 Financial Analytics

The system automatically calculates:

* Total income
* Total expenses
* Savings
* Savings rate
* Top spending categories
* Monthly spending patterns

---

### 📊 Interactive Visualizations

Dynamic charts show:

* Spending by category
* Monthly spending trends
* Income vs expenses

---

### 🤖 AI Financial Advisor

Using a **transformer-based model**, the system generates:

* Personalized financial advice
* Budget improvement suggestions
* Spending optimization tips

Example output:

```
1. Maintain your strong savings rate by continuing disciplined spending.
2. Review housing costs since rent is the largest expense category.
3. Track discretionary spending such as shopping to improve long-term savings.
```

---

# 🧰 Tech Stack

### Data Processing

* Python
* Pandas
* NumPy

### Visualization

* Matplotlib
* Plotly

### AI / Machine Learning

* PyTorch
* Hugging Face Transformers

### Application Layer

* Streamlit

---

# 📁 Project Structure

```
ai-finance-advisor
│
├── app
│   └── streamlit_app.py
│
├── src
│   ├── ai
│   │   └── advisor_model.py
│   │
│   ├── analysis
│   │   └── financial_metrics.py
│   │
│   ├── data
│   │   ├── loader.py
│   │   └── preprocessing.py
│   │
│   └── visualization
│       └── charts.py
│
├── data
│   └── sample_expenses.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 📌 Example Use Cases

This system can be extended for:

* Personal budgeting tools
* AI financial coaching apps
* Expense tracking platforms
* Fintech analytics dashboards

---

# 📚 Key Learnings

This project demonstrates:

* End-to-end **AI application development**
* Integrating **data analytics with Generative AI**
* Using **transformer models with PyTorch**
* Building interactive **AI dashboards**

---

# 🧑‍💻 Author

**Prerit**

Aspiring Data Scientist | AI Enthusiast

---

# ⭐ If You Like This Project

Give the repository a **star ⭐** and feel free to contribute!

---

## 🧠 Future Improvements

Planned features:

* AI spending anomaly detection
* Budget forecasting
* Financial goal tracking
* Multi-user support

