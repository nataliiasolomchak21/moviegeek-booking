# MovieGeek Booking Website

MovieGeek Booking Website is a full-stack application created using HTML, CSS, JS, Python, Django and Bootstrap. It is a movie ticket booking web application that allows users to view showtimes and book tickets for 4 featured new release movies. Customers can select a movie, showtime, number of seats, and complete booking checkout. The site provides an easy way to reserve seats and books tickets online.

View the live project

Screenshot

## Table of Contents

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

### Agile Methodology

## UI

### Design

### Colour Palette

![Colour Palette](documentation/readme_files/colour-palette.png)

For this project, I chose these colors to be presented in my colour palette as they have a positive affect on the user experince.

![Colour Palette](documentation/readme_files/colour-palette-two.png)

I also used black, white and green colours mostly for text or as a background colours. RGB colours such as rgba(0,0,0,0.65), rgba (255, 255, 255, .6), and rgba(0, 0, 0, .3) were used for an overlay.

### Typography

For this project I used Montserrat font family as I thought it was a readable font and would be beneficial to user experience.

## Features

### Existing Features

### Features Left to Implement

## Error Handling

## Technologies Used

### Logic

* [Figma](https://www.figma.com/) was used to create the final design of a website.
* [Font Awesome](https://fontawesome.com/) was used for social media icons in the footer.
* [Iconify](https://iconify.design/) was used for Question Marl icon in the header.
* [Favicon](https://favicon.io/) was used for favicons.
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

## Deployment

Right after finishing the Django setup, the app was deployed to Heroku for the first time to confirm all was working as expected.

## Database (ElephangSQL)

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

## Cloudinary

1. Navigate to https://cloudinary.com/ and log in to your account.
2. Navigate to dashboard/console https://console.cloudinary.com/console/ and copy API Enviroment variable starting with "cloudinary://".
3. Paste copied url into env.py file as CLOUDINARY_URL value and save the file.

```
os.environ["CLOUDINARY_URL"] = "cloudinary://yourAPIEnviromentvariable"
```

## Django secret key

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

### Media

### Code

## Acknowledgements

