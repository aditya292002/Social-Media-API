import os
import constants
from openai import OpenAI
from icecream import ic 
import time

os.environ["OPENAI_API_KEY"] = constants.OPENAI_APIKEY
client = OpenAI()



# MCQ Generator Assistant
assistant_id = 'asst_1MbhtKBV5G9Pi5LCu2Dk8kCM'





"""

Transform Data into Interactive Experiences
Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging multiple-choice questions effortlessly.

s
About WitQuiz Whiz
Unlock the potential of your data with WitQuiz Whiz. Seamlessly convert PDFs and website content into dynamic, interactive learning experiences.

Our user-friendly interface, coupled with advanced data extraction capabilities, makes quiz creation a breeze. Elevate engagement, promote interactive learning, and make your content come alive with WitQuiz Whiz.Transform Data into Interactive Experiences
Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging multiple-choice questions effortlessly.

s
About WitQuiz Whiz
Unlock the potential of your data with WitQuiz Whiz. Seamlessly convert PDFs and website content into dynamic, interactive learning experiences.

Our user-friendly interface, coupled with advanced data extraction capabilities, makes quiz creation a breeze. Elevate engagement, promote interactive learning, and make your content come alive with WitQuiz Whiz.Transform Data into Interactive Experiences
Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging multiple-choice questions effortlessly.

s
About WitQuiz Whiz
Unlock the potential of your data with WitQuiz Whiz. Seamlessly convert PDFs and website content into dynamic, interactive learning experiences.

Our user-friendly interface, coupled with advanced data extraction capabilities, makes quiz creation a breeze. Elevate engagement, promote interactive learning, and make your content come alive with WitQuiz Whiz.Transform Data into Interactive Experiences
Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging multiple-choice questions effortlessly.

s
About WitQuiz Whiz
Unlock the potential of your data with WitQuiz Whiz. Seamlessly convert PDFs and website content into dynamic, interactive learning experiences.

Our user-friendly interface, coupled with advanced data extraction capabilities, makes quiz creation a breeze. Elevate engagement, promote interactive learning, and make your content come alive with WitQuiz Whiz.Transform Data into Interactive Experiences
Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging multiple-choice questions effortlessly.

s
About WitQuiz Whiz
Unlock the potential of your data with WitQuiz Whiz. Seamlessly convert PDFs and website content into dynamic, interactive learning experiences.

Our user-friendly interface, coupled with advanced data extraction capabilities, makes quiz creation a breeze. Elevate engagement, promote interactive learning, and make your content come alive with WitQuiz Whiz.Transform Data into Interactive Experiences
Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging multiple-choice questions effortlessly.

s
About WitQuiz Whiz
Unlock the potential of your data with WitQuiz Whiz. Seamlessly convert PDFs and website content into dynamic, interactive learning experiences.

Our user-friendly interface, coupled with advanced data extraction capabilities, makes quiz creation a breeze. Elevate engagement, promote interactive learning, and make your content come alive with WitQuiz Whiz.
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
        crossorigin="anonymous">
    <title>About Us</title>
    <style>
        /* Add your custom styles here */
        body {
            padding: 20px;
        }

        .container {
            max-width: 800px;
        }

        h1 {
            color: #007bff;
        }

        p {
            font-size: 1.2em;
        }

        img {
            max-width: 100%;
            height: auto;
            margin-bottom: 20px;
        }


        header.jumbotron {
            color: #ffffff;
            text-align: center;
            padding: 100px 0;
        }

        header.jumbotron h1 {
            font-size: 3.5rem;
        }

        header.jumbotron p {
            font-size: 1.5rem;
        }

        section#about {
            padding: 50px 0;
        }

        footer {
            background-color: #343a40;
            color: #ffffff;
            padding: 20px 0;
        }
        h1,p {
            color: black;
        }

        .app-img {
            margin-left: 10rem;
            width: 50%;
            height: auto;
        }
        .navbar-collapse {
            font-size: large;
        }


    </style>
    </style>
</head>

<body>

    <!-- Navigation Bar -->
    <nav class="navbar fixed-top navbar-expand-lg navbar-light">
        <a class="navbar-brand" href="#" style="margin-left: 0.5rem; color: brown;">  Wits<span><b>Quiz</b></span>  Whiz </span></a>
    
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
    
        <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link" href="/">Home</a>
            </li>
    
            <li class="nav-item">
              <a class="nav-link" href="/about-us">About</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/auth/">Login</a>
            </li>
          </ul>
        </div>
      </nav>

    <!-- Hero Section -->
    <header class="jumbotron">
        <div class="container text-center">
            <h1 class="display-3">Transform Data into Interactive Experiences</h1>
            <p class="lead">Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging
                multiple-choice questions effortlessly.</p>
            <a class="btn btn-primary btn-lg" href="/auth/" role="button">Try it</a>
        </div>s
    </header>

    <div class="container">
        <h1>About Us</h1>

        <img src="your-company-logo.png" alt="Company Logo">

        <p>Welcome to WitQuiz Whiz ! We are a passionate team dedicated to [describe your mission or purpose].
            Our journey began [mention a brief history or founding story]. At [Your Company Name], we strive to [highlight
            your core values and goals].</p>

        <p>Our Team:</p>

        <!-- Team Member 1 -->
        <div class="card mb-3">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="team-member1.jpg" alt="Team Member 1" class="img-fluid">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">John Doe</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Team Member 2 -->
        <div class="card mb-3">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="team-member2.jpg" alt="Team Member 2" class="img-fluid">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">Jane Smith</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add more team members as needed -->

        <p>Contact us at <a href="mailto:info@example.com">info@example.com</a> for more information.</p>
    </div>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>

</body>

</html>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
        crossorigin="anonymous">
    <title>About Us</title>
    <style>
        /* Add your custom styles here */
        body {
            padding: 20px;
        }

        .container {
            max-width: 800px;
        }

        h1 {
            color: #007bff;
        }

        p {
            font-size: 1.2em;
        }

        img {
            max-width: 100%;
            height: auto;
            margin-bottom: 20px;
        }


        header.jumbotron {
            color: #ffffff;
            text-align: center;
            padding: 100px 0;
        }

        header.jumbotron h1 {
            font-size: 3.5rem;
        }

        header.jumbotron p {
            font-size: 1.5rem;
        }

        section#about {
            padding: 50px 0;
        }

        footer {
            background-color: #343a40;
            color: #ffffff;
            padding: 20px 0;
        }
        h1,p {
            color: black;
        }

        .app-img {
            margin-left: 10rem;
            width: 50%;
            height: auto;
        }
        .navbar-collapse {
            font-size: large;
        }


    </style>
    </style>
</head>

<body>

    <!-- Navigation Bar -->
    <nav class="navbar fixed-top navbar-expand-lg navbar-light">
        <a class="navbar-brand" href="#" style="margin-left: 0.5rem; color: brown;">  Wits<span><b>Quiz</b></span>  Whiz </span></a>
    
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
    
        <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link" href="/">Home</a>
            </li>
    
            <li class="nav-item">
              <a class="nav-link" href="/about-us">About</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/auth/">Login</a>
            </li>
          </ul>
        </div>
      </nav>

    <!-- Hero Section -->
    <header class="jumbotron">
        <div class="container text-center">
            <h1 class="display-3">Transform Data into Interactive Experiences</h1>
            <p class="lead">Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging
                multiple-choice questions effortlessly.</p>
            <a class="btn btn-primary btn-lg" href="/auth/" role="button">Try it</a>
        </div>s
    </header>

    <div class="container">
        <h1>About Us</h1>

        <img src="your-company-logo.png" alt="Company Logo">

        <p>Welcome to WitQuiz Whiz ! We are a passionate team dedicated to [describe your mission or purpose].
            Our journey began [mention a brief history or founding story]. At [Your Company Name], we strive to [highlight
            your core values and goals].</p>

        <p>Our Team:</p>

        <!-- Team Member 1 -->
        <div class="card mb-3">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="team-member1.jpg" alt="Team Member 1" class="img-fluid">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">John Doe</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Team Member 2 -->
        <div class="card mb-3">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="team-member2.jpg" alt="Team Member 2" class="img-fluid">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">Jane Smith</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add more team members as needed -->

        <p>Contact us at <a href="mailto:info@example.com">info@example.com</a> for more information.</p>
    </div>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>

</body>

</html>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
        crossorigin="anonymous">
    <title>About Us</title>
    <style>
        /* Add your custom styles here */
        body {
            padding: 20px;
        }

        .container {
            max-width: 800px;
        }

        h1 {
            color: #007bff;
        }

        p {
            font-size: 1.2em;
        }

        img {
            max-width: 100%;
            height: auto;
            margin-bottom: 20px;
        }


        header.jumbotron {
            color: #ffffff;
            text-align: center;
            padding: 100px 0;
        }

        header.jumbotron h1 {
            font-size: 3.5rem;
        }

        header.jumbotron p {
            font-size: 1.5rem;
        }

        section#about {
            padding: 50px 0;
        }

        footer {
            background-color: #343a40;
            color: #ffffff;
            padding: 20px 0;
        }
        h1,p {
            color: black;
        }

        .app-img {
            margin-left: 10rem;
            width: 50%;
            height: auto;
        }
        .navbar-collapse {
            font-size: large;
        }


    </style>
    </style>
</head>

<body>

    <!-- Navigation Bar -->
    <nav class="navbar fixed-top navbar-expand-lg navbar-light">
        <a class="navbar-brand" href="#" style="margin-left: 0.5rem; color: brown;">  Wits<span><b>Quiz</b></span>  Whiz </span></a>
    
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
    
        <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link" href="/">Home</a>
            </li>
    
            <li class="nav-item">
              <a class="nav-link" href="/about-us">About</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/auth/">Login</a>
            </li>
          </ul>
        </div>
      </nav>

    <!-- Hero Section -->
    <header class="jumbotron">
        <div class="container text-center">
            <h1 class="display-3">Transform Data into Interactive Experiences</h1>
            <p class="lead">Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging
                multiple-choice questions effortlessly.</p>
            <a class="btn btn-primary btn-lg" href="/auth/" role="button">Try it</a>
        </div>s
    </header>

    <div class="container">
        <h1>About Us</h1>

        <img src="your-company-logo.png" alt="Company Logo">

        <p>Welcome to WitQuiz Whiz ! We are a passionate team dedicated to [describe your mission or purpose].
            Our journey began [mention a brief history or founding story]. At [Your Company Name], we strive to [highlight
            your core values and goals].</p>

        <p>Our Team:</p>

        <!-- Team Member 1 -->
        <div class="card mb-3">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="team-member1.jpg" alt="Team Member 1" class="img-fluid">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">John Doe</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Team Member 2 -->
        <div class="card mb-3">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="team-member2.jpg" alt="Team Member 2" class="img-fluid">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">Jane Smith</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add more team members as needed -->

        <p>Contact us at <a href="mailto:info@example.com">info@example.com</a> for more information.</p>
    </div>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>

</body>

</html>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
        crossorigin="anonymous">
    <title>About Us</title>
    <style>
        /* Add your custom styles here */
        body {
            padding: 20px;
        }

        .container {
            max-width: 800px;
        }

        h1 {
            color: #007bff;
        }

        p {
            font-size: 1.2em;
        }

        img {
            max-width: 100%;
            height: auto;
            margin-bottom: 20px;
        }


        header.jumbotron {
            color: #ffffff;
            text-align: center;
            padding: 100px 0;
        }

        header.jumbotron h1 {
            font-size: 3.5rem;
        }

        header.jumbotron p {
            font-size: 1.5rem;
        }

        section#about {
            padding: 50px 0;
        }

        footer {
            background-color: #343a40;
            color: #ffffff;
            padding: 20px 0;
        }
        h1,p {
            color: black;
        }

        .app-img {
            margin-left: 10rem;
            width: 50%;
            height: auto;
        }
        .navbar-collapse {
            font-size: large;
        }


    </style>
    </style>
</head>

<body>

    <!-- Navigation Bar -->
    <nav class="navbar fixed-top navbar-expand-lg navbar-light">
        <a class="navbar-brand" href="#" style="margin-left: 0.5rem; color: brown;">  Wits<span><b>Quiz</b></span>  Whiz </span></a>
    
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
    
        <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link" href="/">Home</a>
            </li>
    
            <li class="nav-item">
              <a class="nav-link" href="/about-us">About</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/auth/">Login</a>
            </li>
          </ul>
        </div>
      </nav>

    <!-- Hero Section -->
    <header class="jumbotron">
        <div class="container text-center">
            <h1 class="display-3">Transform Data into Interactive Experiences</h1>
            <p class="lead">Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging
                multiple-choice questions effortlessly.</p>
            <a class="btn btn-primary btn-lg" href="/auth/" role="button">Try it</a>
        </div>s
    </header>

    <div class="container">
        <h1>About Us</h1>

        <img src="your-company-logo.png" alt="Company Logo">

        <p>Welcome to WitQuiz Whiz ! We are a passionate team dedicated to [describe your mission or purpose].
            Our journey began [mention a brief history or founding story]. At [Your Company Name], we strive to [highlight
            your core values and goals].</p>

        <p>Our Team:</p>

        <!-- Team Member 1 -->
        <div class="card mb-3">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="team-member1.jpg" alt="Team Member 1" class="img-fluid">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">John Doe</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Team Member 2 -->
        <div class="card mb-3">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="team-member2.jpg" alt="Team Member 2" class="img-fluid">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">Jane Smith</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add more team members as needed -->

        <p>Contact us at <a href="mailto:info@example.com">info@example.com</a> for more information.</p>
    </div>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>

</body>

</html>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
        crossorigin="anonymous">
    <title>About Us</title>
    <style>
        /* Add your custom styles here */
        body {
            padding: 20px;
        }

        .container {
            max-width: 800px;
        }

        h1 {
            color: #007bff;
        }

        p {
            font-size: 1.2em;
        }

        img {
            max-width: 100%;
            height: auto;
            margin-bottom: 20px;
        }


        header.jumbotron {
            color: #ffffff;
            text-align: center;
            padding: 100px 0;
        }

        header.jumbotron h1 {
            font-size: 3.5rem;
        }

        header.jumbotron p {
            font-size: 1.5rem;
        }

        section#about {
            padding: 50px 0;
        }

        footer {
            background-color: #343a40;
            color: #ffffff;
            padding: 20px 0;
        }
        h1,p {
            color: black;
        }

        .app-img {
            margin-left: 10rem;
            width: 50%;
            height: auto;
        }
        .navbar-collapse {
            font-size: large;
        }


    </style>
    </style>
</head>

<body>

    <!-- Navigation Bar -->
    <nav class="navbar fixed-top navbar-expand-lg navbar-light">
        <a class="navbar-brand" href="#" style="margin-left: 0.5rem; color: brown;">  Wits<span><b>Quiz</b></span>  Whiz </span></a>
    
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
    
        <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link" href="/">Home</a>
            </li>
    
            <li class="nav-item">
              <a class="nav-link" href="/about-us">About</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/auth/">Login</a>
            </li>
          </ul>
        </div>
      </nav>

    <!-- Hero Section -->
    <header class="jumbotron">
        <div class="container text-center">
            <h1 class="display-3">Transform Data into Interactive Experiences</h1>
            <p class="lead">Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging
                multiple-choice questions effortlessly.</p>
            <a class="btn btn-primary btn-lg" href="/auth/" role="button">Try it</a>
        </div>s
    </header>

    <div class="container">
        <h1>About Us</h1>

        <img src="your-company-logo.png" alt="Company Logo">

        <p>Welcome to WitQuiz Whiz ! We are a passionate team dedicated to [describe your mission or purpose].
            Our journey began [mention a brief history or founding story]. At [Your Company Name], we strive to [highlight
            your core values and goals].</p>

        <p>Our Team:</p>

        <!-- Team Member 1 -->
        <div class="card mb-3">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="team-member1.jpg" alt="Team Member 1" class="img-fluid">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">John Doe</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Team Member 2 -->
        <div class="card mb-3">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="team-member2.jpg" alt="Team Member 2" class="img-fluid">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">Jane Smith</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add more team members as needed -->

        <p>Contact us at <a href="mailto:info@example.com">info@example.com</a> for more information.</p>
    </div>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>

</body>

</html>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN"
        crossorigin="anonymous">
    <title>About Us</title>
    <style>
        /* Add your custom styles here */
        body {
            padding: 20px;
        }

        .container {
            max-width: 800px;
        }

        h1 {
            color: #007bff;
        }

        p {
            font-size: 1.2em;
        }

        img {
            max-width: 100%;
            height: auto;
            margin-bottom: 20px;
        }


        header.jumbotron {
            color: #ffffff;
            text-align: center;
            padding: 100px 0;
        }

        header.jumbotron h1 {
            font-size: 3.5rem;
        }

        header.jumbotron p {
            font-size: 1.5rem;
        }

        section#about {
            padding: 50px 0;
        }

        footer {
            background-color: #343a40;
            color: #ffffff;
            padding: 20px 0;
        }
        h1,p {
            color: black;
        }

        .app-img {
            margin-left: 10rem;
            width: 50%;
            height: auto;
        }
        .navbar-collapse {
            font-size: large;
        }


    </style>
    </style>
</head>

<body>

    <!-- Navigation Bar -->
    <nav class="navbar fixed-top navbar-expand-lg navbar-light">
        <a class="navbar-brand" href="#" style="margin-left: 0.5rem; color: brown;">  Wits<span><b>Quiz</b></span>  Whiz </span></a>
    
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
    
        <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <a class="nav-link" href="/">Home</a>
            </li>
    
            <li class="nav-item">
              <a class="nav-link" href="/about-us">About</a>
            </li>

            <li class="nav-item">
                <a class="nav-link" href="/auth/">Login</a>
            </li>
          </ul>
        </div>
      </nav>

    <!-- Hero Section -->
    <header class="jumbotron">
        <div class="container text-center">
            <h1 class="display-3">Transform Data into Interactive Experiences</h1>
            <p class="lead">Elevate learning with WitQuiz Whiz. Convert PDFs and website content into engaging
                multiple-choice questions effortlessly.</p>
            <a class="btn btn-primary btn-lg" href="/auth/" role="button">Try it</a>
        </div>s
    </header>

    <div class="container">
        <h1>About Us</h1>

        <img src="your-company-logo.png" alt="Company Logo">

        <p>Welcome to WitQuiz Whiz ! We are a passionate team dedicated to [describe your mission or purpose].
            Our journey began [mention a brief history or founding story]. At [Your Company Name], we strive to [highlight
            your core values and goals].</p>

        <p>Our Team:</p>

        <!-- Team Member 1 -->
        <div class="card mb-3">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="team-member1.jpg" alt="Team Member 1" class="img-fluid">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">John Doe</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Team Member 2 -->
        <div class="card mb-3">
            <div class="row g-0">
                <div class="col-md-4">
                    <img src="team-member2.jpg" alt="Team Member 2" class="img-fluid">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">Jane Smith</h5>
                        <p class="card-text">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod
                            tempor incididunt ut labore et dolore magna aliqua.</p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Add more team members as needed -->

        <p>Contact us at <a href="mailto:info@example.com">info@example.com</a> for more information.</p>
    </div>

    <!-- Bootstrap JS and dependencies -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"
        integrity="sha384-C6RzsynM9kWDrMNeT87bh95OGNyZPhcTNXj1NW7RuBCsyN/o0jlpcV8Qyq46cDfL"
        crossorigin="anonymous"></script>

</body>

</html>


"""