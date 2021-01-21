import cookieUniversal from 'cookie-universal'


export default (error, context) => {
  if (error.toString().indexOf('Signature has expired')) {
    context.app.$apolloHelpers.onLogout(context.app.apolloProvider.defaultClient);
    const cookie_object = cookieUniversal();
    cookie_object.set('jwt_token', undefined);
  } else {
    context.error({statusCode: 304, message: error})
  }
}
