# News Glorious News
![News Glorious News logo](assets/ngn-youtube-thumbnail.png)

--- 
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Figma](https://img.shields.io/badge/figma-%23F24E1E.svg?style=for-the-badge&logo=figma&logoColor=white) ![Canva](https://img.shields.io/badge/Canva-%2300C4CC.svg?style=for-the-badge&logo=Canva&logoColor=white) ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white) ![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)


![Static Badge](https://img.shields.io/badge/She_Codes_Australia-purple?style=for-the-badge)


[![MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

[About](#about) ✦ [Project Requirements](#project-requirements) ✦ [Features](#features) ✦ [Resources](#resources) ✦ [License](#license) ✦ [Contact](#contact)

---

## About
This project is a news app created using Django. Once running, the site allows you to view stories written by authors, create your own account and write your own stories. 

A full list of [features](#features) can be found below. 

To see a full video of the website walk through, click [here](https://youtu.be/0_TCeW0NVMw)

This project was created as part of She Codes Australia Plus Program, December 2023.

Starter code can be found [here](https://github.com/SheCodesAus/plus-django-news-project-template)


## How To Run This Code
*Please note this instructions are for MAC users.*
1. Clone repo
2. Create virtual environment (venv)

    `python -m venv venv`
3. Initialise repo

    `git init`
4. Activate venv

    `source venv/bin/activate`
5. Download the requirements

    `python -m pip install -r requirements.txt`
6. Migrate the database 

    `python manage.py loaddata news`

7. Run server

    `python manage.py runserver`

8. Enjoy browsing the stories.


## Database Schema!
![News Glorious News Database Schema](assets/ngn_database_schema.png)

## Features

*Order stories by date*

![gif showing the stories listed in reverse publishing order ](assets/story_order.gif)


*Styled "new story" form with the ability to upload image URLs to the story. Users can select their publish date and time*
![Add Story form](assets/add_story.png)

*Log-in. Logout available in the nav on all pages.*
![Login form](assets/login.png)

*User profile page*
![user profile](assets/user_profile.png)

*"Create Account" page*
!["Create Account" page](assets/create_account.png)

*View stories by author*

![Author specific stories](assets/author_stories.gif)

*"Log-in" button only visible when no user is logged in*

*"Write New Story" functionality only available when user is logged in*
![Nav bar changes when logged in](assets/write_story_btn.png)


*"Log-out" buttononly visible when a user is logged in*
![Nav bar changes when not logged in](assets/login-btn.png)


*Ability to update and delete stories when the author is logged in*
![Ability to update and delete stories](assets/update_delete_story_btns.png)

![Update story form](assets/update_story.png)
![Delete story form](assets/delete_story.png)


*Ability to update and delete user information*
![Update user form](assets/update_account.png)
![Delete user form](assets/delete_account.png)

## Future Developments
1. Add categories to the stories and allow the user to search for stories bycategory.
2. Add the ability to “favourite” stories and see a page with your favouritestories.


## Resources
https://www.learningaboutelectronics.com/Articles/How-to-add-search-functionality-to-a-website-in-Django.php#google_vignette

https://medium.com/@tech-learner/upload-images-in-database-using-django-dc652941122b

## License

This project is using the following license:

**MIT**

For further information regarding the license, please follow the link below:
https://opensource.org/licenses/MIT

---

## Contact

If you have any further questions, please contact via email or github.

<a href="mailto:caoimhejyoti@gmail.com"><img alt="Link to email contact address" src="https://img.shields.io/badge/email-D14836?style=for-the-badge" target="_blank" /></a> <a href="https://github.com/caoimhejyoti"><img alt="badge for GitHub" src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white" target="_blank" /></a>
