function setCookie(name,value,days) {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}
function getCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for(var i=0;i < ca.length;i++) {
        var c = ca[i];
        while (c.charAt(0)==' ') c = c.substring(1,c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
    }
    return null;
}
function eraseCookie(name) {   
    document.cookie = name +'=; Path=/; Expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}

export const getUserFromCookie = (req) => {
  if (!req.headers.cookie) return
  const tokenCookie = req.headers.cookie.split(';').find(c => c.trim().startsWith('token='))
  if (!tokenCookie) return
  const token = tokenCookie.split('=')[1]
  const usernameCookie = req.headers.cookie.split(';').find(c => c.trim().startsWith('token='))
  if (!usernameCookie) return
  const username = usernameCookie.split('=')[1]
  return {token: token, username: username}
}

export const setUserInformation = (payload) => {
  setCookie('username', payload.username)
  setCookie('token', payload.token)
}

export const unsetUserInformation = () => {
  eraseCookie('username')
  eraseCookie('token')
}
