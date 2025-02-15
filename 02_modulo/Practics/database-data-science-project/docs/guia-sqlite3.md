### **📌 Guía de Instalación de SQLite3 en Diferentes Sistemas Operativos**  

SQLite3 es una base de datos ligera que generalmente viene preinstalada en muchos sistemas, pero si no está disponible, aquí te explico cómo instalarla en **Arch, Debian, Ubuntu, Fedora, macOS y Windows**.  


---

## **🔹 Windows**
SQLite no viene preinstalado en Windows, pero puedes instalarlo manualmente de dos maneras:

### **1️⃣ Instalación manual**
1. Descarga SQLite desde su página oficial:  
   🔗 [https://www.sqlite.org/download.html](https://www.sqlite.org/download.html)  
2. Descarga los siguientes archivos:
   - **SQLite Tools for Windows** (contiene el ejecutable `sqlite3.exe`)
   - **Precompiled Binaries for Windows** (opcional, si necesitas bibliotecas adicionales)  
3. Extrae los archivos en una carpeta, por ejemplo: `C:\sqlite3`  
4. Agrega `C:\sqlite3` al `PATH` de Windows:
   - **CMD:**  
     ```cmd
     setx PATH "%PATH%;C:\sqlite3"
     ```
   - **PowerShell:**  
     ```powershell
     [System.Environment]::SetEnvironmentVariable("Path", $Env:Path + ";C:\sqlite3", [System.EnvironmentVariableTarget]::Machine)
     ```
5. Verifica la instalación con:
   ```cmd
   sqlite3 --version
   ```

---

### **2️⃣ Instalación con `winget`**
Si usas Windows 10/11, puedes instalarlo con:
```powershell
winget install -e --id SQLite.SQLite
```
Luego, verifica con:
```cmd
sqlite3 --version
```


---

## **🔹 Linux (Todas las distros)**
Antes de instalar, revisa si ya tienes SQLite con:
```sh
sqlite3 --version
```
Si devuelve un número de versión, entonces ya está instalado. Si no, sigue la instalación según tu distribución:

### **1️⃣ Arch Linux y Manjaro (Pacman)**
```sh
sudo pacman -S sqlite
```
Para el soporte de Python:
```sh
sudo pacman -S python-sqlite
```

---

### **2️⃣ Debian, Ubuntu y derivados (APT)**
```sh
sudo apt update
sudo apt install sqlite3 libsqlite3-dev
```
Para Python:
```sh
sudo apt install python3-sqlite
```

---

### **3️⃣ Fedora (DNF)**
```sh
sudo dnf install sqlite sqlite-devel
```
Para Python:
```sh
sudo dnf install python3-sqlite
```

---

## **🔹 macOS**
### **Instalación con Homebrew**
```sh
brew install sqlite
```
Para verificar la instalación:
```sh
sqlite3 --version
```

---



¡Con esto SQLite3 estará listo en cualquier sistema! 🚀