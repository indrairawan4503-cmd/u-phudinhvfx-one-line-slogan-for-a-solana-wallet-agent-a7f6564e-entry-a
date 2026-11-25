#!/usr/bin/env python3
"""One-line slogan for a Solana wallet agent (variant A: autopilot / night shift).

Concept: the wallet clocks in when its human clocks out. One concrete scene
(bedtime handover) + one surprising turn (the wallet takes the shift).
"""
import os

# v5 (FINAL): v4's overtime twist is cute but vague; v3 wins — the SOL pun
# ("minding your SOL") keeps the wallet's job clear while the clock-in/clock-out
# contrast gives the rhythm. One scene (bedtime handover) + one turn (wallet takes the shift).
SLOGAN = "You clock out. Your Solana wallet clocks in, sending, swapping, and minding your SOL till sunrise."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SLOGAN + "\n")
    try:
        with open("entry.txt", "w", encoding="utf-8") as f:
            f.write(SLOGAN + "\n")
    except OSError:
        pass

if __name__ == "__main__":
    main()
