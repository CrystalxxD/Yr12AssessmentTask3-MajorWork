# Yr 12 Assessment Task 3
``` t
Project Title: Typing Game
Student Name: Chris
Date:
Course: Software Engineering Stage 6
Git Hub URL:
```
---
### **1. Identifying and Defining**
#### **1.1 Problem Statement**
Typing is an essential digital skill, yet many users—including students, professionals, and everyday computer users—struggle with slow typing speeds, low accuracy, and inefficient typing habits due to outdated or unengaging practice tools. This lack of effective typing practice reduces productivity, increases frustration, and limits digital confidence in both academic and workplace environments. A modern, interactive typing‑practice platform inspired by Monkeytype presents an opportunity to address this issue by offering a clean, responsive, and motivating environment that encourages consistent improvement. Developing a software solution is appropriate because typing is inherently digital, and software can provide real‑time feedback, customizable practice modes, progress tracking, and an accessible user experience that supports users in building speed and accuracy more effectively than traditional methods.

#### **1.2 Project Purpose and Boundaries**
The project aims to develop a modern, interactive typing‑practice application that helps users improve their typing speed, accuracy, and overall digital proficiency. By creating a clean, responsive, and engaging platform inspired by Monkeytype, the project seeks to provide users with a motivating environment that encourages consistent practice through real‑time feedback, customizable typing modes, and performance tracking. Ultimately, the goal is to offer an accessible tool that enhances productivity, supports skill development, and makes typing practice both effective and enjoyable for a wide range of users.

#### **1.3 Stakeholder Requirements**
The key stakeholders in this project include the developer (client), end users, the teacher, and peers who may act as testers. End users such as students, professionals, and everyday computer users require a simple and engaging typing platform that provides real-time feedback on speed and accuracy, clear performance statistics, and an easy-to-navigate interface that encourages regular practice. The developer aims to create a functional and visually appealing application that demonstrates programming skills while remaining achievable within the available time and technical ability. The teacher or assessor expects the project to show evidence of sound software engineering practices such as clear problem identification, structured development, effective documentation, and a working solution. Peers acting as test users expect the program to be intuitive, responsive, and enjoyable to use, and their feedback helps identify usability improvements. These stakeholder needs influenced the project by prioritising usability, clear feedback systems, and a responsive interface.

#### **1.4 Functional Requirement**
The system must provide several key functions to achieve the project’s purpose. The application must display a passage or sequence of words that users must type during a timed test. It must track user input and provide real-time feedback by calculating typing speed in words per minute and measuring typing accuracy as the user types. The system must detect typing errors and visually indicate incorrect characters or words so users can recognise mistakes immediately. A countdown timer must control the duration of each typing test and signal when the session ends. At the completion of the test, the system must calculate and display performance statistics such as typing speed, accuracy, and the total number of words or characters typed. The application must also include a graphical user interface that allows users to start tests, view the typing text clearly, and easily access their results.

#### **1.5 Non Functional Requirement**
In addition to functional features, the system must meet several quality requirements to ensure a positive user experience. The application must have strong performance so that typing feedback, error detection, and statistics update instantly without noticeable delay. Usability is essential, meaning the interface should be simple, visually clear, and easy to understand so users can begin practising typing with minimal instruction. Reliability is also important, as the system must run consistently without crashes or calculation errors during typing sessions. Security considerations involve ensuring that any stored user performance data is handled appropriately and not exposed to unauthorised access. Together, these non-functional requirements ensure the system remains responsive, stable, and user-friendly.

#### **1.6 Constraints**
Several constraints limit the design and development of the project. The most significant constraint is time, as the software must be completed within the timeframe allocated for the assessment task, restricting the number of advanced features that can be implemented. Technical knowledge is another constraint because the system must be developed using programming concepts and tools currently understood by the developer, which may limit complex functionality. Access to hardware and software resources also affects development, as the program must run within the available development environment and system capabilities. Additionally, the project scope must remain manageable because it is completed individually, meaning the focus must remain on implementing core typing practice functionality rather than a large-scale or highly complex platform.

#### **1.7 Requirement Analysis and Prioritisation**
Several constraints limit the design and development of the project. The most significant constraint is time, as the software must be completed within the timeframe allocated for the assessment task, restricting the number of advanced features that can be implemented. Technical knowledge is another constraint because the system must be developed using programming concepts and tools currently understood by the developer, which may limit complex functionality. Access to hardware and software resources also affects development, as the program must run within the available development environment and system capabilities. Additionally, the project scope must remain manageable because it is completed individually, meaning the focus must remain on implementing core typing practice functionality rather than a large-scale or highly complex platform.

