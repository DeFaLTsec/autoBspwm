import os, time
from sys import stdout

import sys
import termios

def wait_for(mess, *keys):
    file_descriptor = sys.stdin.fileno()
    old = termios.tcgetattr(file_descriptor)
    new = old[:]

    try:
        new[3] &= ~(termios.ICANON | termios.ECHO)
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, new)
        print(mess, end="")
        while True:
            letra = sys.stdin.read(1)
            if not keys or letra in keys:
                print()
                break
    finally:
        termios.tcsetattr(file_descriptor, termios.TCSADRAIN, old)

def red():
    RED = "\033[1;31m"
    stdout.write(RED)

def blue():
    BLUE = "\033[1;34m"
    stdout.write(BLUE)
    
def purple():
    PURPLE = "\033[1;35m"
    stdout.write(PURPLE)

def white():
    WHITE = "\033[1;37m"
    stdout.write(WHITE)

os.system('clear')

banner = """
█████╗ ██╗   ██╗████████╗ ██████╗ ██████╗ ███████╗██████╗ ██╗    ██╗███╗   ███╗
██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝██╔══██╗██║    ██║████╗ ████║
███████║██║   ██║   ██║   ██║   ██║██████╔╝███████╗██████╔╝██║ █╗ ██║██╔████╔██║
██╔══██║██║   ██║   ██║   ██║   ██║██╔══██╗╚════██║██╔═══╝ ██║███╗██║██║╚██╔╝██║  by: DeFaLT
██║  ██║╚██████╔╝   ██║   ╚██████╔╝██████╔╝███████║██║     ╚███╔███╔╝██║ ╚═╝ ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝╚═╝      ╚══╝╚══╝ ╚═╝     ╚═╝
"""                                                                                

def menu():
    blue()
    print(banner)
    blue()
    time.sleep(1)
    print("1 -> Instalar Requisitos")
    time.sleep(1)
    print("\n2 -> Instalar Bspwm")
    time.sleep(1)
    print("\n3 -> Instalar Polybar, Powerlevel10k ...")
    time.sleep(1)
    print("\n4 -> Instalar Todo")
    time.sleep(1)
    print("\n5 -> Salir")
    time.sleep(1)

    option = input("\n-->> ")

    if option == "1":
        req()
    if option == "2":
        bspwm()
    if option == "3":
        polybar()
        fonts()
        powerlevel()
        wallpaper()
        picom()
        theme()
        rofi()
        tmux()
        nvim()
        oth()
    if option == "4":
        req()
        bspwm()
        polybar()
        fonts()
        powerlevel()
        wallpaper()
        picom()
        theme()
        rofi()
        tmux()
        nvim()
        oth()
    if option == "5":
        exit()

def exit():
    purple()
    print("Saliendo...")
    time.sleep(3)
    os.system("exit")

def req():
    white()
    print("\nInstalando requisitos...\n")

    # Actualiza los paquetes
    os.system("sudo apt-get update -y")
    os.system("sudo apt upgrade")
    os.system("sudo apt install build-essential git vim xcb libxcb-util0-dev libxcb-ewmh-dev libxcb-randr0-dev libxcb-icccm4-dev libxcb-keysyms1-dev libxcb-xinerama0-dev libasound2-dev libxcb-xtest0-dev libxcb-shape0-dev")
    os.system("sudo apt-get install libuv1-dev")
    # Instala requisitos de La polybar
    os.system("sudo apt install cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev")
    
    # Instala Requisitos de Picom
    os.system("sudo apt install meson libxext-dev libxcb1-dev libxcb-damage0-dev libxcb-xfixes0-dev libxcb-shape0-dev libxcb-render-util0-dev libxcb-render0-dev libxcb-randr0-dev libxcb-composite0-dev libxcb-image0-dev libxcb-present-dev libxcb-xinerama0-dev libpixman-1-dev libdbus-1-dev libconfig-dev libgl1-mesa-dev libpcre2-dev libevdev-dev uthash-dev libev-dev libx11-xcb-dev libxcb-glx0-dev")
    
    # Instals Requisitos de Slim y SLimlock
    os.system("sudo apt install slim libpam0g-dev libxrandr-dev libfreetype6-dev libimlib2-dev libxft-dev")

    # Instala los recursos
    os.system("sudo apt install bspwm rofi caja feh gnome-terminal scrot neovim xclip tmux acpi scrub bat wmname -y")
    
    time.sleep(2)
    blue()
    print("\n[✔] Todos los requisitos han sido instalados correctamente\n")


