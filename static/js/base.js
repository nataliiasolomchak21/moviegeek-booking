$(document).ready(function () {
  var currentPath = window.location.pathname;
  $("nav a").each(function () {
    var linkPath = $(this).attr("href");
    if (currentPath === linkPath && !$(this).hasClass("logo-link")) {
      $(this).addClass("active");
    }
  });
});

document.addEventListener("DOMContentLoaded", function () {
  setTimeout(function () {
    let messages = document.getElementById("msg");
    if (messages) {
      messages.remove();
    }
  }, 2500);
});
