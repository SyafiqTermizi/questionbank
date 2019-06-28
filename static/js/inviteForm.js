import $ from 'jquery'

$( document ).ready(function() {
  $('#div_id_course').hide()

  $('input[type=checkbox][value=2]').change(function(){
    if (!this.checked) {
      $('#div_id_course').hide()
    } else {
      $('#div_id_course').show()
    }
  });
});
