# Mental Energy Level Tracker

This is a simple desktop application designed to help individuals track and manage their mental energy levels throughout the day. This tool provides a structured way to assess cognitive resources, helping users identify patterns and make informed decisions about when to rest, recharge, or push forward.

![Python](https://img.shields.io/badge/python-3.6+-blue.svg)

![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 Overview

The Mental Energy Level Tracker helps answer the question "How much mental energy do I have?" in a concrete, measurable way. By breaking down mental energy into specific components like focus, decision-making ability, and processing speed, the application provides a system for self-assessment that helps users:

* Track fluctuations in mental energy throughout the day
* Identify patterns in cognitive fatigue
* Make informed decisions about when to take breaks
* Communicate needs to others based on objective measurements
* Build self-awareness about personal cognitive resources

## ✨ Features

* **Categorized Assessment**: Evaluate six distinct aspects of mental energy
* **Simple Rating System**: Easy-to-use Good/Moderate/Poor ratings with visual color coding
* **Notes Field**: Add context or observations to each entry
* **Data Storage**: All entries are saved to a local SQLite database
* **History View**: Review past entries to identify patterns over time

## 🔧 Installation

### Requirements

* Python 3.6 or higher
* Tkinter (usually included with Python installation)
* SQLite3 (included in Python's standard library)

### Setup Instructions

1. Clone this repository:

```bash
   git clone https://github.com/pdxiv/mental-energy-level-tracker.git
   cd mental-energy-level-tracker
```

2. No additional package installation is required as the application uses only standard libraries.

3. Run the application:
   

```
   python mental_energy_level_tracker.py
```

## 🚀 Usage

1. Launch the application using the command above
2. Answer the questions in each category by selecting the appropriate rating:
   - **Good (green)** – No issues, feels clear and sharp
   - **Moderate (yellow)** – Mild issues; still functional, but requires noticeable effort
   - **Poor (red)** – Significant difficulty; tasks feel very challenging
3. Add any notes or context in the text field (optional)
4. Click "Submit Entry" to save your assessment
5. View your history of entries by clicking "View History"
6. Use the "Clear Form" button to reset all fields

## 📊 Assessment Categories

The application breaks down mental energy into six key components:

### **1. Focus & Attention**

* Can I easily concentrate on what I'm doing?
* Am I having trouble following conversations or written text?
* Do I have to reread or relisten frequently?

### **2. Decision-making & Problem-solving**

* Is it hard to make simple decisions right now (e.g., deciding what to eat)?
* Does solving simple tasks seem complicated or overwhelming?

### **3. Memory & Recall**

* Am I forgetting simple things (like why I entered a room, or what I was about to do)?
* Am I struggling to recall words, names, or common facts?

### **4. Processing Speed**

* Does my thinking feel unusually slow or sluggish?
* Am I slower to respond to questions than usual?

### **5. Sharpness & Alertness**

* Does my thinking feel fuzzy, unclear, or foggy?
* Am I misreading or misunderstanding things I usually wouldn't?

### **6. Ease of Communication**

* Am I having trouble clearly expressing my thoughts?
* Am I unusually hesitant or stumbling when speaking?

## 📈 Interpreting Your Results

The rating system helps you objectively measure your current mental energy state:

* **All Green (Good)**: Your cognitive resources are fully available
* **Some Yellow (Moderate)**: You're experiencing some mental fatigue, but can still function
* **Multiple Yellow or Any Red**: This is your signal to take action - it's time for a break or to step back and recharge

**Important**: If you find multiple indicators at Moderate or any at Poor, it's a clear sign that you should take a break or step back to recharge. This threshold helps prevent more extensive fatigue.

## 💡 Tips for Effective Use

* **Regular check-ins**: Try to assess your mental energy level at consistent intervals (e.g., morning, midday, evening)
* **Preventative use**: Check in before you feel completely depleted to catch early warning signs
* **Pattern recognition**: After several days of use, look for patterns in your history to identify:
  + Times of day when your mental energy level is typically highest/lowest
  + Activities that seem to drain your mental energy level quickly
  + Environmental factors that might impact your cognitive resources
* **Communicating needs**: Use your assessments to help explain your needs to others in objective terms

## 🛠️ Technical Details

* **Data Storage**: All entries are stored in an SQLite database in the `data` folder
* **UI Framework**: Built with Tkinter for cross-platform compatibility
* **Responsive Design**: The interface automatically adjusts to different window sizes

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! If you'd like to contribute, please:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add some feature'`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

## 📬 Contact

If you have questions or feedback, please open an issue on this repository.
