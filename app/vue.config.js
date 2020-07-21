module.exports = {
  devServer: {
    clientLogLevel: 'info',
    proxy: {
      // proxy all requests starting with /api to target
      '/api': {
        target: 'https://binger-api-testv1.azurewebsites.net',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
}