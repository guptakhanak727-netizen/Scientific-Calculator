
import math
import os
from flask import Flask, render_template, request

app = Flask(__name__,
 template_folder=os.path.join(os.path.dirname(__file__), "templates"))


@app.route("/", methods=["GET", "POST"])
def calculator():
  result = ""
  expression = ""

  if request.method == "POST":
    expression = request.form.get("expression", "")
    button = request.form.get("button", "")

    try:
      if button == "C":
        expression = ""
        result = ""
      elif button == "=":
        # Safe evaluation using restricted globals/locals
        # Allowing basic math and functions from the math module
        safe_dict = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log10,
            "ln": math.log,
            "pi": math.pi,
            "e": math.e,
            "factorial": math.factorial,
            "radians": math.radians,
        }
        # Evaluate expression securely
        result = str(eval(expression, {"__builtins__": {}}, safe_dict))
      else:
        # Append clicked button value to the expression
        expression += button
    except Exception:
      result = "Error"

  return render_template(
      "index.html", expression=expression, result=result
  )


if __name__ == "__main__":
  app.run(debug=True)
