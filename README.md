

# StorageBox

A free web application that allows users to store and share unlimited data files (each file size must be less than 5MB) and obtain shortened URLs for easy sharing.

## Features
- Lifetime Storage: Store your files securely without worrying about expiration dates or storage limits.

- Privacy: Your files are stored securely and are only accessible to you and those you choose to share the shortened URLs with.

- All Types of Files Accepted: Upload any type of file, ranging from documents to images, videos, and more.

- Quick and Convenient Sharing: Obtain shortened URLs for each uploaded file, making it easy to share them with others.

## Installation

1. Clone the repository:
``` 
git clone https://github.com/samay15jan/storage-box.git
```

2. Install the required dependencies:
```
pip install -r requirements.txt
```

3. Set up Google API credentials:

- Visit the Google Cloud Console.
- Create a new project or select an existing project.
- Enable the Google Drive API for the project.
- Create credentials (OAuth 2.0 client ID) for your project, selecting "Web application" as the application type.
- Download the credentials JSON file and save it as credentials.json in the project's root directory.

4. Set up ApiLayer API:
- Visit ApiLayer's website. [here](https://apilayer.com/marketplace/short_url-api)
- Create a account and copy the apikey to main.py under 'def home()' function.
- Create and link shared folders manually of multiple google drives.
- Copy the all folder ID's to folder_id.txt file

5. Run the application:
```
python main.py
```

Access the application in your web browser at http://localhost:5000.

6. Usage

- Sign in using your Google account once.
- Upload your desired files (each file must be less than 5MB).
- The application will automatically upload the files to one of the random shared folders linked to your account.
- Obtain the shortened URL for each uploaded file.
- Share the shortened URLs with others for quick and convenient access to the files.

6. Hosting:
If you want to host the project online for free you can use [pythonanywhere](https://www.pythonanywhere.com/)

## Known Issues
- Tokens generated from google in token.pickle file will expire every 7 days. 
- ApiLayer have monthly limits on api request but will be more than enough for personal use.


## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit/).

Feel free to customize this template according to your needs, and don't forget to add appropriate sections such as "Credits," "Acknowledgments," or any additional sections you find necessary.
