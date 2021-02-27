<h1 style="text-align=center;">Sophie Photograpy - Full Stack with Django Milestone Project</h1>

[View the live project here.](https://sophiephotography.herokuapp.com/)

This is the Full Stack project for Code Institute course.

<h2 style="text-align:center;"><img src="https://drive.google.com/file/d/1bzwBbpKRKGRlgpkS726B10TUgtbBYvdO/view?usp=sharing"></h2>

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the studio.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find examples of previous work.
        3. As a First Time Visitor, I want to look for testimonials to understand what their clients think of them and see if they are trusted. I also want to locate their social media links to see their followings on social media to determine how trusted and known they are.
        4. As a First Time Visitor, I want to be able to book a photoshoot session and understand how it works.
        5. I want to register an account, easily login or logout, receive a confirmation email after registering and have a personalized user profile.

  -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to check my past purchases.
        2. As a Returning Visitor, I want to find community links.
        3. As a Returning Visitor, I want to be able to order the photo sessions by price or by name.

    -   #### Frequent User Goals
        1. As a Frequent User, I want to check to see if there are any newly added photo sessions.
        2. As a Frequent User, I want to update my details on my profile.
        3. As a Frequent User, I want to get in touch with the Studio

-   ### Design

    -   #### General
        -   This Webapp with a simple language keeping the navbar menu on top when on desktop and on mobile activated by a hamburguer button style making the navigation very easy and accessible from anywhere. The Menu is dynamic showing only allowed options to regular or superuser (admin) users. The admin has the power to create Projects and assign to users. Also the admin can reset any user's password if necessary or modify the user to be another admin. After logged in the user is presented with the Dashboard that will list all projects and its related tickets.

    -   #### Colour Scheme
        -   The blue colour was chosen as the main tone as it is known to be a calming colour. The contrast ratio was taken in consideration to every person be able to read clearly.

    -   #### Typography
        -   The Roboto font is the default font used throughout the whole website with Sans Serif as the fallback font in case the font isn't being imported into the site correctly. Roboto is a clean font used frequently in Google ecosystem, so it is both attractive, appropriate and memorable.



   ### Wireframes

    -   Home Page Wireframe - [View](https://drive.google.com/file/d/1EV45ZmMr4QyCafh1h_XwiMk7pK8-Dxdc/view?usp=sharing)

    -   Home Page Wireframe JPG version - [View](https://drive.google.com/file/d/1oKXihibiugZ8QtmP7RD7DCeOKStWrmWa/view?usp=sharing)

    -   Website Logo Icon - [View](https://drive.google.com/file/d/13GM_sZ8SetQWAMI_kevy5dmUIaA5T0wZ/view?usp=sharing)

    
## Features

-   Responsive on all device sizes

-   Interactive elements

-   Parallax Effect on main page and Nabar.

-   AllAuth secure Login, User Registration with email confirmation.

-   Stripe Payments.


- ## Database Design

    -   ### General
        - The Database was laid with tables to reflect the need of the app at initial structure. It was taken in consideration that tables should be simple and data must be easy to retrieve and if necessary to expand for future improvements.
        
        <p style="align=center;"><img src="https://drive.google.com/file/d/1O3BKdAzqGi4NEmzwQIBWzQZj5cPbghNB/view?usp=sharing"></p><br>
        <h8>DB diagram created with <a href="https://dbdiagram.io/" target="_blank">DbDiagram.io</a></h8>

    -   DbDiagram.io Diagram - [View](https://dbdiagram.io/d/603a8b97fcdcb6230b21caad)



## Technologies Used


### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Frameworks, Libraries, APIs & Programs Used

1.  [Django](https://docs.djangoproject.com/en/3.1/)
    - Django Framework was used through the entire webapp to integrate the back-end with the front-end.
1.  [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1.  [Google Fonts](https://fonts.google.com/)
    - Google fonts were used to import the 'Roboto' font into the style.css file which is used on all pages throughout the project.
1.  [Font Awesome](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1.  [jQuery](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used to create the Parallax effect function and other JavaScript functions through the site.
1.  [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1.  [GitHub](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1.  [Affinity Photo](https://affinity.serif.com/en-us/photo/)
    - Photoshop was used to create the logo, resizing images and editing photos for the website.
1.  [Affinity Designer](https://affinity.serif.com/en-us/designer/)
    - Affinity Designer was used to create the [wireframe/mokup](https://drive.google.com/file/d/1oKXihibiugZ8QtmP7RD7DCeOKStWrmWa/view?usp=sharing) during the design process.
1.  [Db Diagram io](https://dbdiagram.io/)
    - Created the Database Schema with this very handy DB tool vizualization website.
1.  [SQLite](https://www.sqlite.org/index.html)
    - SQL Database delivered together with Django Framework used in the development phase.
1.  [PostgreSQL](https://www.postgresql.org/)
    - SQL Database used by Heroku plataform used in the deployment and live website. 
1.  [Heroku](https://heroku.com/)
    - Heroku was used to deploy the project and have the app live.
1.  [AWS](https://aws.amazon.com/)
    - Cloud Bucket used to keep static files and media of the website.
1.  [Visual Studio Code](https://code.visualstudio.com/)
    - Visual Studio Code was used to write the code.




## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate the page of the project to ensure there were no syntax errors.

-   [W3C Markup Validator](https://validator.w3.org/)
    -   The validator picked up 2 different errors and 1 warning on the first run. The errors and warning were corrected.
    -   Test passed with no Warnings or Errors.

-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    -   The validator found 1 Error and 493 Warnings in the Materialize CSS stylesheet. All other CSS were Valid.

-   [W3C Broken Link Checker](https://validator.w3.org/checklink?uri=https%3A%2F%2Fsbug-tracker.herokuapp.com%2F&hide_type=all&depth=&check=Check)
    -   The validator found 1 redirection link that is now corrected.

-   [JSHint](https://jshint.com/)
    -   There was missing one semicolon that was corrected.

-   [Google Chrome LightHouse](https://drive.google.com/file/d/167AAaRL9cYvp9ewtYhp4r7K49wcsjTnM/view?usp=sharing)
    -   It was pointed out security flaw using an older version of JQuery, score improved after update.
    -   It was pointed out to use rel="noopener" on links to external websites for security, score improved after including it.

-   [PEP8 Checker](http://pep8online.com/) - [Error results](https://drive.google.com/file/d/1bpk_cfYu6r4yHhpD8Dfy_MZ65r4BYKQB/view?usp=sharing)
    -   All warnings and lines out of PEP8 Style were corrected.



