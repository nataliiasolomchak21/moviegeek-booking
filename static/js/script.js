document.addEventListener("DOMContentLoaded", function() {
    const movieSelect = document.getElementById('movie');
    const seatsInput = document.getElementById('seats');
    const totalPriceSpan = document.getElementById('total-price');

    // Function to enforce the number of seats between 1 and 8
    function validateSeats() {
        let numSeats = parseInt(seatsInput.value) || 1;

        // Ensure numSeats is between 1 and 8
        numSeats = Math.max(1, Math.min(8, numSeats));

        // Update input value
        seatsInput.value = numSeats;

        // Update total price
        updateTotalPrice();
    }

    // Update total price when movie or seats are changed
    function updateTotalPrice() {
        const selectedMovie = movieSelect.options[movieSelect.selectedIndex];
        const moviePrice = selectedMovie.getAttribute('data-price');
        const numSeats = parseInt(seatsInput.value) || 1;
        const totalPrice = (moviePrice * numSeats).toFixed(2);
        totalPriceSpan.textContent = totalPrice;
    }

    // Attach input event listener directly to seatsInput
    if (seatsInput) {
        seatsInput.addEventListener('input', validateSeats);
        seatsInput.addEventListener('change', validateSeats); 
    }

    // Attach change event listener to movieSelect
    if (movieSelect) {
        movieSelect.addEventListener('change', updateTotalPrice);
    }

    // Initial update of total price
    updateTotalPrice();
});
