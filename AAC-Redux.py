from tkinter import *
import os
import tkinter.messagebox

def folder_init():
    input = popupFolder(root)
    root.wait_window(input.top)
    os.system("mkdir "+input.value+" && cd "+input.value)

def rom_init():
    input = popupRom(root)
    root.wait_window(input.top)

def cm_init():
    input = popupCm(root)
    root.wait_window(input.top)

def fix_dependencies():
    input = popupPack(root)
    root.wait_window(input.top)
def get_repo():
    os.system("mkdir ~/bin")
    os.system("curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo && chmod a+x ~/bin/repo")

def get_java():
    os.system("sudo apt-add-repository ppa:webupd8team/java && sudo apt-get update && sudo apt-get install oracle-java7-installer")

def get_packs():
    os.system("sudo apt-get install git-core gnupg flex bison gperf build-essential \
    zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \
    lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache \
    libgl1-mesa-dev libxml2-utils xsltproc unzip lzop")

def get_all():
    os.system("curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ~/bin/repo && chmod a+x ~/bin/repo")
    os.system("sudo apt-get install git-core gnupg flex bison gperf build-essential \
    zip curl zlib1g-dev gcc-multilib g++-multilib libc6-dev-i386 \
    lib32ncurses5-dev x11proto-core-dev libx11-dev lib32z-dev ccache \
    libgl1-mesa-dev libxml2-utils xsltproc unzip lzop")
    os.system("sudo apt-add-repository ppa:webupd8team/java && sudo apt-get update && sudo apt-get install oracle-java7-installer")
def sync():
    os.system("repo sync")

def build():
    prompt = tkinter.messagebox.askquestion("Prompt", "Please ensure that you have selected ROM \n and synced sources before proceeding")
    if prompt == "yes":
        input = popupBuild(root)
        root.wait_window(input.top)
        build_actual()

def build_actual():
    os.system("source build/envsetup.sh && brunch "+device)


class popupBuild(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Enter codename of device to begin build")
        self.l.pack()
        device_name = ""
        self.b1=Entry(top,textvariable=device_name,width=30)
        self.b1.pack()
        self.b2=Button(top,text="OK",command=build_actual)
        self.b2.pack()
        global device
        device = device_name

class popupPack(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Select what all do you need to Install... \n If in doubt, click All")
        self.l.pack()
        self.b1=Button(top,text="repo",command=get_repo)
        self.b1.pack()
        self.b2=Button(top,text="Java",command=get_java)
        self.b2.pack()
        self.b3=Button(top,text="Other dependencies...",command=get_packs)
        self.b3.pack()
        self.b4=Button(top,text="Get All",command=get_all)
        self.b4.pack()

    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class popupCm(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Select the branch you want to sync...")
        self.l.pack()
        self.b1=Button(top,text="CM13.0 - MarshMallow",command=os.system("repo init -u git://github.com/CyanogenMod/android.git -b cm-13.0"))
        self.b1.pack()
        self.b2=Button(top,text="CM12.1 - Lollipop 5.1",command=os.system("repo init -u git://github.com/CyanogenMod/android.git -b cm-12.1"))
        self.b2.pack()
        self.b3=Button(top,text="CM12.0 - Lollipop 5.0",command=os.system("repo init -u git://github.com/CyanogenMod/android.git -b cm-12.0"))
        self.b3.pack()
        self.b4=Button(top,text="CM11 - KitKat",command=os.system("repo init -u git://github.com/CyanogenMod/android.git -b cm-11.0"))
        self.b4.pack()

    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()


class popupRom(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Select the ROM you want to sync...")
        self.l.pack()
        self.b1=Button(top,text="CyanogenMod",command=cm_init)
        self.b1.pack()

    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()


class popupFolder(object):
    def __init__(self,master):
        top=self.top=Toplevel(master)
        self.l=Label(top,text="Enter the folder name where you want to see your sources...")
        self.l.pack()
        self.e=Entry(top)
        self.e.pack()
        self.b=Button(top,text='Ok',command=self.cleanup)
        self.b.pack()
    def cleanup(self):
        self.value=self.e.get()
        self.top.destroy()

class mainWindow(object):
    def __init__(self,master):
        self.master=master
        self.l=Label(master,text="Android Auto Compiler v"+version+"\n"+"By @MSF-Jarvis"+"\n"+"Original Concept by @AndroGeek974",bg="lightblue")
        self.l.pack(fill="x")
        self.b=Button(master,text="Install required packages and applications",command=fix_dependencies)
        self.b.pack()
        self.b1=Button(master,text="Enter Folder name for sources",command=folder_init)
        self.b1.pack()
        self.b2=Button(master,text="Select ROM to sync sources",command=rom_init)
        self.b2.pack()
        self.b3=Button(master,text="Sync the sources",command=sync)
        self.b3.pack()
        self.b4=Button(master,text="Build ROM",command=build)
        self.b4.pack()


if __name__ == "__main__":
    version="1.0_25112015"
    root=Tk()
    root.geometry("400x440")
    root.title("AAC-Redux v"+version)
    m=mainWindow(root)
    root.mainloop()
