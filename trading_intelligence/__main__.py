"""`python -m trading_intelligence` runs the MCP server over stdio.
`python -m trading_intelligence --update` re-downloads the knowledge base (GitHub installs only).
`python -m trading_intelligence --where` prints which copy of the knowledge base is in use."""
import sys

if "--update" in sys.argv:
    from ._paths import download
    print(download(force=True))
elif "--where" in sys.argv:
    from ._paths import repo_root
    print(repo_root())
else:
    from .mcp_server import main
    main()
