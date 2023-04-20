# Unpinning-ssl-android

A simple Python script which patches the security configuration of an Android APK file to trust user root certificatesfor bypass SSL-pinning.

## Requirements

- Python3
- Java

## How to Run

```sh
git clone https://github.com/aniruddhmistry/unpinning-ssl.git
cd unpinning-ssl


python patch.py <APK filename>
```

## How it works

1. Decompile the APK file using [APKtool](https://ibotpeaches.github.io/Apktool/install/)
2. Modify `AndroidManifest.xml` and `network_security_config.xml` to trust user certificate
3. Recompile the APK file using [APKtool](https://ibotpeaches.github.io/Apktool/install/)
4. Sign the APK file using [uber-apk-signer](https://github.com/patrickfav/uber-apk-signer)

## References

- [APKtool](https://ibotpeaches.github.io/Apktool/install/)
- [uber-apk-signer](https://github.com/patrickfav/uber-apk-signer)
