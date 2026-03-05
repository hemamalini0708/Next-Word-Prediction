# Next Word Prediction

> Deep Learning Model for Text Prediction using LSTM and Neural Networks

---

## Overview

A machine learning application that predicts the next word in a sentence using **LSTM (Long Short-Term Memory)** neural networks. The model is trained on "The Adventures of Sherlock Holmes" by Arthur Conan Doyle and deployed using **Streamlit** for easy interaction.

---

## Project Details

**Dataset:** The Adventures of Sherlock Holmes (104,527 words)  
**Algorithm:** Embedding + LSTM + Dense layers  
**Training:** 50 epochs with Adam optimizer  
**Framework:** TensorFlow/Keras  
**Deployment:** Streamlit web application  

---

## Project Structure

```
.
├── Next_Word_Prediction.ipynb  # Jupyter notebook (training & evaluation)
├── app.py                      # Streamlit application
├── next_words.h5              # Trained model
├── token.pkl                  # Tokenizer pickle file
├── data.txt                   # Training dataset
└── README.md
```

---

##  Tech Stack

- **Python 3**
- **TensorFlow / Keras** - Deep Learning
- **Streamlit** - Web Interface
- **NumPy** - Numerical Computing
- **Pickle** - Serialization

---

##  How It Works

1. **Data Preprocessing:** Text cleaned and tokenized from data.txt
2. **Tokenization:** Vocabulary created from 105,879 token sequences
3. **Model Training:** LSTM neural network with embedding layer (50 epochs)
4. **Prediction:** Takes last 3 words → predicts next word using the trained model
5. **Deployment:** Streamlit interface for real-time predictions

---

##  Features

✅ **LSTM-based Architecture** - Learns sequential patterns  
✅ **Real-time Predictions** - Instant next word suggestions  
✅ **Text Preprocessing** - Handles multiple special characters  
✅ **User-Friendly Interface** - Simple Streamlit web app  
✅ **High Accuracy** - Trained on classic literature dataset  

---

##  Model Architecture

```
Input (Sequence) → Embedding (128 dims) → LSTM (256 units) → Dense → Output
```

**Parameters:**
- Vocabulary Size: ~6500 words
- Max Sequence Length: 32
- Embedding Dimensions: 128
- LSTM Units: 256
- Training Loss: 0.457 (final epoch)

---

##  Installation & Setup

### Prerequisites
```bash
pip install streamlit tensorflow numpy pickle
```

### Run the Application
```bash
streamlit run app.py
```

---

##  Usage Example

1. Start the Streamlit app
2. Enter text (e.g., "A Scandal in Bohemia")
3. Click "Predict" button
4. Get the next word prediction

**Example:**
- Input: "A Scandal in"
- Output: "Bohemia"

---

##  Training Details

- **Epochs:** 50
- **Optimizer:** Adam
- **Loss Function:** Categorical Crossentropy
- **Batch Size:** 32
- **GPU:** T4 (trained on Google Colab)

---

##  Files Explanation

| File | Purpose |
|------|---------|
| `Next_Word_Prediction.ipynb` | Model training & testing notebook |
| `app.py` | Streamlit web application |
| `next_words.h5` | Trained LSTM model |
| `token.pkl` | Serialized tokenizer |
| `data.txt` | Training corpus (Sherlock Holmes) |

---

##  Key Learnings

- LSTM networks for sequence prediction
- Text tokenization and preprocessing
- Model serialization with Pickle
- Deploying ML models with Streamlit
- Sequence padding and padding sequences

---

##  Future Improvements

- Increase training data for better accuracy
- Multi-word prediction
- Beam search for better candidates
- API deployment
- Mobile app interface

---

##  License

MIT License

---

##  Author

**Hema Malini**  
GitHub: [@hemamalini0708](https://github.com/hemamalini0708)  
LinkedIn: [Hema Malini](https://www.linkedin.com/in/hema-malini-1434bb29b)

---

<div align="center">

### ⭐ If you find this useful, please star the repository!

</div>
