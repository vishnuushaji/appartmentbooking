$(document).ready(function() {
    // Initialize Summernote
    $('#review').summernote();
});

// Flag to check if the toast has been shown
var isToastShown = false;

// Function to show Toastify message
function showToast() {
    if (!isToastShown) {
        Toastify({
            text: "Submitted",
            duration: 3000,
            gravity: "top", // or "bottom"
            position: "center", // or "center" or "right"
            style: {
                background: "linear-gradient(to right, #ff9900, red)", // Change the gradient colors
            },
            onClick: function() {
                // Your callback function after click
            }
        }).showToast();

        // Set the flag to true after showing the toast
        isToastShown = true;
    }
}
