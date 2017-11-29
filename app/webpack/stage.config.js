const merge = require('webpack-merge');
const base = require('./base.config.js');
const path = require('path');
var webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = merge(base, {
    entry: [
        '../src/index.js'
    ],
    output: {
        filename: 'bundle.js',
        path: path.resolve(__dirname, '../assets/bundles/'),
        publicPath: 'http://127.0.0.1:8081/static/bundles/'
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
        new webpack.NoEmitOnErrorsPlugin(), // don't reload if there is an error
        new BundleTracker({filename: './webpack/stage-webpack-stats.json'}),
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery"
        }),
        new webpack.DefinePlugin({
            'API_URL': JSON.stringify("http://127.0.0.1:8081/api/")
        })
    ]
});
