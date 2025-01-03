"""
Définition des couleurs pour l'interface CLI
"""
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

def colorize(text: str, color: str) -> str:
    """Ajoute de la couleur au texte"""
    return f"{color}{text}{Colors.ENDC}"

def success(text: str) -> str:
    return colorize(text, Colors.GREEN)

def error(text: str) -> str:
    return colorize(text, Colors.FAIL)

def warning(text: str) -> str:
    return colorize(text, Colors.WARNING)

def info(text: str) -> str:
    return colorize(text, Colors.CYAN)

def header(text: str) -> str:
    return colorize(text, Colors.HEADER + Colors.BOLD)