def bspwm():
    white()
    print("\nInstalando bspwm...\n")
    
    # Clona el repositorio de Bspwm
    os.system("git clone https://github.com/baskerville/bspwm.git")
    os.chdir("bspwm/")
    os.system("make")
    os.system("sudo make install")

    # Elimina los archivos de bspwm
    os.system("sudo rm -r artworks/ contrib/ doc/ src/ tests/ bspc bspc.o bspwm bspwm.o desktop.o events.o ewmh.o geometry.o helpers.o history.o jsmn.o LICENSE Makefile messages.o monitor.o parse.o pointer.o query.o README.md restore.o rule.o settings.o Sourcedeps stack.o subscribe.o tree.o VERSION window.o")
    os.chdir("../")

    # Clona el repositorio de Sxhkd
    os.system("git clone https://github.com/baskerville/sxhkd.git")
    os.chdir("./sxhkd/")
    os.system("make")
    os.system("sudo make install")
    os.chdir("../")

    # Crea carpetas de bspwm y sxhkd
    os.system("mkdir ~/.config/bspwm")
    os.system("mkdir ~/.config/sxhkd")
    os.system("cp files/bspwmrc ~/.config/bspwm/")
    os.system("cp files/sxhkdrc ~/.config/sxhkd/")
    os.system("mkdir ~/.config/bspwm/scripts")
    os.system("cp files/scripts/bspwm_resize ~/.config/bspwm/scripts")
 
    # Da permisos de ejecución
    os.system("chmod +x ~/.config/bspwm/bspwmrc")
    os.system("chmod +x ~/.config/sxhkd/sxhkdrc")
    os.system("chmod +x ~/.config/bspwm/scripts/bspwm_resize")

    # Elimina los archivos de sxhkd
    os.chdir("./sxhkd")
    os.system("sudo rm -r contrib/ doc/ examples/ src/ grab.o helpers.o LICENSE Makefile parse.o README.md Sourcedeps sxhkd sxhkd.o types.o VERSION")
    os.chdir("../")

    # Update
    os.system("sudo apt-get update -y")
    os.system("sudo apt upgrade -y")
    
    time.sleep(2)
    blue()
    print("\n[✔] Bspwm instalado correctamente!\n")

def polybar():
    white()
    print("\n Instalando polybar...\n")

    # Clona el repositorio de polybar 
    os.system("git clone --recursive https://github.com/polybar/polybar")
    os.chdir("polybar/")
    os.system("cmake .")
    os.system("make -j$(nproc)")
    os.system("sudo make install")

    # Elimina los archivos de polybar
    os.system("sudo rm -r bin/ cmake/ CMakeFiles/ common/ config/ contrib/ doc/ generated-sources/ include/ lib/ libs/ polybar/ src/ tests/ banner.png build.sh CHANGELOG.md CMajeCache.txt cmake_install.cmake CMakeLists.txt compile_commands.json CONTRIBUTING.md install_manifest LICENSE Makefile README.md SUPPORT.md version.txt")
    os.chdir("../")     

    time.sleep(2)
    blue()
    print("\n[✔] Polybar Instalada correctamente!\n")