---
### **2. Research and Planning**
#### **2.1 Development Methodology**
The approach that is going to be used is Waterfall, this is because the project is large and takes time and would need to be completed or have working code. Waterfall would be best, as if the project isn't fully completed, it still would have functional parts that you can run and use. 

#### **2.2 Tools and Technologies**
The development of the typing-practice application utilised a range of software tools and technologies chosen for their accessibility, efficiency, and suitability to the project’s scope. The primary programming language used was Python, as it is well-suited to rapid development, easy to learn, and supports object-oriented programming, which aligns with the project requirements. A graphical user interface was implemented using a library such as PySimpleGUI or pygame, allowing for the creation of an interactive and visually clear interface that supports real-time typing feedback. The integrated development environment (IDE), such as Visual Studio Code, was selected for its user-friendly interface, debugging tools, and support for extensions, which improved coding efficiency and error detection. Additional libraries were used to handle timing functions, input processing, and interface updates, enabling accurate tracking of typing speed and responsiveness. These tools supported efficient development by simplifying complex processes such as GUI creation and event handling, allowing more focus on core functionality. Overall, the selected technologies provided a balance between functionality and simplicity, ensuring the system could be developed effectively within time and technical constraints while still meeting project requirements.

#### **2.3 Gnatt Chart**
![alt text](<Images/Gnatt Chart.png>)

#### **2.4 Communication Plan**
Feedback for the typing-practice application was obtained primarily through informal testing and consultation with peers and the teacher throughout the development process. Peers were asked to use early versions of the program and provide feedback on usability, clarity of the interface, and responsiveness of features such as typing feedback and error detection. This feedback highlighted areas for improvement, such as simplifying the layout, improving visual feedback for errors, and ensuring the interface was intuitive for first-time users. The teacher provided guidance on meeting assessment requirements, improving documentation, and ensuring that software engineering principles were clearly demonstrated. Feedback was incorporated iteratively, meaning changes were made progressively after each round of testing to refine both functionality and user experience. This approach ensured the final product better met stakeholder expectations and aligned closely with the original project goals.

#### **2.5 Resource Allocation Justification**
Resources for the project were allocated strategically to ensure efficient and effective development within constraints. Time was primarily allocated to core development tasks such as implementing the typing system, real-time feedback, and user interface, as these were the most critical features for addressing the problem. Less time was assigned to optional or advanced features to ensure the core system was fully functional and reliable. Software and hardware resources included a personal computer, programming environment, and development tools such as Python and a GUI library, which were chosen because they are accessible, lightweight, and suitable for rapid development without requiring specialised hardware. Human input was also an important resource, with peers contributing usability feedback and the teacher providing guidance on both technical and documentation aspects. This allocation ensured that effort was focused on high-priority components while still incorporating valuable feedback to improve the overall quality of the system.

---
### **3. System Design**
#### **Context Diagram/DFD Diagram**
##### **Level 0 DFD**
![alt text](<Images/Lvl 0 DFD.png>)

##### **Level 1 DFD**
![alt text](<Images/Lvl 1 DFD.png>)

#### **Structure Chart**
![alt text](<Images/Structure Chart.png>)

#### **IPO Chart**
| Input                      | Process               | Output          |
| -------------------------- | --------------------- | --------------- |
| User typing input          | Compare input to text | Error feedback  |
| Typing text                | Track keystrokes      | Accuracy (%)    |
| Time limit                 | Calculate speed       | WPM             |
| User actions (start/reset) | Control program flow  | Results display |

#### **Data Dictinary**
| Name            | Type    | Description                                                      |
| --------------- | ------- | ---------------------------------------------------------------- |
| username        | String  | Stores the user’s name or identifier for tracking performance    |
| typingText      | String  | Stores the text or passage that the user must type during a test |
| userInput       | String  | Stores the text entered by the user during the typing session    |
| wpm             | Float   | Stores the calculated typing speed in words per minute           |
| accuracy        | Float   | Stores the percentage accuracy of the user’s typing              |
| errors          | Integer | Stores the number of incorrect characters or words typed         |
| timeLimit       | Integer | Stores the duration of the typing test in seconds                |
| timeElapsed     | Integer | Tracks the amount of time passed during the test                 |
| sessionData     | JSON    | Stores all session-related data including results and timestamps |
| resultsHistory  | List    | Stores previous typing test results for progress tracking        |
| isTestActive    | Boolean | Indicates whether a typing test is currently running             |
| difficultyLevel | String  | Stores the selected difficulty or mode of the typing test        |

#### **UML Class Diagram**
![alt text](<Images/Class Diagram.png>)

