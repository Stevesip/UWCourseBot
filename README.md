# UWCourseBot

A Facebook Messenger Bot to help students get the most up to date and recent information about their courses.

## Motivation

This project first started as a hackathon idea for EngHack 2016. We decided to take a step forward to enhance this idea into a full project.

## Usage

Visit [UW Course Bot](https://www.facebook.com/UWCourseBot/) and request course information for any specific course.
- Uses [wit.ai](https://wit.ai/) to parse natural language into structured data to make API calls.
- Fetches the information from [UW Open Data API](https://uwaterloo.ca/api/).
- Parses the JSON return into viewable data for the user in the reply.
- Some sample inputs:
	* I want information on ECON101
	* When is CS240?
	* Who is teaching SCI238 this term?
	* *More example coming soon*


## API Reference

All API calls are made towards the University of Waterloo Open Data API.
See [Documentation](https://github.com/uWaterloo/api-documentation) for more information.
