import matplotlib.pyplot as plt
import seaborn as sns
import os
import uuid
import logging

logger = logging.getLogger(__name__)

def generate_visualization(df, question):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    plot_dir = os.path.join(base_dir, "static", "plots")
    os.makedirs(plot_dir, exist_ok=True)

    visual_keywords = [
        "plot", "chart", "graph",
        "visualize", "distribution",
        "histogram", "bar"
    ]

    if not any(word in question.lower() for word in visual_keywords):
        return None

    try:
        plt.clf()

        if "surviv" in question.lower():
            sns.barplot(x='Pclass', y='Survived', data=df)
            plt.title("Survival Rate by Class")

        elif "age" in question.lower():
            df['Age'].hist(bins=20)
            plt.title("Age Distribution")

        else:
            sns.countplot(x='Survived', data=df)
            plt.title("Survival Count")

        filename = f"plot_{uuid.uuid4().hex[:8]}.png"
        save_path = os.path.join(plot_dir, filename)

        plt.savefig(save_path)
        plt.close()

        return f"/static/plots/{filename}"

    except Exception as e:
        logger.error(f"Visualization failed: {e}")
        return None