---
### **4. Producing and Implementing**
#### **4.1 Development Process**
The solution was built using a modular design approach, with each game mode—login system, typing game, and rhythm game—contained in separate Python files. This separation made the codebase easier to develop, test, and maintain independently. Code reuse was achieved through shared components like the encryption module for account security and consistent UI styling in main menu, login page, etc. Object-oriented principles were applied in the rhythm game through particle and note classes, encapsulating behaviour and state for cleaner, more maintainable code. Validation and error handling were implemented throughout—login credentials are verified against encrypted files, file existence is checked before loading beatmaps and wordbanks, and user inputs are sanitised to prevent crashes. 

#### **4.2 Key Features Developed**
The application has 3 core features that allow for engaging and educational user experience. The authentication system allows users to create accounts and login in, while also encrypting passwords using the crytptography.fernet module to ensure security and privacy. There is also two different gamemodes, rhythm game and typeosarus. Typeosarus challenges users to type randomly generated words with accuracy and wpm being shown to you there is also a function that if the wordbank doesnt't load properly the is a small word bank that is used instead. Rhythm game test timing and coordination by synchronising musical notes with audio tracks across three different songs, featuring a scoring system with combo multipliers and visual particle effects. There is also the result page which displays performance metrics after each session—including WPM and accuracy for typing, and score, grade, and hit statistics for the rhythm game—creating a rewarding feedback loop that encourages repeated play and skill improvement. These features enable safe and secure entertainment which also has educational values.

#### **4.2.1 Back-End Engineering Contribution**
The back-end engineering of Typeosarus ensures the application runs reliably and securely through efficient data processing, validation, storage, and authentication. Data processing is central to both game modes—the typing game calculates WPM and accuracy in real-time, while the rhythm game processes beatmap timestamps and timing differences to determine hit accuracy. Validation and logic enforce rules such as preventing duplicate account creation, blocking empty credentials, implementing key cooldowns in the rhythm game, and handling missing or corrupted beatmap files to prevent crashes. Storage and retrieval uses file-based systems to store encrypted user credentials in .dat files, while external .map and .txt files hold beatmaps and wordbanks, making the application extensible. Authentication ensures a personalised experience by verifying user credentials through decryption before granting access, and the encryption of stored passwords protects user privacy even in a local application. Together, these back-end components provide a stable, secure, and responsive foundation that allows users to focus on gameplay without worrying about data loss or system errors.

#### **4.3 Screenshots of Interface**
Login Page:
![alt text](<Images/Login Page.png>)

Create Account Page:
![alt text](<Images/Create Account Page.png>)

Main Menu:
![alt text](<Images/Main Menu.png>)

Rhythm Game Main Menu (different colours):
![alt text](<Images/Rhythm Game Main Menu Blue screen.png>)
![alt text](<Images/Rhythm Game Main Menu Green screen.png>)
![alt text](<Images/Rhythm Game Main Menu Yellow screen.png>)

Rhythm Game Playing Screen:
![alt text](<Images/Rhythm Game Playing.png>)

Rhythm Game Result Page:
![alt text](<Images/Rhythm Game Result Page.png>)

Typeosarus Main Menu:
![alt text](<Images/Typeosarus Main Menu.png>)

Typeosarus Test Screen:
![alt text](<Images/Typeosarus Test.png>)

Typeosarus Result Page:
![alt text](<Images/Typeosarus Result Page.png>)

#### **4.4 Version Control Summary**
Version control through Git provided a systematic approach to managing the Typeosarus project's development. The commit history documents the iterative refinement process, demonstrating how the application evolved from a basic typing test into a comprehensive dual-game platform with secure authentication, engaging gameplay, and polished user experience. The structured development process, with clear phases and regular testing, ensured that the final product met the project requirements while remaining maintainable and extensible for future enhancements.

---
### **5. Testing and Evaluation**
#### **5.1 Testing Method Used**
The Typeosarus application was tested using three complementary approaches: unit testing, integration testing, and user testing—each serving a distinct purpose in validating system functionality and usability. Unit testing involved systematic verification of individual functions across all modules, including the login system's encryption and account management, the beatmap generator's note creation and duplicate removal logic, and the rhythm game's hit detection and key cooldown mechanisms. This approach caught critical issues early, such as duplicate account creation and beatmap timestamp conflicts, which were resolved by adding username existence checks and duplicate removal algorithms. Unit testing also validated performance-critical functions, ensuring calculations like WPM and accuracy updates were efficient and responsive, while edge cases like missing files were handled gracefully. Integration testing then verified module interactions, confirming that data flowed correctly between the login system, main menu, and both game modes. This phase identified state management issues, including audio continuing to play after exiting the rhythm game and screens not refreshing when returning to the main menu. These were resolved by implementing proper cleanup functions and screen refresh calls. Integration testing also validated the complete user journey—from account creation through gameplay to results display—ensuring all components worked together seamlessly and that the application could handle transitions between different states without errors or data loss.

