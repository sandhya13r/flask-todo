from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # List of dicts: {text: 'Task...', done: False}

@app.route("/")
def home():
    return render_template("home.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task_text = request.form.get("task")
    if task_text:
        tasks.append({"text": task_text, "done": False})
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

@app.route("/toggle/<int:index>")
def toggle(index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = not tasks[index]["done"]
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


