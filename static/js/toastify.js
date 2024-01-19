document.addEventListener('DOMContentLoaded', function () {
    Toastify({
        text: "Successfull",
        duration: 3000,
        gravity: "top", // or "bottom"
        position: "right", // or "center" or "right"
        offset: {
            x: 50, // horizontal offset
            y: 10  // vertical offset
        },
        style: {
            background: "linear-gradient(to right, #ff9900, #ff0000)", 
        },
        onClick: function() {
            // Your callback function after click
        }
    }).showToast();
});
