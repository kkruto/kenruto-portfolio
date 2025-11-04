/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './core/templates/**/*.html',
    './static/js/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          DEFAULT: '#F59E0B',
          light: '#FCD34D',
          dark: '#D97706',
        },
        about: {
          primary: '#1E3A8A',
          secondary: '#F59E0B',
          bg: '#F8FAFC',
          text: '#1E293B',
          accent: '#3B82F6',
        },
        tlw: {
          primary: '#7C2D12',
          secondary: '#FBBF24',
          bg: '#0F0F0F',
          text: '#F1F5F9',
          accent: '#DC2626',
        },
        bets: {
          primary: '#0EA5E9',
          secondary: '#84CC16',
          bg: '#111827',
          text: '#10B981',
          accent: '#F97316',
        },
        kiota: {
          primary: '#374151',
          secondary: '#059669',
          bg: '#FFFBEB',
          text: '#1F2937',
          accent: '#0891B2',
        },
        gallery: {
          primary: '#0C4A6E',
          secondary: '#EA580C',
          bg: '#FFFFFF',
          text: '#18181B',
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
        serif: ['Lora', 'serif'],
      },
      transitionDuration: {
        '400': '400ms',
        '600': '600ms',
        '700': '700ms',
      },
      animation: {
        'fade-in': 'fadeIn 0.5s ease-in-out',
        'slide-up': 'slideUp 0.5s ease-out',
        'slide-down': 'slideDown 0.5s ease-out',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { transform: 'translateY(20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
        slideDown: {
          '0%': { transform: 'translateY(-20px)', opacity: '0' },
          '100%': { transform: 'translateY(0)', opacity: '1' },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('@tailwindcss/forms'),
  ],
}