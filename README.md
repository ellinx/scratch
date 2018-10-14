# scratch

# Install Babel and transcompile ES6 to ES5
1. `npm install --save-dev babel-cli`
2. `npm install babel-preset-env`
3. Compile ES6 to ES5
`npx babel --presets env source.js --out-file compiled.js`
