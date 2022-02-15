#!/usr/bin/python3
import os

distro = input("Enter name of your Linux distro (e.g. fedora, opensuse, archlinux and debian): ")
braveinstall = input("Want you install Brave: stable, beta or nightly? ")

if distro == 'fedora':
    if braveinstall  == 'stable':
        print("Installing dnf-plugins-core...")
        os.system("sudo dnf install -y dnf-plugins-core")
        print("Adding Brave repository to your OS (% s)..." % distro)
        os.system("sudo dnf config-manager --add-repo https://brave-browser-rpm-release.s3.brave.com/x86_64/")
        os.system("sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc")
        print("Installing brave-browser...")
        os.system("sudo dnf install -y brave-browser")
        print("Brave Browser was installed successfully!")
        exit()

    if braveinstall == 'beta':
        print("Installing dnf-plugins-core...")
        os.system("sudo dnf install -y dnf-plugins-core")
        print("Adding Brave repository to your OS (% s)..." % distro)
        os.system("sudo dnf config-manager --add-repo https://brave-browser-rpm-beta.s3.brave.com/x86_64/")
        os.system("sudo rpm --import https://brave-browser-rpm-beta.s3.brave.com/brave-core-nightly.asc")
        print("Installing brave-browser-beta...")
        os.system("sudo dnf install -y brave-browser-beta")
        print("Brave Browser Beta was installed successfully!")
        exit()

    if braveinstall == 'nightly':
        print("Installing dnf-plugins-core...")
        os.system("sudo dnf install -y dnf-plugins-core")
        print("Adding Brave repository to your OS (% s)..." % distro)
        os.system("sudo dnf config-manager --add-repo https://brave-browser-rpm-nightly.s3.brave.com/x86_64/")
        os.system("sudo rpm --import https://brave-browser-rpm-nightly.s3.brave.com/brave-core-nightly.asc")
        print("Instaling brave-browser-nightly...")
        os.system("sudo dnf install -y brave-browser-nightly")
        print("Brave Browser Nightly was installed successfully!")
        exit()

if distro == 'opensuse':
    if braveinstall == 'stable':
        print("Instaling curl...")
        os.system("sudo zypper install -y curl")
        print("Adding Brave repository to your OS (% s)..." % distro)
        os.system("sudo rpm --import https://brave-browser-rpm-release.s3.brave.com/brave-core.asc")
        os.system("sudo zypper addrepo https://brave-browser-rpm-release.s3.brave.com/x86_64/ brave-browser")
        print("Installing brave-browser...")
        os.system("sudo zypper install -y brave-browser")
        print("Brave Browser was installed successfully!")
        exit()

    if braveinstall == 'beta':
        print("Installing curl...")
        os.system("sudo zypper install curl")
        print("Adding Brave repository to your OS (% s)..." % distro)
        os.system("sudo rpm --import https://brave-browser-rpm-beta.s3.brave.com/brave-core-nightly.asc")
        os.system("sudo zypper addrepo https://brave-browser-rpm-beta.s3.brave.com/x86_64/ brave-browser-beta")
        print("Installing brave-browser...")
        os.system("sudo zypper install -y brave-browser-beta")
        print("Brave Browser Beta was installed successfully!")
        exit()


    if braveinstall == 'nightly':
        print("Installing curl...")
        os.system("sudo zypper install -y curl")
        print("Adding Brave repository to your OS (% s)..." % distro)
        os.system("sudo rpm --import https://brave-browser-rpm-nightly.s3.brave.com/brave-core-nightly.asc")
        os.system("sudo zypper addrepo https://brave-browser-rpm-nightly.s3.brave.com/x86_64/ brave-browser-nightly")
        print("Installing brave-browser-nightly...")
        os.system("sudo zypper install -y brave-browser-nightly")
        print("Brave Browser Nightly was installed successfully!")
        exit()

