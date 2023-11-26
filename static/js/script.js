document.addEventListener("DOMContentLoaded", function() {
  const movieSelect = document.getElementById('movie');
  const seatsInput = document.getElementById('seats');
  const totalPriceSpan = document.getElementById('total-price');

  // Update total price when movie or seats are changed
  function updateTotalPrice() {
      const selectedMovie = movieSelect.options[movieSelect.selectedIndex];
      const moviePrice = selectedMovie.getAttribute('data-price');
      const numSeats = seatsInput.value;
      const totalPrice = (moviePrice * numSeats).toFixed(2);
      totalPriceSpan.textContent = totalPrice;
  }

  // Attach event listeners
  if (movieSelect) {
    movieSelect.addEventListener('change', updateTotalPrice);
  }
  if (seatsInput) {
    seatsInput.addEventListener('input', updateTotalPrice);
  }
  // Initial update of total price
  updateTotalPrice();
});