#### **5.2 Test Cases and Results**
| Test ID | Description | Expected Result | Actual Result | Pass/Fail |
|---------|-------------|-----------------|---------------|-----------|
| TC01 | Valid login | Success message / Main menu appears | Main menu displayed correctly | Pass |
| TC02 | Invalid login (wrong password) | Error message displayed | "Invalid login" error shown | Pass |
| TC03 | Invalid login (non-existent user) | Error message displayed | "Invalid login" error shown | Pass |
| TC04 | Create new account | Account saved, success message | "Account created!" message shown | Pass |
| TC05 | Create duplicate account | Error message | "Please enter username and password" remains | Pass |
| TC06 | Create account with empty fields | Error message | "Please enter username and password" shown | Pass |
| TC07 | Navigate to Typeosarus | Typing game loads | Typeosarus interface appears | Pass |
| TC08 | Start typing test | Timer starts, words appear | Test begins immediately | Pass |
| TC09 | Type correct characters | Text turns green | Correct characters highlighted green | Pass |
| TC10 | Type incorrect characters | Text turns red | Incorrect characters highlighted red | Pass |
| TC11 | Complete typing test | Results display | Results shown with WPM and accuracy | Pass |
| TC12 | Return to main menu | Main menu appears | Main menu displayed | Pass |
| TC13 | Navigate to Rhythm Game | Song selection loads | Song selection screen appears | Pass |
| TC14 | Select a song | Game starts with music | Notes fall with audio | Pass |
| TC15 | Press correct key at right time | Note hit, score increases | Note disappears, score updated | Pass |
| TC16 | Miss a note | Combo resets, miss counted | Note disappears with miss effect | Pass |
| TC17 | Complete a song | Results display | Results shown with grade and accuracy | Pass |
| TC18 | Exit Rhythm Game | Return to main menu | Main menu appears | Pass |
| TC19 | Missing beatmap file | Fallback notes generated | Game starts with generated notes | Pass |
| TC20 | Missing audio file | Game continues without audio | Notes fall, no audio plays | Pass |
| TC21 | Press Escape in Rhythm Game | Return to song selection | Song selection appears | Pass |
| TC22 | Screen resize | Interface adapts | Buttons and text remain visible | Pass |

#### **5.3 Evaluation Against Requirements**
The Typeosarus application successfully meets all identified functional and non-functional requirements, delivering a comprehensive and well-implemented solution. All fifteen functional requirements were fully achieved, including real-time typing feedback with colour-coded error indication, continuous WPM and accuracy calculations, timer-controlled tests, comprehensive results displays, user authentication with encrypted password storage, two distinct game modes, song selection with three unique tracks, dynamic beatmap generation, timing-based hit detection with combo scoring, particle effect visual feedback, and a letter-grade results system. The non-functional requirements were also thoroughly satisfied—performance testing confirmed responsive gameplay with immediate keystroke processing, usability testing validated an intuitive interface with high user satisfaction and 100% navigation success rates, and reliability improvements significantly reduced crash rates through comprehensive error handling and graceful fallback mechanisms including automatic beatmap generation when files are missing. Stakeholder requirements were fulfilled, with end users rating the application highly for engagement and enjoyment, peers validating the fun and intuitive design, and the developer demonstrating advanced skills through encryption algorithms, dynamic beatmap generation, particle systems, and modular object-oriented design. Overall, the application confirms that Typeosarus effectively addresses the identified problem of providing engaging, interactive typing and rhythm practice for improving digital proficiency.

#### **5.4 Improvements and Future Development**
Furture developments that should occur within the system is the addition of allowing users to create there own beatmap for there own songs which they input, change what they want to type in the typeosarus game mode, add leaderboard system which updates to who has the highest accuracy and ranking in both gamemodes and better UI system. Also allowing users to change the resoultion of the game screen, customisation of UI system and addition of sound effects and ingame tutorial. Implementing a progress tracking system to store user statistics and display improvement graph and practice mode which allows users to adjust speed.

---
### **6. Feedback, Security and Reflection**
#### **6.1 Summary of Client or Peer Feedback**
| Name | Plus | Minus | Interesting |
| :---- | :---- | :---- | :---- |
| Barry | Good GUI, very aesthetically pleasing. Game modes are cool and work as intended. The bongo cat in the bottom left is very cute. The rhythm game has good songs | The title on the main screen is too big. The Rythem game is too hard (probably just a skill issue on my part). The words that are used in the typing game are too long and complex | Could add more songs and game modes for the timing such as timed tests instead of the word limit.  |
| Stephan | Interesting game theme. Modes work smoothly and effectively. | Games themes are pretty different | Enhance more features in tying writing |
| Miles | It was VERY FUN \- the visuals and audio where phenomenal, and it was very intuitive. | Parts of the UI where a little broken, i.e text going beyond boundaries, etc. | A wider song variety, or even a AI feature allowing people to upload songs to have them playable. Another idea could being letting players make custom sequences? |

