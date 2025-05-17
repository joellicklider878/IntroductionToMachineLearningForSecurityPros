# IntroductionToMachineLearningForSecurityPros
Changes needed for setup.sh script on wsl2 for windows 11
# notes
install dos2unix for newline problems with setup.sh
convert script to UNIX format
dependency problem with ssdeep
change sklearn to scikit-learn
run python 3 in virtual environment - source venv/bin/activate
# applications
sudo apt-get install dos2unix
dos2unix script.sh
sudo apt-get install libfuzzy-dev
sudo apt-get install python3-venv
# format
updated python 2 scripts to python 3

created folders for deep_learning_examples
data/
	      dataset.py
	      test-train.py
    processed/
	      lstm_model.h5
	      X_train.py
	      y_train.py
src/
	 classify_with_model.py
	 generate_xor.py
	 lstm-lr-0.001-od-256-oa-softmax-a-relu.keras
	 train_model.py
	 train_xor.sh

changed requirements.txt
