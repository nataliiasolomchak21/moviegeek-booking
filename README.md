# MovieGeek Booking Website

MovieGeek Booking Website is a full-stack application created using HTML, CSS, JS, Python, Django and Bootstrap. It is a movie ticket booking web application that allows users to view showtimes and book tickets for 4 featured new release movies. Customers can select a movie, showtime, number of seats, and complete booking checkout. The site provides an easy way to reserve seats and books tickets online.

View the live project

Screenshot

## Table of Contents

- [UX](#ux)
    - [Target Audience](#target-audience)
    - [Key Project Goals](#key-project-goals)
    - [User Stories](#user-stories)
    - [Agile Methodology](#agile-methodology)
- [UI](#ui)
    - [Initial Design](#design)
    - [Colour Palette](#colour-palette)
    - [Typography](#typography)
- [ERD (Entity-Relationship Diagram)](#erd-entity-relationship-diagram)
- [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
- [Technologies Used](#technologies-used)
- [Deployment](#deployment)
    - [Database (ElephangSQL)](#database-elephangsql)
    - [Cloudinary](#cloudinary)
    - [Django secret key](#django-secret-key)
    - [Heroku](#heroku)
    - [How to Fork the Github Repository](#how-to-fork-the-github-repository)
    - [How to Clone the Github Repository](#how-to-clone-the-github-repository)
- [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
- [Acknowledgements](#acknowledgements)

## UX

### Target Audience

The primary audience is moviegoers and cinephiles looking to conveniently book tickets online for upcoming movie releases. This includes casual movie fans, friends/family planning a night out, as well as frequent moviegoers who attend opening weekends. The focus is providing quick booking for the latest films.

### Key Project Goals

- Allow users to search for and view information about movies playing, including title, showtimes, ticket prices, and seat availability.
- Provide users with a personal profile where they can view their past and current bookings.
- Integrate a ticketing system that updates seat availability in real-time as tickets are booked.
- Implement a seamless mobile-friendly booking flow for smartphone users.
- Build an admin portal where staff can manage movie and showtime listings.

### User Stories

#### Site-visitor

> *"As a user I can access main pages and features through the header and footer so that I can easily navigate the site"*
>
> *"As a new user, I can sign up with form validation so that I can create a new account to book movies."*
>
> *"As a user I can login so that I can access my account."*
>
> *"As a user I can select a movie, date, time, and up to 8 seats so that I can book tickets and see them in "My bookings."*
>
> *"As a user I can edit or delete my existing bookings on my profile so that I can manage my tickets."*
>
> *"As a user I can view information about movies so that I can choose movie to book tickets to."*
>
> *"As a user I can view my profile containing my details so that I can confirm my account information."*
>
> *"As a a logged in user I can log out so that I can securely end my session."*

#### Site-admin

> *"As a site owner/administrator I can create, read, update and delete movies so that I can manage showtime content.*

### Agile Methodology

For this project I used Agile methodology. Agile methodology is a project management approach that prioritizes cross-functional collaboration and continuous improvement. It divides projects into smaller phases and guides teams through cycles of planning, execution, and evaluation.

#### Kanban Board

![Kanban Board](documentation/readme_files/kanban-board.png)

This a visual representaion of my Kanban Board during the project. In addition to three essential columns, I created a column "Won't Have For This Project" for the user stories that I wasn't able to implement.
My process is divided into 3 iterations (Milestones). Once the iteration is done, all of the user stories from that iteration are going to "Done" column. If any of the user stories from a particular iteration weren't implemented, they are going back to the Product Backlog.

#### Iterations

<details><summary><b>Iteration 1</b></summary>

![Iteration One](documentation/readme_files/iteration-one.png)
</details>

The first iteration is focused on creating the look of the website (home page and profile page) and part of the CRUD functionality.

<details><summary><b>Iteration 2</b></summary>

![Iteration Two](documentation/readme_files/iteration-two.png)
</details>

The second iteration is focused on creating site navigation, the rest of the CRUD functionality as well as profile page features.

<details><summary><b>Iteration 3</b></summary>

![Iteration Three](documentation/readme_files/iteration-three.png)
</details>

The third iteration is focused on authorisation.

#### Issues

I had 15 issues: 

* 3 epics:
    * Admin Site
    * Booking
    * Authorisation
* 7 must-haves
    * Admin
    * Sign Up
    * Log In
    * Log Out
    * Site Navigation
    * Create/View booking
    * Edit/Delete booking
* 4 should-haves 
    * Main page
    * Home page
    * Profile Details
    * Update/Delete Profile
* 4 could-haves
    * Verify Email
    * Password Reset
    * Profile Picture Update/Upload
    * Error pages

[View here](https://github.com/nataliiasolomchak21/moviegeek-booking/issues)

#### Labels, Issues and MoSCoW prioritization

<details><summary><b>Labels</b></summary>

![Labels](documentation/readme_files/labels.png)
</details>

The labels were given to each user stories based on MoSCoW prioritization which is a technique used in project management, particularly in the context of Agile and Scrum methodologies, to prioritize and categorize requirements or features.

<details><summary><b>Issues</b></summary>

![Issues](documentation/readme_files/issues.png)
</details>

- **Must Have**: features we absolutely need for the project to succeed (*max 60% of stories*)
- **Should Have**:  important features that make the project better but aren't absolutely necessary (*the rest ~20% of stories*)
- **Could Have**: features that, if included, would have a relatively small impact on the project(*20% of stories*)
- **Won't Have**: are not considered a priority for this iteration and are deferred for future consideration

#### Won't have for this deployment

## UI

### Initial Design

After discussing wireframes with my mentor, we determined that visual mockups were not necessary for this project. Since my designs thoroughly document the website's functionality and features in detail, comprehensive wireframes would be redundant.

The sizes that were used for the design:

* Mobile (360x740)
* Tablet (768x1024)
* Desktop (1440x1024)

#### Header (Authenticated User)

<details><summary><b>Header (Authenticated User)</b></summary>

![Header (Authenticated User)](documentation/readme_files/header-authenticated-user-design.png)
</details>

#### Header (Non-Authenticated User)
<details><summary><b>Header (Non-Authenticated User)</b></summary>

![Header (Non-Authenticated User)](documentation/readme_files/header-non-authenticated-user-design.png)
</details>

Things I have changed: The header looks a little bit different as for the mobile size I used a Bootstrap collapsed navbar instead of using my own.

#### Footer
<details><summary><b>Footer</b></summary>

![Footer](documentation/readme_files/footer-design.png)
</details>

Things I have changed: I got rid of logo and added "Admin Only" button to the footer.

#### Sign Up page
<details><summary><b>Sign Up page</b></summary>

![Sign Up page](documentation/readme_files/sign-up-page-design.png)
</details>

Things I have changed: I've added "Password Rules" for better UX as well as for the desktop size I got rid of the image.

#### Log In page
<details><summary><b>Log In page</b></summary>

![Log In page](documentation/readme_files/log-in-page-design.png)
</details>

Things I have changed: I also got rid of the image for the desktop size and changed "Email address" field to "Username".

#### Home page (Authenticated User)
<details><summary><b>Home page (Authenticated User)</b></summary>

![Home page (Authenticated User)](documentation/readme_files/home-page-design.png)
</details>

#### Home page (Non-Authenticated User)
<details><summary><b>Home page (Non-Authenticated User)</b></summary>

![Home page (Non-Authenticated User)](documentation/readme_files/home-page-no-authenticated-user-design.png)
</details>

Nothing was changed here.

#### Booking page
<details><summary><b>Booking page</b></summary>

![Booking page](documentation/readme_files/booking-one-design.png)
</details>
<details><summary><b>Booking page</b></summary>

![Booking page](documentation/readme_files/booking-two-design.png)
</details>

Things I have changed: I wanted to created a real ciname experience by letting users choose the seats for the movie but because I wasn't able to implement that functionality, I stick to the number input (users can choose the number of seats they want to book). Also, for the date and time I did a dropdown menu.

#### Booking Confirmation page
<details><summary><b>Booking Confirmation page</b></summary>

![Booking Confirmation page)](documentation/readme_files/booking-confirmation-design.png)
</details>

Nothing was changed here.

#### Profile page (with bookings)
<details><summary><b>Profile page (with bookings)</b></summary>

![Profile page (with bookings)](documentation/readme_files/profile-with-bookings-design.png)
</details>

Things I have changed: The "My bookings" section looks the same the only thing is that the user can't edit or delete their profile.

#### Profile page (without bookings)
<details><summary><b>Profile page (without bookings)</b></summary>

![Profile page (without bookings)](documentation/readme_files/profile-without-bookings-design.png)
</details>

Nothing was changed here.

#### Log Out page
<details><summary><b>Log Out page</b></summary>

![Log Out page](documentation/readme_files/log-out-design.png)
</details>

Things I have changed: I wanted to make the log out modal first but then stick to the html template for that.

#### Messages
<details><summary><b>Sign Up</b></summary>

![Messages](documentation/readme_files/successful-sign-up-message-design.png)
</details>

<details><summary><b>Log In</b></summary>

![Messages](documentation/readme_files/successful-log-in-message-design.png)
</details>

<details><summary><b>Edit booking</b></summary>

![Messages](documentation/readme_files/successful-edit-message-design.png)
</details>

<details><summary><b>Delete booking</b></summary>

![Messages](documentation/readme_files/successful-delete-message-design.png)
</details>

<details><summary><b>Log Out</b></summary>

![Messages](documentation/readme_files/successful-log-out-message-design.png)
</details>

Things I have changed: I wanted to create my own messages but to save some time I used Bootstrap alert messages.

#### Modals
<details><summary><b>Delete booking confirmation</b></summary>

![Modals](documentation/readme_files/delete-booking-modal-design.png)
</details>

Things I have changed: Although I wanted to create my own modal, I used Bootstrap modal as it (again) was less time-consuming.

### Colour Palette

![Colour Palette](documentation/readme_files/colour-palette.png)

For this project, I chose these colors to be presented in my colour palette as they have a positive affect on the user experince.

![Colour Palette](documentation/readme_files/colour-palette-two.png)

I also used black, white and green colours mostly for text or as a background colours. RGB colours such as rgba(0,0,0,0.65), rgba (255, 255, 255, .6), and rgba(0, 0, 0, .3) were used for an overlay.

### Typography

For this project I used Montserrat font family as I thought it was a readable font and would be beneficial to user experience.

## ERD (Entity-Relationship Diagram)

I've used Entity-Relationship Diagram(ERD) Entity-Relationship Diagram represent the relationships between entities, more specifically the relationships between my "Movie" and "Booking" models as well as Django built-in User model.

This ERD conveys that:

- Each Movie can have multiple Booking entries (one-to-many).
- Each User can have multiple Booking entries (one-to-many).

![ERD](documentation/readme_files/er-diagram.png)

## Features

### Existing Features

The features that are presented are for desktop size.

#### Header (Authenticated User)

<details><summary><b>Header (Authenticated User)</b></summary>

![Header (Authenticated User)](documentation/readme_files/header-authenticated-user-feature.png)
</details>

If the user is authenticated, they will see Home, Profile and Log Out links in the navigation menu which gives them ability to go through the available movies and book them, go to their Profile page and see the bookings they have there or make a new one. They also can log out from their account and will be redirected to the Home page.

#### Header (Non-Authenticated User)
<details><summary><b>Header (Non-Authenticated User)</b></summary>

![Header (Non-Authenticated User)](documentation/readme_files/header-non-authenticated-user-feature.png)
</details>

If the user is not authenticated, they will see Home, Sign Up and Log In links in the navigation menu which gives them ability to go through the available movies and watch trailers, sign up as a new user or log in as an existing one.

#### Footer
<details><summary><b>Footer</b></summary>

![Footer](documentation/readme_files/footer-feature.png)
</details>

The footer includes links to the social media that each opens in a new tab and "Admin Only" button which is available only to the superuser/admin of the website.

#### Sign Up page
<details><summary><b>Sign Up page</b></summary>

![Sign Up page](documentation/readme_files/sign-up-feature.png)
</details>

The sign up page gives user ability to enter their information(username, email address, password and confirm password) in order to authorise them as a website user and give them ability to create, view, edit and delete their bookings.

#### Log In page
<details><summary><b>Log In page</b></summary>

![Log In page](documentation/readme_files/log-in-feature.png)
</details>

The log in page gives user ability to enter their information(username and password) in order to get access to their existing profile and give them ability to create, view, edit and delete their bookings.

#### Home page (Authenticated User)
<details><summary><b>Home page (Authenticated User)</b></summary>

![Home page (Authenticated User)](documentation/readme_files/home-page-authenticated-user-feature.png)
</details>

If the user is authenticated, they will see the welcome message with their username and "My bookings" button that will redirect them to their Profile page where they can manage their bookings. They have an ability to go through the available movies and book them as well as watch trailers.

#### Home page (Non-Authenticated User)
<details><summary><b>Home page (Non-Authenticated User)</b></summary>

![Home page (Non-Authenticated User)](documentation/readme_files/home-page-non-authenticated-user-feature.png)
</details>

If the user is not authenticated, they will see the general welcome message and information about the website. They can watch trailers but don't have an ability to book movies and if they click on "Book Now" button will redicted to Log In page.

#### Booking page (Create booking)
<details><summary><b>Booking page</b></summary>

![Booking page](documentation/readme_files/booking-feature.png)
</details>

The booking page includes a dropdown with four movies to choose from, the numbers of seats you can select, date and time, and price which populates depending on how many tickets the user will choose with "Book" button.

#### Booking Confirmation page
<details><summary><b>Booking Confirmation page</b></summary>

![Booking Confirmation page)](documentation/readme_files/booking-confirmation-feature.png)
</details>

After the user did their booking, they will be redirected to the "Booking confirmation" page that confirm that their booking was successful. They also have an option to either see their newly creayed booking in their Profile page or go back to the Home page.

#### Profile page (with bookings) (View booking)
<details><summary><b>Profile page (with bookings)</b></summary>

![Profile page (with bookings)](documentation/readme_files/profile-with-bookings-feature.png)
</details>

The Profile page with existing bookings includes information about the user (username and email address) as well as information about their bookings. Each booking has the date and time of movie being screened, movie title, an amount of seats, price as well as "Edit" and "Delete" buttons so that the user can change their booking or delete it completely.

#### Profile page (without bookings)
<details><summary><b>Profile page (without bookings)</b></summary>

![Profile page (without bookings)](documentation/readme_files/profile-without-bookings-feature.png)
</details>

The Profile page without bookings includes the text with "No bookings yet" and "Book a Movie" button that gives the user an ability to book a movie.

#### Edit booking
<details><summary><b>Edit booking</b></summary>

![Edit booking](documentation/readme_files/edit-booking-feature.png)
</details>

User can edit their booking and will be presented with a page identical to the Booking page but with functionality to change their booking and "Update" button to save their changes. The message about their booking being changed is displayed.

#### Delete booking
<details><summary><b>Delete booking</b></summary>

![Delete booking](documentation/readme_files/delete-booking-feature.png)
</details>

User can delet their booking and will be presented with a modal to confirm the delete process. The message about their booking being deleted is displayed.

#### Admin panel
<details><summary><b>Admin panel</b></summary>

![Admin panel](documentation/readme_files/admin-panel.png)
</details>

Although, the Django admin panel is not created by me, it's still plays the most important part for the website. In my admin panel, I have two models: Booking and Movie and I also use the default User model. I customize the admin title and header.

#### Log Out page
<details><summary><b>Log Out page</b></summary>

![Log Out page](documentation/readme_files/log-out-feature.png)
</details>

The Log Out page gives the user the ability to log out from their account. After logging out they will be redirected to the Home page.

#### Messages
<details><summary><b>Sign Up</b></summary>

![Messages](documentation/readme_files/signed-up-message.png)
</details>

<details><summary><b>Sign In (Log In)</b></summary>

![Messages](documentation/readme_files/logged-in-message.png)
</details>

<details><summary><b>Updated booking</b></summary>

![Messages](documentation/readme_files/updated-booking-message.png)
</details>

<details><summary><b>Deleted booking</b></summary>

![Messages](documentation/readme_files/deleted-booking-message.png)
</details>

<details><summary><b>Sign Out (Log Out)</b></summary>

![Messages](documentation/readme_files/signed-out-message.png)
</details>

Each of the alert messages being displayed when the various actions such as Sign In, Log In, Log Out, Create, Edit or Delete a booking is being done to give a visual feedback to the user. The user can close the message or it will dissapear in a few seconds.

#### Error pages
<details><summary><b>403 Forbidden</b></summary>

![Error page](documentation/readme_files/403-error-page.png)
</details>

<details><summary><b>500 Internal Server Error</b></summary>

![Error page](documentation/readme_files/500-error-page.png)
</details>

<details><summary><b>404 Page Not Found</b></summary>

![Error page](documentation/readme_files/404-error-page.png)
</details>

### Features Left to Implement

## Technologies Used

* [Figma](https://www.figma.com/) was used to create the final design of a website.
* [Font Awesome](https://fontawesome.com/) was used for social media icons in the footer.
* [Iconify](https://iconify.design/) was used for Question Marl icon in the header.
* [Favicon](https://favicon.io/) was used for favicons.
* [LucidChart](https://favicon.io/) was used for favicons.
* [Google Fonts](https://fonts.google.com/) was used to add specific font family to the stylesheet.
* [Adobe Color](https://color.adobe.com/create/color-wheel) was used to create a colour palette.
* [VSCode](https://code.visualstudio.com/) was used to code the website.
* [W3C validation](https://validator.w3.org/) was used to check the markup validity of html file.
* [Jigsaw](https://jigsaw.w3.org/css-validator/) was used to check the validity of css file.
* [JSHint](https://jshint.com/) was used to check the validity of css file.
* [Am I Responsive](https://ui.dev/amiresponsive) was used to get a screenshot of a final look of the website on various devices.
* [Github](https://github.com/) was used to store the code of the website.
* Chrome DevTools was used to check the responsiveness of the website as well as to debug it.
* Chrome's Developer Tool Lighthouse was used to check the performance of the website.

## Testing

All the information on testing is in [TESTING.md](TESTING.md)

## Deployment

Right after finishing the Django setup, the app was deployed to Heroku for the first time to confirm all was working as expected.

### Database (ElephangSQL)

1. Navitate to [ElephantSQL website](https://www.elephantsql.com/), log in to your account
2. Click “Create New Instance”.
3. Enter database name, leave plan field as it is. You can leave the Tags field blank.
4. Select region, click on "Review".
5. Check that your details are correct. Then click “Create instance”
6. Return to the ElephantSQL dashboard and click on the database instance name for this project.
7. Copy your ElephantSQL database URL using the Copy.
8. Paste this URL into env.py file as DATABASE_URL value and save the file.

```
os.environ["DATABASE_URL"] = "postgres://yourdatabaseURL"
```

### Cloudinary

1. Navigate to https://cloudinary.com/ and log in to your account.
2. Navigate to dashboard/console https://console.cloudinary.com/console/ and copy API Enviroment variable starting with "cloudinary://".
3. Paste copied url into env.py file as CLOUDINARY_URL value and save the file.

```
os.environ["CLOUDINARY_URL"] = "cloudinary://yourAPIEnviromentvariable"
```

### Django secret key

You need to include you Django secret key that you can generate using any of the Django secret keys generators online.
In order to protect django app secret key it was set as an enviroment variable and stored in env.py.

```
os.environ["SECRET_KEY"] = "yourSecretKey"
```
### Heroku

1. Log in to Heroku or create an account.
2. Navigate to your Heroku dashboard, click "New" and select "Create new app".
3. Enter a name for your app (can be a name of your project) and choose the region that suits best to your location.
4. Select "Settings" from the tabs.
5. Click "Reveal Config Vars".
6. These are:
CLOUDINARY_API_KEY - Get from Cloudinary.
DATABASE_URL - Get from your SQL provider.
DEBUG - Leave blank for False, any value for True.
DISABLE_COLLECTSTATIC - Set to '0' (without '')
SECRET_KEY - This is your Django project secret key, generated by your Django project. You can generate a new key that is different from your localhost version.
7. Select "Deploy" from the tabs.
8. Select "GitHub - Connect to GitHub" from deployment methods.
9. Click "Connect to GitHub" in the created section.
10. Search for the GitHub repository by name.
11. Click to 'Connect' to the relevant repo.
12. Either click ‘Enable Automatic Deploys’ for automatic deploys or ‘Deploy Branch’ to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
13. Click 'View' to view the deployed site.

### How to Fork the Github Repository

1. If you want to fork the repository log in to Github or create an account.
2. Locate to the repository for the project.
3. In the top right corner click on 'Fork' button. 
4. Now you have a copy of the original repository in your Github account.

### How to Clone the Github Repository

1. If you want to clone the repository log in to Github or create an account.
2. Go to the main page of the repository.
3. Click on '<> Code' and copy the URL from HTTPS.
4. Open Git Bash.
5. Change your current working directory to the location where you want your clone to be made.
6. Type 'git clone' into your terminal window, paste the URL you copied earlier and press Enter to create your local clone.

## Credits

### Content

* The definition of Agile Methodology was taken from [here](https://www.wrike.com/project-management-guide/faq/what-is-agile-methodology-in-project-management/).
* The text content for the Home section was created by me.
* Movies description was taken from IMDB website (in order):
  1. [Spider-Man: Across The Spider-Verse](https://www.imdb.com/title/tt9362722/?ref_=nv_sr_srsg_0_tt_8_nm_0_q_spider)
  2. [Barbie](https://www.imdb.com/title/tt1517268/?ref_=nv_sr_srsg_2_tt_3_nm_3_q_ba)
  3. [Mission Impossible: Dead Reckoning Part One](https://www.imdb.com/title/tt9603212/)
  4. [Oppenheimer](https://www.imdb.com/title/tt15398776/?ref_=nv_sr_srsg_0_tt_7_nm_1_q_opp)

### Media

* The hero image was taken from [here](https://www.pinterest.com.au/pin/589408669974067553/).
* The favicon image was taken from [here](https://www.goodgoodgood.co/articles/positive-words-that-start-with-m).
* Movies posters (in order):
  1. [Spider-Man: Across The Spider-Verse](https://www.imdb.com/title/tt9362722/)
  2. [Barbie](https://deadline.com/gallery/barbie-movie-posters/barbie-barbie_vert_tsr_w_talent_2764x4096_dom_rgb/)
  3. [Mission Impossible: Dead Reckoning Part One](https://www.imdb.com/title/tt9603212/)
  4. [Oppenheimer](https://www.imdb.com/title/tt15398776/)

### Code

* The initial deployment, js code for alert messages, information on how to create models as well as how to add authorisation to my project were taken from [Code Institute's I Think Therefore I Blog](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+FST101+2021_T1/courseware/b31493372e764469823578613d11036b/9236975633b64a12a61a00e0cca7c47d/)

## Acknowledgements

I express my sincere gratitude to my mentor, Dick Vlaanderen, for his invaluable assistance and feedback during the entire project. Additionally, I extend my thanks to our facilitator, Marko Tot, for his guidance on the material and practical advice. Special appreciation goes to my fellow groupmate, Gbemi Akadiri, for his steadfast help and support throughout the project.