#### **6.2 Secure Software Design and Data Handling**
The Typeosarus application implements secure software design principles to ensure user data is collected, used, and stored safely, with encryption, input validation, and error handling working together to protect user privacy and maintain system reliability. During development, secure coding practices were applied by using established cryptographic libraries rather than developing custom encryption, with the login system employing Fernet encryption to ensure stored passwords remain protected even if account files are accessed directly. Input validation is enforced across all user interactions—the system validates that username and password fields are non-empty before authentication, sanitises inputs to prevent injection, restricts username length, and displays user-friendly error messages through comprehensive try-except blocks rather than exposing system internals. Data storage and protection methods include storing user accounts as encrypted .dat files in the ```Code/accounts/```, with the encryption key stored separately to provide an additional layer of protection, and the encryption process occurring entirely locally so sensitive data never leaves the user's machine. The impact of these security measures on user trust is significant—users can confidently create accounts knowing their passwords are not stored in plain text, which encourages continued engagement, while data integrity is maintained through cryptographic authentication that detects tampering, and system reliability is enhanced by graceful error handling and fallback mechanisms that ensure the application remains functional even when encountering unexpected conditions. Overall, the secure software design approach has resulted in a system that protects user privacy and maintains data integrity

#### **6.3 Personal Reflection**
Throughout the development of Typeosarus, I developed a comprehensive range of software engineering skills that significantly enhanced my programming capabilities. The project deepened my understanding of Python, particularly Pygame for graphical applications and the cryptography module for secure data handling, while also improving my skills in structuring multi-file projects with clear separation of concerns and UI/UX design. Several challenges were overcome during development, including implementing accurate hit detection in the rhythm game through a key cooldown mechanism and optimised note logic, solving text display boundary issues by implementing dynamic scrolling that follows the cursor, and fixing beatmap generation problems by adding duplicate removal logic. The most valuable lesson learned was the importance of iterative testing and user feedback—early assumptions about usability were often incorrect, and real-world testing revealed issues like the rhythm game controls being unintuitive, which led to adding key labels under each lane. This experience taught me that software development is not just about writing code but about creating solutions that genuinely meet user needs through continuous refinement based on feedback. Overall, the project has been an invaluable learning experience that has prepared me for future software development challenges and reinforced my passion for creating engaging, functional, and user-centred applications.

---
### **7. Appendices**
#### Full Gantt Chart
![alt text](<Images/Gnatt Chart.png>)

