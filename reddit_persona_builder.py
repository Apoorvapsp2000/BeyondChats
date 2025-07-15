import praw

# ✅ Step 1: Connect to Reddit API
reddit = praw.Reddit(
    client_id="I3D_cmf9WnhkeekE2kUBIA",
    client_secret="Sg4G5tYnBGO-glkBWhKN5FxLkbZD1w",
    user_agent="persona_script by u/PersonaApp1",
    username="PersonaApp1",
    password="PersonaApp"  # ⚠️ Replace with your Reddit password
)

# ✅ Step 2: Ask for a Reddit user profile URL
profile_url = input("Enter a Reddit user profile URL (e.g. https://www.reddit.com/user/Hungry-Move-6603/): ").strip()
target_username = profile_url.rstrip("/").split("/")[-1]

# ✅ Step 3: Fetch posts and comments
try:
    user = reddit.redditor(target_username)

    print(f"\n🔎 Fetching data for u/{target_username}...")

    posts = [post for post in user.submissions.new(limit=30)]
    comments = [comment for comment in user.comments.new(limit=30)]

    print(f"✅ Fetched {len(posts)} posts and {len(comments)} comments.\n")

    # ✅ Step 4: Format all data into a single string
    user_data = ""
    for post in posts:
        user_data += f"📝 Post Title: {post.title}\n📄 Content: {post.selftext}\n\n"
    for comment in comments:
        user_data += f"💬 Comment: {comment.body}\n\n"

    # ✅ Save raw data for review or LLM input
    with open(f"{target_username}_raw_data.txt", "w", encoding="utf-8") as file:
        file.write(user_data)

    print(f"📁 Saved user activity to {target_username}_raw_data.txt")

except Exception as e:
    print("❌ Failed to fetch data. Check the username or login credentials.")
    print("Error:", e)
