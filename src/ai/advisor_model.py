from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class FinancialAdvisor:

    def __init__(self):

        model = "google/flan-t5-small"

        self.tokenizer = AutoTokenizer.from_pretrained(model)

        self.model = AutoModelForSeq2SeqLM.from_pretrained(model)

    def generate_advice(self, metrics):

        income = metrics["total_income"]
        expenses = metrics["total_expenses"]
        savings = metrics["savings"]
        savings_rate = metrics["savings_rate"]

        category_spending = metrics["category_spending"].head(3)

        category_text = "\n".join(
            [f"{cat}: {amt}" for cat, amt in category_spending.items()]
        )

        prompt = f"""
        A user has the following financial data:

        Income: {income}
        Expenses: {expenses}
        Savings: {savings}
        Savings Rate: {savings_rate:.2f}%

        Top Spending Categories:
        {category_text}

        Give personalized financial advice to improve their financial health.
        """

        inputs = self.tokenizer(prompt, return_tensors="pt")

        outputs = self.model.generate(
            **inputs,
            max_length=150
        )

        advice = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        return advice