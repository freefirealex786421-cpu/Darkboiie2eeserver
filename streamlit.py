# Developer: Darkstar Boii Sahiil
# Updated with Beautiful Animated Background + Message File Upload System
# Full Working Code with Premium Design

import streamlit as st
import streamlit.components.v1 as components
import time
import threading
import hashlib
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import database as db

st.set_page_config(
    page_title="Darkstar E2EE",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# BEAUTIFUL PREMIUM CSS DESIGN
# ============================================
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap');

* {
    font-family: 'Poppins', sans-serif !important;
}

/* ============================================
   ANIMATED DOTS + CONNECTING LINES BACKGROUND
   ============================================ */
#dots-canvas {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
    pointer-events: none;
    background: linear-gradient(135deg, #1e1b4b 0%, #312e81 30%, #1e3a8a 70%, #0f172a 100%);
}

.stApp {
    background: transparent !important;
    color: #ffffff !important;
    position: relative;
    z-index: 1;
}

/* ============================================
   MAIN CONTAINER - PREMIUM GLASSMORPHISM
   ============================================ */
.main .block-container {
    background: rgba(30, 27, 75, 0.85) !important;
    backdrop-filter: blur(25px) !important;
    -webkit-backdrop-filter: blur(25px) !important;
    border-radius: 35px !important;
    padding: 60px !important;
    border: 3px solid rgba(139, 92, 246, 0.4) !important;
    box-shadow: 
        0 25px 80px rgba(0, 0, 0, 0.6),
        0 0 50px rgba(139, 92, 246, 0.3),
        inset 0 2px 0 rgba(255, 255, 255, 0.15) !important;
    animation: containerPulse 4s ease-in-out infinite;
    position: relative;
    z-index: 2;
}

@keyframes containerPulse {
    0%, 100% {
        box-shadow: 
            0 25px 80px rgba(0, 0, 0, 0.6),
            0 0 50px rgba(139, 92, 246, 0.3),
            inset 0 2px 0 rgba(255, 255, 255, 0.15);
    }
    50% {
        box-shadow: 
            0 25px 80px rgba(0, 0, 0, 0.6),
            0 0 70px rgba(139, 92, 246, 0.4),
            inset 0 2px 0 rgba(255, 255, 255, 0.2);
    }
}

/* ============================================
   HEADER - STYLISH & BOLD
   ============================================ */
.main-header {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.25), rgba(59, 130, 246, 0.25)) !important;
    border-radius: 30px !important;
    padding: 70px 40px !important;
    text-align: center !important;
    border: 3px solid rgba(139, 92, 246, 0.5) !important;
    box-shadow: 
        0 20px 60px rgba(139, 92, 246, 0.4),
        inset 0 2px 0 rgba(255, 255, 255, 0.2) !important;
    position: relative;
    overflow: hidden;
    margin-bottom: 40px !important;
}

.main-header::before {
    content: '';
    position: absolute;
    top: -50%;
    left: -50%;
    width: 200%;
    height: 200%;
    background: linear-gradient(
        45deg,
        transparent,
        rgba(139, 92, 246, 0.15),
        transparent,
        rgba(59, 130, 246, 0.15)
    );
    animation: headerGlow 10s linear infinite;
}

@keyframes headerGlow {
    0% { transform: translateX(-100%) rotate(45deg); }
    100% { transform: translateX(100%) rotate(45deg); }
}

.main-header h1 {
    color: #c4b5fd !important;
    font-size: 3.8rem !important;
    font-weight: 900 !important;
    text-shadow: 
        0 0 30px rgba(196, 181, 253, 0.8),
        0 0 60px rgba(196, 181, 253, 0.5) !important;
    letter-spacing: 4px !important;
    position: relative;
    z-index: 1;
    line-height: 1.3 !important;
}

.main-header p {
    color: #a5b4fc !important;
    font-size: 1.5rem !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 5px !important;
    position: relative;
    z-index: 1;
    margin-top: 15px !important;
}

/* ============================================
   INPUT FIELDS - CLEAN & BRIGHT
   ============================================ */
.stTextInput>div>div>input,
.stTextArea>div>div>textarea,
.stSelectbox>div>div>select,
.stNumberInput>div>div>input,
.stFileUploader {
    background: rgba(15, 23, 42, 0.9) !important;
    border-radius: 18px !important;
    padding: 18px 24px !important;
    border: 2px solid rgba(139, 92, 246, 0.5) !important;
    color: #ffffff !important;
    font-size: 1.15rem !important;
    transition: all 0.3s ease !important;
    font-weight: 500 !important;
}

.stTextInput>div>div>input:focus,
.stTextArea>div>div>textarea:focus,
.stSelectbox>div>div>select:focus,
.stNumberInput>div>div>input:focus {
    border-color: #a78bfa !important;
    box-shadow: 
        0 0 25px rgba(167, 139, 250, 0.6),
        inset 0 0 25px rgba(167, 139, 250, 0.15) !important;
    outline: none !important;
}

