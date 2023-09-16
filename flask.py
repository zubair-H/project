from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    product_image = None
    dietary_restrictions = None

    if request.method == 'POST':
        serial_number = request.form['serial_number']
        dietary_restrictions = request.form['dietary_restrictions']

        # Make an API request to get product data
        api_url = f'https://api.example.com/products/{serial_number}'
        response = requests.get(api_url)

        if response.status_code == 200:
            product_data = response.json()
            product_image = product_data['image']
            # Extract dietary restrictions from the product data
            # This may vary depending on the API response structure

    return render_template('index.html', product_image=product_image, dietary_restrictions=dietary_restrictions)

if __name__ == '__main__':
    app.run(debug=True)
