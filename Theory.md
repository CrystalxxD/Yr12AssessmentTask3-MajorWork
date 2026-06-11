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

##### **Level 1 DFD**

#### **Structure Chart**


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

---
### **4. Producing and Implementing**
#### **4.1 Development Process**

#### **4.2 Key Features Developed**
#### **4.2.1 Back-End Engineering Contribution**
#### **4.3 Screenshots of Interface**
#### **4.4 Version Control Summary**

---
### **5. Testing and Evaluation**
#### **5.1 Testing Method Used**
#### **5.2 Test Cases and Results**
#### **5.3 Evaluation Against Requirements**
#### **5.4 Improvements and Future Development**

---
### **6. Feedback, Security and Reflection**
#### **6.2 Secure Software Design and Data Handling**
#### **6.3 6.3 Personal Reflection**

---
### **7. Appendices**
#### Full Gantt Chart

#### Complete Data Dictionary 

#### Full Test Logs

#### Raw Feedback Notes

#### Exemplar Code Snippets