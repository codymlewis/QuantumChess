# QuantumChess
Quantum Chess by Cody Lewis

This is a python implementation of quantum chess using IBM's Qiskit for the
case of piece superposition. That is, to calculate the probability of the
entire pieces death. Sadly, the game runs for too long to have entanglement
of the qubits.
The web server side was intended to only be a graphical frontend to the program,
thus is a bit inefficient as a web app, and on heroku the backend sometimes gets
reset, so the frontend no longer matchs the backend.

## Requirements
- Python 3.6+
- qiskit
- Flask
- bleach

## Running
From this root execute `export FLASK_APP=WebApp && flask run`
