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
| As a user I can reset my password by entering my email so that I can recover access if forgotten. | ![screenshot](documentation/readme_files/password-reset-user-story.png) |
| As a user I can select a movie, date, time, and up to 8 seats so that I can book tickets and see them in "My bookings". | ![screenshot](documentation/readme_files/booking-feature.png) |
| As a user I can edit or delete my existing bookings on my profile so that I can manage my tickets. (Edit) | ![screenshot](documentation/readme_files/edit-booking-feature.png) |
| As a user I can edit or delete my existing bookings on my profile so that I can manage my tickets. (Delete) | ![screenshot](documentation/readme_files/delete-booking-feature.png) |
| As a user I can view information about movies so that I can choose movie to book tickets to. | ![screenshot](documentation/readme_files/movies-home-page-user-story.png) |
| As a user I can view my profile containing my details so that I can confirm my account information. | ![screenshot](documentation/readme_files/profile-with-bookings-feature.png) |
| As a a logged in user I can log out so that I can securely end my session. | ![screenshot](documentation/readme_files/log-out-feature.png) |
| As a user, I can see customized and informative error pages for 404 and 500 errors so that I understand what happened and can take appropriate action. | ![screenshot](documentation/readme_files/404-error-page.png) |
| As a user, I can see customized and informative error pages for 404 and 500 errors so that I understand what happened and can take appropriate action. | ![screenshot](documentation/readme_files/500-error-page.png) |
| As a site owner/administrator I can create, read, update and delete movies so that I can manage showtime content. (Create) | ![screenshot](documentation/testing_files/create-admin.png) |
| As a site owner/administrator I can create, read, update and delete movies so that I can manage showtime content. (Read) | ![screenshot](documentation/testing_files/read-admin.png) |
| As a site owner/administrator I can create, read, update and delete movies so that I can manage showtime content. (Update) | ![screenshot](documentation/testing_files/update-admin.png) |
| As a site owner/administrator I can create, read, update and delete movies so that I can manage showtime content. (Delete) | ![screenshot](documentation/testing_files/delete-admin.png) |

## Validator Testing

### HTML

