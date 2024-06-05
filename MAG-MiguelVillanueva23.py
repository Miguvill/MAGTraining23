from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    # HTML content with embedded CSS
    message = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>ROI Calculator</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                background: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            h1 {
                margin-bottom: 20px;
            }
            form {
                display: flex;
                align-items: center;
            }
            input {
                margin-right: 10px;
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }
            button {
                padding: 10px;
                background: white;
                color: black;
                border: 1px solid #ccc;
                border-radius: 4px;
                cursor: pointer;
            }
            button:hover {
                background: #f4f4f4;
            }
            #results {
                margin-top: 20px;
                display: none;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>ROI Calculator</h1>
            <form id="calculator-form">
                <input type="text" id="returned_amount" name="returned_amount" placeholder="Returned Amount" required>
                <input type="text" id="invested_amount" name="invested_amount" placeholder="Invested Amount" required>
                <button type="submit">Calculate</button>
            </form>
            <div id="results">
                <p id="gain"></p>
                <p id="roi"></p>
            </div>
        </div>
        <script>
            document.getElementById('calculator-form').addEventListener('submit', function(e) {
                e.preventDefault();
                const returnedAmount = document.getElementById('returned_amount').value;
                const investedAmount = document.getElementById('invested_amount').value;
                fetch('/calculate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ returned_amount: returnedAmount, invested_amount: investedAmount }),
                })
                .then(response => response.json())
                .then(data => {
                    document.getElementById('gain').textContent = `Gain: ${data.gain.toFixed(2)}`;
                    document.getElementById('roi').textContent = `ROI: ${data.roi.toFixed(2)}%`;
                    document.getElementById('results').style.display = 'block';
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
            });
        </script>
    </body>
    </html>
    """
    return message

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    returned_amount = float(data['returned_amount'])
    invested_amount = float(data['invested_amount'])
    
    gain = abs(returned_amount - invested_amount)
    roi = abs(((returned_amount - invested_amount) / invested_amount) * 100)
    
    return jsonify({'gain': gain, 'roi': roi})

if __name__ == '__main__':
    app.run(debug=True)

