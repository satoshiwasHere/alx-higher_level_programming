$(document).ready(function () {
  function getTargetLanguageTxt () {
    const sourceLanguageCode = $('#language_code').val();
    const apiUrl = `https://hellosalut.stefanbohacek.dev/?lang=${sourceLanguageCode}`;

    $.get(apiUrl, function (data) {
      $('#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(function () {
    getTargetLanguageTxt();
  });
});
