<script>
    $(document).ready(function () {
        $('#bookingForm').validate({
            // Specify validation rules
            rules: {
                name: 'required',
                email: {
                    required: true,
                    email: true
                },
                num_guests: {
                    required: true,
                    min: 1
                },
                booking_date: 'required'
            },
            // Specify validation error messages
            messages: {
                name: 'Please enter your name',
                email: {
                    required: 'Please enter your email address',
                    email: 'Please enter a valid email address'
                },
                num_guests: {
                    required: 'Please enter the number of guests',
                    min: 'Number of guests must be at least 1'
                },
                booking_date: 'Please select a booking date'
            }
        }
        )};
    );
</script>
