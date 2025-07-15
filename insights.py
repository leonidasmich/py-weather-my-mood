import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from database import get_all_logs

def mood_distribution():
    df = get_all_logs()
    if df.empty:
        return None
    mood_counts = df["mood"].value_counts()
    fig, ax = plt.subplots()
    mood_counts.plot(kind="bar", ax=ax, color="skyblue")
    ax.set_title("Mood Distribution")
    ax.set_ylabel("Count")
    ax.set_xlabel("Mood")
    return fig

def mood_by_weekday():
    df = get_all_logs()
    if df.empty:
        return None
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df["weekday"] = df["timestamp"].dt.day_name()
    weekday_mood = pd.crosstab(df["weekday"], df["mood"])
    fig, ax = plt.subplots(figsize=(10, 6))
    weekday_mood.plot(kind="bar", stacked=True, ax=ax, colormap="Pastel1")
    ax.set_title("Mood by Weekday")
    ax.set_ylabel("Count")
    ax.set_xlabel("Weekday")
    plt.xticks(rotation=45)
    return fig