def picom():
    white()
    print("\n Instalando Picom...\n")

    # Clona el repositorio de Picom
    os.chdir("../")
    os.system("git clone https://github.com/ibhagwan/picom.git")
    os.chdir("picom/")
    os.system("git submodule update --init --recursive")
    os.system("meson --buildtype=release . build")
    os.system("ninja -C build")
    os.system("sudo ninja -C build install")

    # Elimina los archivos de picom
    os.system("sudo rm -r *.md *.conf *.desktop *.txt *.build *.spdx *.glsl COPYING Doxyfile CONTRIBUTORS bin/ build/ dbus-examples/ LICENSES/ man/ media/ meson/ src/ subprojects/ tests/")
    os.chdir("../autoBspwm")

    time.sleep(2)
    blue()
    print("\n[✔] Picom Instalado correctamente!\n")

def wallpaper():
    white()
    print("\n Agregando Walpaper...\n")
    
    # Añade el wallpaper
    os.system("mkdir ~/.wallpapers")
    os.system("cp files/wallpaper.jpg ~/.wallpapers")
    os.system("echo 'wmname LG3D &' >> ~/.config/bspwm/bspwmrc")
    
    time.sleep(2)
    blue()
    print("\n[✔] Wallpaper Agregado Correctamente!\n")

def theme():
    white()
    print("\n Configurando tema para polybar...\n")
    
    # Crea el directorio para polybar en config
    os.system("mkdir ~/.config/polybar")

    # Copia los archivos de configuracion para polybar
    os.system("cp -r files/polybarconf/* ~/.config/polybar")
    
    # Carga los scripts personalizados
    os.system("mkdir ~/.config/bin")
    os.system("cp files/configbin/* ~/.config/bin")

    # Da permisos de ejecucion a los scripts
    os.system("chmod +x ~/.config/bin/ethernet_status.sh")
    os.system("chmod +x ~/.config/bin/hackthebox_status.sh")
    os.system("chmod +x ~/.config/bin/target_to_hack.sh")

    # Crea la carpeta para picom
    os.system("mkdir ~/.config/picom")

    time.sleep(2)
    blue()
    print("\n[✔] El Tema para Polybar ha sido aplicada correctamente!\n")

def rofi():
    white()
    print("\n Configurando el tema para Rofi...\n")

    # Crea los directorios y copia la configuracion
    os.system("mkdir ~/.config/rofi")
    os.system("mkdir ~/.config/rofi/themes")
    os.system("cp files/nord.rasi ~/.config/rofi/themes")
    purple()
    print("\n A continuacion se te presentara un menu en donde deberas bajar y elegir nord y presionar las teclas 'Alt + A'...")
    blue()
    wait_for("Presione una tecla para continuar")
    time.sleep(2)
    os.system("rofi-theme-selector nord nord")
    
    time.sleep(2)
    blue()
    print("\n[✔] El Tema para Rofi ha sido aplicado correctamente!\n")

def powerlevel():
    white()
    print("\n Instalando Powerlevel10k...\n")

    # Instalacion de powerlevel10k
    os.system("git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ~/.powerlevel10k")
    os.system("echo 'source ~/.powerlevel10k/powerlevel10k.zsh-theme' >>~/.zshrc")

    # Instalacion de powerlevel10k para root
    os.system("sudo git clone --depth=1 https://github.com/romkatv/powerlevel10k.git /root/.powerlevel10k")
    os.system("sudo chmod +x+w+r /root/.zshrc")
    os.system("sudo echo 'source ~/.powerlevel10k/powerlevel10k.zsh-theme' >> /root/.zshrc")

    # Añadiendo scripts personalizados
    os.system("cp files/zshrc_conf ~/.zshrc")
    os.system("cp files/oth/p10k.zsh ~/.p10k.zsh")
    os.system("mkdir ~/powerlevel10k")
    os.system("sudo mkdir /root/powerlevel10k")
    os.system("cp -r files/oth/powerlevel10kcopie/* ~/powerlevel10k")
    os.system("sudo cp -r files/oth/powerlevel10kcopie/* /root/powerlevel10k")
    
    # cambiando a zsh por defecto
    os.system("usermod --shell /usr/bin/zsh $USER")
    os.system("usermod --shell /usr/bin/zsh root")
  
    time.sleep(2)
    blue()
    print("\n[✔] La powerlevel10k ha sido instalada correctamente!\n")


