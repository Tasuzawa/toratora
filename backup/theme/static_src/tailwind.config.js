/**
 * This is a minimal config.
 *
 * If you need the full config, get it from here:
 * https://unpkg.com/browse/tailwindcss@latest/stubs/defaultConfig.stub.js
 */

module.exports = {
    content: [
        /**
         * HTML. Paths to Django template files that will contain Tailwind CSS classes.
         */

        /*  Templates within theme app (<tailwind_app_name>/templates), e.g. base.html. */
        '../templates/**/*.html',

        /*
         * Main templates directory of the project (BASE_DIR/templates).
         * Adjust the following line to match your project structure.
         */
        '../../templates/**/*.html',

        /*
         * Templates in other django apps (BASE_DIR/<any_app_name>/templates).
         * Adjust the following line to match your project structure.
         */
        '../../**/templates/**/*.html',

        /**
         * JS: If you use Tailwind CSS in JavaScript, uncomment the following lines and make sure
         * patterns match your project structure.
         */
        /* JS 1: Ignore any JavaScript in node_modules folder. */
        // '!../../**/node_modules',
        /* JS 2: Process all JavaScript files in the project. */
        // '../../**/*.js',

        /**
         * Python: If you use Tailwind CSS classes in Python, uncomment the following line
         * and make sure the pattern below matches your project structure.
         */
        // '../../**/*.py'
        'node_modules/preline/dist/*.js',
    ],
    theme: {
        screens: {
            xs: '320px',
            sm: '640px',
            md: '768px',
            lg: '1024px',
            xl: '1280px',
            '2xl': '1536px',
          },
        extend: {
            scrollbar: {
                comment: {
                    width: '3px',
                    height: '3px',
                    borderRadius: '3px',
                    backgroundColor: 'transparent',
                    thumb: {
                        backgroundColor: '#ccc',
                        borderRadius: '3px',
                    },
                },
            },
        },
        colors:{
            transparent: 'transparent',
            current: 'currentColor',
            'black': '#000000',
            'white': '#ffffff',
            'gray': {
                50: '#f9fafb',
                100: '#f3f4f6',
                200: '#e5e7eb',
                300: '#d1d5db',
                400: '#9ca3af',
                500: '#6b7280',
                600: '#4b5563',
                700: '#374151',
                800: '#1f2937',
                900: '#111827',
                950: '#030712',
            },
            'buttermilk': {
                50: '#fef9e8',
                100: '#ffeead',
                200: '#ffe288',
                300: '#ffcb44',
                400: '#feb111',
                500: '#ee9804',
                600: '#cd7201',
                700: '#a44e04',
                800: '#873e0c',
                900: '#733310',
                950: '#431805',
            },
            'letto': {
                50: '#fdf4f3',
                100: '#fce7e7',
                200: '#f8d3d3',
                300: '#f3aeb0',
                400: '#eb8185',
                500: '#e0535c',
                600: '#cb3344',
                700: '#a02334',
                800: '#8f2234',
                900: '#7b2032',
                950: '#440d16',
            },
            'slate': {
                50: '#f8fafc',
                100: '#f1f5f9',
                200: '#e2e8f0',
                300: '#cbd5e1',
                400: '#94a3b8',
                500: '#64748b',
                600: '#475569',
                700: '#334155',
                800: '#1e293b',
                900: '#0f172a',
                950: '#020617',
            },
            'vistablue': {
                50: '#f0f9f4',
                100: '#dbf0e4',
                200: '#bae0cc',
                300: '#96ceb4',
                400: '#5bac89',
                500: '#3a8f6d',
                600: '#297256',
                700: '#215b47',
                800: '#1c4939',
                900: '#183c31',
                950: '#0c221c',
            },
            'blue': {
                50: '#eff6ff',
                100: '#dbeafe',
                200: '#bfdbfe',
                300: '#93c5fd',
                400: '#60a5fa',
                500: '#3b82f6',
                600: '#2563eb',
                700: '#1d4ed8',
                800: '#1e40af',
                900: '#1e3a8a',
                950: '#172554',
            },
            'orange': {
                50: '#fff7ed',
                100: '#ffedd5',
                200: '#fed7aa',
                300: '#fdba74',
                400: '#fb923c',
                500: '#f97316',
                600: '#ea580c',
                700: '#c2410c',
                800: '#9a3412',
                900: '#7c2d12',
                950: '#431407',
            },

        }
    },
    plugins: [
        /**
         * '@tailwindcss/forms' is the forms plugin that provides a minimal styling
         * for forms. If you don't like it or have own styling for forms,
         * comment the line below to disable '@tailwindcss/forms'.
         */
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
        require('preline/plugin'),
    ],
}
