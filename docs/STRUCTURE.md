# PixAI Account Creator - Project Structure

## Directory Structure

```
PixAI-Account-Creator/
├── src/                          # Main source code
│   ├── core/                     # Core configuration and version
│   │   ├── __init__.py
│   │   ├── config.py             # Centralized configuration
│   │   └── version.py             # Version management
│   ├── ui/                       # UI enhancement modules
│   │   ├── __init__.py
│   │   └── ui_enhancer.py        # Browser UI enhancements
│   ├── utils/                    # Utility modules
│   │   ├── __init__.py
│   │   └── system_check.py       # System analysis tool
│   └── scripts/                  # Executable scripts
│       ├── __init__.py
│       ├── account_creator.py    # Main account creation script
│       ├── preview_browser.py    # Browser preview script
│       └── install.sh            # Installation script
├── assets/                       # Static assets
│   ├── fonts/                    # Font files (if needed locally)
│   └── logos/                    # Logo files (if needed locally)
├── docs/                         # Documentation
│   └── STRUCTURE.md              # This file
├── lib/                          # External libraries (if any)
├── account_creator.py           # Main script wrapper
├── preview_browser.py           # Preview script wrapper
├── system_check.py              # System check wrapper
├── version.py                   # Version wrapper
├── requirements.txt             # Python dependencies
├── README.md                    # Main documentation
└── .gitignore                   # Git ignore rules
```

##Module Responsibilities

### Core (`src/core/`)
- **`config.py`** - Centralized configuration (URLs, settings, colors)
- **`version.py`** - Version management and build info

### UI (`src/ui/`)
- **`ui_enhancer.py`** - Browser UI enhancements (fonts, logos, styling)

### Utils (`src/utils/`)
- **`system_check.py`** - System analysis and browser recommendations

### Scripts (`src/scripts/`)
- **`account_creator.py`** - Main automation script
- **`preview_browser.py`** - Browser preview with UI enhancements
- **`install.sh`** - Automated installation script

##Usage

### Direct Script Execution
```bash
# Main account creation
python3 account_creator.py --accounts=5 --browsers=1

# Browser preview
python3 preview_browser.py --headless=false

# System check
python3 system_check.py --json

# Version info
python3 version.py
```

### Module Import
```python
from src.core import config as cfg
from src.ui.ui_enhancer import ui_enhancer
from src.core.version import get_version
```

##Benefits

1. **Clean Separation** - Each module has a specific purpose
2. **Easy Maintenance** - Changes isolated to specific modules
3. **Scalable** - Easy to add new features without cluttering
4. **Professional** - Industry-standard Python project structure
5. **Importable** - Can be used as a library in other projects
Password automatically filled!