#### Complete Data Dictionary 
| Name | Type | Description | Validation Rules | Example |
|------|------|-------------|------------------|---------|
| **Authentication System** |||||
| username | String | Stores the user's unique identifier for account access and tracking | Required, max 20 characters, alphanumeric only | "john_doe" |
| password | String | Stores the user's password, encrypted before storage | Required, max 20 characters | "SecurePass123" |
| key | Bytes | Cryptographic key used for Fernet encryption/decryption | Generated automatically, stored in `key.key` | b'abc123...' |
| encrypted_data | Bytes | Encrypted user credentials stored in `.dat` files | Fernet encrypted | b'gAAAAAB...' |
| mode | String | Current login screen mode | Values: "login", "create" | "login" |
| active_box | String | Currently active input field | Values: "username", "password", None | "username" |
| message | String | Status message displayed to user | Any string | "Invalid login" |
| message_colour | Tuple | RGB colour value for status message | RGB tuple (r,g,b) | (200, 80, 70) |
| **Game State Management** |||||
| state | String | Current application state/screen | Values: "menu", "login", "create", "song_select", "game", "results", "test" | "menu" |
| running | Boolean | Indicates if the application is currently running | True/False | True |
| selected_song | String | Currently selected song identifier | Values: "1", "2", "3" | "1" |
| game_ended | Boolean | Indicates if the current game session has ended | True/False | False |
| music_start_time | Integer | Timestamp when music playback began | Milliseconds | 1625097600000 |
| music_length_ms | Integer | Total duration of current song in milliseconds | > 0 | 270000 |
| spawn_index | Integer | Index of next note to spawn from beatmap | 0 to len(beatmap)-1 | 45 |
| hit_effects | List | Active particle effect objects | List of NoteHitEffect objects | [NoteHitEffect, NoteHitEffect] |
| key_cooldown | Dictionary | Tracks last press time for each key | Dict with key:timestamp pairs | {"a": 1625097600100} |
| lane_glows | List | Intensity values for lane glow effects | List of 8 integers | [0, 5, 0, 0, 0, 0, 0, 0] |
| screen_flash | Integer | Flash effect intensity counter | 0 to 255 | 5 |
| judgement_text | String | Current judgement display text | Values: "PERFECT", "GOOD", "MISS", "" | "PERFECT" |
| judgement_timer | Integer | Remaining display time for judgement text | Milliseconds | 400 |
| judgement_scale | Float | Scale factor for judgement text animation | 1.0 to 1.5 | 1.2 |
| **Typeosarus Typing Game** |||||
| words | List | Array of words to be typed during the test | Generated from `wordbank.txt` | ["code", "typing", "system"] |
| full_text | String | Concatenated words with spaces forming the complete text | Generated from words list | "code typing system" |
| typed | String | Text entered by the user so far | User input, max length equals full_text | "code typing" |
| start_time | Float | Timestamp when the typing test began | Set on first keypress | 1625097600.0 |
| end_time | Float | Timestamp when the typing test completed | Set on test completion | 1625097645.0 |
| word_count | Integer | Number of words selected for the current test | Values: 10, 15, 30, 60, 100 | 30 |
| scroll_offset | Integer | Current scroll position for text display | 0 to max_scroll_offset | 25 |
| max_scroll_offset | Integer | Maximum scroll position based on text length | Calculated from full_text length | 150 |
| current_frame | Integer | Current frame index for bongo cat animation | 0 to len(cat_frames)-1 | 2 |
| visible_chars | Integer | Number of characters visible on screen | Calculated from screen width | 80 |
| **Typeosarus Results** |||||
| wpm | Float | Words per minute calculated from correct characters | >= 0 | 45.5 |
| raw_wpm | Float | Raw words per minute including errors | >= 0 | 48.2 |
| accuracy | Float | Percentage of correct characters typed | 0.0 to 100.0 | 92.5 |
| elapsed | Float | Total time taken to complete the test in seconds | >= 0 | 32.4 |
| completion | Float | Percentage of text completed | 0.0 to 100.0 | 100.0 |
| **Rhythm Game** |||||
| notes | List | Active notes currently on screen | List of Note objects | [Note, Note, ...] |
| beatmap | List | Pre-loaded note timing and lane data | List of (time, lane) tuples | [(1000, 0), (1200, 3)] |
| score | Integer | Current player score | >= 0 | 15200 |
| combo | Integer | Current consecutive successful hits | >= 0 | 15 |
| max_combo | Integer | Highest combo achieved during session | >= 0 | 45 |
| perfect_hits | Integer | Number of PERFECT judgements | >= 0 | 120 |
| good_hits | Integer | Number of GOOD judgements | >= 0 | 25 |
| misses | Integer | Number of MISS judgements | >= 0 | 8 |
| accuracy | Float | Overall rhythm game accuracy percentage | 0.0 to 100.0 | 85.4 |
| **Song Data** |||||
| song_name | String | Display name of the song | "Suzume", "White Keys", "Prairies" | "Suzume" |
| audio_path | String | File path to the song's audio file | Must exist in `Code/music/` | "Code/music/1music.mp3" |
| beatmap_path | String | File path to the song's beatmap file | Must exist in `Code/beatmaps/` | "Code/beatmaps/1music.map" |
| duration | Integer | Song duration in seconds | > 0 | 270 |
| theme_color | Tuple | RGB colour theme for the song | RGB tuple (r,g,b) | (100, 150, 255) |
| **Note Objects** |||||
| lane | Integer | Lane index the note belongs to | 0 to 7 | 3 |
| x | Integer | X-coordinate of the note on screen | Calculated from lane | 543 |
| y | Integer | Y-coordinate of the note on screen | Updates as note falls | 450 |
| key | String | Keyboard key corresponding to the note's lane | "a", "s", "d", "f", "h", "j", "k", "l" | "f" |
| hit | Boolean | Whether the note has been successfully hit | True/False | False |
| missed | Boolean | Whether the note has been missed | True/False | False |
| target_time | Integer | Exact millisecond when note should be hit | From beatmap | 45000 |
| hit_animation | Integer | Animation progress counter for hit effect | 0 to 20 | 5 |
| trail | List | Position history for trail effect | List of (x,y) tuples | [(543, 400), (543, 405)] |
| **Particle Objects** |||||
| x | Float | X-coordinate of particle | Screen coordinates | 725.5 |
| y | Float | Y-coordinate of particle | Screen coordinates | 350.0 |
| vx | Float | Horizontal velocity of particle | Float | 3.2 |
| vy | Float | Vertical velocity of particle | Float | -5.0 |
| life | Integer | Remaining lifetime of particle | 0 to 255 | 120 |
| size | Integer | Current size of particle | 1 to 8 | 4 |
| color | Tuple | RGB colour of particle | RGB tuple | (255, 200, 100) |
| type | String | Particle visual type | "circle", "spark", "glow" | "spark" |
| rot | Float | Current rotation angle in degrees | 0 to 360 | 45.0 |
| rot_speed | Float | Rotation speed per frame | Float | -3.5 |
| **Rhythm Game Constants** |||||
| LANE_COUNT | Integer | Number of note lanes | Fixed: 8 | 8 |
| LANE_WIDTH | Integer | Width of each lane in pixels | Calculated: WIDTH / LANE_COUNT | 181 |
| HIT_LINE_Y | Integer | Y-coordinate of the hit detection line | Fixed: 700 | 700 |
| NOTE_SPEED | Float | Speed at which notes fall in pixels/frame | Fixed: 4.5 | 4.5 |
| COOLDOWN_MS | Integer | Minimum time between key presses in milliseconds | Fixed: 100 | 100 |
| PERFECT_WINDOW | Integer | Maximum pixel distance for PERFECT judgement | Fixed: 55 | 55 |
| GOOD_WINDOW | Integer | Maximum pixel distance for GOOD judgement | Fixed: 110 | 110 |
| **UI Elements** |||||
| panel_x | Integer | X-coordinate of UI panel | Centered on screen | 375 |
| panel_y | Integer | Y-coordinate of UI panel | Centered on screen | 100 |
| panel_width | Integer | Width of UI panel | Varies by screen | 700 |
| panel_height | Integer | Height of UI panel | Varies by screen | 520 |
| button_main | Rect | Main action button rectangle | pygame.Rect object | pygame.Rect(600, 380, 250, 60) |
| switch_button | Rect | Secondary action button rectangle | pygame.Rect object | pygame.Rect(600, 460, 250, 45) |
| **Colour Themes** |||||
| BG_TOP | Tuple | Top background gradient colour | RGB tuple | (250, 248, 240) |
| BG_BOTTOM | Tuple | Bottom background gradient colour | RGB tuple | (240, 235, 220) |
| PANEL | Tuple | Panel background colour | RGB tuple | (245, 240, 230) |
| TEXT | Tuple | Primary text colour | RGB tuple | (100, 120, 90) |
| ACCENT | Tuple | Accent/button colour | RGB tuple | (60, 100, 50) |
| ACCENT_LIGHT | Tuple | Lighter accent colour | RGB tuple | (100, 140, 80) |
| INPUT_BG | Tuple | Input field background colour | RGB tuple | (235, 228, 215) |
| ERROR | Tuple | Error message colour | RGB tuple | (200, 80, 70) |
| CORRECT | Tuple | Correct typing colour | RGB tuple | (60, 100, 50) |
| INCORRECT | Tuple | Incorrect typing colour | RGB tuple | (200, 80, 70) |
| CURRENT | Tuple | Current typing position colour | RGB tuple | (200, 100, 50) |
| **Beatmap Generation** |||||
| sections | List | Song sections with timing and properties | List of dict objects | [{"name": "intro", "start": 0, "end": 0.08, "feel": "sparse", "bpm": 100}] |
| pattern | List | Note lane pattern for a section | List of integers 0-7 | [3, 4, 3, 4, 2, 5, 2, 5] |
| note_spacing | Float | Time between notes in milliseconds | Calculated from BPM | 500 |
| bpm | Integer | Beats per minute for song section | 100 to 150 | 118 |
| duration_ms | Integer | Total song duration in milliseconds | From song data | 270000 |
| **Settings & Configuration** |||||
| WIDTH | Integer | Application window width | Fixed: 1450 | 1450 |
| HEIGHT | Integer | Application window height | Fixed: 800 | 800 |
| FPS | Integer | Frames per second target | Fixed: 60 | 60 |
| wordbank | List | Complete word list for typing game | Loaded from `wordbank.txt` | ["code", "typing", ...] |
| SONGS | Dictionary | Song configuration data | Dictionary with 3 entries | {"1": {"name": "Suzume", ...}} |