if distro == 'archlinux':
    if braveinstall == 'stable':
        print('\033[1m' + 'Downloading Brave-stable sources for Arch Linux...' + '\033[0m')
        os.makedirs("archlinux-brave-stable")
        os.chdir("archlinux-brave-stable")
        os.system("git clone https://aur.archlinux.org/brave.git")
        os.system("makepkg PKGBUILD")
        os.system("sudo pacman -U ./brave-1.29.79-1-x86_64.tar.zst")
        print('\033[1m' + 'Brave stable pkg for Arch Linux was created successfully!' + '\033[0m')
        exit()

    if braveinstall == 'beta':
        print('\033[1m' + 'Downloading Brave-beta sources for Arch Linux...' + '\033[0m')
        os.makedirs("archlinux-brave-beta")
        os.chdir("archlinux-brave-beta")
        os.system("git clone https://aur.archlinux.org/brave-beta-bin.git")
        os.system("makepkg PKGBUILD")
        os.system("sudo pacman -U ./brave-beta-bin-1.36.94-1-x86_64.tar.zst")
        print('\033[1m' + 'Brave beta pkg for Arch Linux was created successfully!' + '\033[0m')
        exit()

    if braveinstall == 'nightly':
        print('\033[1m' + 'Downloading Brave-nightly sources for Arch Linux...' + '\033[0m')
        os.makedirs("archlinux-brave-nightly")
        os.chdir("archlinux-brave-nightly")
        os.system("git clone https://aur.archlinux.org/brave-nightly-bin.git")
        os.system("makepkg PKGBUILD")
        os.system("sudo pacman -U ./brave-nightly-bin-1.37.49-1-x86_64.tar.zst")
        print('\033[1m' + 'Brave nightly pkg for Arch Linux was created successfully!' + '\033[0m')
        exit()

if distro == 'debain' or 'ubuntu' or 'linuxmint':
    if braveinstall == 'stable':
        print("Installing apt-transport-https curl")
        os.system("sudo apt install apt-transport-https curl")
        print("Installing gnupg usr/share/keyrings/brave-browser-archive-keyring.gpg...")
        os.system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
        print("Adding Brave Browser repository to your OS (% s)..." % distro)
        os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
        print("Updating (refreshing) APT repositories (sudo dnf update)...")
        os.system("sudo apt update")
        print("Installing brave-browser...")
        os.system("sudo apt install -y brave-browser")
        print("Brave Browser was installed successfully!")
        exit()

    if braveinstall == 'beta':
        print("Installing apt-transport-https curl")
        os.system("sudo apt install -y apt-transport-https curl")
        print("Installing gnupg to usr/share/keyrings/brave-browser-archive-keyring.gpg...")
        os.system('sudo curl -fsSLo /usr/share/keyrings/brave-browser-beta-archive-keyring.gpg https://brave-browser-apt-beta.s3.brave.com/brave-browser-beta-archive-keyring.gpg')
        print("Adding Brave repository to your OS (% s)..." % distro)
        os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-beta-archive-keyring.gpg arch=amd64] https://brave-browser-apt-beta.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-beta.list')
        print("Updating (refreshing) APT repostories (sudo apt update)...")
        os.system("sudo apt update")
        print("Installing brave-browser-beta")
        os.system("sudo apt install -y brave-browser-beta")
        print("Brave Browswer Beta was installed successfully!")
        exit()

    if braveinstall == 'nightly':
        print("Installing apt-transport-https curl")
        os.system("sudo apt install -y apt-transport-https curl")
        print("Installing gnupg to usr/share/keyrings/brave-browser-archive-keyring.gpg...")
        os.system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-nightly-archive-keyring.gpg https://brave-browser-apt-nightly.s3.brave.com/brave-browser-nightly-archive-keyring.gpg")
        print("Adding Brave repository to your OS (% s)" % distro)
        os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-nightly-archive-keyring.gpg arch=amd64] https://brave-browser-apt-nightly.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-nightly.list')
        print("Updating (refreshing) APT repostories (sudo apt update)...")
        os.system("sudo apt update")
        print("Installing brave-browser-nightly")
        os.system("sudo apt install -y brave-browser-nightly")
        print("Brave Browser Nightly was installed successfully!")
        exit()
