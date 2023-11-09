// Select the container element and all the available seats (not occupied)
const container = document.querySelector('.seats-container');
const seats = document.querySelectorAll('.row .seat');
// Get the count and total elements
const count = document.getElementById('total-seats');
const total = document.getElementById('total-price');
// Get the select element for movie selection
const movieSelect = document.getElementById('movie');

// Initialize the UI
populateUI()
// Get the initial ticket price from the selected movie
let ticketPrice = +movieSelect.value;

// Save selected movie index and price to localStorage
function setMovieData(movieIndex, moviePrice) {
    localStorage.setItem('selectedMovieIndex', movieIndex);
    localStorage.setItem('selectedMoviePrice', moviePrice);
}

// Update count and total when seats are selected
function updateSelectedCount() {
    // Query select all the seats that have the 'selected' class
    const selectedSeats = document.querySelectorAll('.row .seat.selected');
    // Get the count of selected seats
    const selectedSeatsCount = selectedSeats.length;

    if (selectedSeatsCount > 8) {
        const overselectionMessage = document.createTextNode("You can select up to 8 seats only"); 
        document.body.appendChild(overselectionMessage);
    }

    // Create an array of the selected seats
    // Map each seat to its index
    // Loop through the array of selected seats, and find the index of each seat in the full seats array.
    // This returns a new array containing the indices of the selected seats.
    const seatsIndex = [...selectedSeats].map(function(seat) {
        return[...seats].indexOf(seat);
    })
    // Stringify and save to localStorage
    // Convert the array of indices to a JSON string, and save it to localStorage with the key 'selectedSeats'.
    localStorage.setItem('selectedSeats', JSON.stringify(seatsIndex));

    console.log(seatsIndex);
    // Update the count text
    count.innerText = selectedSeatsCount;
    // Calculate the total
    total.innerText = selectedSeatsCount * ticketPrice;
}

// Get data from localstorage and populate the ui
function populateUI() {
    // Get the selected seats from localStorage
    // Get the selectedSeats string from localStorage and parse it back into an array.
    const selectedSeats = JSON.parse(localStorage.getItem('selectedSeats'));
    // Check if seats were selected
    // If there are selected seats, continue to restore them.
    if (selectedSeats !== null && selectedSeats.length > 0) {
        // Loop through all seats
        // Loop through each seat element, also getting its index.
        seats.forEach((seat, index) => {
            // Check if seat index was selected
            // If the index exists in the selectedSeats array, it was previously selected.
            if (selectedSeats.indexOf(index) > -1) {
                // Add the 'selected' class to style the seat as selected.
                seat.classList.add('selected');
            }
        });
    }

    // Get selected movie index (Get the saved movie index.)
    const selectedMovieIndex = localStorage.getItem('selectedMovieIndex');
    // Set movie select index
    // If there is a saved index, set the select element's selected index.
    if(selectedMovieIndex !== null) {
        movieSelect.selectedIndex = selectedMovieIndex;
    }
}

// So in summary, it restores which seats were selected previously, and which movie was selected.

// movie select event
// Add event listener to movie select element
// This will run the code inside when the movie selection changes.
movieSelect.addEventListener('change', e => {
    // Get new ticket price
    // When the selection changes, get the new selected option's value (the ticket price) and update the ticketPrice variable.
    ticketPrice = +e.target.value;
    // Save movie data
    // Call the setMovieData function, passing the new selected index and price. This saves them to localStorage.
    setMovieData(e.target.selectedIndex, e.target.value);
    // Call the updateSelectedCount function to recalculate and update the count and total display with the new ticket price.
    updateSelectedCount();
});

// Add click event listener to the container element.
// This will run the code inside when a click happens in the container.
container.addEventListener('click', (e) => {
    // Check if click target is a seat and not occupied.
    // Only run the code if an available seat was clicked.
    if (e.target.classList.contains('seat') && !e.target.classList.contains('occupied')) {
        // Toggle the 'selected' class on the clicked seat.
        // This will add or remove the 'selected' class, to visually select/deselect it.
        e.target.classList.toggle('selected');
    }
    // Update the count and total.
    // Call the function to recount selected seats and update the total.
    updateSelectedCount();
});

updateSelectedCount();