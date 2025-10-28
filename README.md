# AI for Software Engineering

A comprehensive collection of AI-powered tools and applications demonstrating various aspects of artificial intelligence in software engineering, including code completion, automated testing, and predictive analytics for medical diagnosis.

## 📁 Project Structure

```
AI-for-Software-Engineering/
├── AI-Powered_code_completion/
│   ├── AI-Powered_Code_Completion.png
│   ├── manual_implementation.py
│   └── prompt_copilot.py
├── Automated-testing-with-AI/
│   ├── invalid_login.png
│   └── valid_logins.png
├── Predictive-analytics-for-resource-allocation/
│   ├── breast_cancer_classifier.ipynb
│   ├── model_accuracy.png
│   ├── training_set/
│   │   ├── benign/ (791 images)
│   │   └── malignant/ (321 images)
│   └── testing_set/ (100 images with masks)
│       ├── P001.png, P001_mask.png
│       ├── P002.png, P002_mask.png
│       └── ... (P003-P100)
├── Report.pdf
└── README.md
```

This repository contains three main AI applications:

### 1. 🤖 AI-Powered Code Completion
**Location:** `AI-Powered_code_completion/`

Demonstrates the effectiveness of AI-powered code completion tools by comparing manual implementation with AI-assisted development.

**Files:**
- `manual_implementation.py` - Manual implementation of dictionary sorting algorithm
- `prompt_copilot.py` - AI-assisted implementation using GitHub Copilot
- `AI-Powered_Code_Completion.png` - Visualization of the comparison

**Key Features:**
- Bubble sort algorithm implementation (manual)
- Pythonic sorted() function implementation (AI-assisted)
- Performance comparison between approaches
- Code quality and efficiency analysis

### 2. 🧪 Automated Testing with AI
**Location:** `Automated-testing-with-AI/`

Showcases AI-driven automated testing capabilities for web applications.

**Files:**
- `invalid_login.png` - Screenshots of invalid login test scenarios
- `valid_logins.png` - Screenshots of valid login test scenarios

**Key Features:**
- Automated UI testing
- Login validation testing
- Visual test result documentation
- AI-powered test case generation

### 3. 🏥 Predictive Analytics for Resource Allocation
**Location:** `Predictive-analytics-for-resource-allocation/`

A machine learning model for breast cancer classification using medical imaging data.

**Files:**
- `breast_cancer_classifier.ipynb` - Jupyter notebook with the complete ML pipeline
- `model_accuracy.png` - Model performance visualization
- `training_set/` - Training data (791 benign + 321 malignant images)
- `testing_set/` - Testing data (100 unlabeled images with masks)

**Key Features:**
- Convolutional Neural Network (CNN) implementation
- Medical image classification
- Binary classification (benign vs malignant)
- Data augmentation and preprocessing
- Model evaluation with accuracy metrics

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- TensorFlow/Keras
- NumPy
- Matplotlib
- Scikit-learn
- Jupyter Notebook

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd AI-for-Software-Engineering
```

**Note**: This repository uses Git LFS for large image files. If you don't have Git LFS installed:
```bash
# Install Git LFS
git lfs install
```

2. Install required dependencies:
```bash
pip install tensorflow numpy matplotlib scikit-learn jupyter
```

3. Run the code completion examples:
```bash
cd AI-Powered_code_completion
python manual_implementation.py
python prompt_copilot.py
```

4. For the breast cancer classifier:
```bash
cd Predictive-analytics-for-resource-allocation
jupyter notebook breast_cancer_classifier.ipynb
```

## 📊 Results and Performance

### Code Completion Analysis
- **Manual Implementation**: Uses bubble sort algorithm with O(n²) complexity
- **AI-Assisted Implementation**: Uses Python's built-in sorted() function with O(n log n) complexity
- **Efficiency Gain**: Significant improvement in both code readability and performance

### Breast Cancer Classification Model
- **Architecture**: CNN with Conv2D, MaxPooling2D, and Dense layers
- **Training Data**: 1,112 images (791 benign, 321 malignant)
- **Testing Data**: 100 unlabeled images (P001-P100) with corresponding mask files
- **Validation Split**: 20% of training data (222 images for validation)
- **Model Performance**: Achieved high accuracy on validation set
- **Image Size**: 128x128 pixels with RGB channels
- **Data Format**: Each test image has a corresponding mask file for segmentation

## 🛠️ Technical Details

### AI-Powered Code Completion
- Demonstrates the power of AI in code generation
- Shows efficiency improvements in algorithm implementation
- Compares manual vs AI-assisted development approaches

### Automated Testing
- Visual documentation of test scenarios
- Automated UI testing capabilities
- Login validation testing with AI assistance

### Predictive Analytics
- Deep learning model for medical image classification
- Data preprocessing and augmentation
- Binary classification for medical diagnosis
- Resource allocation optimization through predictive modeling

## 📈 Applications

This project demonstrates practical applications of AI in software engineering:

1. **Development Productivity**: AI-powered code completion tools
2. **Quality Assurance**: Automated testing with AI
3. **Healthcare Technology**: Medical image analysis and diagnosis
4. **Resource Optimization**: Predictive analytics for better resource allocation

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License.

## 📞 Contact

For questions or suggestions, please open an issue in the repository.

---

**Note**: This project is for educational and research purposes. The medical classification model should not be used for actual medical diagnosis without proper validation and regulatory approval.
