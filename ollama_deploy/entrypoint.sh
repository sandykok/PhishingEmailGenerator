#!/bin/bash

ollama serve &
sleep 5m &
wait

ollama create llama3 -f /usr/src/app/Modelfile 
ollama run llama3