[W3C validation](https://validator.w3.org/) was used to check the markup validity of html file.

<details><summary><b>Home page (base.html and index.html)</b></summary>

![Home page](documentation/testing_files/home-page-w3c-validator.png)
</details>
<details><summary><b>Profile page (profile.html)</b></summary>

![Profile page](documentation/testing_files/profile-page-w3c-validator.png)
</details>
<details><summary><b>Booking (booking.html)</b></summary>

![Booking](documentation/testing_files/make-booking-w3c-validator.png)
</details>
<details><summary><b>Edit booking (edit_booking.html)</b></summary>

![Edit booking](documentation/testing_files/edit-booking-w3c-validator.png)
</details>
<details><summary><b>Booking confirmation (boooking_confirmation.html)</b></summary>

![Booking confirmation](documentation/testing_files/booking-confirmation-w3c-validator.png)
</details>
<details><summary><b>Password Reset (password_reset.html)</b></summary>

![Password Reset page](documentation/testing_files/password-reset-input-email-w3c-validator.png)
</details>
<details><summary><b>Password Reset Done(password_reset_done.html)</b></summary>

![Password Reset](documentation/testing_files/link-password-reset-sent-w3c-validator.png)
</details>
<details><summary><b>Password Reset From Key (password_reset_from_key.html)</b></summary>

![Password Reset](documentation/testing_files/change-password-w3c-validator.png)
</details>
<details><summary><b>Password Reset From Key Done(password_reset_from_key_done.html)</b></summary>

![Password Reset](documentation/testing_files/password-is-changed-w3c-validator.png)
</details>

The rest of the pages and folders that are in Github like: socialaccount, etc. weren't used by me and thus weren't validated.

### CSS

[Jigsaw](https://jigsaw.w3.org/css-validator/) was used to check the validity of css file.

<details><summary><b>style.css</b></summary>

![Css](documentation/testing_files/css-validator.png)
</details>

### JavaScript

[JSHint](https://jshint.com/) was used for validation.

<details><summary><b>script.js</b></summary>

![JS](documentation/testing_files/script-js-file-validation.png)
</details>
<details><summary><b>base.js</b></summary>

![JS](documentation/testing_files/base-js-validator.png)
</details>
<details><summary><b>booking.js</b></summary>

![JS](documentation/testing_files/booking-js-validator.png)
</details>

No errors in all the files.

### Python

[CI Python Linter](https://pep8ci.herokuapp.com/) was used to check the validity of python files.

<details><summary><b>asgi.py</b></summary>

![Python](documentation/testing_files/asgi-python.png)
</details>
<details><summary><b>wsgi.py</b></summary>

![Python](documentation/testing_files/wsgi-python.png)
</details>
<details><summary><b>urls.py (moviegeek)</b></summary>

![Python](documentation/testing_files/urls-moviegeek-python.png)
</details>
<details><summary><b>urls.py (booking)</b></summary>

![Python](documentation/testing_files/urls-booking-python.png)
</details>
<details><summary><b>views.py (moviegeek)</b></summary>

![Python](documentation/testing_files/views-moviegeek-python.png)
</details>
<details><summary><b>views.py (booking)</b></summary>

![Python](documentation/testing_files/views-booking-python.png)
</details>
<details><summary><b>test_forms.py</b></summary>

![Python](documentation/testing_files/test-forms-python.png)
</details>
<details><summary><b>test_models.py</b></summary>

![Python](documentation/testing_files/test-models-python.png)
</details>
<details><summary><b>test_views.py</b></summary>

![Python](documentation/testing_files/test-views-python.png)
</details>
<details><summary><b>forms.py</b></summary>

![Python](documentation/testing_files/forms-python.png)
</details>
<details><summary><b>models.py</b></summary>

![Python](documentation/testing_files/models-python.png)
</details>
<details><summary><b>admin.py</b></summary>

![Python](documentation/testing_files/admin-python.png)
</details>
<details><summary><b>apps.py</b></summary>

![Python](documentation/testing_files/apps-python.png)
</details>

## Unit Testing

### Coverage

In order to run the tests, I ran the following command in the terminal each time:

`python3 manage.py test name-of-app `

To create the coverage report, I would then run the following commands:

`coverage run --source=name-of-app manage.py test`

`coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

`coverage html`

`python3 -m http.server`

#### Booking app

12 tests were ran.

![Coverage](documentation/testing_files/coverage.png)

## Error Handling

### Error Pages Testing

<details><summary><b>500 Internal Server Error</b></summary>

![Error page](documentation/readme_files/500-error-page.png)
</details>

To test if the 500 page is working, I tried to reset the password and because at that time I haven't add my credentials to Config Vars on Heroku, it was showing 500 error page.

<details><summary><b>404 Page Not Found</b></summary>

![Error page](documentation/readme_files/404-error-page.png)
</details>

To test if the 404 page is working, I just typed in a non-existent url.

## Manual Testing

![Screenshot](documentation/testing_files/manual-testing-one.png)
![Screenshot](documentation/testing_files/manual-testing-two.png)
![Screenshot](documentation/testing_files/manual-testing-three.png)
![Screenshot](documentation/testing_files/manual-testing-four.png)
![Screenshot](documentation/testing_files/manual-testing-five.png)
![Screenshot](documentation/testing_files/manual-testing-six.png)

### SEO

Meta tags were included in a head of base.html file to tell the search engines and users more about the website and the information it contains.

![SEO](documentation/testing_files/seo.png)

### Accessibility

To ensure that the website was accessible to all users the following steps were taken:

* All the images has clear alt attribute that explains what it is about.
* Aria-labels were included to all the internal and external links to provide the purpose for them for screen readers.

### Lighthouse

After deploying to Heroku, the lighthouse for error pages is not loaded.

##### Mobile

| Page | Size | Screenshot |
| ---  | ---  | --- |
| Home | Mobile | ![screenshot](documentation/testing_files/home-page-lighthouse-mobile.png) |
| Profile | Mobile | ![screenshot](documentation/testing_files/profile-lighthouse-mobile.png) |
| Booking | Mobile | ![screenshot](documentation/testing_files/booking-lighthouse-mobile.png) |
| Edit booking | Mobile | ![screenshot](documentation/testing_files/edit-booking-lighthouse-mobile.png) |
| Sign Up | Mobile | ![screenshot](documentation/testing_files/signup-lighthouse-mobile.png) |
| Log In | Mobile | ![screenshot](documentation/testing_files/login-lighthouse-mobile.png) |
| Log Out | Mobile | ![screenshot](documentation/testing_files/logout-lighthouse-mobile.png) |
| Booking confirmation | Mobile | ![screenshot](documentation/testing_files/booking-confirmation-lighthouse-mobile.png) |
| Password Reset | Mobile | ![screenshot](documentation/testing_files/password-reset-lighthouse-mobile.png) |
| Password Reset Done | Mobile | ![screenshot](documentation/testing_files/password-reset-done-lighthouse-mobile.png) |
| Password Reset From Key | Mobile | ![screenshot](documentation/testing_files/password-reset-from-key-lighthouse-mobile.png) |
| Password Reset From Key Done | Mobile | ![screenshot](documentation/testing_files/password-reset-from-key-lighthouse-mobile.png) |

##### Desktop

| Page | Size | Screenshot |
| ---  | ---  | --- |
| Home | Desktop | ![screenshot](documentation/testing_files/home-page-lighthouse-desktop.png) |
| Profile | Desktop | ![screenshot](documentation/testing_files/profile-lighthouse-desktop.png) |
| Booking | Desktop | ![screenshot](documentation/testing_files/booking-lighthouse-desktop.png) |
| Edit booking | Desktop | ![screenshot](documentation/testing_files/edit-booking-lighthouse-desktop.png) |
| Sign Up | Desktop | ![screenshot](documentation/testing_files/signup-lighthouse-desktop.png) |
| Log In | Desktop | ![screenshot](documentation/testing_files/login-lighthouse-desktop.png) |
| Log Out | Desktop | ![screenshot](documentation/testing_files/logout-lighthouse-desktop.png) |
| Booking confirmation | Desktop | ![screenshot](documentation/testing_files/booking-confirmation-lighthouse-desktop.png) |
| Password Reset | Desktop | ![screenshot](documentation/testing_files/password-reset-lighthouse-desktop.png) |
| Password Reset Done | Desktop | ![screenshot](documentation/testing_files/password-reset-done-lighthouse-desktop.png) |
| Password Reset From Key | Desktop | ![screenshot](documentation/testing_files/password-reset-from-key-lighthouse-desktop.png) |
| Password Reset From Key Done |Desktop | ![screenshot](documentation/testing_files/password-reset-from-key-done-lighthouse-desktop.png) |

### Responsiveness

Responsiveness is tested on various devices such as:

<details><summary><b>Samsung Galaxy S8+</b></summary>

![Screenshot](documentation/testing_files/samsung-responsive.png)
</details>
<details><summary><b>Samsung Galaxy A34</b></summary>

![Screenshot](documentation/testing_files/samsung-a34-responsive.jpg)
</details>
<details><summary><b>Oppo A12</b></summary>

![Screenshot](documentation/testing_files/oppo-responsive.jpg)
</details>
<details><summary><b>Xiaomi 12T Pro</b></summary>

![Screenshot](documentation/testing_files/xiaomi-responsive.jpg)
</details>
<details><summary><b>IPad</b></summary>

![Screenshot](documentation/testing_files/ipad-responsive.png)
</details>
<details><summary><b>Acer Nitro</b></summary>

![Screenshot](documentation/testing_files/chrome.png)
</details>

### Browser compatibility

| Browser | Fail/Pass | Screenshot |
| ---  | ---  | --- |
| Chrome | Pass | ![screenshot](documentation/testing_files/chrome.png) |
| Edge | Pass | ![screenshot](documentation/testing_files/edge.png) |
| Opera | Pass | ![screenshot](documentation/testing_files/opera.png) |
| Firefox | Pass | ![screenshot](documentation/testing_files/firefox.png) |

## Bugs

### Solved

* The information about the booking when click on "Edit" button was not displayed properly. I fixed by adding `"date:"Y-m-d""` and `"date:"H:i""` to `form.instance.date` and `form.instance.time`

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

* I had a problem with navbar toggle still appearing on 1024x768 size, even with `display: none` for `(min-width: 992px)`, so I fixed it by adding `(min-width: 1024px)` to media queries. It still can be visible a little bit if you are testing sizes manually.
* The "Change Password" input and labels were suppose to go one after another but they are next to each other, and although I tried to modify it using different styles, it still doesn't work.

![Bug](documentation/testing_files/password-reset-bug.png)

* I have a problem with the number input in booking.html, although I put max and min value in the input when you manually entering the numbers, you can enter any number you want. You can't book the seats as their is validation present.

![Bug](documentation/testing_files/number-input-bug.png)

* To test if the 403 page is working, I logged in as a user Grace and click on "Edit" button on one of her bookings, then I copied that the link of that page, log out as Grace and log in as another user called Michael, then I pasted in the link that I copied before and see if the user "Michael" can edit booking of the user "Grace". It was showing me 403 error page, as it's forbidden access and one user can't edit the booking of another. But now it's showing me 404 error page or 500 error page if the user tries to paste in the link without being logged in and signed up.

![Bug](documentation/testing_files/error-page-bug.png)
