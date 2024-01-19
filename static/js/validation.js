$(document).ready(function() {
    // Custom validation method for letters only
    jQuery.validator.addMethod("lettersonlys", function(value, element) {
        return this.optional(element) || /^[a-zA-Z ]*$/.test(value);
    });

    // Initialize jQuery Validation Plugin
    $("#bookingForm").validate({
        onkeyup: false,
        onfocusout: function(element, event) {
            this.element(element);
        },
        rules: {
            name: {
                required: true,
                minlength: 3,
                lettersonlys: true
            },
            email: {
                required: true,
                email: true
            },
            num_guests: {
                required: true,
                min: 1
            },
            booking_date: {
                required: true
            }
        },
        messages: {
            name: {
                required: "Please enter your name",
                minlength: "Name must be at least 3 characters",
                lettersonlys: "Please enter only letters in the name"
            },
            email: {
                required: "Please enter your email address",
                email: "Please enter a valid email address"
            },
            num_guests: {
                required: "Please enter the number of guests",
                min: "Number of guests must be at least 1"
            },
            booking_date: {
                required: "Please select a booking date"
            }
        },
        submitHandler: function(form) {
            // Handle form submission here
            form.submit();
        }
    });
});
