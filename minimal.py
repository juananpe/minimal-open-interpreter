from interpreter import interpreter
from dotenv import load_dotenv
import os
import sys

# Load environment variables from .env file
load_dotenv()

# Get the API key from the environment variable
interpreter.llm.api_key = os.getenv("OPENAI_API_KEY")

# Initialize interpreter
interpreter.messages = []
interpreter.auto_run = True

# Check if URL was provided as argument
if len(sys.argv) < 2:
    print("Please provide a GitHub project URL as an argument")
    sys.exit(1)

project_url = sys.argv[1]

# Execute the tasks
interpreter.chat(f"""
Please perform the following steps:
0. If {project_url} does not include github.com in the domain, just 
evaluate the submission as FAIL (don't clone anything and follow rule 5)
1. Clone in /tmp the private project {project_url} using git+ssh. The path to the
 private SSH key is ~/.ssh/id_rsa. When cloning, use a random name for the
 folder that will contain the project.
2. Once cloned, analyze the js/main.js file and explain what it's doing.
3. These are the user requirements (in Spanish):

Estos dos ejercicios se centran en la manipulación del DOM y el manejo de 
eventos en JavaScript. Resumidamente: En el primer ejercicio ("Bat"), debes 
cambiar el color de todos los encabezados h1 a rojo cuando se hace clic
 en un botón. En el segundo ejercicio ("Bi"), al hacer clic en otro botón, debes 
cambiar el texto de los encabezados h2 para que muestren "goiburu2-1",
 "goiburu2-2", etc.
Cada ejercicio implica seleccionar elementos del DOM, manejar eventos de 
clic y manipular propiedades o contenido de los elementos seleccionados.

4. Compare the implementation in js/main.js with the requirements. Determine 
if the main.js file implements the requirements.

5. Provide a final VERDICT. It should be one of:
   - PASS (if in general the main.js file fulfills the requirements specified)
   - FAIL (if it doesn't fulfill the requirements)
   - UNCERTAIN (if you are uncertain about the verdict or need more information)

Don't use the word verdict, pass or fail except in the final verdict.
""")

# Print the last interpreter message
last_message = interpreter.messages[-1]
print(f"\n{last_message['role'].upper()}:\n{last_message['content']}")
