$(document).ready(function () {
  var currentPath = window.location.pathname;
  // Iterate over each anchor element inside the navigation.
  $("nav a").each(function () {
    var linkPath = $(this).attr("href");
    // Check if the current path matches the link path and the anchor
    if (currentPath === linkPath && !$(this).hasClass("logo-link")) {
      $(this).addClass("active");
    }
  });
});

document.addEventListener("DOMContentLoaded", function () {
  // Set a timeout function to execute after 2500 milliseconds (2.5 seconds).
  setTimeout(function () {
    let messages = document.getElementById("msg");
    if (messages) {
      messages.remove();
    }
  }, 2500);
});
