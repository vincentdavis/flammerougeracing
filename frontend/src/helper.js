export function status_color(status_code) {
  if (status_code == '400' || status_code == '409') {
    return 'error'
  }
  return 'success'
}

export function exception_rest_api_handler(message) {
  if (typeof message == 'object') {
    var str = ''
    for (var p in message) {
      if (Object.prototype.hasOwnProperty.call(message, p)) {
        str += String(p).toLocaleUpperCase() + ':' + message[p] + '\n'
      }
    }
    return str
  }
  return message
}

export function extract_api_data(value) {
  let formData = new FormData()
  for (var data of value) {
    console.log(data)

    if (data.dbfield && (data.value || data.value == false)) {
      // formData[data.dbfield] = data.value
      if (String(typeof data.value) != 'object') {
        formData.append(data.dbfield, data.value)
      } else {
        try {
          for (var object of data.value) {
            console.log(object)
            formData.append('attachments', object)
          }
        } catch (err) {
          console.error(err)
        }
      }
    }
  }
  console.log(formData)
  return formData
}
