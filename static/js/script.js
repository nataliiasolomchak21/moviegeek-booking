// Inside your JavaScript code where the user selects a movie
document.getElementById('movie').addEventListener('change', function() {
    // Get the selected movie element
    const selectedMovieElement = this.options[this.selectedIndex];

    // Get the movie ID from the data-movie-id attribute
    const selectedMovieId = selectedMovieElement.getAttribute('data-movie-id');

    // Set the value of the hidden field
    document.getElementById('selected-movie').value = selectedMovieId;
});

// Add the click event listener for the "Book" button.
document.querySelector('.book-btn').addEventListener('click', () => {
    // Optionally, you can add some additional logic here
    console.log('Book button clicked!');
});

document.getElementById('booking-form').addEventListener('submit', (event) => {
    event.preventDefault();  // Prevent the default form submission
    console.log('Form submitted!');
});
