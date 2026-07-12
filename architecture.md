Frontend:
- React, nothing completed i want to make sure that what i did on backend is working. Have to be responsive.
- Frontend is responsible for displaying data to the user, collecting user input, uploading files, displaying routes on the map and communicating with the backend API. The application should be responsive and accessible on different screen sizes.

Backend:
- Python/Flask - prefectly capable of being used for this certing program.
- Backend is responsible for processing user input, parsing uploaded files, executing application logic, communicating with the database and providing API endpoints for frontend communication.

Database:
- SQlite - i dont want to create multiscaling app that turn over whole word - only for testing my personal skills
- SQLite was chosen because the application is a personal/testing project and does not require high scalability or concurrent access from many users. It provides simple local data persistence.

Comunication:
Front <-> Back
- user PUT data mannauly or within a file(CSV, txt, xlsx) -> backend parse it and do all needed functions and we send it database for memoy and possiblty to back to this routes
- We(program) POST output/result for user with route
- DELETE - user can delete route

1. User enters route data manually or uploads CSV/TXT/XLSX file.

2. Frontend sends data to backend using HTTP request.

3. Backend validates and parses received data.

4. Backend processes the data and stores results in SQLite database.

5. Frontend requests stored routes from backend API.

6. Backend returns data in JSON format.

7. Frontend displays routes and results to the user.

| Method | Endpoint       | Purpose            |
| ------ | -------------- | ------------------ |
| POST   | `/routes`      | Create new route   |
| GET    | `/routes`      | Get saved routes   |
| GET    | `/routes/{id}` | Get specific route |
| DELETE | `/routes/{id}` | Delete route       |


map provider:
https://react-leaflet.js.org/
React-Leaflet was selected as the frontend mapping library. OpenStreetMap tiles will be used as the map data provider.