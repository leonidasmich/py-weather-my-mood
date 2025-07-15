import streamlit as st
from datetime import datetime
from database import init_db, insert_log, get_all_logs
from mood_analysis import extract_mood
from weather import get_current_weather
import insights

# Αρχικοποίηση βάσης δεδομένων
init_db()

st.set_page_config(page_title="🌤️ Η Διάθεσή μου & ο Καιρός", layout="centered")
st.title("🌤️ Η Διάθεσή μου & ο Καιρός")

st.markdown("""
Πώς νιώθεις σήμερα; Πληκτρολόγησε λίγα λόγια και θα αναλύσουμε τη διάθεσή σου σε συνδυασμό με τον τρέχοντα καιρό.
""")

user_input = st.text_area("📝 Πώς νιώθεις σήμερα;", height=150)

if st.button("Καταγραφή Διάθεσης"):
    if user_input.strip():
        mood = extract_mood(user_input)
        weather_data = get_current_weather()
        desc = f"{weather_data['temperature']}°C, άνεμος {weather_data['windspeed']} m/s, καιρικός κωδικός {weather_data['weathercode']}"

        insert_log(
            timestamp=datetime.now(),
            text=user_input,
            mood=mood,
            weather=desc
        )

        st.success(f"Η διάθεση καταχωρήθηκε ως '{mood}' με τον καιρό: {desc}.")
    else:
        st.warning("Παρακαλώ γράψε κάτι για το πώς νιώθεις.")

st.markdown("---")
st.subheader("📘 Ημερολόγιο Διάθεσης")

logs = get_all_logs()

if not logs.empty:
    # Απόκρυψη της στήλης "text"
    logs_display = logs.drop(columns=["text"])
    st.dataframe(logs_display, use_container_width=True)
else:
    st.info("Δεν υπάρχουν ακόμα καταχωρήσεις διάθεσης.")

st.markdown("---")
st.subheader("📊 Στατιστικά Διάθεσης")

if st.checkbox("Εμφάνιση κατανομής διάθεσης"):
    fig1 = insights.mood_distribution()
    if fig1:
        st.pyplot(fig1)

if st.checkbox("Εμφάνιση διάθεσης ανά ημέρα εβδομάδας"):
    fig2 = insights.mood_by_weekday()
    if fig2:
        st.pyplot(fig2)
