from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get form data
        pay_method = request.form.get("pay_method", "")
        amount = request.form.get("amount", "")
        currency = request.form.get("currency", "")
        success_url = request.form.get("success_url", "")
        cancel_url = request.form.get("cancel_url", "")
        client_email = request.form.get("client_email", "")
        web_id = request.form.get("web_id", "")
        order_id = request.form.get("order_id", "")
        addi_info = request.form.get("addi_info", "")

        # Prepare data for POST request
        payload = {
            "pay_method": pay_method,
            "amount": amount,
            "currency": currency,
            "success_url": success_url,
            "cancel_url": cancel_url,
            "client_email": client_email,
            "web_id": web_id,
            "order_id": order_id,
            "addi_info": addi_info,
        }

        headers = request.headers
        print(headers)

        # Make POST request
        response = requests.post(
            "https://www.cashmaal.com/Pay/", data=payload, headers=headers
        )

        # Handle response, you can customize this based on the API's response
        if response.status_code == 200:
            return f"Success! Response: {response.text}"
        else:
            return f"Error! Status Code: {response.status_code}"

    # Render the form template for GET requests
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
