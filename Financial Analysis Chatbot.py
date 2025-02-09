from flask import Flask, request, jsonify, send_from_directory

def simple_chatbot(user_query):
    if user_query == "What is the total revenue?":
        return "The total revenue is [amount]."
    elif user_query == "How has net income changed over the last year?":
        return "The net income has [increased/decreased] by [amount] over the last year."
    elif user_query == "What is the average revenue growth for Tesla?":
        return "The average revenue growth for Tesla is -24.88%."
    elif user_query == "What is the average net income growth for Microsoft?":
        return "The average net income growth for Microsoft is -8.69%."
    elif user_query == "What is the average gross margin growth for Apple?":
        return "The average gross margin growth for Apple is 0.67%."
    else:
        return "Sorry, I can only provide information on predefined queries."

# Example interaction
user_query = input("Ask a financial question: ")
response = simple_chatbot(user_query)
print(response)

app = Flask(__name__)

# Route for chatbot interaction
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_query = request.json.get('query')
    response = simple_chatbot(user_query)
    return jsonify({'response': response})

# Route for favicon
@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico')

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')