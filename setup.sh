# Create venv.

python3 -m venv tensile-venv
source tensile-venv/bin/activate

pip install -r requirements.txt

git submodules update --init
