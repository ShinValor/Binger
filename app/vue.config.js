
module.exports = {
  devServer: {
    clientLogLevel: 'info',
    proxy: {
      // proxy all requests starting with /api to target
      '/api': {
        target: 'http://binger-api-test-env.eba-mdbndpwy.us-east-2.elasticbeanstalk.com',
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
}