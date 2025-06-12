# **RoutineZ - Course Routine Generator**

Welcome to RoutineZ! This application helps university students create optimal class schedules by automatically generating conflict-free routines based on their course preferences and constraints.

## **Overview of the App**

RoutineZ is designed to simplify the course registration process by:
* Automatically generating conflict-free class schedules
* Checking for exam time conflicts
* Providing real-time seat availability information
* Offering AI-powered schedule optimization
* Supporting flexible time and day preferences

The app combines a powerful backend API with an intuitive frontend interface to make course planning effortless.

## **How the App Works**

1. **Course Selection**: Browse and select your desired courses from the available offerings
2. **Preference Setting**: Choose your preferred:
   * Days of the week
   * Time slots
   * Faculty members (optional)
   * Commute preferences (for AI optimization)
3. **Routine Generation**: The app will generate a conflict-free schedule based on your selections
4. **AI Optimization**: Optionally use AI to optimize your schedule for better time management

## **Key Features**

### **1. Course Management**

* View all available courses with seat availability
* Get detailed course information including sections and faculty
* Real-time updates of seat status
* Filter courses by various criteria

### **2. Schedule Generation**

* Automatic conflict detection for class times
* Exam schedule conflict checking
* Multiple schedule options when available
* Manual and AI-powered generation modes

### **3. AI Assistant**

* Get intelligent answers about your schedule
* Receive optimization suggestions
* Analyze potential conflicts
* Get commute-optimized schedules

## **API Endpoints**

### **Course Information**

#### **Get All Courses**
```http
GET /api/courses
```
Returns a list of all available courses with their codes, names, and seat availability.

#### **Get Course Details**
```http
GET /api/course_details?course={courseCode}
```
Returns detailed information about a specific course, including:
* Available sections
* Faculty members
* Seat availability
* Exam schedules

### **Routine Generation**

#### **Generate Routine**
```http
POST /api/routine
```
Generate a course routine based on preferences:

```json
{
  "courses": [
    {
      "course": "CSE101",
      "faculty": ["John Doe"],
      "sections": {
        "John Doe": "A"
      }
    }
  ],
  "days": ["SUNDAY", "TUESDAY"],
  "times": ["8:00 AM-9:20 AM", "9:30 AM-10:50 AM"],
  "useAI": true,
  "commutePreference": "balanced"
}
```

### **AI Features**

#### **Ask AI Assistant**
```http
POST /api/ask_ai
```
Get AI-powered answers about your schedule:
```json
{
  "question": "How can I optimize my schedule?",
  "routine": [/* Your current routine */]
}
```

#### **Check Exam Conflicts**
```http
POST /api/check_exam_conflicts_ai
```
Analyze potential exam conflicts in your schedule.

## **Getting Started**

### **1. Accessing the Application**
* Visit [https://routinez.vercel.app](https://routinez.vercel.app)
* No installation or login required
* Works on all modern browsers

### **2. Creating Your First Schedule**

1. Click "Generate Routine" on the homepage
2. Select your desired courses from the course list
3. Choose your preferred days and time slots
4. (Optional) Select specific faculty members
5. Choose between AI or manual generation
6. Click "Generate" to create your schedule

### **3. Using the AI Assistant**

1. Generate a routine first
2. Click on the AI Assistant button
3. Ask questions about your schedule
4. Get intelligent suggestions and analysis

## **Troubleshooting**

### **Common Issues**

* **No schedules generated**
  * Check if you've selected compatible time slots
  * Ensure courses have available seats
  * Try different day/time combinations

* **AI features not working**
  * Check your internet connection
  * Try refreshing the page
  * Clear browser cache

* **Seat availability issues**
  * Click refresh to get latest data
  * Check the API status indicator
  * Try again in a few minutes

## **Best Practices**

1. **Course Selection**
   * Start with required courses first
   * Keep alternative courses in mind
   * Check seat availability before planning

2. **Schedule Optimization**
   * Consider your commute time
   * Balance your daily course load
   * Leave gaps for breaks and study time

3. **Using AI Features**
   * Be specific with your questions
   * Provide context about your preferences
   * Review AI suggestions carefully

## **Updates and Support**

* The application is regularly updated with new features
* Clear your browser cache after updates
* For support, use the feedback form in the app

## **Contributing**

We welcome contributions! To contribute:
1. Fork the repository
2. Create your feature branch
3. Submit a pull request

For detailed contribution guidelines, see our [GitHub repository](https://github.com/cswasif/routinez_Latest).

## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## **Project Structure**

This project follows a standard structure suitable for Vercel deployment:

```
RoutinEZ/
├── api/                     # Contains Vercel Serverless Functions (Python)
│   ├── requirements.txt     # Python dependencies for serverless function
│   └── usisvercel.py        # Main backend serverless function (Flask application)
├── USIS/
│   └── usis-frontend/       # React frontend application
│       ├── public/          # Static assets
│       ├── src/             # Frontend source code
│       │   ├── components/  # Reusable React components
│       │   │   ├── ui/      # UI components (e.g., waves, grid)
│       │   │   └── ...      # Other components
│       │   ├── App.js       # Main application component and core logic
│       │   ├── App.css      # Main application styles
│       │   └── index.js     # Application entry point
│       └── package.json     # Frontend dependencies and scripts
├── .gitignore              # Specifies intentionally untracked files
├── LICENSE                 # Project license
├── README.md               # Project documentation (this file)
└── vercel.json             # Vercel configuration for routing serverless functions
```

## **Vercel Deployment**

This project is configured for easy deployment on Vercel. The `vercel.json` file at the root of the repository specifies how incoming requests are handled.

-   The `rewrites` rule in `vercel.json` routes all requests to `/api/*` to the `api/usisvercel.py` serverless function.
-   Vercel automatically detects the React application in the `USIS/usis-frontend` directory and builds/serves it as the frontend.

To deploy to Vercel:

1.  Push your changes to the `main` branch of your connected GitHub repository.
2.  Vercel will automatically detect the push and trigger a new build and deployment.
3.  Once the deployment is complete, your application will be live at your Vercel project URL.

### 🚨 Important: Clear Browser Cache After Deployment

After a new Vercel deployment, it is **highly recommended** to clear your browser's cache and cookies for the application's URL. This ensures that your browser loads the latest version of the frontend code, which is crucial for seeing recent changes and avoiding issues like outdated API endpoints being called.

## **Acknowledgements**

-   Based on the USIS course data structure.
-   Utilizes open-source libraries like React, Flask, Axios, date-fns, and html2canvas.

## **Contact**

For any questions, issues, or feedback, please open an issue on the GitHub repository.

## **Future Enhancements**

-   [ ] Dark mode support
-   [ ] Mobile responsiveness improvements
-   [ ] More advanced conflict resolution algorithms
-   [ ] Integration of course prerequisites checking
-   [ ] Analysis of GPA impact based on routine choices
-   [ ] Export routine to other formats (e.g., PDF, iCal)
-   [ ] Multi-language support 