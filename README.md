# Alex O'Connor Project Proposal

[Selection](##-App-Type-&-Option) |
[Description](##-Description) |
[Tools](##-Tools) |
[Features](##-Feature-List) |
[UI](##-UI-Sketch) |
[API](##-API-Design)  |
[Architecture](##-Architecture) |
[MVP](##-MVP) |
[Challenges](##-Interesting-Challenges) |
[Goals](##-Stretch-Goals)

## App Type & Option     
    Clearly state which app type you've successfully "claimed" and what specific option within it you've chosen. This combination must be completely unique to you, so discuss it with anyone else who's chosen the same app type to avoid significant overlap. Consult with the instructor if you have any doubts on this. (It's better to discover it now than when you're submitting your final project after spending many hours on it.)

> I have claimed BYOP. My proposal is to make a simple chat room.

## Description
    A paragraph or two describing what your app will do. You may begin with the generic description provided, but it must be a lot more specific than that.

### Usage: Login &rightarrow; Chat

#### Login

>Making use of passphrase hashing, store login credentials as safely as possible. On login submit, send passphrase as (HTTPS encrypted) plain text to server server to hash. If hashed on client computer, it is as good as storing a plaintext passphrase. On successful login, server returns a unique string that is stored on server. This string is used for making sure the user authenticated. The string is changed on every login.

#### Chat
    
>Text box entry, button to submit. Sends to server along with unique string. By doing this, XSS attacks are mitigated. If a user notices someone else posting chats as them, all they have to do is login again. Roughly, every 5 seconds, the server will update webpages, letting them know if there are any new messages. If there are, the browser asks for them, using the unique string to show successful login. New chats will appear at the top, so the page is not constantly scrolling to the bottom.   

    
## Tools

    Which languages will you use? What modules/libraries/frameworks (in the language's standard library, or 3rd party) will you be adding? Which software tools will you use (IDE, etc.)?

>I use `VSCode` for coding, as with all the extensions, I can do everything from make and test the python server, to HTML pages.
>For the backend, I am using `python`. This is easiest because I am using bottle for web hosting, which allows me to import other python files I make, and run when needed.
>The main python imports I believe I will need are `os`, `time`, and `bottle`. Specifically for hashing, I plan on importing `hashlib` and `binascii`.
>For the website, I will use `HTML`, `JS`, and `CSS`.
>Everything I am using are very standard, and should not require specific `pip3 install`

## Feature List
    What specific things can the user do with your app? This will be used as a checklist to evaluate your success--a significant portion of your final grade for the project--so make it as unambiguous as possible. You may use a UML use case diagram to summarize this, but a simple (numbered) list is OK also. 
>* Working login
>    * Server-side passphrase hashing
>    * Storing logins
>    * Generate unique strings and store
>    * Make sign-up page
>        * 2 passphrase fields
>        * Make sure passphrases match
>        * Check that login isn't taken
>* Working chat
>    * Submit chats
>        * Authenticate with unique
>    * Receive chats
>        * keep list of received chats, so not reloading same chats
>        * Request with unique string
>    * Display chats
>        * Make possible to see who sent

## UI Sketch
    Draw a rough sketch of what your front end will look like. Include all the major screens, with at least all the essential UI elements for getting input from the user and showing the user results. You may simply create a simple mockup using HTML and CSS, or use a tool like Balsamiq, Figma, or any drawing package (Diagrams.net, Google Drawings, Gliffy, etc.), or just create a carefully hand-drawn sketch.

![UML Diagram](https://paintrain.pythonanywhere.com/images/uml.png)

## API Design
    Since the project must be split into a front end and a back end, you need to think about the interface you'll provide for the back end--your API. List the basic API endpoints you'll provide, with a list of parameters and types for each one, and a description of the actions and return values you'll receive (including the format of the return value--JSON?).
> Server &rightarrow;
>    * Hash and store passphrases
>    * Generate adn store sessionIds
>    * Store chat history
>    * Let browsers know what chats are in history
> 
> Browser &rightarrow;
>    * Ask for chats that are not loaded
>    * Store sessionId on login
>    * Display chats
>    * Ask user for credentials for authentication
>
> I plan on using the POST method, as it allows for the browser to ask for and send information with everything encrypted. It has a body for me to write messages in. To make my life easy, I will keep these messages in a JSON format, so that it easy to do things with in Python and JS.
>
> My end points for the browser to request things from will be `/chat/message`, `/update` and`/chat/<id:int>`. 

## Architecture
    Spend some time considering the structure of your project, especially the back end. You must use at least 1 class, with reasonable fields and methods to represent and manipulate the "stuff" being tracked in the back end--possibly more. A UML class diagram neatly drawn by hand or using the yUML extension for VS Code is a good way to do this. You don't have to include details inside each class box--just boxes and the connections between them--unless you only have 1 class.

## MVP
    What subset of what you're proposing will be your Minimum Viable Product? You should aim to have as much as possible of this done by the beginning of the 2nd lab period we'll spend on this so I can give you feedback on the direction you're heading.

> The order in which I plan on getting things done are as follows (The line is what my minimum is)
> 1. Working chat page
> 2. Working login page
> 3. Working authentication for sending and receiving chats
>---
> 4. Working sign-up page
> 5. Users change passwords
> 6. Custom colors
> 7. Unique avatars


## Interesting Challenges
    Briefly describe one or two of the most interesting challenges you think you'll face as you work on this project.

> * I think that one of the most interesting challenges will be updating browsers on whether or not there are new messages, while keeping traffic to a minimum. I'm not claiming to use the best method, but I plan on using Server-Sent Events (SSE) to accomplish this. 
>* The second challenge I will face is how I will store user credentials, as this is something that is easier to mess up than do right. Any attempt at encrypting the file will result in a hardcoded key being in my code, which is just about as good as having a plaintext file. Due to this, I do not plan on encrypted the file. As I mentioned earlier, I plan on hashing the passphrases, which should provide enough security, provided users use secure passphrases. 

## Stretch Goals
    
    What would you do to enhance this project if you have a bit of extra time (or a lot)? List at least 2 realistic-ish stretch goals and at least 1 that's extremely ambitious.
> * Allow change of passphrase
> * Allow upload of user avatars
> * Allow custom chat colors
> * Word filter
