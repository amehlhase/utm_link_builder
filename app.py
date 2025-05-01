from flask import Flask, render_template, request
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    final_url = None
    if request.method == 'POST':
        base_url = request.form['base_url']
        source = request.form['source']
        medium = request.form['medium']
        campaign = request.form['campaign']
        content = request.form.get('content', '')
        term = request.form.get('term', '')

        final_url = f"{base_url}?utm_source={source}&utm_medium={medium}&utm_campaign={campaign}"
        if content:
            final_url += f"&utm_content={content}"
        if term:
            final_url += f"&utm_term={term}"

    return render_template('index.html', final_url=final_url)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # safe for deployment
    app.run(host='0.0.0.0', port=port)
