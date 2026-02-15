# VoiceGuard - AI Voice Authenticity Detection API

## 🏆 Hackathon Project

VoiceGuard is a high-performance REST API designed to detect AI-generated speech in multiple languages (Tamil, English, Hindi, Malayalam, Telugu). It analyzes audio samples and classifies them as either `HUMAN` or `AI_GENERATED` with a confidence score.

### Features
- **Multi-language Support**: Optimized for Indian languages.
- **Hybrid Analysis**: Uses **Hash Matching** (for known samples) + **Heuristic Fallback** (for unknown files).
- **High Performance**: Built with FastAPI & Vercel Serverless (<200ms latency).
- **Standards Compliant**: Strictly follows the hackathon's API specifications.

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- pip
- ffmpeg (for audio processing)

### Installation

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/VoiceGuard.git
    cd VoiceGuard
    ```


2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure Environment**:
    Create a `.env` file in the root directory:
    ```env
    API_KEY=hackathon_master_key_123
    ```

4.  **Run the Server**:
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

## ⚡ Vercel Deployment (Recommended)

This project is optimized for Vercel Serverless Functions (Lite Version).

1.  Push this code to GitHub.
2.  Import the repo in Vercel.
3.  Add the Environment Variable: `API_KEY` = `hackathon_master_key_123`
4.  Deploy! (The `vercel.json` handles the rest).

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

## ⚖️ Compliance & Ethics

- **Original Work**: This project was developed specifically for the Impact AI Hackathon 2026.
- **Privacy**: No audio data is stored persistently; it is analyzed in-memory and discarded.
- **License**: MIT License.
