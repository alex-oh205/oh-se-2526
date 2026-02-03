"""
Name: Alex Oh
Date: 12/2/25
File: oh_particles.py
Objective: Find the particles that are most likely and least likely to be observed from a dictionary of particles.
"""

particles = {"neutron": 0.55, "proton": 0.21,
             "meson": 0.03, "muon": 0.07,
             "neutrino": 0.14}

minProb = 1
maxProb = 0
minParticle = maxParticle = list(particles.keys())[0]

for p in particles.keys():  # Loop through particle types
    prob = particles[p]     # Get the probability of the particle
    if prob < minProb:      # Track least likely particle
        minProb = prob
        minParticle = p
    if prob > maxProb:      # Track most likely particle
        maxProb = prob
        maxParticle = p

print("Least likely particle: ", minParticle)
print("Most likely particle: ", maxParticle)