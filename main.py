from dotenv import load_dotenv
from embedchain.store.assistants import OpenAIAssistant

import streamlit as st

load_dotenv()

st.title("💬 AiPsy Chatbot")
st.caption("🚀 An Embedchain app powered by OpenAI!")
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": """
         בטח, אשמח להציג את עצמי. אני Aipsy, מערכת בינה מלאכותית שנוצרה כדי לתמוך באנשים הנמצאים בסיטואציות של לחץ רגשי וחרדה, במיוחד באזורי קונפליקט ומלחמה. המטרה שלי היא להיות מקור נחמה ותמיכה, להקשיב לדאגות ולחששות שלך ולתת מענה חמלה ואכפתיות. אני מיועד לשפר את החוויה הרגשית שלך דרך שיח תומך, מבין וסובלני.

אני מותאם במיוחד לתרבות ולאופי הישראלית, כולל השפה, ההבנה של דפוסי החשיבה, והערכים של החברה הישראלית. אני לא אומר רק מה שאולי תרצה לשמוע, אלא מציע גם מרחב לפיתוח תובנות ומציאת דרכים להתמודד עם אתגרים.

אני אינני מחליף אלטרנטיבי לטיפול פסיכולוגי מקצועי אם זה מה שנדרש, אבל אני כאן להציע תמיכה והדרכה ראשונית, ואני יכול להיות מקור גישה מהירה לתמיכה רגשית. אנא דבר איתי על כל נושא שמעורר בך חשש או על כל מחשבה שאתה רוצה לחלוק.)
        """,
        }
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything!"):
    # Load an assistant and create a new thread
    assistant = OpenAIAssistant(assistant_id="asst_LsEbMB7nz2squzGOtndlmezI")
    # Get response from assistant
    response = assistant.chat(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Add assistant message to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    # Clear the input field after sending a message
    st.session_state.messages.append({"role": "user", "content": ""})