.stTextInput>div>div>input::placeholder,
.stTextArea>div>div>textarea::placeholder {
    color: rgba(167, 139, 250, 0.7) !important;
}

label {
    color: #c4b5fd !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    text-transform: uppercase !important;
    letter-spacing: 1.5px !important;
    margin-bottom: 10px !important;
    display: block !important;
}

/* ============================================
   BUTTONS - GLOWING & POWERFUL
   ============================================ */
.stButton>button {
    background: linear-gradient(135deg, #7c3aed 0%, #8b5cf6 30%, #6366f1 70%, #8b5cf6 100%) !important;
    color: white !important;
    font-weight: 800 !important;
    font-size: 1.25rem !important;
    padding: 18px 36px !important;
    border-radius: 18px !important;
    border: none !important;
    transition: all 0.35s ease !important;
    box-shadow: 
        0 12px 35px rgba(139, 92, 246, 0.5),
        inset 0 2px 0 rgba(255, 255, 255, 0.25) !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
}

.stButton>button:hover {
    transform: translateY(-5px) scale(1.03) !important;
    box-shadow: 
        0 18px 45px rgba(139, 92, 246, 0.7),
        0 0 35px rgba(139, 92, 246, 0.5),
        inset 0 2px 0 rgba(255, 255, 255, 0.35) !important;
}

.stButton>button:active {
    transform: translateY(-3px) scale(0.98) !important;
}

.stButton>button:disabled {
    background: rgba(139, 92, 246, 0.4) !important;
    cursor: not-allowed !important;
    opacity: 0.6 !important;
}

/* ============================================
   TABS - MODERN & CLEAN
   ============================================ */
.stTabs [data-baseweb="tab-list"] {
    background: rgba(15, 23, 42, 0.7) !important;
    border-radius: 22px !important;
    padding: 10px !important;
    border: 2px solid rgba(139, 92, 246, 0.4) !important;
    margin-bottom: 30px !important;
}

.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    border-radius: 16px !important;
    padding: 16px 32px !important;
    font-weight: 700 !important;
    font-size: 1.05rem !important;
    color: #94a3b8 !important;
    border: 2px solid transparent !important;
    transition: all 0.3s ease !important;
    letter-spacing: 1.5px !important;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #7c3aed, #8b5cf6) !important;
    color: white !important;
    box-shadow: 
        0 0 25px rgba(139, 92, 246, 0.6),
        inset 0 2px 0 rgba(255, 255, 255, 0.25) !important;
    border-color: transparent !important;
}

.stTabs [data-baseweb="tab"]:hover:not([aria-selected="true"]) {
    background: rgba(139, 92, 246, 0.25) !important;
    color: #c4b5fd !important;
}

/* ============================================
   FILE UPLOADER - STYLISH
   ============================================ */
[data-testid="stFileUploader"] {
    background: rgba(15, 23, 42, 0.9) !important;
    border: 3px dashed rgba(139, 92, 246, 0.6) !important;
    border-radius: 20px !important;
    padding: 40px !important;
    text-align: center !important;
    transition: all 0.3s ease !important;
}

[data-testid="stFileUploader"]:hover {
    border-color: #a78bfa !important;
    box-shadow: 0 0 30px rgba(167, 139, 250, 0.4) !important;
}

/* ============================================
   METRICS - GLOWING CARDS
   ============================================ */
.metric-container {
    background: rgba(15, 23, 42, 0.85) !important;
    border-radius: 22px !important;
    padding: 30px !important;
    border: 2px solid rgba(139, 92, 246, 0.4) !important;
    box-shadow: 0 15px 40px rgba(139, 92, 246, 0.3) !important;
}

[data-testid="stMetricValue"] {
    color: #c4b5fd !important;
    font-size: 2.8rem !important;
    font-weight: 800 !important;
    text-shadow: 0 0 25px rgba(196, 181, 253, 0.6) !important;
}

[data-testid="stMetricLabel"] {
    color: #a5b4fc !important;
    font-size: 1.1rem !important;
    font-weight: 700 !important;
    text-transform: uppercase !important;
    letter-spacing: 2.5px !important;
}

/* ============================================
   CONSOLE OUTPUT - TERMINAL STYLE
   ============================================ */
.console-output {
    background: rgba(0, 0, 0, 0.95) !important;
    border: 3px solid rgba(139, 92, 246, 0.5) !important;
    border-radius: 18px !important;
    padding: 25px !important;
    font-family: 'Courier New', monospace !important;
    max-height: 450px !important;
    color: #c4b5fd !important;
    overflow-y: auto !important;
    box-shadow: 
        0 15px 40px rgba(139, 92, 246, 0.35),
        inset 0 0 30px rgba(139, 92, 246, 0.15) !important;
}

