import axios from "axios"
const  Domain = process.env.VUE_APP_Backed_URL
const  env = process.env.VUE_APP_ENV

var Axios= axios.create({
    baseURL:Domain,
    withCredentials: true

})


function getCookie(name) {
    if (!document.cookie) {
      return null;
    }

    const xsrfCookies = document.cookie.split(';')
      .map(c => c.trim())
      .filter(c => c.startsWith(name + '='));

    if (xsrfCookies.length === 0) {
      return null;
    }
    return decodeURIComponent(xsrfCookies[0].split('=')[1]);
  }

  Axios.interceptors.request.use(function (config) {
    var csrfToken = getCookie('csrftoken');
     config.headers['X-CSRFToken'] =  csrfToken;
    return config;
});

Axios.interceptors.response.use(function (response) {
    // Do something with response data
    return response;
  }, function (error) {
    // Do something with response erro
    // console.log('Axios Global Eror', error.response.status)
    // if (error.response.status == 403){
    //     window.location.replace(process.env.VUE_APP_Backed_URL)
    //     return;
    // }
    // else{
    //     return Promise.reject(error);
    // }

    return Promise.reject(error);

    
  });

export  default  Axios