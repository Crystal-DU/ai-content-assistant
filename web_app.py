from flask import Flask, render_template, request
from pathlib import Path

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prompt = ""
    #如果用户上传文件，则读取文件内容，覆盖文本框内容
    if request.method == "POST":

        note = request.form.get("note", "")

    uploaded_file = request.files.get("file")

    if uploaded_file and uploaded_file.filename:
        note = uploaded_file.read().decode("utf-8")

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