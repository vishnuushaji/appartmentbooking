// File: static/js/select2_init.js

$(document).ready(function() {
    // Initialize Select2 for the number of guests dropdown
    $('#num_guests').select2({
        tags: true,
        placeholder: 'Select number of guests',
        minimumResultsForSearch: -1 // Hide the search box
    });
});
