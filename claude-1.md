# Task: Create Basic HTML Landing Page

## Objective
Create the initial `index.html` file for the Destiny API Tools project. This page will serve as the user's entry point and will contain a "Log In" button to initiate the Bungie.net authentication process.

## Project Context
The project is a new web application, "Destiny API Tools," which will allow users to interact with their Destiny 2 account data. This is the very first step in building the user interface. The project currently has no codebase, only API reference documentation.

## Required Resources
This task does not require any specific API endpoints or entities. It is purely a frontend setup task.

### Authentication
No authentication is required for this static page itself, but the page must include a button that will later be used to trigger the OAuth flow.

## Implementation Requirements
### Technical Specifications
- Create a single HTML5 file named `index.html`.
- The page should have a clear title, such as "Destiny API Tools".
- Include a main heading (`<h1>`) with the text "Welcome to Destiny API Tools".
- Add a paragraph (`<p>`) with a brief welcome message, inviting the user to log in to see their characters.
- Create a button with the text "Log In with Bungie.net". This button should have a unique ID (e.g., `login-button`) so it can be targeted by JavaScript later.
- Add a `div` element with a unique ID (e.g., `character-display`) that will be used later to display the character list. This `div` should be empty initially.
- Link to a non-existent `style.css` for styling and a `main.js` for JavaScript. We will create these files in subsequent tasks.

### File Structure
Create the following file in the project's root directory:
- `index.html`

## Success Criteria
- The `index.html` file is created in the project root.
- When opened in a web browser, the page displays the title, heading, welcome message, and the "Log In with Bungie.net" button.
- The `character-display` div exists but is empty.
- The HTML is well-formed and valid.

## Testing Requirements
- Open the `index.html` file directly in a modern web browser (Chrome, Firefox, Edge).
- Verify that all specified elements are present and display correctly.
- Check the browser's developer console to ensure there are no HTML parsing errors (404 errors for the CSS and JS files are expected and acceptable at this stage).