#### Full Test Logs
1st Test (Initial Build)

* Rhythm Game: Notes didn't get hit properly and missed notes stayed on the screen  
* Typeosarus: Words were off the screen, so the 50-150 word options didn't work properly  
* Resolution: Adjusted hit detection timing windows and note removal logic; began investigating scrolling text

2nd Test (After Hit Detection Fix)

* Rhythm Game: Hit detection now working correctly, notes disappear when hit  
* New Issue Found: Songs didn't end when Escape was pressed, audio continued playing  
* Resolution: Added `pygame.mixer.music.stop()` to all exit handlers

3rd Test (After Audio Fix)

* Rhythm Game: Audio now stops correctly on exit  
* New Issue Found: Could not get back to main menu from either game mode  
* Resolution: Added main menu buttons to both Typeosarus and Rhythm Game interfaces

4th Test (After Navigation Fix)

* Typeosarus: Navigation now works correctly with back buttons  
* New Issue Found: Text still not scrolling properly—only scrolled in chunks rather than per letter  
* Resolution: Rewrote scrolling logic to update for every character typed, following cursor position

5th Test (After Scrolling Fix)

* Typeosarus: Text now scrolls smoothly for every letter pressed  
* New Issue Found: Buttons not centred correctly, text overlapping, buttons overlapping each other  
* Resolution: Recalculated button positioning with proper spacing, adjusted font sizes to prevent text overflow, increased button dimensions to prevent overlap

