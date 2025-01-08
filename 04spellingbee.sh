gunzip -c ~/Code/MCB185/data/dictionary.gz | grep -E "^[rzoniac]+$" | grep "r" | grep -E "^.{4,}$"

