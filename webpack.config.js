var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    entry:{
        main:  './static/js/index',
        invite_form: './static/js/inviteForm',
        main_css: './static/scss/index.scss'
    },
    output: {
      path: path.resolve('./static/bundles/'),
      filename: "[name].js"
    },

  plugins: [
    new BundleTracker({filename: './webpack-stats.json'})
  ],

  optimization: {
    runtimeChunk: 'single',
    splitChunks: {
      cacheGroups: {
        lazy_libraries: {
          test: /[\\/]node_modules[\\/]/,
          chunks: 'async'
        },
        vendor: {
          test: /[\\/]node_modules[\\/]/,
          name: 'vendor',
          chunks: 'all'
        }
      }
    }
  },

  module: {
    rules: [{
        test: /\.scss$/,
        use: [
            // fallback to style-loader in development
            process.env.NODE_ENV !== 'production' ? 'style-loader' : MiniCssExtractPlugin.loader,
            "css-loader",
            "sass-loader"
        ]
    }]
  }
}
