from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prompt = ""

    if request.method == "POST":
        note = request.form.get("note", "")

        prompt = f"""
# AI Learning Assistant Prompt

You are an AI learning assistant.

Please analyze the following learning note and generate a structured summary.

## Topics Learned
- List the main topics.

## Key Takeaways
- Summarize the important points.

## Action Items
- List next actions or things to review.

## Interview Talking Points
- Explain how I can describe this learning experience in a professional setting.

## Learning Note

{note}
"""

    return render_template("index.html", prompt=prompt)

if __name__ == "__main__":
    app.run(debug=True)