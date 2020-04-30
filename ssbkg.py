import os
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("package")
arp=ap.parse_args()
pkg=arp.package


print("Attempting to download "+pkg+"...")
rawdl=os.popen("wget https://github.com/hpott/ssbkg-repo/raw/master/"+pkg+".ssb").read()

error = "ERROR" in rawdl


if error:
    print(pkg+" not found, try again")
    quit()

print("Download sucessfull")
print("Installing "+pkg+".ssb...")
os.system("./pssb_install "+pkg+".ssb")
print("sucessfull installed "+pkg)
