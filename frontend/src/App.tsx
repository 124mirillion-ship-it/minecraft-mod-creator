import { useEffect, useState } from 'react'
import { useTranslation } from 'react-i18next'
import './App.css'

function App() {
  const { t, i18n } = useTranslation()
  const [selectedLanguage, setSelectedLanguage] = useState<string>('en')

  useEffect(() => {
    i18n.changeLanguage(selectedLanguage)
  }, [selectedLanguage, i18n])

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      <nav className="bg-gray-800 p-4">
        <div className="max-w-7xl mx-auto flex justify-between items-center">
          <h1 className="text-2xl font-bold">⛏️ Minecraft Mod Creator</h1>
          <select
            value={selectedLanguage}
            onChange={(e) => setSelectedLanguage(e.target.value)}
            className="bg-gray-700 text-white px-4 py-2 rounded"
          >
            <option value="en">English</option>
            <option value="ja">日本語</option>
            <option value="es">Español</option>
            <option value="fr">Français</option>
            <option value="de">Deutsch</option>
            <option value="zh">中文</option>
          </select>
        </div>
      </nav>

      <main className="max-w-7xl mx-auto p-8">
        <h2 className="text-4xl font-bold mb-4">{t('welcome')}</h2>
        <p className="text-gray-400 mb-8">{t('description')}</p>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          <div className="bg-gray-800 p-6 rounded-lg hover:bg-gray-700 transition">
            <h3 className="text-xl font-bold mb-2">🌍 {t('multiLanguage')}</h3>
            <p className="text-gray-400">{t('multiLanguageDesc')}</p>
          </div>
          <div className="bg-gray-800 p-6 rounded-lg hover:bg-gray-700 transition">
            <h3 className="text-xl font-bold mb-2">🎮 {t('dimensions')}</h3>
            <p className="text-gray-400">{t('dimensionsDesc')}</p>
          </div>
          <div className="bg-gray-800 p-6 rounded-lg hover:bg-gray-700 transition">
            <h3 className="text-xl font-bold mb-2">📦 {t('export')}</h3>
            <p className="text-gray-400">{t('exportDesc')}</p>
          </div>
          <div className="bg-gray-800 p-6 rounded-lg hover:bg-gray-700 transition">
            <h3 className="text-xl font-bold mb-2">🔧 {t('editor')}</h3>
            <p className="text-gray-400">{t('editorDesc')}</p>
          </div>
        </div>

        <button className="mt-8 bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 px-6 rounded-lg">
          {t('getStarted')}
        </button>
      </main>
    </div>
  )
}

export default App
