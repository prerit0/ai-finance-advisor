from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class FinancialAdvisor:

    def __init__(self):
        model_name = "google/flan-t5-small"

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def generate_advice(self, metrics):

        income = metrics["total_income"]
        expenses = metrics["total_expenses"]
        savings = metrics["savings"]
        savings_rate = metrics["savings_rate"]

        category_spending = metrics["category_spending"]

        # -----------------------------
        # Rule-based financial insights
        # -----------------------------

        insights = []

        if savings_rate < 20:
            insights.append("Your savings rate is below the recommended 20%.")
        elif savings_rate < 40:
            insights.append("Your savings rate is moderate.")
        else:
            insights.append("Your savings rate is healthy.")

        # Top spending category
        top_category = category_spending.index[0]
        top_amount = category_spending.iloc[0]

        insights.append(
            f"Your highest spending category is {top_category} ({top_amount})."
        )

        insight_text = "\n".join(insights)

        # -----------------------------
        # Generate financial suggestions
        # -----------------------------

        recommendations = []

        if savings_rate < 20:
            recommendations.append(
                "Increase your savings rate to at least 20% of your income."
            )

        if top_category.lower() == "rent":
            recommendations.append(
                "Review your housing expenses to ensure rent remains affordable."
            )

        recommendations.append(
            "Track discretionary spending like shopping and groceries to maintain financial stability."
        )

        recommendations.append(
            "Create a monthly budget to better manage your income and expenses."
        )

        recommendation_text = "\n".join(recommendations)

        # -----------------------------
        # Prompt for LLM explanation
        # -----------------------------

        prompt = f"""
        Explain the following financial recommendations clearly and briefly.

        Financial Insights:
        {insight_text}

        Recommendations:
        {recommendation_text}

        Advice:
        """

        # Tokenize prompt
        inputs = self.tokenizer(prompt, return_tensors="pt")

        outputs = self.model.generate(
            **inputs,
            max_new_tokens=80,
            num_beams=4,
            no_repeat_ngram_size=3,
            early_stopping=True
        )

        advice = self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()

        # fallback if model gives very short output
        if len(advice) < 40:
            advice = f"""
        1. Maintain your strong savings rate of {savings_rate:.2f}% by continuing disciplined spending.
        2. Monitor your largest expense category ({top_category}) to ensure it stays within budget.
        3. Track discretionary expenses like shopping and groceries each month.
        """

        return advice

# python -m streamlit run app/streamlit_app.py