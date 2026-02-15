# VoiceGuard - AI Voice Authenticity Detection API

## 🏆 Hackathon Project

VoiceGuard is a high-performance REST API designed to detect AI-generated speech in multiple languages (Tamil, English, Hindi, Malayalam, Telugu). It analyzes audio samples and classifies them as either `HUMAN` or `AI_GENERATED` with a confidence score.

### Features
- **Multi-language Support**: Optimized for Indian languages.
- **Robust Inference**: Uses spectral feature analysis (MFCCs, Spectral Centroid) via `librosa`.
- **High Performance**: Built with FastAPI for <200ms latency.
- **Standards Compliant**: Strictly follows the hackathon's API specifications.

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip
- ffmpeg (for audio processing)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/voice-guard-api.git
    cd voice-guard-api
    ```

2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the Server**:
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

## 🛠 Usage

### API Endpoint
**POST** `/api/v1/detect`

**Headers**:
- `Content-Type`: `application/json`
- `x-api-key`: `hackathon_master_key_123`

**Request Body**:
```json
{
  "language": "English",
  "audioFormat": "mp3",
  "audioBase64": "<base64_encoded_audio_string>"
}
```

**Response**:
```json
{
  "status": "success",
  "classification": "AI_GENERATED",
  "confidenceScore": 0.98
}
```

## 🧪 Testing

We have included a self-evaluation script `test_my_api.py` that runs the API against the provided sample dataset.

1.  Start the server.
2.  Run the test:
    ```bash
    python test_my_api.py
    ```

## 🐳 Docker Deployment

Build and run the container:

```bash
docker build -t voiceguard .
docker run -p 8000:8000 voiceguard
```

## 📂 Project Structure

```
├── app/
│   ├── api/            # API Endpoints
│   ├── core/           # Configuration
│   ├── services/       # Inference Logic (Feature Extraction)
│   └── main.py         # App Entry Point
├── test_my_api.py      # Evaluation Script
├── requirements.txt    # Dependencies
├── Dockerfile          # Container Configuration
└── README.md           # Documentation
```
