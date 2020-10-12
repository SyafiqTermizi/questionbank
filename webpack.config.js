var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    context: __dirname,
    devtool: 'inline-source-map',
    entry:{
        main:  './static/js/index',
        invite_form: './static/js/inviteForm',
        choice_form: './static/ts/components/ChoiceFormContainer',
        user_change_form: './static/js/userChangeForm',
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
    rules: [
      {
        test: /\.scss$/,
        use: [
            // fallback to style-loader in development
            process.env.NODE_ENV !== 'production' ? 'style-loader' : MiniCssExtractPlugin.loader,
            "css-loader",
            "sass-loader"
        ]
      },
      {
        test: /\.tsx?$/,
        use: 'ts-loader',
        exclude: /node_modules/,
      },
    ]
  },
  resolve: {
    extensions: [ '.tsx', '.ts', '.js' ],
  }
}
