from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.form['user_message']

    if user_message.lower() == 'hi' or user_message.lower() == 'hello':
        bot_response = "Hi there! How can I help you?"
    elif user_message.lower() == 'how are you?':
        bot_response = "I'm just a bot, but thanks for asking!"
    else:
        bot_response = "Sorry, I didn't understand that. Can you please rephrase?"

    return jsonify({'bot_response': bot_response})


if __name__ == '__main__':
    app.run(debug=True)