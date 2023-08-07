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

  $('#language_code').keypress(function (event) {
    if (event.which === 13) { // Check if the pressed key is ENTER (key code 13)
      getTargetLanguageTxt();
    }
  });
});
