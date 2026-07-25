# Setup Guide

## Prerequisites

- Node.js 18+
- Python 3.9+
- Firebase Account
- OpenAI API Key (GPT-5)

## Frontend Setup

### 1. Navigate to frontend directory
```bash
cd frontend
```

### 2. Install dependencies
```bash
npm install
```

### 3. Create `.env.local` file
```bash
cp .env.example .env.local
```

### 4. Update `.env.local` with your Firebase credentials
```
VITE_FIREBASE_API_KEY=your_api_key
VITE_FIREBASE_AUTH_DOMAIN=your_auth_domain
VITE_FIREBASE_PROJECT_ID=your_project_id
VITE_FIREBASE_STORAGE_BUCKET=your_storage_bucket
VITE_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
VITE_FIREBASE_APP_ID=your_app_id
VITE_API_URL=http://localhost:8000/api
```

### 5. Start development server
```bash
npm run dev
```

The frontend will be available at `http://localhost:3000`

## Backend Setup

### 1. Navigate to backend directory
```bash
cd backend
```

### 2. Create Python virtual environment
```bash
python -m venv venv
```

### 3. Activate virtual environment
```bash
# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Create `.env` file
```bash
cp .env.example .env
```

### 6. Update `.env` with your credentials
```
DEBUG=True
API_PREFIX=/api

FIREBASE_PROJECT_ID=your_project_id
FIREBASE_PRIVATE_KEY_ID=your_key_id
FIREBASE_PRIVATE_KEY=your_private_key
FIREBASE_CLIENT_EMAIL=your_email
FIREBASE_CLIENT_ID=your_client_id
FIREBASE_AUTH_URI=https://accounts.google.com/o/oauth2/auth
FIREBASE_TOKEN_URI=https://oauth2.googleapis.com/token
FIREBASE_AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs

OPENAI_API_KEY=your_openai_api_key
OPENAI_MODEL=gpt-5

CORS_ORIGINS=["http://localhost:3000"]
```

### 7. Start backend server
```bash
python -m uvicorn app.main:app --reload
```

The backend will be available at `http://localhost:8000`

## Firebase Setup

1. Create a Firebase project at https://console.firebase.google.com
2. Enable Realtime Database
3. Download service account key and save as `serviceAccountKey.json` in backend directory
4. Update `.env` with Firebase credentials from service account key

## Deployment

### Frontend (Vercel)

1. Push code to GitHub
2. Go to https://vercel.com
3. Import your GitHub repository
4. Add environment variables
5. Deploy

### Backend

To be determined - options include Heroku, Railway, or AWS
