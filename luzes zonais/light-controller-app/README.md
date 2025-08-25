# Light Controller App

This project is a simple Streamlit application that allows users to control the intensity of four lights, each with three levels of intensity. 

## Features

- Control up to four lights.
- Set intensity levels for each light (Low, Medium, High).
- User-friendly interface built with Streamlit.

## Project Structure

```
light-controller-app
├── src
│   ├── app.py          # Entry point of the Streamlit application
│   └── controller.py   # Contains the LightController class
├── requirements.txt    # Lists the project dependencies
└── README.md           # Documentation for the project
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/light-controller-app.git
   cd light-controller-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command in your terminal:
```
streamlit run src/app.py
```

Open your web browser and go to `http://localhost:8501` to access the application.

## License

This project is licensed under the MIT License.