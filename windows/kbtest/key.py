from enum import Enum

class Key(Enum):
    """
    These are generic platform independent key constants
    Each graphics backend maps from its own specific key codes to
    these constants
    """
    BACKQUOTE = 'btnBACKQUOTE'
    ASCII_TILDE = 'btnASCII_TILDE'
    DIGIT_1 = 'btn1'
    EXCLAMATION = 'btn1'
    DIGIT_2 = 'btn2'
    AT = 'btn2'
    DIGIT_3 = 'btn3'
    NUMBER = 'btn3'
    DIGIT_4 = 'btn4'
    DOLLAR = 'btn4'
    DIGIT_5 = 'btn5'
    PERCENT = 'btn5'
    DIGIT_6 = 'btn6'
    CARET = 'btn6'
    DIGIT_7 = 'btn7'
    AMPERSAND = 'btn8'
    DIGIT_8 = 'btn8'
    ASTERISK = 'btn8'
    DIGIT_9 = 'btn9'
    DIGIT_0 = 'btn0'
    MINUS = 'btnMIN'
    UNDERSCORE = 'btnMIN'
    EQUALS = 'btnEQUAL'
    PLUS = 'btnEQUAL'
    BACKSPACE = 'btnBACKSP'
    TAB = 'btnTAB'
    Q = 'btnQ'
    Q_UPPER = 'btnQ'
    W = 'btnW'
    W_UPPER = 'btnW'
    E = 'btnE'
    E_UPPER = 'btnE'
    R = 'btnR'
    R_UPPER = 'btnR'
    T = 'btnT'
    T_UPPER = 'btnT'
    Y = 'btnY'
    Y_UPPER = 'btnY'
    U = 'btnU'
    U_UPPER = 'btnU'
    I = 'btnI'
    I_UPPER = 'btnI'
    O = 'btnO'
    O_UPPER = 'btnO'
    P = 'btnP'
    P_UPPER = 'btnP'
    LEFTPAREN = 'btn9'
    RIGHTPAREN = 'btn0'
    LEFTBRACKET = 'btnLEFTBRACKET'
    RIGHTBRACKET = 'btnRIGHTBRACKET'
    BRACELEFT = 'btnLEFTBRACKET'
    BRACERIGHT = 'btnRIGHTBRACKET'
    BACKSLASH = 'btnBACKSLASH'
    PIPE = 'btnBACKSLASH'
    CAPSLOCK = 'btnCAPS'
    A = 'btnA'
    A_UPPER = 'btnA'
    S = 'btnS'
    S_UPPER = 'btnS'
    D = 'btnD'
    D_UPPER = 'btnD'
    F = 'btnF'
    F_UPPER = 'btnF'
    G = 'btnG'
    G_UPPER = 'btnG'
    H = 'btnH'
    H_UPPER = 'btnH'
    J = 'btnJ'
    J_UPPER = 'btnJ'
    K = 'btnK'
    K_UPPER = 'btnK'
    L = 'btnL'
    L_UPPER = 'btnL'
    SEMICOLON = 'btnSEMICOLON'
    COLON = 'btnSEMICOLON'
    DOUBLEQUOTE = 'btnSINGLEQUOTE'
    SINGLEQUOTE = "btnSINGLEQUOTE"
    RETURN = 'btnENTER'
    LEFT_SHIFT = 'btnLSHIFT'
    Z = 'btnZ'
    Z_UPPER = 'btnZ'
    X = 'btnX'
    X_UPPER = 'btnX'
    C = 'btnC'
    C_UPPER = 'btnC'
    V = 'btnV'
    V_UPPER = 'btnV'
    B = 'btnB'
    B_UPPER = 'btnB'
    N = 'btnN'
    N_UPPER = 'btnN'
    M = 'btnM'
    M_UPPER = 'btnM'
    COMMA = 'btnCOMMA'
    LESSTHAN = 'btnCOMMA'
    PERIOD = 'btnPERIOD'
    GREATERTHAN = 'btnPERIOD'
    FORWARDSLASH = 'btnFORWARDSLASH'
    QUESTION = 'btnFORWARDSLASH'
    RIGHT_SHIFT = 'btnRSHIFT'
    LEFT_CONTROL = 'btnLCTRL'
    LEFT_META = 'btnWIN'
    LEFT_ALT = 'btnLALT'
    SPACE = 'btnSPACE'
    RIGHT_ALT = 'btnRALT'
    RIGHT_META = 'btnWIN'
    CONTEXT_MENU = 'btnMENU'  # windows key
    RIGHT_CONTROL = 'btnRCTRL'
    FUNCTION = 'btnFUNCTION'
    LEFT_ARROW = 'btnLEFT'
    RIGHT_ARROW = 'btnRIGHT'
    UP_ARROW = 'btnUP'
    DOWN_ARROW = 'btnDOWN'
    # azerty
    TWO_SUPERIOR = '²'
    U_GRAVE = 'ù'
    E_ACUTE = 'é'
    E_GRAVE = 'è'
    C_CEDILLE = 'ç'
    A_GRAVE = 'à'
    DEGREE = '°'
    DIACRATICAL = '¨'
    CIRCUMFLEX = 'ˆ'
    POUND = '£'
    A_CIRCUMFLEX = 'ậ'
    E_CIRCUMFLEX = 'ê'
    I_CIRCUMFLEX = 'î'
    O_CIRCUMFLEX = 'ô'
    U_CIRCUMFLEX = 'û'
    SECTION = '§'
    MU = 'μ'
    #Function Keys
    F1 = 'btnF1'
    F2 = 'btnF2'
    F3 = 'btnF3'
    F4 = 'btnF4'
    F5 = 'btnF5'
    F6 = 'btnF6'
    F7 = 'btnF7'
    F8 = 'btnF8'
    F9 = 'btnF9'
    F10 = 'btnF10'
    F11 = 'btnF11'
    F12 = 'btnF12'
    DEL = 'btnDEL'
    ESCAPE = 'btnESC'
    SCROLLOCK = 'btnSCRLK'
    PAUSE = 'btnPAUSE'
    INSERT = 'btnINS'
    HOME = 'btnHOME'
    PAGEUP = 'btnPGUP'
    PAGEDOWN = 'btnPGD'
    END = 'btnEND'

