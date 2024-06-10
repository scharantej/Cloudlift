
# main.py

from flask import Flask, request, render_template
from sales_plan_generator import generate_sales_plan

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/create_sales_plan", methods=["POST"])
def create_sales_plan():
    customer_info = request.form.get("customer_info")
    current_infrastructure = request.form.get("current_infrastructure")
    desired_benefits = request.form.get("desired_benefits")

    sales_plan = generate_sales_plan(customer_info, current_infrastructure, desired_benefits)

    return render_template("sales_plan.html", sales_plan=sales_plan)

@app.route("/download_sales_plan")
def download_sales_plan():
    sales_plan = request.args.get("sales_plan")
    # Logic to generate PDF or other suitable format
    return send_file("sales_plan.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run()
