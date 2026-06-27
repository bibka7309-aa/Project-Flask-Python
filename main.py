from server_flask_file import *
import os
import time 

def starting_create_server():
  print("Creating main dir\n")
  time.sleep(4)
  os.mkdir("templates")

  print("Creating html css and js files \n")
  time.sleep(10)
  
  file = open("templates/index.html", "w") 
  file.write("\n<!DOCTYPE html>")
  file.write("\n<html>")
  file.write("\n<head>")
  file.write("\n  <meta charset='utf-8' ")
  file.write("\n  <title>Easy Site</title>")
  file.write("\n  <link rel='stylesheet' href='style.css' />")
  file.write("\n  <script src='script.js'></script>")
  file.write("\n</head>")
  file.write("\n<body>")
  file.write("\n   <button id='btn1' type='button'>Click</button>")
  file.write("\n</body>")
  file.write("\n</html>")

  style = open("templates/style.css", "w")
  style.write("\n* {")
  style.write("\n  background: whitesmoke;")
  style.write("\n  color: black;")
  style.write("\n  font-family: sans-serif;")
  style.write("\n}")

  script = open("templates/script.js", "w")
  script.write("\n const btn = document.getElementById('btn1');")
  script.write("\n ")
  script.write("\n btn.addEventListener('click', function () { ")
  script.write("\n   window.alert('Noooooooooooooooooooo');")
  script.write("\n});")

  flask_function()
  

def main():
  print("Hi! \n")
  time.sleep(2)
  que = input("Do you want to start server? (y/n) :")

  if (que == "y" or que == "Y"):
    print("Okay!\n")
    time.sleep(4)
    starting_create_server()
  else:
    print("Bye!")
    exit(0)
