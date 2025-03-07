1. Implement version control. 
2. Implement a side-by-side comparison of the two versions. 
3. Build the .deb and .exe versions of the note-creating app. 
4. Provide an option to store notes in a database.
5. Handle the sync conflict

----------------------------------


1. Decide on storage strategy: snapshots, diffs, or hybrid.

2. Design database schema to store versions.

3. Implement backend logic to create versions on save.

4. Handle diff calculation and snapshot generation.

5. Create API endpoints to retrieve version history and restore versions.

6. Build frontend components to display and interact with version history.

7. Test thoroughly, especially for performance and edge cases.


I want to build an offline note-taking application that can be downloaded on Linux, Windows, and Mac. In the application, users can create multiple versions of a single file, like the git, and compare the 2 versions side by side. If users need to back up their data including the versions, they only need to add their DB URI in the settings. Here the data upload to the DB should done from the user's system and not use any server code.

Please help me choose the tech stack to build this project and also give me the step-by-step guide to implement the project.