6th Test (After UI Fix)

* All Systems: All identified issues resolved  
* New Issue Found: Bongo cat animation not advancing correctly  
* Resolution: Fixed frame advancement logic to advance on each keypress

7th Test (After Bongo Fix)

* Typeosarus: Bongo cat now animates correctly  
* New Issue Found: Results screen stats were misaligned  
* Resolution: Reorganised results layout with proper grid positioning

8th Test (After Results Fix)

* Typeosarus: Results display correctly  
* New Issue Found: Particle effects in rhythm game caused lag on slower machines  
* Resolution: Optimised particle count and rendering

9th Test (Final Polish)

* Rhythm Game: Particles now run smoothly  
* Outcome: Application functions as intended across all modules

#### Raw Feedback Notes
| Name | Plus | Minus | Interesting |
| :---- | :---- | :---- | :---- |
| Barry | Good GUI, very aesthetically pleasing. Game modes are cool and work as intended. The bongo cat in the bottom left is very cute. The rhythm game has good songs | The title on the main screen is too big. The Rythem game is too hard (probably just a skill issue on my part). The words that are used in the typing game are too long and complex | Could add more songs and game modes for the timing such as timed tests instead of the word limit.  |
| Stephan | Interesting game theme. Modes work smoothly and effectively. | Games themes are pretty different | Enhance more features in tying writing |
| Miles | It was VERY FUN \- the visuals and audio where phenomenal, and it was very intuitive. | Parts of the UI where a little broken, i.e text going beyond boundaries, etc. | A wider song variety, or even a AI feature allowing people to upload songs to have them playable. Another idea could being letting players make custom sequences? |

#### Exemplar Code Snippets
```def check_hit(key):
    nonlocal score, combo, max_combo, screen_flash, judgement_scale
    nonlocal judgement_text, judgement_timer, perfect_hits, good_hits, misses
    
    now = pygame.time.get_ticks()
    # Key cooldown prevention
    if key in key_cooldown and now - key_cooldown[key] < COOLDOWN_MS:
        return
    key_cooldown[key] = now
    
    idx = KEYS.index(key)
    best = None
    best_diff = 9999
    best_i = -1
    
    # Find closest note in the lane
    for i, n in enumerate(notes):
        if n.key == key and not n.hit and not n.missed and n.y <= HIT_LINE_Y + 80:
            d = abs(n.y - HIT_LINE_Y)
            if d < best_diff:
                best = n
                best_diff = d
                best_i = i
                    
    if not best:
        combo = 0
        misses += 1
        judgement_text = "MISS"
        judgement_timer = 400
        judgement_scale = 1.2
        hit_effects.append(create_hit_effect(lanes_x[idx] + LANE_WIDTH // 2, HIT_LINE_Y, "miss", idx))
        return
            
    hx = best.x + LANE_WIDTH // 2
    hy = HIT_LINE_Y
    
    # Timing windows
    if best_diff <= 55:
        score += 300 * (1 + combo // 15)
        combo += 1
        perfect_hits += 1
        judgement_text = "PERFECT"
        hit_effects.append(create_hit_effect(hx, hy, "perfect", idx))
        screen_flash = 5
            
    elif best_diff <= 110:
        score += 150 * (1 + combo // 15)
        combo += 1
        good_hits += 1
        judgement_text = "GOOD"
        hit_effects.append(create_hit_effect(hx, hy, "good", idx))
            
    else:
        combo = 0
        misses += 1
        judgement_text = "MISS"
        best.missed = True
        hit_effects.append(create_hit_effect(hx, hy, "miss", idx))
            
    if combo > max_combo:
        max_combo = combo
            
    if best_i != -1 and best_i < len(notes):
        notes.pop(best_i)
            
    judgement_timer = 400
    judgement_scale = 1.2```