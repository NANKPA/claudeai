"""python -m trading_intelligence.sniper {lab,scan,size} ..."""
from __future__ import annotations

import sys


def main(argv=None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    cmds = {"lab": "lab", "scan": "scanner", "size": "smallaccount"}
    if not argv or argv[0] not in cmds:
        print(__doc__.strip())
        print("  lab    backtest every setup in-sample vs out-of-sample and write the gate records")
        print("  scan   watch live closed candles, run signals through PhilosophyGate, paper-trade them")
        print("  size   what a setup costs in R and the smallest position a venue allows, for any account size")
        return 2
    import importlib
    mod = importlib.import_module(f".{cmds[argv[0]]}", __package__)
    return mod.main(argv[1:])


if __name__ == "__main__":
    raise SystemExit(main())
