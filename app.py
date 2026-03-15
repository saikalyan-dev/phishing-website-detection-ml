from flask import Flask, render_template, request
import joblib
import numpy as np
import pandas as pd
from urllib.parse import urlparse
import plotly.graph_objects as go
import plotly.io as pio

app = Flask(__name__)

# Load the trained model (Decision Tree)
model = joblib.load('notebook/dt_model.pkl')

# Function to extract features from a URL (simplified for demo purposes)
def extract_features(url):
    parsed_url = urlparse(url)
    features = {
        'url_length': len(url),
        'domain_length': len(parsed_url.netloc),
        'path_length': len(parsed_url.path),
        'https': 1 if parsed_url.scheme == 'https' else 0,
        'num_subdomains': len(parsed_url.hostname.split('.')) - 2,
    }
    return np.array(list(features.values())).reshape(1, -1)

# Read dataset from CSV (without the target column)
data = pd.read_csv('notebook/data/phishing.csv')

# Check the columns to debug
print(data.columns)

# Prepare the dataset with only the features (no 'target' column)
X = data  # Use the entire dataset (no target column)

# Calculate distribution of phishing vs. legitimate URLs (mock distribution in this case)
# Since we do not have the 'target' column, this is a mock distribution (you can remove this if not needed)
labels = ['Phishing', 'Legitimate']
values = [len(X) // 2, len(X) // 2]  # Mock distribution (equal split, can be modified)

# Create the pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=0.3)])
pie_chart = pio.to_html(fig, full_html=False)  # Convert to HTML to embed in template

@app.route('/')
def home():
    return render_template('index.html', pie_chart=pie_chart)

@app.route('/check', methods=['POST'])
def check_url():
    url = request.form['url']
    features = extract_features(url)
    prediction = model.predict(features)[0]
    result = 'Phishing' if prediction == 1 else 'Legitimate'


    
    
    # Return the prediction result and the pie chart
    return render_template('index.html', result=result,url=url , pie_chart=pie_chart)


if __name__ == "__main__":
    app.run(debug=True)
