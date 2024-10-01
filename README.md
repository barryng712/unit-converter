# Unit Converter

## Overview
Unit Converter is a web application that allows users to convert between different units of measurement. Currently, it supports conversions for length, weight, and temperature.

## Features
- Convert between various units of length
- Convert between different weight units
- Convert between temperature scales (Celsius, Fahrenheit, Kelvin)
- User-friendly interface with separate tabs for each conversion category
- Responsive design for both desktop and mobile devices

## Technology Stack
- Backend: Python with Flask framework
- Frontend: HTML, CSS, JavaScript
- Template Engine: Jinja2

## Project Structure
- `app.py`: Main application file containing route definitions and conversion logic
- `templates/`: Directory containing HTML templates
  - `layout.html`: Base template for all pages
  - `index.html`: Home page template
  - `length.html`, `weight.html`, `temperature.html`: Category-specific conversion templates
  - `result.html`: Template for displaying conversion results
- `static/`: Directory for static assets
  - `styles.css`: CSS file for styling the application

## How to Use
1. Select a conversion category (Length, Weight, or Temperature) from the tabs.
2. Enter the value you want to convert.
3. Choose the unit you're converting from and the unit you want to convert to.
4. Click the "Convert" button to see the result.

## Setup and Installation
1. Clone the repository
2. Install the required dependencies (Flask)
3. Run the application using `python app.py`
4. Access the application in your web browser at `http://localhost:5000`

## Future Enhancements
- Add more conversion categories (e.g., volume, area)
- Implement user accounts for saving favorite conversions
- Add a history feature to track recent conversions
- Integrate an API for real-time currency conversion

src: https://roadmap.sh/projects/unit-converter
