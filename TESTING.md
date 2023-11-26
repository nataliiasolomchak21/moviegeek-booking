# MovieGeek Booking Website

Back to [README](README.md)

## Testing Overview

## Table of Contents

- [User Story Tests](#user-story-tests)
- [Validator Testing](#validator-testing)
    - [HTML](#html)
    - [CSS](#css)
    - [JS](#javascript)
    - [Python](#python)
- [Unit Testing](#unit-testing)
    - [Coverage](#coverage)
- [Error Handling](#error-handling)
- [Manual Testing](#manual-testing)
    - [SEO](#seo)
    - [Accessibility](#accessibility)
        - [Lighthouse](#lighthouse)
        - [Responsiveness](#responsiveness)
        - [Browser compatibility](#browser-compatibility)
- [Bugs](#bugs)
    - [Solved](#solved)
    - [Unsolved](#unsolved)

## User Story Tests

| User Story | Screenshot |
| --- | --- |
| As a user I can access main pages and features through the header and footer so that I can easily navigate the site (Authenticated User) | ![screenshot](documentation/readme_files/header-authenticated-user-feature.png) |
| As a user I can access main pages and features through the header and footer so that I can easily navigate the site (Non-Authenticated User) | ![screenshot](documentation/readme_files/header-non-authenticated-user-feature.png) |
| As a user I can access main pages and features through the header and footer so that I can easily navigate the site (Footer) | ![screenshot](documentation/readme_files/footer-feature.png) |
| As a new user, I can sign up with form validation so that I can create a new account to book movies. | ![screenshot](documentation/readme_files/sign-up-feature.png) |
| As a user I can login so that I can access my account. | ![screenshot](documentation/readme_files/log-in-feature.png) |
| As a user I can select a movie, date, time, and up to 8 seats so that I can book tickets and see them in "My bookings". | ![screenshot](documentation/readme_files/booking-feature.png) |
| As a user I can edit or delete my existing bookings on my profile so that I can manage my tickets. (Edit) | ![screenshot](documentation/readme_files/edit-booking-feature.png) |
| As a user I can edit or delete my existing bookings on my profile so that I can manage my tickets. (Delete) | ![screenshot](documentation/readme_files/delete-booking-feature.png) |
| As a user I can view information about movies so that I can choose movie to book tickets to. | ![screenshot](documentation/readme_files/movies-home-page-user-story.png) |
| As a user I can view my profile containing my details so that I can confirm my account information. | ![screenshot](documentation/readme_files/profile-with-bookings-feature.png) |
| As a a logged in user I can log out so that I can securely end my session. | ![screenshot](documentation/readme_files/log-out-feature.png) |
| As a site owner/administrator I can create, read, update and delete movies so that I can manage showtime content. (Create) | ![screenshot](documentation/testing_files/create-admin.png) |
| As a site owner/administrator I can create, read, update and delete movies so that I can manage showtime content. (Read) | ![screenshot](documentation/testing_files/read-admin.png) |
| As a site owner/administrator I can create, read, update and delete movies so that I can manage showtime content. (Update) | ![screenshot](documentation/testing_files/update-admin.png) |
| As a site owner/administrator I can create, read, update and delete movies so that I can manage showtime content. (Delete) | ![screenshot](documentation/testing_files/delete-admin.png) |

## Validator Testing

### HTML

<details><summary><b>base.html</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>

<details><summary><b>index.html</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>
<details><summary><b>booking.html</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>
<details><summary><b>booking_confirmation.html</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>
<details><summary><b>edit_booking.html</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>
<details><summary><b>profile.html</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>
<details><summary><b>signup.html</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>
<details><summary><b>login.html</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>
<details><summary><b>logout.html</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>

### CSS

<details><summary><b>style.css</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>

### JavaScript

<details><summary><b>script.js</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>

### Python

<details><summary><b>logout.html</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>

## Unit Testing

### Coverage

## Error Handling

### Error Pages Testing

<details><summary><b>403 Forbidden</b></summary>

![Error page](documentation/readme_files/403-error-page.png)
</details>

To test if the 403 page is working, I logged in as a user Grace and click on "Edit" button on one of her bookings, then I copied that the link of that page, log out as Grace and log in as another user called Michael, then I pasted in the link that I copied before and see if the user "Michael" can edit booking of the user "Grace". It showed me 403 error page, as it's forbidden access and one user can't edit the booking of another.

<details><summary><b>500 Internal Server Error</b></summary>

![Error page](documentation/readme_files/500-error-page.png)
</details>

To test if the 500 page is working, I tried to reset the password and because at that time I haven't add my credentials to Config Vars on Heroku, it was showing 500 error page.

<details><summary><b>404 Page Not Found</b></summary>

![Error page](documentation/readme_files/404-error-page.png)
</details>

To test if the 404 page is working, I just typed in a non-existent url.

## Manual Testing

### SEO

Meta tags were included in a head of base.html file to tell the search engines and users more about the website and the information it contains.

![SEO](documentation/testing_files/seo.png)

### Accessibility

To ensure that the website was accessible to all users the following steps were taken:

* All the images has clear alt attribute that explains what it is about.
* Aria-labels were included to all the internal and external links as well as buttons to provide the purpose for them for screen readers.

#### Lighthouse

#### Responsiveness

#### Browser compatibility

## Bugs

### Solved

* The information about the booking when click on "Edit" button was not displayed properly. I fixed by adding `"date:"Y-m-d""` and `"date:"H:i""` to form.instance.date and fomr.instance.time

![Bug](documentation/testing_files/edit-booking-bug.png)

* I changed `alert.close()` to `messages.remove()` in js code for Bootstrap alert messages as it was throwing an error in the console.

![Bug](documentation/testing_files/error-messages-bug.png)

* Bootstrap alert messages were also hidden under my header element and I fixed it by adding `z-index: 1000` to the container they are in.

* In edit_booking.html where the user was manually entering the number of tickets, the `total-price` was showing `NaN` first if there is no numbers in the input. I fixed by adding `data-price="{{ movie.price }}"` to my template and modifying js code for that.

```javascript
// Update total price when movie or seats are changed
  function updateTotalPrice() {
      const selectedMovie = movieSelect.options[movieSelect.selectedIndex];
      const moviePrice = selectedMovie.getAttribute('data-price');
      const numSeats = seatsInput.value;
      const totalPrice = (moviePrice * numSeats).toFixed(2);
      totalPriceSpan.textContent = totalPrice;
  }
```

### Unsolved

* I had a problem with navbar toggle still appearing on 1024x768 size, even with `display: none` for `(min-width: 992px)`, so I fixed it by adding `(min-width: 1024px)` to media queries. It still can be visible a little bit if you are testing sizez manually.