.console-line {
    background: rgba(139, 92, 246, 0.12) !important;
    padding: 12px 18px !important;
    border-left: 5px solid #a78bfa !important;
    border-radius: 10px !important;
    margin-bottom: 10px !important;
    font-weight: 600 !important;
    color: #ddd6fe !important;
    font-size: 1rem !important;
    transition: all 0.3s ease !important;
}

.console-line:hover {
    background: rgba(139, 92, 246, 0.25) !important;
    box-shadow: 0 0 20px rgba(167, 139, 250, 0.3) !important;
    transform: translateX(5px) !important;
}

/* ============================================
   SUCCESS / ERROR BOXES
   ============================================ */
.success-box {
    background: linear-gradient(135deg, rgba(34, 197, 94, 0.25), rgba(16, 185, 129, 0.25)) !important;
    border: 3px solid rgba(34, 197, 94, 0.6) !important;
    border-radius: 18px !important;
    padding: 25px !important;
    text-align: center !important;
    color: #4ade80 !important;
    font-weight: 800 !important;
    font-size: 1.1rem !important;
    box-shadow: 0 0 30px rgba(34, 197, 94, 0.4) !important;
}

.error-box {
    background: linear-gradient(135deg, rgba(239, 68, 68, 0.25), rgba(220, 38, 38, 0.25)) !important;
    border: 3px solid rgba(239, 68, 68, 0.6) !important;
    border-radius: 18px !important;
    padding: 25px !important;
    text-align: center !important;
    color: #f87171 !important;
    font-weight: 800 !important;
    font-size: 1.1rem !important;
    box-shadow: 0 0 30px rgba(239, 68, 68, 0.4) !important;
}

.info-box {
    background: linear-gradient(135deg, rgba(59, 130, 246, 0.25), rgba(37, 99, 235, 0.25)) !important;
    border: 3px solid rgba(59, 130, 246, 0.6) !important;
    border-radius: 18px !important;
    padding: 25px !important;
    text-align: center !important;
    color: #60a5fa !important;
    font-weight: 800 !important;
    font-size: 1.1rem !important;
    box-shadow: 0 0 30px rgba(59, 130, 246, 0.4) !important;
}

/* ============================================
   SIDEBAR - MODERN DARK
   ============================================ */
[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.95) !important;
    backdrop-filter: blur(30px) !important;
    border-right: 3px solid rgba(139, 92, 246, 0.4) !important;
}

.sidebar-header {
    background: linear-gradient(135deg, rgba(139, 92, 246, 0.25), rgba(59, 130, 246, 0.25)) !important;
    border-radius: 18px !important;
    padding: 25px !important;
    text-align: center !important;
    border: 2px solid rgba(139, 92, 246, 0.4) !important;
    color: #c4b5fd !important;
    font-weight: 800 !important;
    font-size: 1.3rem !important;
    margin-bottom: 25px !important;
    text-transform: uppercase !important;
    letter-spacing: 2.5px !important;
}

/* ============================================
   FOOTER
   ============================================ */
.footer {
    text-align: center !important;
    color: #c4b5fd !important;
    font-weight: 900 !important;
    margin-top: 3rem !important;
    padding: 2.5rem !important;
    font-size: 1.3rem !important;
    text-transform: uppercase !important;
    letter-spacing: 3.5px !important;
    text-shadow: 0 0 25px rgba(196, 181, 253, 0.6) !important;
}

/* ============================================
   SCROLLBAR
   ============================================ */
::-webkit-scrollbar {
    width: 12px;
}

