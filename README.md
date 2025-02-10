# ImageInsight 🔍📸

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/flask-3.0.2-green)](https://flask.palletsprojects.com/)

A web application powered by **Azure Computer Vision** that provides AI-powered image analysis. Upload any image to get instant insights including tags, descriptive captions, and detected objects.

![Demo](static/demo.gif) *Replace with your actual demo GIF*

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
