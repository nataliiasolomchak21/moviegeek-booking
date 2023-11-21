const movieSelect = document.getElementById("movie");
const seatsInput = document.getElementById("seats");
const totalPriceElement = document.getElementById("total-price");

// Set the default price
const defaultPrice = 12;

// Set default value for seats input
seatsInput.value = 1;

// Event listeners for changes in movie selection and seats input
movieSelect.addEventListener("change", updateTotalPrice);
seatsInput.addEventListener("input", updateTotalPrice);

// Initial update for default values
updateTotalPrice();

function updateTotalPrice() {
  const selectedSeats = parseFloat(seatsInput.value);

  // Calculate total price based on selected seats and movie price
  const totalPrice = selectedSeats * defaultPrice;

  // Update the total price in the UI
  totalPriceElement.textContent = totalPrice.toFixed(2);
}


