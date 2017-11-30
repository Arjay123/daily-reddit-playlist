module.exports = {
    context: __dirname,
    devServer: {
        contentBase: './dist'
    },
    module: {
        rules:[
            {
                test: /\.js$/,
                exclude: /(node_modules|bower_components)/,
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: ['react']
                    }
                }
            },
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader' ]
            },
            {
                test: /\.(png|jpg)$/,
                loader: 'url-loader'
            }
        ]
    }
};