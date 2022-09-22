$.get('https://stefanbohacek.com/hellosalut/?lang=fr', function (data) {
  $('#hello').append(data.hello);
});
