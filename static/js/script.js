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
  movieSelect.addEventListener('change', updateTotalPrice);
  seatsInput.addEventListener('input', updateTotalPrice);

  // Get the query parameter from the URL
  const urlParams = new URLSearchParams(window.location.search);
  const selectedMovieTitle = urlParams.get('movie_title');

  // Set the selected option in the dropdown
  if (selectedMovieTitle) {
      const option = [...movieSelect.options].find(option => option.text === selectedMovieTitle);

      if (option) {
          option.selected = true;
      }
  }

  // Initial update of total price
  updateTotalPrice();
});