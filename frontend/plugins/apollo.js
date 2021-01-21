import cookieUniversal from 'cookie-universal'

export default function ({req, res, app}) {
  var headers = {};
  const cookie_object = cookieUniversal(req, res);

  let url = process.env.BACKEND_URL || false;
  let browser_url = process.env.BROWSER_BACKEND_URL || url;


  let config = {
    httpEndpoint: process.server
      ? url + '/graphql'
      : browser_url + '/graphql',
    httpLinkOptions: {
      headers: headers
    }
  };


  return config
}
