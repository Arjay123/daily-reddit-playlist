const merge = require('webpack-merge');
const baseConfig = require('./base.config.js');
const path = require('path');
var webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = merge(baseConfig, {
    entry: [
        'webpack-dev-server/client?http://localhost:3001',
        'webpack/hot/only-dev-server',
        '../src/index.js'
    ],
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
        new BundleTracker({filename: './webpack/dev-webpack-stats.json'}),
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
            "window.jQuery": "jquery"
        }),
        new webpack.DefinePlugin({
            'API_URL': JSON.stringify("http://localhost:8001/api/"),
            'USER_ID': JSON.stringify("1214623406")
        })
    ],
    output: {
        filename: 'bundle.js',
        publicPath: 'http://localhost:3001/static/bundles/'
    },
});