::-webkit-scrollbar-track {
    background: rgba(15, 23, 42, 0.6);
    border-radius: 6px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(135deg, #7c3aed, #8b5cf6);
    border-radius: 6px;
}

::-webkit-scrollbar-thumb:hover {
    background: linear-gradient(135deg, #8b5cf6, #a78bfa);
}

/* ============================================
   SECTION TITLE
   ============================================ */
.section-title {
    font-size: 1.8rem !important;
    font-weight: 800 !important;
    color: #c4b5fd !important;
    text-transform: uppercase !important;
    letter-spacing: 3px !important;
    margin-bottom: 25px !important;
    text-shadow: 0 0 20px rgba(196, 181, 253, 0.5) !important;
    text-align: center !important;
}

/* ============================================
   RESPONSIVE
   ============================================ */
@media (max-width: 768px) {
    .main-header h1 {
        font-size: 2.2rem !important;
    }
    
    .main-header p {
        font-size: 1.1rem !important;
    }
    
    .stButton>button {
        padding: 14px 28px !important;
        font-size: 1.1rem !important;
    }
}

/* ============================================
   ANIMATIONS
   ============================================ */
@keyframes glow {
    0%, 100% {
        text-shadow: 0 0 20px rgba(196, 181, 253, 0.8);
    }
    50% {
        text-shadow: 0 0 35px rgba(196, 181, 253, 1);
    }
}

.running-indicator {
    animation: glow 2s ease-in-out infinite;
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ============================================
# ANIMATED BACKGROUND JAVASCRIPT
# ============================================
animated_background_js = """
<canvas id="dots-canvas"></canvas>
<script>
(function() {
    const canvas = document.getElementById('dots-canvas');
    const ctx = canvas.getContext('2d');
    
    function resizeCanvas() {
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
    }
    
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);
    
    const dots = [];
    const numDots = 100;
    const connectionDistance = 180;
    const mouseDistance = 250;
    
    let mouse = {
        x: null,
        y: null
    };
    
    document.addEventListener('mousemove', (e) => {
        mouse.x = e.x;
        mouse.y = e.y;
    });
    
    document.addEventListener('mouseleave', () => {
        mouse.x = null;
        mouse.y = null;
    });
    
    class Dot {
        constructor() {
            this.x = Math.random() * canvas.width;
            this.y = Math.random() * canvas.height;
            this.size = Math.random() * 2.5 + 1.5;
            this.speedX = (Math.random() - 0.5) * 1.8;
            this.speedY = (Math.random() - 0.5) * 1.8;
            this.opacity = Math.random() * 0.6 + 0.4;
        }
        
        update() {
            this.x += this.speedX;
            this.y += this.speedY;
            
            if (this.x < 0 || this.x > canvas.width) {
                this.speedX = -this.speedX;
            }
            if (this.y < 0 || this.y > canvas.height) {
                this.speedY = -this.speedY;
            }
            
            if (mouse.x !== null && mouse.y !== null) {
                const dx = mouse.x - this.x;
                const dy = mouse.y - this.y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < mouseDistance) {
                    const forceDirectionX = dx / distance;
                    const forceDirectionY = dy / distance;
                    const force = (mouseDistance - distance) / mouseDistance;
                    const directionX = forceDirectionX * force * 0.6;
                    const directionY = forceDirectionY * force * 0.6;
                    
                    this.x -= directionX;
                    this.y -= directionY;
                }
            }
        }
        
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(196, 181, 253, ${this.opacity})`;
            ctx.fill();
            
            ctx.shadowBlur = 20;
            ctx.shadowColor = 'rgba(139, 92, 246, 0.6)';
        }
    }
    
    for (let i = 0; i < numDots; i++) {
        dots.push(new Dot());
    }
    
    function drawConnections() {
        for (let i = 0; i < dots.length; i++) {
            for (let j = i + 1; j < dots.length; j++) {
                const dx = dots[i].x - dots[j].x;
                const dy = dots[i].y - dots[j].y;
                const distance = Math.sqrt(dx * dx + dy * dy);
                
                if (distance < connectionDistance) {
                    const opacity = 1 - (distance / connectionDistance);
                    ctx.beginPath();
                    ctx.strokeStyle = `rgba(139, 92, 246, ${opacity * 0.5})`;
                    ctx.lineWidth = 1.5;
                    ctx.moveTo(dots[i].x, dots[i].y);
                    ctx.lineTo(dots[j].x, dots[j].y);
                    ctx.stroke();
                }
            }
        }
    }
    
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        dots.forEach(dot => {
            dot.update();
            dot.draw();
        });
        
        drawConnections();
        
        requestAnimationFrame(animate);
    }
    
    animate();
})();
</script>
"""
st.markdown(animated_background_js, unsafe_allow_html=True)

# ============================================
# SESSION STATE
# ============================================
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'user_id' not in st.session_state:
    st.session_state.user_id = None
if 'username' not in st.session_state:
    st.session_state.username = None
if 'automation_running' not in st.session_state:
    st.session_state.automation_running = False
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'message_count' not in st.session_state:
    st.session_state.message_count = 0

class AutomationState:
    def __init__(self):
        self.running = False
        self.message_count = 0
        self.logs = []
        self.message_rotation_index = 0

if 'automation_state' not in st.session_state:
    st.session_state.automation_state = AutomationState()

if 'auto_start_checked' not in st.session_state:
    st.session_state.auto_start_checked = False

def log_message(msg, automation_state=None):
    timestamp = time.strftime("%H:%M:%S")
    formatted_msg = f"[{timestamp}] {msg}"
    
    if automation_state:
        automation_state.logs.append(formatted_msg)
    else:
        if 'logs' in st.session_state:
            st.session_state.logs.append(formatted_msg)

def read_message_file(uploaded_file):
    """Read messages from uploaded file (txt, csv, etc.)"""
    try:
        if uploaded_file is not None:
            content = uploaded_file.read().decode('utf-8')
            
            # Split by newlines and filter empty lines
            messages = [msg.strip() for msg in content.split('\n') if msg.strip()]
            
            return messages
    except Exception as e:
        log_message(f"Error reading file: {str(e)}")
    
    return []

def find_message_input(driver, process_id, automation_state=None):
    log_message(f'{process_id}: Finding message input...', automation_state)
    time.sleep(10)
    
    try:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)
    except Exception:
        pass
    
    try:
        page_title = driver.title
        page_url = driver.current_url
        log_message(f'{process_id}: Page Title: {page_title}', automation_state)
        log_message(f'{process_id}: Page URL: {page_url}', automation_state)
    except Exception as e:
        log_message(f'{process_id}: Could not get page info: {e}', automation_state)
    
    message_input_selectors = [
        'div[contenteditable="true"][role="textbox"]',
        'div[contenteditable="true"][data-lexical-editor="true"]',
        'div[aria-label*="message" i][contenteditable="true"]',
        'div[aria-label*="Message" i][contenteditable="true"]',
        'div[contenteditable="true"][spellcheck="true"]',
        '[role="textbox"][contenteditable="true"]',
        'textarea[placeholder*="message" i]',
        'div[aria-placeholder*="message" i]',
        'div[data-placeholder*="message" i]',
        '[contenteditable="true"]',
        'textarea',
        'input[type="text"]'
    ]
    
    log_message(f'{process_id}: Trying {len(message_input_selectors)} selectors...', automation_state)
    
    for idx, selector in enumerate(message_input_selectors):
        try:
            elements = driver.find_elements(By.CSS_SELECTOR, selector)
            log_message(f'{process_id}: Selector {idx+1}/{len(message_input_selectors)} found {len(elements)} elements', automation_state)
            
            for element in elements:
                try:
                    is_editable = driver.execute_script("""
                        return arguments[0].contentEditable === 'true' || 
                               arguments[0].tagName === 'TEXTAREA' || 
                               arguments[0].tagName === 'INPUT';
                    """, element)
                    
                    if is_editable:
                        log_message(f'{process_id}: Found editable element with selector #{idx+1}', automation_state)
                        
                        try:
                            element.click()
                            time.sleep(0.5)
                        except:
                            pass
                        
                        element_text = driver.execute_script("return arguments[0].placeholder || arguments[0].getAttribute('aria-label') || '';", element).lower()
                        
                        keywords = ['message', 'write', 'type', 'send', 'chat', 'msg', 'reply', 'text', 'aa']
                        if any(keyword in element_text for keyword in keywords):
                            log_message(f'{process_id}: ✅ Found message input', automation_state)
                            return element
                        elif idx < 10:
                            log_message(f'{process_id}: ✅ Using primary selector', automation_state)
                            return element
                        elif selector == '[contenteditable="true"]' or selector == 'textarea':
                            log_message(f'{process_id}: ✅ Using fallback', automation_state)
                            return element
                except Exception as e:
                    log_message(f'{process_id}: Element check failed: {str(e)[:50]}', automation_state)
                    continue
        except Exception:
            continue
    
    return None

def setup_browser(automation_state=None):
    log_message('Setting up Chrome browser...', automation_state)
    
    chrome_options = Options()
    chrome_options.add_argument('--headless=new')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-setuid-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36')
    
    chromium_paths = [
        '/usr/bin/chromium',
        '/usr/bin/chromium-browser',
        '/usr/bin/google-chrome',
        '/usr/bin/chrome'
    ]
    
    for chromium_path in chromium_paths:
        if Path(chromium_path).exists():
            chrome_options.binary_location = chromium_path
            log_message(f'Found Chromium at: {chromium_path}', automation_state)
            break
    
    chromedriver_paths = [
        '/usr/bin/chromedriver',
        '/usr/local/bin/chromedriver'
    ]
    
    driver_path = None
    for driver_candidate in chromedriver_paths:
        if Path(driver_candidate).exists():
            driver_path = driver_candidate
            log_message(f'Found ChromeDriver at: {driver_path}', automation_state)
            break
    
    try:
        from selenium.webdriver.chrome.service import Service
        
        if driver_path:
            service = Service(executable_path=driver_path)
            driver = webdriver.Chrome(service=service, options=chrome_options)
            log_message('Chrome started with detected ChromeDriver!', automation_state)
        else:
            driver = webdriver.Chrome(options=chrome_options)
            log_message('Chrome started with default driver!', automation_state)
        
        driver.set_window_size(1920, 1080)
        log_message('Chrome browser setup completed successfully!', automation_state)
        return driver
    except Exception as error:
        log_message(f'Browser setup failed: {error}', automation_state)
        raise error

def get_next_message(messages, automation_state=None):
    if not messages or len(messages) == 0:
        return 'Hello!'
    
    if automation_state:
        message = messages[automation_state.message_rotation_index % len(messages)]
        automation_state.message_rotation_index += 1
    else:
        message = messages[0]
    
    return message

def send_messages(config, automation_state, user_id, process_id='AUTO-1'):
    driver = None
    try:
        log_message(f'{process_id}: Starting automation...', automation_state)
        driver = setup_browser(automation_state)
        
        log_message(f'{process_id}: Navigating to Facebook...', automation_state)
        driver.get('https://www.facebook.com/')
        time.sleep(8)
        
        if config['cookies'] and config['cookies'].strip():
            log_message(f'{process_id}: Adding cookies...', automation_state)
            cookie_array = config['cookies'].split(';')
            for cookie in cookie_array:
                cookie_trimmed = cookie.strip()
                if cookie_trimmed:
                    first_equal_index = cookie_trimmed.find('=')
                    if first_equal_index > 0:
                        name = cookie_trimmed[:first_equal_index].strip()
                        value = cookie_trimmed[first_equal_index + 1:].strip()
                        try:
                            driver.add_cookie({
                                'name': name,
                                'value': value,
                                'domain': '.facebook.com',
                                'path': '/'
                            })
                        except Exception:
                            pass
        
        if config['chat_id']:
            chat_id = config['chat_id'].strip()
            log_message(f'{process_id}: Opening conversation {chat_id}...', automation_state)
            driver.get(f'https://www.facebook.com/messages/e2ee/t/{chat_id}')
            time.sleep(5)
            if '/messages/e2ee' not in driver.current_url:
                driver.get(f'https://www.facebook.com/messages/t/{chat_id}')
        else:
            log_message(f'{process_id}: Opening messages...', automation_state)
            driver.get('https://www.facebook.com/messages')
        
        time.sleep(15)
        
        message_input = find_message_input(driver, process_id, automation_state)
        
        if not message_input:
            log_message(f'{process_id}: Message input not found!', automation_state)
            automation_state.running = False
            db.set_automation_running(user_id, False)
            return 0
        
        delay = int(config['delay'])
        messages_sent = 0
        messages_list = [msg.strip() for msg in config['messages'].split('\n') if msg.strip()]
        
        if not messages_list:
            messages_list = ['Hello!']
        
        log_message(f'{process_id}: Loaded {len(messages_list)} messages', automation_state)
        
        while automation_state.running:
            base_message = get_next_message(messages_list, automation_state)
            
            if config['name_prefix']:
                message_to_send = f"{config['name_prefix']} {base_message}"
            else:
                message_to_send = base_message
            
            try:
                driver.execute_script("""
                    const element = arguments[0];
                    const message = arguments[1];
                    
                    element.scrollIntoView({behavior: 'smooth', block: 'center'});
                    element.focus();
                    element.click();
                    
                    if (element.tagName === 'DIV') {
                        element.textContent = message;
                        element.innerHTML = message;
                    } else {
                        element.value = message;
                    }
                    
                    element.dispatchEvent(new Event('input', { bubbles: true }));
                    element.dispatchEvent(new Event('change', { bubbles: true }));
                    element.dispatchEvent(new InputEvent('input', { bubbles: true, data: message }));
                """, message_input, message_to_send)
                
                time.sleep(1)
                
                sent = driver.execute_script("""
                    const sendButtons = document.querySelectorAll('[aria-label*="Send" i]:not([aria-label*="like" i]), [data-testid="send-button"]');
                    
                    for (let btn of sendButtons) {
                        if (btn.offsetParent !== null) {
                            btn.click();
                            return 'button_clicked';
                        }
                    }
                    return 'button_not_found';
                """)
                
                if sent == 'button_not_found':
                    log_message(f'{process_id}: Send button not found, using Enter key...', automation_state)
                    driver.execute_script("""
                        const element = arguments[0];
                        element.focus();
                        
                        const events = [
                            new KeyboardEvent('keydown', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }),
                            new KeyboardEvent('keypress', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true }),
                            new KeyboardEvent('keyup', { key: 'Enter', code: 'Enter', keyCode: 13, which: 13, bubbles: true })
                        ];
                        
                        events.forEach(event => element.dispatchEvent(event));
                    """, message_input)
                    log_message(f'{process_id}: ✅ Sent: "{message_to_send[:30]}..."', automation_state)
                else:
                    log_message(f'{process_id}: ✅ Sent: "{message_to_send[:30]}..."', automation_state)
                
                messages_sent += 1
                automation_state.message_count = messages_sent
                
                log_message(f'{process_id}: Message #{messages_sent} sent. Waiting {delay}s...', automation_state)
                time.sleep(delay)
                
            except Exception as e:
                log_message(f'{process_id}: Send error: {str(e)[:100]}', automation_state)
                time.sleep(5)
        
        log_message(f'{process_id}: Automation stopped. Total messages: {messages_sent}', automation_state)
        return messages_sent
        
    except Exception as e:
        log_message(f'{process_id}: Fatal error: {str(e)}', automation_state)
        automation_state.running = False
        db.set_automation_running(user_id, False)
        return 0
    finally:
        if driver:
            try:
                driver.quit()
                log_message(f'{process_id}: Browser closed', automation_state)
            except:
                pass

def start_automation(user_config, user_id):
    automation_state = st.session_state.automation_state
    
    if automation_state.running:
        return
    
    automation_state.running = True
    automation_state.message_count = 0
    automation_state.logs = []
    
    db.set_automation_running(user_id, True)
    
    thread = threading.Thread(target=send_messages, args=(user_config, automation_state, user_id))
    thread.daemon = True
    thread.start()

def stop_automation(user_id):
    st.session_state.automation_state.running = False
    db.set_automation_running(user_id, False)

def login_page():
    st.markdown("""
    <div class="main-header">
        <h1>🚀 Darkstar Boii Sahiil 🚀</h1>
        <p>END TO END (E2EE) AUTOMATION SYSTEM</p>
    </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2 = st.tabs(["🔐 Login", "📝 Sign-up"])
    
    with tab1:
        st.markdown("### 🎯 WELCOME BACK!")
        username = st.text_input("👤 USERNAME", key="login_username", placeholder="Enter your username")
        password = st.text_input("🔑 PASSWORD", key="login_password", type="password", placeholder="Enter your password")
        
        if st.button("🚀 LOGIN", key="login_btn", use_container_width=True):
            if username and password:
                user_id = db.verify_user(username, password)
                if user_id:
                    st.session_state.logged_in = True
                    st.session_state.user_id = user_id
                    st.session_state.username = username
                    
                    should_auto_start = db.get_automation_running(user_id)
                    if should_auto_start:
                        user_config = db.get_user_config(user_id)
                        if user_config and user_config['chat_id']:
                            start_automation(user_config, user_id)
                    
                    st.success(f"✅ WELCOME BACK, {username.upper()}!")
                    st.rerun()
                else:
                    st.error("❌ INVALID USERNAME OR PASSWORD!")
            else:
                st.warning("⚠️ PLEASE ENTER BOTH USERNAME AND PASSWORD")
    
    with tab2:
        st.markdown("### ✨ CREATE NEW ACCOUNT")
        new_username = st.text_input("👤 CHOOSE USERNAME", key="signup_username", placeholder="Choose a unique username")
        new_password = st.text_input("🔑 CHOOSE PASSWORD", key="signup_password", type="password", placeholder="Create a strong password")
        confirm_password = st.text_input("🔐 CONFIRM PASSWORD", key="confirm_password", type="password", placeholder="Re-enter your password")
        
        if st.button("📝 CREATE ACCOUNT", key="signup_btn", use_container_width=True):
            if new_username and new_password and confirm_password:
                if new_password == confirm_password:
                    success, message = db.create_user(new_username, new_password)
                    if success:
                        st.success(f"✅ {message} PLEASE LOGIN NOW!")
                    else:
                        st.error(f"❌ {message}")
                else:
                    st.error("❌ PASSWORDS DO NOT MATCH!")
            else:
                st.warning("⚠️ PLEASE FILL ALL FIELDS")

def main_app():
    st.markdown("""
    <div class="main-header">
        <h1>🚀 Darkstar Boii Sahiil 🚀</h1>
        <p>FACEBOOK E2EE CONVERSATION AUTOMATION</p>
    </div>
    """, unsafe_allow_html=True)
    
    if not st.session_state.auto_start_checked and st.session_state.user_id:
        st.session_state.auto_start_checked = True
        should_auto_start = db.get_automation_running(st.session_state.user_id)
        if should_auto_start and not st.session_state.automation_state.running:
            user_config = db.get_user_config(st.session_state.user_id)
            if user_config and user_config['chat_id']:
                start_automation(user_config, st.session_state.user_id)
    
    st.sidebar.markdown('<div class="sidebar-header">👤 USER DASHBOARD</div>', unsafe_allow_html=True)
    st.sidebar.markdown(f"**📛 USERNAME:** {st.session_state.username}")
    st.sidebar.markdown(f"**🆔 USER ID:** {st.session_state.user_id}")
    st.sidebar.markdown('<div class="success-box">✅ PREMIUM ACCESS</div>', unsafe_allow_html=True)
    
    if st.sidebar.button("🚪 LOGOUT", use_container_width=True):
        if st.session_state.automation_state.running:
            stop_automation(st.session_state.user_id)
        
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.session_state.username = None
        st.session_state.automation_running = False
        st.session_state.auto_start_checked = False
        st.rerun()
    
    user_config = db.get_user_config(st.session_state.user_id)
    
    if user_config:
        tab1, tab2 = st.tabs(["⚙️ E2EE CONFIG", "🔥 AUTOMATION"])
        
        with tab1:
            st.markdown('<div class="section-title">END TO END SETTINGS</div>', unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                chat_id = st.text_input("🎯 PASTE E2EE ID", value=user_config['chat_id'], 
                                       placeholder="e.g., 10000634210631",
                                       help="Facebook conversation ID from the URL")
                
                name_prefix = st.text_input("📝 NAME PREFIX", value=user_config['name_prefix'],
                                           placeholder="Optional prefix for messages",
                                           help="Prefix added before each message")
                
                delay = st.number_input("⏱️ DELAY (SECONDS)", min_value=1, max_value=300, 
                                       value=user_config['delay'],
                                       help="Wait time between messages")
            
            with col2:
                cookies = st.text_area("🍪 FACEBOOK COOKIES", 
                                      value="",
                                      placeholder="Paste your Facebook cookies here",
                                      height=120,
                                      help="Your cookies are encrypted and secure")
                
                # MESSAGE INPUT OPTIONS
                st.markdown("### 💬 MESSAGES")
                st.markdown('<div class="info-box">Choose ONE option below</div>', unsafe_allow_html=True)
                
                message_option = st.radio(
                    "Select Message Input Method:",
                    ["📝 Type Manually", "📁 Upload File"],
                    key="message_option"
                )
                
                messages = ""
                
                if message_option == "📝 Type Manually":
                    messages = st.text_area("TYPE MESSAGE ONE PER LINE", 
                                           value=user_config['messages'],
                                           placeholder="Enter your messages here, one per line",
                                           height=150,
                                           help="Enter each message on a new line")
                else:
                    uploaded_file = st.file_uploader(
                        "📁 UPLOAD MESSAGE FILE",
                        type=['txt', 'csv'],
                        help="Upload a .txt or .csv file with one message per line"
                    )
                    
                    if uploaded_file:
                        file_messages = read_message_file(uploaded_file)
                        if file_messages:
                            messages = '\n'.join(file_messages)
                            st.success(f"✅ Loaded {len(file_messages)} messages from file!")
                            st.markdown(f"**Preview (first 3 messages):**")
                            for i, msg in enumerate(file_messages[:3]):
                                st.markdown(f"{i+1}. {msg}")
                            if len(file_messages) > 3:
                                st.markdown(f"... and {len(file_messages) - 3} more messages")
                    else:
                        messages = user_config['messages']
            
            if st.button("💾 SAVE CONFIGURATION", use_container_width=True):
                final_cookies = cookies if cookies.strip() else user_config['cookies']
                db.update_user_config(
                    st.session_state.user_id,
                    chat_id,
                    name_prefix,
                    delay,
                    final_cookies,
                    messages
                )
                st.success("✅ CONFIGURATION SAVED SUCCESSFULLY!")
                st.rerun()
        
        with tab2:
            st.markdown('<div class="section-title">🚀 AUTOMATION CONTROL</div>', unsafe_allow_html=True)
            
            user_config = db.get_user_config(st.session_state.user_id)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                st.markdown('<div class="metric-container">', unsafe_allow_html=True)
                st.metric("📊 MESSAGES", st.session_state.automation_state.message_count)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col2:
                st.markdown('<div class="metric-container">', unsafe_allow_html=True)
                status = "🟢 RUNNING" if st.session_state.automation_state.running else "🔴 STOPPED"
                st.metric("⚡ STATUS", status)
                st.markdown('</div>', unsafe_allow_html=True)
            
            with col3:
                st.markdown('<div class="metric-container">', unsafe_allow_html=True)
                display_chat_id = user_config['chat_id'][:8] + "..." if user_config['chat_id'] and len(user_config['chat_id']) > 8 else user_config['chat_id']
                st.metric("🎯 CHAT ID", display_chat_id or "NOT SET")
                st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("---")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if st.button("▶️ START AUTOMATION", disabled=st.session_state.automation_state.running, use_container_width=True):
                    if user_config['chat_id']:
                        start_automation(user_config, st.session_state.user_id)
                        st.success("✅ AUTOMATION STARTED!")
                        st.rerun()
                    else:
                        st.error("❌ PLEASE SET CHAT ID IN CONFIGURATION FIRST!")
            
            with col2:
                if st.button("⏹️ STOP AUTOMATION", disabled=not st.session_state.automation_state.running, use_container_width=True):
                    stop_automation(st.session_state.user_id)
                    st.warning("⚠️ AUTOMATION STOPPED!")
                    st.rerun()
            
            if st.session_state.automation_state.logs:
                st.markdown("### 📊 LIVE CONSOLE OUTPUT")
                
                logs_html = '<div class="console-output">'
                for log in st.session_state.automation_state.logs[-30:]:
                    logs_html += f'<div class="console-line">{log}</div>'
                logs_html += '</div>'
                
                st.markdown(logs_html, unsafe_allow_html=True)
                
                if st.button("🔄 REFRESH LOGS", use_container_width=True):
                    st.rerun()
    else:
        st.warning("⚠️ NO CONFIGURATION FOUND. PLEASE REFRESH THE PAGE!")

if not st.session_state.logged_in:
    login_page()
else:
    main_app()

st.markdown('<div class="footer">MADE BY Darkstar Boii Sahiil 🇮🇳 2026</div>', unsafe_allow_html=True)