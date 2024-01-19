// static/js/datepicker.js



$(document).ready(function(){
    $('.date-picker').datepicker({
        format: 'yyyy-mm-dd',
        todayBtn: 'linked',
        clearBtn: true,
        todayHighlight: true,
        autoclose: true
    });
});