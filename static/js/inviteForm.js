import $ from 'jquery'

$( document ).ready(function() {
  $('#div_id_course').hide()

  $('#id_roles_3').change(function(){
    if (!this.checked) {
      $('#div_id_course').hide()
    } else {
      $('#div_id_course').show()
    }
  });
});
