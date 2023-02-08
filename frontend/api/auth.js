export default {
 sendAccountPasswordResetEmail(email) {
   const requestOptions = {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email: email })
  };
  return fetch('/auth/password/reset/', requestOptions)
},
  resetAccountPassword(uid, token, new_password1, new_password2) { // eslint-disable-line camelcase
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ uid: uid,new_password1:new_password1,new_password2:new_password2 })
    };
    return fetch('/auth/password/reset/confirm/', requestOptions)
  },

};
