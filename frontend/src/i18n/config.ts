import i18n from 'i18next'
import { initReactI18next } from 'react-i18next'
import enTranslation from './locales/en.json'
import jaTranslation from './locales/ja.json'
import esTranslation from './locales/es.json'
import frTranslation from './locales/fr.json'
import deTranslation from './locales/de.json'
import zhTranslation from './locales/zh.json'

const resources = {
  en: { translation: enTranslation },
  ja: { translation: jaTranslation },
  es: { translation: esTranslation },
  fr: { translation: frTranslation },
  de: { translation: deTranslation },
  zh: { translation: zhTranslation },
}

i18n
  .use(initReactI18next)
  .init({
    resources,
    lng: 'en',
    interpolation: {
      escapeValue: false,
    },
  })

export default i18n
