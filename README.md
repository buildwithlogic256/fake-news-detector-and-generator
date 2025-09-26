


text
# Fake News Detector and Generator

An advanced AI-powered platform that detects fake news and generates realistic fake articles using state-of-the-art NLP models. This project integrates a BERT-based fake news detection model and GPT-2 text generation model into a clean, interactive web interface.

---

## Features

- **Fake News Detection**: Classifies news articles as fake or real with confidence scores using a BERT model.
- **Fake News Generation**: Produces AI-generated fake news articles from user prompts using GPT-2.
- **User-friendly Frontend**: Responsive UI with text input, file upload, and visual analytics.
- **Real-time Feedback**: Immediate predictions and text generation via backend API integration.

---

## Technologies

- Python 3.8+
- FastAPI (backend server)
- PyTorch & HuggingFace Transformers (BERT, GPT-2)
- HTML/CSS/JavaScript (frontend)
- GitHub Pages (frontend hosting)
- Cloud Platforms (backend deployment)

---

## Usage

### Running Locally

1. Clone the repository:

git clone https://github.com/buildwithlogic256/fake-news-detector-and-generator.git
cd fake-news-detector-and-generator

text

2. Install dependencies:

pip install -r requirements.txt

text

3. Start the backend server:

uvicorn backend:app --reload

text

4. Open `fake.html` in a browser locally or via a live server.

5. Use UI to detect or generate news articles. Frontend communicates with backend API automatically.

### Hosting Frontend on GitHub Pages

- Enable GitHub Pages in repository settings (select main branch and root folder).
- Access your frontend live at:

https://buildwithlogic256.github.io/fake-news-detector-and-generator/fake.html

text

- Update frontend API base URLs to point to your live backend when deployed.

---

## Backend Deployment

Backend must be deployed separately to cloud platforms like Heroku, Render, or AWS to provide public API access. Update frontend with the deployed backend URL accordingly.

---

## How It Works

- **Detection**: User inputs or uploads news text → Frontend sends text to backend → BERT model classifies as real or fake → Result with confidence returned and displayed.
- **Generation**: User inputs prompt → Frontend sends prompt to backend → GPT-2 generates realistic fake news text → Displayed to user.

---

## Contribution

Contributions, bug reports, and feature requests are welcome! Feel free to fork this repo and submit pull requests.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Developed by buildwithlogic256
