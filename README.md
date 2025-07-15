# Reddit User Persona Builder ::
# Project Contents

| File | Description |
| `reddit_persona_builder.py` | Main script to scrape Reddit posts/comments of a user |
| `Hungry-Move-6603_raw_data.txt` | Sample raw user data scraped from Reddit |
| `Hungry-Move-6603_persona.txt` | Sample persona generated manually via ChatGPT |
| `README.md` | Project setup and usage instructions |

----Setup Instructions-----

### 1. Install Python Requirements

Make sure Python 3.8+ is installed.  
Then install the required Reddit library:
``bash
pip install praw

### 2. Create a Reddit App

Go to https://www.reddit.com/prefs/apps
Click Create App
Set the type to script
Fill in:
Name: PersonaApp
Redirect URI: http://localhost
Copy the:
client_id
client_secret

### 3. Edit the Script with Your Credentials
Open reddit_persona_builder.py and insert your Reddit app details:
python 
Copy Edit
reddit = praw.Reddit(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_SECRET",
    user_agent="persona_script by u/YOUR_USERNAME",
    username="YOUR_USERNAME",
    password="YOUR_REDDIT_PASSWORD"
)

### 4. Running the Tool
Step 1: Scrape a Reddit Profile
Run the script:
bash:
Copy Edit
python reddit_persona_builder.py

Step 2: Generate the Persona 
Open the file Hungry-Move-6603_raw_data.txt
Open ChatGPT and paste this prompt:
sql
Copy
Edit
You are a persona builder AI.

Here is a Reddit user’s post and comment history. Analyze it and write a complete user persona that includes:
- Name (you can assume one)
- Age range (based on clues)
- Interests and hobbies
- Personality traits
- Preferred subreddits
- Political/ideological leanings (if any)
- Writing style and tone
- Anything else noticeable

Step 3: Save the Persona
as
Hungry-Move-6603_persona.txt


