from flask import Flask, request, jsonify
import stripe

app = Flask(__name__)

# Configure Stripe API key
stripe.api_key = 'sk_test_your_stripe_secret_key'

@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    # Get product ID and price from the request
    product_id = request.json.get('productId')
    price = request.json.get('price')
    
    # Create a new Checkout session
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'usd',
                    'product': product_id,
                    'unit_amount': price,
                },
                'quantity': 1,
            },
        ],
        mode='payment',
        success_url='http://localhost:5000/success',
        cancel_url='http://localhost:5000/cancel',
    )
    
    return jsonify({'sessionId': checkout_session['id']})

if __name__ == '__main__':
    app.run(debug=True)