from flask import request, render_template, session, redirect, url_for
from main_utils import classify_with_context, generate_response, initialize_conversation

def register_routes(app):
    @app.route("/", methods=["GET", "POST"])
    def index():
        if "conversation" not in session:
            initialize_conversation()

        if request.method == "POST":
            user_input = request.form.get("user_input", "").strip()
            if user_input:
                session["conversation"].append({"role": "user", "content": user_input})
                last_context = session.get("last_cooking_context", "")
                is_cooking = classify_with_context(user_input, last_context)

                if is_cooking:
                    session["last_cooking_context"] = user_input
                    assistant_reply = generate_response(session["conversation"])
                    session["conversation"].append({"role": "assistant", "content": assistant_reply})
                    session["last_cooking_context"] += " " + assistant_reply
                else:
                    refusal_msg = (
                        "I'm sorry, I only discuss cooking or food-related topics. "
                        "Please ask about recipes, ingredients, or cooking techniques."
                    )
                    session["conversation"].append({"role": "assistant", "content": refusal_msg})
                    session["last_cooking_context"] = ""

                session.modified = True
            return redirect(url_for("index"))

        return render_template("index.html", conversation=session.get("conversation", []))

    @app.route("/clear")
    def clear_chat():
        session.pop("conversation", None)
        session.pop("last_cooking_context", None)
        return redirect(url_for("index"))


