from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Career database with required skills and descriptions
CAREERS = {
    "Software Developer": {
        "description": "Design, develop, and maintain software applications",
        "required_skills": ["Programming", "Problem Solving", "Data Structures", "Algorithms", "Version Control"],
        "interests": ["Technology", "Problem Solving", "Mathematics", "Innovation"],
        "academic_backgrounds": ["Computer Science", "Information Technology", "Software Engineering", "Mathematics"],
        "learning_resources": [
            "Learn programming languages (Python, JavaScript, Java)",
            "Master data structures and algorithms",
            "Practice on LeetCode, HackerRank",
            "Build personal projects and portfolio",
            "Contribute to open-source projects"
        ]
    },
    "Data Scientist": {
        "description": "Analyze complex data to help organizations make better decisions",
        "required_skills": ["Python", "Statistics", "Machine Learning", "Data Analysis", "SQL"],
        "interests": ["Mathematics", "Statistics", "Problem Solving", "Research"],
        "academic_backgrounds": ["Computer Science", "Statistics", "Mathematics", "Data Science", "Engineering"],
        "learning_resources": [
            "Learn Python and R for data analysis",
            "Study statistics and probability",
            "Master machine learning algorithms",
            "Complete Kaggle competitions",
            "Get certifications from Coursera or edX"
        ]
    },
    "Web Developer": {
        "description": "Create and maintain websites and web applications",
        "required_skills": ["HTML", "CSS", "JavaScript", "React", "Backend Development"],
        "interests": ["Technology", "Design", "Creativity", "Problem Solving"],
        "academic_backgrounds": ["Computer Science", "Information Technology", "Web Development", "Design"],
        "learning_resources": [
            "Learn HTML, CSS, and JavaScript fundamentals",
            "Master frontend frameworks (React, Vue, Angular)",
            "Learn backend technologies (Node.js, Python, PHP)",
            "Build responsive web designs",
            "Create a portfolio website"
        ]
    },
    "Mobile App Developer": {
        "description": "Develop applications for mobile devices (iOS, Android)",
        "required_skills": ["Mobile Development", "Java", "Swift", "React Native", "UI/UX Design"],
        "interests": ["Technology", "Design", "Innovation", "Problem Solving"],
        "academic_backgrounds": ["Computer Science", "Information Technology", "Software Engineering"],
        "learning_resources": [
            "Learn Swift for iOS or Kotlin/Java for Android",
            "Study mobile app design principles",
            "Master React Native or Flutter for cross-platform",
            "Publish apps on App Store and Google Play",
            "Follow mobile development best practices"
        ]
    },
    "Cybersecurity Analyst": {
        "description": "Protect computer systems and networks from security threats",
        "required_skills": ["Network Security", "Ethical Hacking", "Risk Assessment", "Cryptography", "Programming"],
        "interests": ["Technology", "Security", "Problem Solving", "Investigation"],
        "academic_backgrounds": ["Computer Science", "Information Security", "Network Engineering", "IT"],
        "learning_resources": [
            "Get CompTIA Security+ certification",
            "Learn ethical hacking and penetration testing",
            "Study network protocols and security",
            "Practice on TryHackMe and HackTheBox",
            "Get CISSP or CEH certification"
        ]
    },
    "Digital Marketing Specialist": {
        "description": "Plan and execute digital marketing campaigns",
        "required_skills": ["SEO", "Social Media Marketing", "Content Marketing", "Analytics", "Communication"],
        "interests": ["Marketing", "Communication", "Creativity", "Business"],
        "academic_backgrounds": ["Marketing", "Business", "Communications", "Media Studies"],
        "learning_resources": [
            "Get Google Analytics certification",
            "Learn SEO and SEM fundamentals",
            "Master social media platforms",
            "Study content marketing strategies",
            "Get HubSpot or Google Ads certification"
        ]
    },
    "Product Manager": {
        "description": "Lead product development from conception to launch",
        "required_skills": ["Product Strategy", "Market Research", "Project Management", "Communication", "Analytics"],
        "interests": ["Business", "Technology", "Leadership", "Strategy"],
        "academic_backgrounds": ["Business", "Computer Science", "Engineering", "Marketing"],
        "learning_resources": [
            "Learn product management frameworks",
            "Study agile and scrum methodologies",
            "Get PMP or Scrum Master certification",
            "Build case studies and portfolio",
            "Network with product management communities"
        ]
    },
    "UX/UI Designer": {
        "description": "Design user-friendly and visually appealing interfaces",
        "required_skills": ["User Research", "Wireframing", "Prototyping", "Visual Design", "Design Tools"],
        "interests": ["Design", "Creativity", "Psychology", "Technology"],
        "academic_backgrounds": ["Design", "Computer Science", "Psychology", "Human-Computer Interaction"],
        "learning_resources": [
            "Master Figma, Sketch, or Adobe XD",
            "Study user research methodologies",
            "Learn design thinking principles",
            "Build a design portfolio",
            "Take courses on Interaction Design Foundation"
        ]
    },
    "Business Analyst": {
        "description": "Analyze business processes and recommend improvements",
        "required_skills": ["Business Analysis", "Data Analysis", "Communication", "Problem Solving", "SQL"],
        "interests": ["Business", "Analysis", "Strategy", "Problem Solving"],
        "academic_backgrounds": ["Business", "Economics", "Computer Science", "Management"],
        "learning_resources": [
            "Get CBAP certification",
            "Learn business process modeling",
            "Master data analysis tools",
            "Study business intelligence platforms",
            "Develop domain expertise in specific industries"
        ]
    },
    "Cloud Engineer": {
        "description": "Design, implement, and manage cloud infrastructure",
        "required_skills": ["Cloud Platforms", "DevOps", "Networking", "Security", "Automation"],
        "interests": ["Technology", "Infrastructure", "Problem Solving", "Innovation"],
        "academic_backgrounds": ["Computer Science", "Information Technology", "Engineering"],
        "learning_resources": [
            "Get AWS, Azure, or Google Cloud certification",
            "Learn containerization (Docker, Kubernetes)",
            "Master infrastructure as code (Terraform)",
            "Study cloud security best practices",
            "Build cloud-based projects"
        ]
    }
}

