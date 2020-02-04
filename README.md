# World-views

## Description

- This app is used to display images from different locations and categories. 
- A user can click on an image to view the image details.
-  A user can also copy an image link.

## User Story

- As a user I can:

1. View different photos that interest them.
2. Click on a single photo to expand it and also view the details of the photo.
3. View the most recent posts.
4. Search for different categories of photos. (ie. Travel, Food).
5. Copy a link to the photo to share with my friends.
6. View photos based on the location they were taken.

## Running the Application

- create virtual enviroment:

    $ virtualenv virtual
    $ source virtual/bin/activate

- Installing Django and other Modules:

    $ pip install -r requirements.txt

- Run the application, in your terminal:

    $ python3.6 manage.py runserver

### Prerequisites

  * python3.6 
  * pip
  * postgres database
  * virtualenv
  * django

  ## BDD
  | Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display gallery page | **On page load** | Site description and gallery pictures |
| Display picture information | **Click gallery on picture** | Opens a modal that shows a large version of the picture and its details |
| Display picture categories | **Enter search term on the search bar** | Display search results if search term meets database categories |
| Display pictures from different location |**Click 'Location on the navigation bar**|Displays a select field that allows users to search for pictures from a specific country/location|