def fonts():
    white()
    print("\n Instalando Fuente 'Hack Nerd Fonts'...\n")

    # Instala Hack Nerd Fonts
    os.system("cp files/Hack.zip .")
    os.system("unzip Hack.zip")
    os.system("sudo mv *.ttf /usr/share/fonts")
    os.system("rm *.zip")

    expback = input("\nPuede visualizar estos iconos perfectamente?  / / / / . [S/N] \n")
    
    if expback == "N":                                                                                                            
        os.system("sudo apt upgrade ")                                                                                             
        os.system("sudo apt-get update -y")
        os.system("sudo apt-get update --fix-missing") 
        os.system("sudo apt --fix-missing update")
    
        time.sleep(3)
        red()
        print("[¡] Hubo unos problemas con la instalacion y han sido reparados\n")

    if expback == "S":
        os.system("sudo apt upgrade")

    time.sleep(2)
    blue()
    print("\n[✔] Hack Nerd Font se ha instalado correctamente!\n")

def nvim():
    white()
    print("\n Instalando Tema de Nvim...\n")
    
    # Instala el tema de nvim
    os.system("wget https://github.com/arcticicestudio/nord-vim/archive/master.zip")
    os.system("unzip master.zip")
    os.system("rm master.zip")
    os.system("mkdir ~/.config/nvim")
    os.system("mv nord-vim-master/colors/ ~/.config/nvim")
    os.system("sudo rm -r nord-vim-master/")
    os.system("wget https://raw.githubusercontent.com/Necros1s/lotus/master/lotus.vim")
    os.system("wget https://raw.githubusercontent.com/Necros1s/lotus/master/lotusbar.vim")
    
    os.system("cp init.vim ~/.config/nvim")
    os.system("mv *.vim ~/.config/nvim")

    time.sleep(2)
    blue()
    print("\n[✔] Nvim ha sido instalado correctamente\n")

def tmux():
    white()
    print("\n Instalando oh my tmux...\n")
    
    # Instala Oh My Tmux
    os.system("git clone https://github.com/gpakosz/.tmux.git /home/$USER/.tmux")
    os.system("ln -s -f .tmux/.tmux.conf /home/$USER")
    os.system("cp /home/$USER/.tmux/.tmux.conf.local /home/$USER")
    
    # Instala Oh My Tmux para root
    os.system("sudo git clone https://github.com/gpakosz/.tmux.git /root/.tmux")
    os.system("sudo ln -s -f .tmux/.tmux.conf /root")
    os.system("sudo cp /root/.tmux/.tmux.conf.local /root")
    
    time.sleep(2)
    blue()
    print("\n[✔] Oh My Tmux instalado correctamente!\n")

def oth():
    white()
    print("\n Instalando fastTCPscan, wichSystem, lsd, batcat...\n")

    # Instala fastTCPscan.go y wichSystem.py
    os.system("sudo cp files/fastTCPscan.go /bin/")
    os.system("sudo cp files/whichSystem.py /bin/")
    os.system("chmod +x /bin/whichSystem.py")
    os.system("chmod +x /bin/fastTCPscan.go")

    # Instala lsd para zsh
    os.system("sudo dpkg -i files/oth/lsd.deb")
    
    # Instala batcat
    os.system("sudo dpkg -i files/oth/bat.deb")
    
    # Instala fzf
    os.system("git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf")
    
    # Instala Ranger
    os.system("sudo apt install ranger")
    
    # Instala Firefox y Firejail
    os.system("tar -xf files/firefox.tar.bz2")
    os.system("sudo apt install firejail")

    # Instala tema para slim-slimlock
    os.system("sudo rm -r /usr/share/slim/themes/default/*")
    os.system("cp files/oth/slim/* /usr/share/slim/themes/default")

    print("\n[✔] Toda la configuracion se ha instalado correctamente!!\n")

if __name__ == '__main__':
    id = os.getuid()
    
    if id == 0:
        red()
        print()
        print("[!] No necesitas ser root para ejecutar la herramienta")
        print()
    else:
        menu()
