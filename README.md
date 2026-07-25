# Minecraft Mod Creator

AI-powered Minecraft Mod Creator with multi-language support using GPT-5.

## Features

- 🌍 **Multi-language Support**: 50+ languages powered by GPT-5 API
- 🎮 **Dimension Management**: Create, edit, delete, and merge dimensions
- 📦 **Mod Export**: Export custom mods as .jar files
- 🔧 **Visual Editor**: Drag-and-drop UI for easy mod creation
- 🚀 **Real-time Preview**: See changes instantly
- 📌 **Version Management**: Create and manage multiple mod versions with semantic versioning

## Tech Stack

### Frontend
- React 18
- Vite
- TypeScript
- Tailwind CSS
- i18next (Multi-language support)

### Backend
- Python FastAPI
- Firebase Realtime Database
- OpenAI GPT-5 API

### Deployment
- Frontend: Vercel
- Backend: (To be decided)

## Project Structure

```
minecraft-mod-creator/
├── frontend/                 # React application
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   ├── index.css
│   │   └── i18n/
│   │       ├── config.ts
│   │       └── locales/      # 6 languages
│   ├── package.json
│   ├── vite.config.ts
│   ├── tsconfig.json
│   └── .env.example
├── backend/                  # FastAPI application
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── models/
│   │   │   ├── dimension.py
│   │   │   ├── translation.py
│   │   │   ├── mod.py
│   │   │   └── version.py
│   │   ├── routes/
│   │   │   ├── dimensions.py
│   │   │   ├── translations.py
│   │   │   ├── mods.py
│   │   │   └── versions.py
│   │   └── services/
│   │       ├── dimension_service.py
│   │       ├── translation_service.py
│   │       ├── mod_service.py
│   │       └── version_service.py
│   ├── requirements.txt
│   └── .env.example
├── docs/
│   ├── API.md                # Complete API documentation
│   └── SETUP.md              # Setup guide
└── README.md
```

## Getting Started

### Prerequisites
- Node.js 18+
- Python 3.9+
- Firebase Account
- OpenAI API Key (GPT-5)

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/124mirillion-ship-it/minecraft-mod-creator.git
   cd minecraft-mod-creator
   ```

2. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   cp .env.example .env.local
   # Edit .env.local with your Firebase credentials
   npm run dev
   ```

3. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env with your Firebase and OpenAI credentials
   python -m uvicorn app.main:app --reload
   ```

4. **Access the application**
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - API Docs: http://localhost:8000/docs

## API Endpoints

### Dimensions
- `POST /api/dimensions/` - Create dimension
- `GET /api/dimensions/` - List dimensions
- `GET /api/dimensions/{dimension_id}` - Get dimension
- `PUT /api/dimensions/{dimension_id}` - Update dimension
- `DELETE /api/dimensions/{dimension_id}` - Delete dimension
- `POST /api/dimensions/merge/` - Merge dimensions

### Translations (GPT-5)
- `POST /api/translations/translate/` - Translate text
- `GET /api/translations/languages/` - List supported languages
- `GET /api/translations/languages/{language_code}` - Get language info

### Mods
- `POST /api/mods/` - Create mod
- `GET /api/mods/` - List mods
- `GET /api/mods/{mod_id}` - Get mod
- `PUT /api/mods/{mod_id}` - Update mod
- `DELETE /api/mods/{mod_id}` - Delete mod
- `POST /api/mods/{mod_id}/export/` - Export mod

### Versions
- `POST /api/versions/` - Create version
- `GET /api/versions/mod/{mod_id}/` - List versions
- `GET /api/versions/mod/{mod_id}/latest` - Get latest version
- `GET /api/versions/{version_id}` - Get version
- `PUT /api/versions/{version_id}` - Update version
- `DELETE /api/versions/{version_id}` - Delete version
- `POST /api/versions/{version_id}/download` - Track download

See [API.md](docs/API.md) for detailed documentation.

## Supported Languages

English, 日本語, Español, Français, Deutsch, 中文, 한국어, Русский, العربية, Português, and 45+ more via GPT-5.

## Environment Variables

### Frontend (.env.local)
```
VITE_FIREBASE_API_KEY=your_api_key
VITE_FIREBASE_AUTH_DOMAIN=your_auth_domain
VITE_FIREBASE_PROJECT_ID=your_project_id
VITE_FIREBASE_STORAGE_BUCKET=your_storage_bucket
VITE_FIREBASE_MESSAGING_SENDER_ID=your_sender_id
VITE_FIREBASE_APP_ID=your_app_id
VITE_API_URL=http://localhost:8000/api
```

### Backend (.env)
```
DEBUG=True
API_PREFIX=/api
OPENAI_API_KEY=your_gpt5_api_key
OPENAI_MODEL=gpt-5
FIREBASE_PROJECT_ID=your_project_id
CORS_ORIGINS=["http://localhost:3000"]
```

## Development

### Running Tests
```bash
# Frontend
cd frontend && npm run lint

# Backend
cd backend && pytest
```

### Building for Production
```bash
# Frontend
cd frontend && npm run build

# Backend is ready as-is for deployment
```

## Deployment

### Frontend (Vercel)
1. Push to GitHub
2. Connect repository to Vercel
3. Add environment variables
4. Deploy

### Backend
Deploy to your preferred platform (Heroku, Railway, AWS, etc.)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - see LICENSE file for details

## Support

For questions and support, please open an issue on GitHub.

## Roadmap

- [ ] User authentication and profiles
- [ ] Mod marketplace
- [ ] Collaborative mod editing
- [ ] Advanced block/item editor
- [ ] Custom recipe creation
- [ ] Mod dependency management
- [ ] GitHub integration for version control
