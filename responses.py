import random

def handle_response(message) -> str:
    p_message = message.lower()

    if p_message == 'hello' or "hi" or 'good morning':
        return 'Hey there! Let\'s study!'

    if p_message == '!define Periodic Motion':
        return 'Any motion which repeats itself at regular intervals of time.'

    if p_message == '!define Oscillatory motion':
        return 'If the particle moves back and forth along the same path and repeats itself at regular intervals of time'   

    if p_message == '!define SHM':
        return 'Consider a particle executing oscillations. If no forces are acting on it, the oscillations will continue for an indefinite period without change in amplitude. In this oscillation total energy of the system remains the same always. This type of oscillations is called free oscillations.' 

    if p_message == '!define Damped Harmonic Oscillation':
        return 'A harmonic oscillator in which the motion is damped by the action of an additional force is called a damped harmonic oscillator. Damped oscillations are oscillations under the action of resistive forces.'  
        
    if p_message == '!define Forced Harmonic Oscillation':
        return 'If an external force acts on a damped oscillatory system it is called a Forced Harmonic Oscillator. The oscillations produced, under the action of external periodic force on the body is called forced oscillations'           
