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
  // Initial update of total price
  updateTotalPrice();
});

document.addEventListener("DOMContentLoaded", function() {
    // Get the query parameter from the URL
    const urlParams = new URLSearchParams(window.location.search);
    const selectedMovieTitle = urlParams.get('movie_title');

    // Set the selected option in the dropdown
    if (selectedMovieTitle) {
        const selectElement = document.getElementById('movie');
        const option = [...selectElement.options].find(option => option.text === selectedMovieTitle);

        if (option) {
            option.selected = true;
        }
    }
});

$(document).ready(function() {
    var currentPath = window.location.pathname;
    $('nav a').each(function() {
        var linkPath = $(this).attr('href');
        if (currentPath === linkPath && !$(this).hasClass('logo-link')) {
            $(this).addClass('active');
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
setTimeout(function () {
    let messages = document.getElementById('msg');
    if (messages) {
        messages.remove();
    }
}, 2500);
});

document.addEventListener("DOMContentLoaded", function() {
    // Add click event listener to all elements with the class "delete-btn"
    var deleteButtons = document.querySelectorAll(".delete-button");

    deleteButtons.forEach(function(button) {
        button.addEventListener("click", function() {
            // Retrieve data attributes
            var bookingId = button.getAttribute("data-booking-id");
            var deleteUrl = button.getAttribute("data-delete-url");

            // Redirect to the delete view
            window.location.href = deleteUrl.replace('0', bookingId);
        });
    });
});

