from pathlib import Path

input_dir = Path("input")
prompt_dir = Path("prompts")
prompt_dir.mkdir(exist_ok=True)

files = list(input_dir.glob("*.txt")) + list(input_dir.glob("*.md"))

if not files:
    print("No input files found.")
    exit()

for file in files:
    note = file.read_text()

    prompt = f"""# AI Learning Assistant Prompt

You are an AI learning assistant.

Please analyze the following learning note and generate a structured summary in Markdown.

## Output Format

# Learning Summary

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

    output_file = prompt_dir / f"{file.stem}_prompt.md"
    output_file.write_text(prompt)

    print(f"Generated prompt: {output_file}")