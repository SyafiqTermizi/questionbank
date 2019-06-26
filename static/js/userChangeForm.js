import $ from 'jquery'

$( document ).ready(function() {
  if ($('#id_groups_2').is(':checked')) {
    $('#div_id_course').show()
  } else {
    $('#div_id_course').hide()
  }

  $('#id_groups_2').change(function(){
    if (!this.checked) {
      $('#div_id_course').hide()
    } else {
      $('#div_id_course').show()
    }
  });
});
