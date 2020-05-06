/* Trigger flash modal */
$(document).ready(function() {
    var messages = "{{ get_flashed_messages() }}";

    if (typeof messages != 'undefined' && messages != '[]') {
        $('.alert').alert()
    };
});