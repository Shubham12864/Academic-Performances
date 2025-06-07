# Student Performance Analysis

This project is designed to analyze the academic performance of students in a Bachelor of Computer Applications (BCA) program. It utilizes Streamlit for the frontend to visualize data through various charts and analyses.

## Project Structure

```
student-performance-analysis
├── src
│   ├── app.py                  # Main entry point for the Streamlit application
│   ├── data
│   │   └── students_data.py    # Generates random student performance data
│   ├── analysis
│   │   └── performance_analysis.py # Contains functions for data analysis
│   └── utils
│       └── charts.py           # Functions to create visualizations
├── requirements.txt             # Lists project dependencies
├── config.py                    # Configuration settings for the application
└── README.md                    # Documentation for the project
```

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/student-performance-analysis.git
   cd student-performance-analysis
   ```

2. **Install Dependencies**
   Ensure you have Python installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Start the Streamlit application by executing:
   ```bash
   streamlit run src/app.py
   ```

## Usage Guidelines

- Upon running the application, you will see a dashboard displaying various charts representing the academic performance of students.
- The data is randomly generated, with the first student named Ankit. You can explore different visualizations to analyze performance across five subjects.

## Project Functionality

- **Data Generation**: The project generates random data for students' academic performances in five subjects.
- **Data Analysis**: It calculates averages, pass rates, and other relevant statistics to provide insights into student performance.
- **Visualization**: Various types of charts (bar charts, pie charts, line graphs) are created to visualize the analysis results effectively.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.