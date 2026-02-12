# Personalized Career Path Recommendation System

A full-stack web application that analyzes a student's interests, current skills, and academic background to recommend suitable career paths along with required skills and learning suggestions.

## Features

- **Personalized Recommendations**: Get career suggestions based on your unique profile
- **Skill Gap Analysis**: Identify which skills you need to develop for each career
- **Learning Resources**: Receive curated learning paths and resources for each recommended career
- **Match Scoring**: See how well you match each career path (percentage-based)
- **Interactive UI**: User-friendly interface with real-time recommendations
- **Multiple Career Options**: Covers 10+ career paths including Software Development, Data Science, Web Development, and more

## Technology Stack

### Backend
- **Flask**: Python web framework for RESTful API
- **Flask-CORS**: Cross-Origin Resource Sharing support
- **Python 3.x**: Programming language

### Frontend
- **HTML5/CSS3**: Modern, responsive design
- **Vanilla JavaScript**: For dynamic interactions
- **No build tools required**: Simple setup and deployment

## Project Structure

```
Personalized-Career-Path-Recommendation-System/
├── backend/
│   ├── app.py              # Flask application with API endpoints
│   └── requirements.txt    # Python dependencies
├── frontend/
│   ├── index.html          # Single-page application
│   └── package.json        # Frontend metadata
└── README.md               # This file
```

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- A modern web browser

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Start the Flask server:
```bash
python app.py
```

The backend server will start on `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:
```bash
cd frontend
```

2. Open `index.html` in your web browser, or serve it using a simple HTTP server:

**Option 1 - Direct file open:**
- Simply double-click `index.html` to open it in your browser

**Option 2 - Using Python's HTTP server:**
```bash
python -m http.server 8000
```
Then visit `http://localhost:8000`

**Option 3 - Using Node.js http-server:**
```bash
npx http-server -p 8000
```
Then visit `http://localhost:8000`

## Usage

1. **Start the Backend**: Make sure the Flask backend is running on port 5000
2. **Open the Frontend**: Open `index.html` in your browser
3. **Fill Out Your Profile**:
   - Enter your name
   - Select your academic background
   - Check your areas of interest
   - Select your current skills
4. **Get Recommendations**: Click "Get Career Recommendations"
5. **Review Results**: 
   - See career paths ranked by match percentage
   - Review required skills (red tags show skills you need to develop)
   - Explore learning resources for each career

## API Endpoints

### GET /api/health
Health check endpoint
```json
{
  "status": "healthy",
  "timestamp": "2024-01-01T12:00:00"
}
```

### GET /api/careers
Get list of all available careers
```json
{
  "careers": [
    {
      "name": "Software Developer",
      "description": "...",
      "required_skills": [...]
    }
  ]
}
```

### GET /api/skills
Get list of all available skills
```json
{
  "skills": ["Programming", "Python", "JavaScript", ...]
}
```

### GET /api/interests
Get list of all interests
```json
{
  "interests": ["Technology", "Problem Solving", ...]
}
```

### POST /api/recommend
Get career recommendations based on student profile

**Request Body:**
```json
{
  "name": "John Doe",
  "academic_background": "Computer Science",
  "interests": ["Technology", "Problem Solving"],
  "skills": ["Programming", "Python"]
}
```

**Response:**
```json
{
  "recommendations": [
    {
      "career_name": "Software Developer",
      "description": "...",
      "match_score": 85.5,
      "required_skills": [...],
      "skill_gaps": [...],
      "learning_resources": [...],
      "matching_interests": [...]
    }
  ],
  "student_profile": {...},
  "timestamp": "2024-01-01T12:00:00"
}
```

## Career Paths Included

1. **Software Developer** - Design and develop software applications
2. **Data Scientist** - Analyze complex data for decision-making
3. **Web Developer** - Create and maintain websites
4. **Mobile App Developer** - Develop mobile applications
5. **Cybersecurity Analyst** - Protect systems from security threats
6. **Digital Marketing Specialist** - Plan digital marketing campaigns
7. **Product Manager** - Lead product development
8. **UX/UI Designer** - Design user-friendly interfaces
9. **Business Analyst** - Analyze business processes
10. **Cloud Engineer** - Design and manage cloud infrastructure

## Algorithm

The recommendation system uses a weighted scoring algorithm:

- **Skills Match (40%)**: Compares student's current skills with required skills
- **Interests Match (30%)**: Matches student interests with career-related interests
- **Academic Background (30%)**: Checks alignment with suitable academic backgrounds

Each career receives a match score (0-100%), and results are sorted by relevance.

## Future Enhancements

- User authentication and profile saving
- Database integration for persistent storage
- Machine learning-based recommendations
- Industry trends and salary information
- Course recommendations from online platforms
- Interview preparation resources
- Career progression paths
- Mentor matching system

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Chaitra (2410030171)

## Acknowledgments

- Career data compiled from industry standards and job market research
- Learning resources curated from popular educational platforms