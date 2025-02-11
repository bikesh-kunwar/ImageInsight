# ImageInsight 🔍📸

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.0.2-green)](https://flask.palletsprojects.com/)

A web application powered by **Azure Computer Vision** that provides AI-powered image analysis. Upload any image to get instant insights including tags, descriptive captions, and detected objects.

![Demo](static/demo.gif) <!-- Replace with your actual demo GIF -->

## 🌟 Features

- **Smart Image Analysis**
  - **Tags**: Automatic labeling of objects/scenes (e.g., "mountain", "car")
  - **Captions**: AI-generated descriptive sentences
  - **Objects**: Specific detected items with confidence scores
- **File Handling**
  - Auto-resizing for Azure compatibility (≤4MB, ≤4200px)
  - Supports JPG, PNG, BMP, GIF formats
- **Secure Configuration**
  - Environment variable protection for API keys
  - Input validation and error handling

## 🛠️ Tech Stack

**Backend**  
![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask)
![Azure Computer Vision](https://img.shields.io/badge/-Azure%20CV-0078D4?logo=microsoft-azure)

**Frontend**  
![HTML5](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/-CSS3-1572B6?logo=css3)

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- [Azure Account](https://azure.microsoft.com/) (Free tier available)
- Git (for version control)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/ImageInsight.git
   cd ImageInsight
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Azure Setup**
   - Create a Computer Vision resource in [Azure Portal](https://portal.azure.com/)
   - Get your:
     - **API Key**
     - **Endpoint URL**

4. **Configure Environment**
   Create `.env` file:
   ```plaintext
   API_KEY=your_azure_key_here
   ENDPOINT=your_azure_endpoint_here
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```
   Visit ➡️ `http://localhost:5000`

## 🏗️ Architecture

```mermaid
graph TD
    A[User] --> B[Flask Web Interface]
    B --> C[Image Processing]
    C --> D[Azure Computer Vision API]
    D --> E[Analysis Results]
    E --> B
    B --> A
```

## 📂 Project Structure

```
ImageInsight/
├── app.py                 # Main application logic
├── requirements.txt       # Dependency list
├── README.md              # This documentation
├── .gitignore             # Ignored files/folders
├── .env                   # Environment variables
├── static/
│   ├── styles.css         # Styling
│   └── uploads/           # Uploaded images storage
├── templates/
│   ├── index.html         # Upload interface
│   └── result.html        # Results display
```

## 🔒 Security Best Practices

1. **Never commit sensitive data**
   - Keep `.env` in `.gitignore`
2. **Azure Key Management**
   - Use least-privilege access
   - Rotate keys regularly
3. **Input Validation**
   - File type restrictions
   - Size limitations

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the project
2. Create your feature branch:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. Commit changes:
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. Push to branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. Open a Pull Request

## 📜 License

Distributed under MIT License. See [LICENSE](LICENSE) for details.

---

**Created with ❤️ by bikesh-kunwar**  
[![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github)](https://github.com/your-username)
