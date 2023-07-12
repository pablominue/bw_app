ECHO Creating folders...
current_user=$(whoami)
mkdir C:/Users/$current_user/KivyApps
mkdir C:/Users/$current_user/KivyApps/BWAnalytics
cd C:/Users/$current_user/KivyApps

ECHO Creating Environment...
python -m pip install --upgrade pip setuptools virtualenv
python -m virtualenv kivy_venv
source kivy_venv/Scripts/activate

ECHO Installing Dependencies...
pip install Kivy==2.2.1
pip install kivy-deps.angle==0.3.3
pip install kivy-deps.glew==0.3.1
pip install kivy-deps.gstreamer==0.3.3
pip install kivy-deps.sdl2==0.6.0
pip install Kivy-examples==2.2.1
pip install Kivy-Garden==0.1.5
pip install certifi==2023.5.7
pip install cffi==1.15.1
pip install charset-normalizer==3.2.0
pip install cryptography==41.0.1
pip install docutils==0.20.1
pip install idna==3.4
pip install joblib==1.3.1
pip install kivymd==1.1.1
pip install numpy==1.25.1
pip install pandas==2.0.3
pip install Pillow==10.0.0
pip install pycparser==2.21
pip install Pygments==2.15.1
pip install pyOpenSSL==23.2.0
pip install pypiwin32==223
pip install python-dateutil==2.8.2
pip install pytz==2023.3
pip install pywin32==306
pip install requests==2.31.0
pip install scikit-learn==1.3.0
pip install scipy==1.11.1
pip install six==1.16.0
pip install threadpoolctl==3.1.0
pip install tzdata==2023.3
pip install urllib3==2.0.3

ECHO Dependencies Installed!
ECHO Cloning Repository...
cd BWAnalytics
git clone https://github.com/pablominue/bw_app.git

ECHO Done!
ECHO Openning App...

python BW_APP/main.py