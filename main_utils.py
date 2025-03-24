# main_utils.py
import openai
import joblib

# Load classifier and model
classifier = joblib.load("topic_classifier_final.pkl")
openai.api_key = "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"
FINE_TUNED_MODEL = "ft:gpt-4o-mini-2024-07-18:personal:cooking-model:BDk7GJ6r"

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
