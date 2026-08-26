print(
    "\nCANONICAL SIGNAL INTEGRITY"
)

print(
    f"Probability source : Proba"
)

print(
    f"Neutrality         : {neutrality:.6f}"
)

print(
    f"Alpha mean         : "
    f"{(probability - neutrality).mean():.6f}"
)

print(
    f"Confidence mean    : "
    f"{((probability - neutrality).abs() * 2).mean():.6f}"
)