KEY_MAP = {
    96: Key.BACKQUOTE,
    126: Key.ASCII_TILDE,
    49: Key.DIGIT_1,
    33: Key.EXCLAMATION,
    50: Key.DIGIT_2,
    64: Key.AT,
    51: Key.DIGIT_3,
    35: Key.NUMBER,
    52: Key.DIGIT_4,
    36: Key.DOLLAR,
    53: Key.DIGIT_5,
    37: Key.PERCENT,
    54: Key.DIGIT_6,
    94: Key.CIRCUMFLEX,
    55: Key.DIGIT_7,
    38: Key.AMPERSAND,
    56: Key.DIGIT_8,
    42: Key.ASTERISK,
    57: Key.DIGIT_9,
    40: Key.LEFTPAREN,
    48: Key.DIGIT_0,
    41: Key.RIGHTPAREN,
    45: Key.MINUS,
    43: Key.PLUS,
    61: Key.EQUALS,
    65288: Key.BACKSPACE,
    65289: Key.TAB,
    113: Key.Q,
    81: Key.Q_UPPER,
    119: Key.W,
    87: Key.W_UPPER,
    101: Key.E,
    69: Key.E_UPPER,
    114: Key.R,
    82: Key.R_UPPER,
    116: Key.T,
    84: Key.T_UPPER,
    121: Key.Y,
    89: Key.Y_UPPER,
    117: Key.U,
    85: Key.U_UPPER,
    105: Key.I,
    73: Key.I_UPPER,
    111: Key.O,
    79: Key.O_UPPER,
    112: Key.P,
    80: Key.P_UPPER,
    91: Key.LEFTBRACKET,
    123: Key.BRACELEFT,
    93: Key.RIGHTBRACKET,
    125: Key.BRACERIGHT,
    92: Key.BACKSLASH,
    124: Key.PIPE,
    65509: Key.CAPSLOCK,
    65792: Key.CAPSLOCK, # MACOS
    97: Key.A,
    65: Key.A_UPPER,
    115: Key.S,
    83: Key.S_UPPER,
    100: Key.D,
    68: Key.D_UPPER,
    102: Key.F,
    70: Key.F_UPPER,
    103: Key.G,
    71: Key.G_UPPER,
    104: Key.H,
    72: Key.H_UPPER,
    106: Key.J,
    74: Key.J_UPPER,
    107: Key.K,
    75: Key.K_UPPER,
    108: Key.L,
    76: Key.L_UPPER,
    59: Key.SEMICOLON,
    58: Key.COLON,
    39: Key.SINGLEQUOTE,
    34: Key.DOUBLEQUOTE,
    65293: Key.RETURN,
    131074: Key.LEFT_SHIFT, # macOs
    131330: Key.LEFT_SHIFT, # macOs
    65505: Key.LEFT_SHIFT,
    122: Key.Z,
    90: Key.Z_UPPER,
    120: Key.X,
    88: Key.X_UPPER,
    99: Key.C,
    67: Key.C_UPPER,
    118: Key.V,
    86: Key.V_UPPER,
    98: Key.B,
    66: Key.B_UPPER,
    110: Key.N,
    78: Key.N_UPPER,
    109: Key.M,
    77: Key.M_UPPER,
    44: Key.COMMA,
    60: Key.LESSTHAN,
    46: Key.PERIOD,
    62: Key.GREATERTHAN,
    47: Key.FORWARDSLASH,
    63: Key.QUESTION,
    131076: Key.RIGHT_SHIFT, # macOs
    65506: Key.RIGHT_SHIFT,
    262145: Key.LEFT_CONTROL, # macOs
    65507: Key.LEFT_CONTROL,
    1048584: Key.LEFT_META, # macOs
    65511: Key.LEFT_META,
    524320: Key.LEFT_ALT, # macOs
    65513: Key.LEFT_ALT,
    32: Key.SPACE,
    524352: Key.RIGHT_ALT, # macOs
    65514: Key.RIGHT_ALT,
    1048592: Key.RIGHT_META, # macOs
    65512: Key.RIGHT_META,
    7208976: Key.CONTEXT_MENU, # macOs
    1073741925: Key.CONTEXT_MENU,
    270336: Key.RIGHT_CONTROL,
    65508: Key.RIGHT_CONTROL, # macOs
    65362: Key.UP_ARROW,
    65364: Key.DOWN_ARROW,
    65361: Key.LEFT_ARROW,
    65363: Key.RIGHT_ARROW,
    # azerty
    249: Key.U_GRAVE,
    2812: Key.CARET,
    233: Key.E_ACUTE,
    45: Key.MINUS,
    232: Key.E_GRAVE,
    95: Key.UNDERSCORE,
    231: Key.C_CEDILLE,
    224: Key.A_GRAVE,
    61: Key.EQUALS,
    176: Key.DEGREE,
    168: Key.DIACRATICAL,
    163: Key.POUND,
    226: Key.A, # A_CIRCUMFLEX
    234: Key.E, # E_CIRCUMFLEX
    238: Key.I, # I_CIRCUMFLEX
    244: Key.O, # O_CIRCUMFLEX
    251: Key.U, # U_CIRCUMFLEX
    167: Key.SECTION,
    16777264: Key.F1,
    16777265: Key.F2,
    16777266: Key.F3,
    16777267: Key.F4,
    16777268: Key.F5,
    16777269: Key.F6,
    16777270: Key.F7,
    16777271: Key.F8,
    16777272: Key.F9,
    16777273: Key.F10,
    16777274: Key.F11,
    16777275: Key.F12,
    16777223: Key.DEL,
    16777249: Key.LEFT_CONTROL,
    16777248: Key.LEFT_SHIFT,
    16777252: Key.CAPSLOCK,
    16777216: Key.ESCAPE,
    16777220: Key.RETURN,
    16777254: Key.SCROLLOCK,
    16777224: Key.PAUSE,
    16777222: Key.INSERT,
    16777232: Key.HOME,
    16777238: Key.PAGEUP,
    16777239: Key.PAGEDOWN,
    16777235: Key.UP_ARROW,
    16777237: Key.DOWN_ARROW,
    16777236: Key.RIGHT_ARROW,
    16777234: Key.LEFT_ARROW,
    16777301: Key.CONTEXT_MENU,
    16777250: Key.LEFT_META,
    16777251: Key.LEFT_ALT,
    16777219: Key.BACKSPACE,
    16777217: Key.TAB,
    16777233: Key.END,
}