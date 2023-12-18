const path = require('path');

module.exports = {
    mode: 'dev',
    entry: './lead-manager/frontend/src/index.js',
    output: {
        filename: 'main.js',
        path: path.resolve(__dirname, 'lead-manager/frontend/static/frontend'),
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader"
                }
            }
        ]
    }
};