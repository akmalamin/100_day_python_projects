# Password Manager 🔐

A simple and secure password manager built with Python and Tkinter.

## Features

- 🔑 **Password Generator**: Creates strong, random passwords
- 💾 **Save Passwords**: Store website credentials securely
- 📋 **Clipboard Copy**: Automatically copies generated passwords
- ✅ **Validation**: Ensures all fields are filled before saving
- 🎨 **Clean UI**: Simple and intuitive interface


## Requirements

- Python 3.6+
- tkinter (usually comes with Python)
- pyperclip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/akmal_amin/password-manager.git
cd password-manager
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python password_manager.py
```

## Usage

1. **Enter Website**: Type the website name or URL
2. **Enter Email/Username**: Your login email or username
3. **Generate Password**: Click "Generate Password" to create a strong random password (automatically copied to clipboard)
4. **Save**: Click "Add" to save your credentials

All passwords are saved to `data.txt` in the format:
```
website | email | password
```

## Password Generation

The password generator creates strong passwords with:
- 8-12 random letters (uppercase and lowercase)
- 2-4 random numbers
- 2-4 random special characters

## Security Note

⚠️ **Important**: This is a basic password manager for learning purposes. For production use, consider:
- Encrypting the `data.txt` file
- Using a master password
- Implementing secure storage solutions
- Using established password managers like Bitwarden or 1Password

## File Structure

```
password-manager/
├── password_manager.py    # Main application
├── logo.png              # Application logo (optional)
├── data.txt             # Stored passwords (created automatically)
├── requirements.txt     # Python dependencies
├── README.md           # Project documentation
└── .gitignore         # Git ignore rules
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).

## Future Enhancements

- [ ] Search functionality to find saved passwords
- [ ] Encryption for stored passwords
- [ ] Master password protection
- [ ] Password strength indicator
- [ ] Export/Import functionality
- [ ] Dark mode
- [ ] Cross-platform packaging

## Author

Your Name - [Your GitHub Profile](https://github.com/akmalamin)

## Acknowledgments

- Built as a learning project for Python GUI development
- Inspired by modern password management needs
