

================URL https://www.omgubuntu.co.uk/2016/08/peek-desktop-gif-screen-recorder-linux
1. Peek
sudo add-apt-repository ppa:peek-developers/stable
sudo apt update
sudo apt install peek

2.Gifine
sudo apt install ffmpeg graphicsmagick gifsicle luarockscmake \
compiz gengetopt slop libxext-dev libimlib2-dev mesa-utils \
libxrender-dev glew-utils libglm-dev libglu1-mesa-dev \
libglew-dev libxrandr-dev libgirepository1.0-dev
sudo luarocks install lgi
sudo luarocks install --server=http://luarocks.org/dev gifine

http://www.tokeru.com/cgwiki/index.php?title=GeneralUtilties#Gifs