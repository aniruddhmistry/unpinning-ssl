import os
import sys
import shutil
import subprocess as sp

def die(msg):
    print(msg)
    exit(1)

def main():

    shutil.which("java") or die("Java is not installed")

    if len(sys.argv) < 2:
        print("Usage: python {} <APK file to sign>".format(sys.argv[0]))
        exit(1)

    sign = "sign.jar"
    target_apk = sys.argv[1]

    if not target_apk.endswith(".apk"):
        print(
            "The extension of `{}` is not .apk, is it really a APK file?".format(
                target_apk
            )
        )
        exit(1)

    # Signing
    print(f"[*] Signing {target_apk}...")
    sp.run(["java", "-jar", sign, "-a", target_apk])


if __name__ == "__main__":
    main()
