# Instrucciones:
Haz un clon de mi repositorio

```bash
#Clonar el repositorio
git clone https://github.com/CorvussCorax/automata.git

# Entrar al directorio
cd automata
# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```
# Ejecucion:
Una vez instalados todos los requerimentos solo ejecuta main.py
├── automata/
    ├── pyproject.toml
    ├── README.md
    ├── directorios.py
    ├── requirements.txt
    ├── tree.txt
    ├── .gitignore
    ├── src/
        ├── router.py
        ├── main.py  <---------------- Este merooooooooooooooooooooooooooooo
        ├── assets/
            ├── icon.png
        ├── views/
            ├── calcular_subcadenas_view.py
            ├── home_view.py
            ├── simulacion_afd_view.py
            ├── definir_afd_view.py
            ├── calcular_cerraduras_view.py
        ├── utils/
            ├── mk_img_automaton.py
            ├── load_jff.py
            ├── save_jff.py
            ├── tabla_transiciones.py
            ├── utilidades.py

y ya eso es todo
