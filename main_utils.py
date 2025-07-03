# main_utils.py
import openai
import joblib
import os

# Load classifier and model
classifier = joblib.load("topic_classifier_final.pkl")
openai.api_key = os.environ["OPENAI_API_KEY"]
FINE_TUNED_MODEL = os.environ["FINE_TUNED_MODEL"]

def classify_with_context(user_input, last_cooking_context):
    combined = user_input + " " + last_cooking_context
    prediction = classifier.predict([combined])[0]
    return prediction == "cooking"

def generate_response(conversation):
    try:
        response = openai.ChatCompletion.create(
            model=FINE_TUNED_MODEL,
            messages=conversation,
            max_tokens=1500,
            temperature=0.7
        )
        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error: {str(e)}"

def initialize_conversation():
    session = __import__('flask').session  # lazy import to avoid circular issues
    session["conversation"] = [
        {"role": "system", "content": "You are a helpful cooking assistant."},
        {"role": "system", "content": "Always provide metric and imperial units."},
        {"role": "system", "content": "You don't answer non-cooking questions..."},
        {"role": "system", "content": "All responses must relate back to food or cooking."}
    ]
    session["last_cooking_context"] = ""
