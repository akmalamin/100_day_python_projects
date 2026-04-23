# Quick Start Guide 🚀

## Setup (5 minutes)

### Step 1: Install Python
Make sure you have Python 3.6 or higher installed.
```bash
python --version
```

### Step 2: Install Dependencies
```bash
pip install pyperclip
```

### Step 3: Run the Application
```bash
python password_manager.py
```

## How to Use

### Generating a Password
1. Enter the website name
2. Enter your email/username
3. Click **"Generate Password"** - it will create a strong password and copy it to your clipboard
4. Click **"Add"** to save

### Manually Entering a Password
1. Fill in all three fields
2. Click **"Add"**
3. Confirm in the dialog box

### Finding Your Passwords
Open `data.txt` in any text editor to view all saved passwords.

## Tips

- The default email is pre-filled - change it to your most-used email
- Generated passwords are automatically copied to clipboard
- Keep `data.txt` secure and backed up
- Don't commit `data.txt` to GitHub (it's already in .gitignore)

## Uploading to GitHub

```bash
# Initialize git repository
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Password Manager application"

# Add your GitHub repository
git remote add origin https://github.com/yourusername/password-manager.git

# Push to GitHub
git branch -M main
git push -u origin main
```

Remember to update the README.md with your actual GitHub username!
