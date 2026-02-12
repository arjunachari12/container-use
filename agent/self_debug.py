
import subprocess
from openai import OpenAI

client = OpenAI()

def generate_code(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def run_code(code):
    with open("generated.py", "w") as f:
        f.write(code)
    result = subprocess.run(
        ["python", "generated.py"],
        capture_output=True,
        text=True
    )
    return result

prompt = "Write Python code to calculate factorial of 5."

code = generate_code(prompt)
result = run_code(code)

if result.returncode != 0:
    fix_prompt = f"Fix this error:\n{result.stderr}"
    code = generate_code(fix_prompt)
    result = run_code(code)

print(result.stdout)
