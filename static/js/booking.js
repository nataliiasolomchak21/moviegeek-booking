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