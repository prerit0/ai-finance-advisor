import matplotlib.pyplot as plt


def plot_category_spending(category_spending):
    """
    Bar chart of spending by category
    """

    fig, ax = plt.subplots()

    category_spending.plot(kind = "bar", ax = ax, color = "red")

    ax.set_title("Spending by Category")
    ax.set_xlabel("Category")
    ax.set_ylabel("Amount")

    return fig


def plot_monthly_spending(monthly_spending):
    """
    Line chart of monthly expenses
    """

    fig, ax = plt.subplots()

    monthly_spending.plot(kind = "line", marker = "o", ax = ax, color = "red")

    ax.set_title("Monthly Spending")
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount")

    return fig


def plot_income_vs_expenses(income, expenses):
    """
    Comparison chart for income vs expenses
    """

    fig, ax = plt.subplots()

    labels = ["Income", "Expenses"]
    values = [income, expenses]

    ax.bar(labels, values, color = ["red", "black"])

    ax.set_title("Income vs Expenses")
    ax.set_ylabel("Amount")

    return fig