def calculate_match_score(student_profile, career_data):
    """Calculate how well a student matches a career path"""
    score = 0
    max_score = 0
    
    # Check skills match (40% weight)
    student_skills = set(skill.lower() for skill in student_profile.get('skills', []))
    required_skills = set(skill.lower() for skill in career_data['required_skills'])
    if required_skills:
        skill_match = len(student_skills & required_skills) / len(required_skills)
        score += skill_match * 40
    max_score += 40
    
    # Check interests match (30% weight)
    student_interests = set(interest.lower() for interest in student_profile.get('interests', []))
    career_interests = set(interest.lower() for interest in career_data['interests'])
    if career_interests:
        interest_match = len(student_interests & career_interests) / len(career_interests)
        score += interest_match * 30
    max_score += 30
    
    # Check academic background match (30% weight)
    student_background = student_profile.get('academic_background', '').lower()
    matching_backgrounds = [bg.lower() for bg in career_data['academic_backgrounds']]
    if any(bg in student_background or student_background in bg for bg in matching_backgrounds):
        score += 30
    max_score += 30
    
    return (score / max_score * 100) if max_score > 0 else 0

def get_skill_gaps(student_skills, required_skills):
    """Identify skills the student needs to develop"""
    student_skills_lower = set(skill.lower() for skill in student_skills)
    required_skills_lower = set(skill.lower() for skill in required_skills)
    gaps = required_skills_lower - student_skills_lower
    
    # Return the original case version of the gaps
    gap_skills = []
    for gap in gaps:
        for req_skill in required_skills:
            if req_skill.lower() == gap:
                gap_skills.append(req_skill)
                break
    
    return gap_skills

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "timestamp": datetime.now().isoformat()})

@app.route('/api/careers', methods=['GET'])
def get_careers():
    """Get list of all available careers"""
    career_list = [
        {
            "name": name,
            "description": data["description"],
            "required_skills": data["required_skills"]
        }
        for name, data in CAREERS.items()
    ]
    return jsonify({"careers": career_list})

@app.route('/api/recommend', methods=['POST'])
def recommend_careers():
    """Recommend career paths based on student profile"""
    try:
        student_profile = request.json
        
        # Validate input
        if not student_profile:
            return jsonify({"error": "No student profile provided"}), 400
        
        # Calculate match scores for all careers
        recommendations = []
        for career_name, career_data in CAREERS.items():
            match_score = calculate_match_score(student_profile, career_data)
            
            # Get skill gaps
            skill_gaps = get_skill_gaps(
                student_profile.get('skills', []),
                career_data['required_skills']
            )
            
            recommendations.append({
                "career_name": career_name,
                "description": career_data["description"],
                "match_score": round(match_score, 2),
                "required_skills": career_data["required_skills"],
                "skill_gaps": skill_gaps,
                "learning_resources": career_data["learning_resources"],
                "matching_interests": list(
                    set(interest.lower() for interest in student_profile.get('interests', [])) &
                    set(interest.lower() for interest in career_data['interests'])
                )
            })
        
        # Sort by match score (descending)
        recommendations.sort(key=lambda x: x['match_score'], reverse=True)
        
        # Return top recommendations
        return jsonify({
            "recommendations": recommendations,
            "student_profile": student_profile,
            "timestamp": datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/skills', methods=['GET'])
def get_all_skills():
    """Get list of all available skills across all careers"""
    all_skills = set()
    for career_data in CAREERS.values():
        all_skills.update(career_data['required_skills'])
    
    return jsonify({"skills": sorted(list(all_skills))})

@app.route('/api/interests', methods=['GET'])
def get_all_interests():
    """Get list of all interests"""
    all_interests = set()
    for career_data in CAREERS.values():
        all_interests.update(career_data['interests'])
    
    return jsonify({"interests": sorted(list(all_interests))})

if __name__ == '__main__':
    # For development, set debug=True
    # For production, set debug=False or use environment variable
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
